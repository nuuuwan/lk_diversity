import json
import os
import subprocess

import geopandas as gpd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
from gig import Ent, EntType, GIGTable
from utils import Log

log = Log("Diversity")


DIR_IMAGES = "output/images"
DIR_HS = "output/hs"


# RDI bands and colours matching the Voronoi/Pew visualisation
RDI_BANDS = [
    (7.0, 10.0, "#1d6614", "Very High (≥7.0)"),
    (5.5, 7.0, "#6a9f3a", "High (5.5–6.9)"),
    (3.0, 5.5, "#d4b030", "Moderate (3.0–5.4)"),
    (1.0, 3.0, "#e07030", "Low (1.0–2.9)"),
    (0.0, 1.0, "#c03025", "Very Low (<1.0)"),
]


def _rdi_color(rdi: float) -> str:
    for lo, hi, color, _ in RDI_BANDS:
        if lo <= rdi <= hi:
            return color
    return RDI_BANDS[-1][2]


ENT_TYPE_LABELS = {
    "ED": "Electoral Districts",
    "PD": "Polling Divisions",
}


class Diversity:
    def __init__(self, ent_type: EntType):
        self.ent_type = ent_type

    def compute_herfindahl_simpson(self) -> dict[str, tuple[float, str]]:
        ents = Ent.list_from_type(self.ent_type)
        n_ents = len(ents)
        log.info(f"Found {n_ents} {self.ent_type.name} entities")

        gig_table_religion = GIGTable(
            "population-religion", "regions", "2012"
        )
        d = {}
        for ent in ents:
            try:
                religion = ent.gig(gig_table_religion).dict
            except Exception as e:
                log.warning(
                    f"Could not get religion data for {
                        ent.name} ({
                        ent.id}): {e}"
                )
                continue
            buddhist = religion.get("buddhist", 0)
            hindu = religion.get("hindu", 0)
            muslims = religion.get("islam", 0)
            christian = religion.get("roman_catholic", 0) + religion.get(
                "other_christian", 0
            )
            other = religion.get("other", 0)

            religion_counts = {
                "buddhist": buddhist,
                "hindu": hindu,
                "muslims": muslims,
                "christian": christian,
                "religiously_unaffiliated": 0,
                "jews": 0,
                "other": other,
            }
            total = sum(religion_counts.values())
            if total == 0:
                rdi = 0.0
            else:
                n = len(religion_counts)
                shares = [c / total for c in religion_counts.values()]
                rdi = 10 * (1 - sum(s**2 for s in shares)) / (1 - 1 / n)

            d[ent.id] = rdi
        return d

    def save_hs(self):
        rdi_by_id = self.compute_herfindahl_simpson()
        ents = {ent.id: ent.name for ent in Ent.list_from_type(self.ent_type)}
        data = [
            {
                "id": ent_id,
                "name": ents.get(ent_id, ent_id),
                "rdi": round(rdi, 4),
            }
            for ent_id, rdi in sorted(rdi_by_id.items())
        ]
        os.makedirs(DIR_HS, exist_ok=True)
        output_path = os.path.join(
            DIR_HS, f"hs_{self.ent_type.name.lower()}.json"
        )
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)
        log.info(f"HS data saved to {output_path}")

    def plot(self):
        os.makedirs(DIR_IMAGES, exist_ok=True)
        output_path = os.path.join(
            DIR_IMAGES, f"diversity_map_{self.ent_type.name.lower()}.png"
        )
        rdi_by_id = self.compute_herfindahl_simpson()
        ents = Ent.list_from_type(self.ent_type)

        _COUNTRY_TOPOJSON = (
            "https://raw.githubusercontent.com/nuuuwan/"
            "lk_admin_regions/main/data/geo/topojson/original/countrys.topojson"
        )

        frames = []
        for ent in ents:
            if self.ent_type == EntType.COUNTRY:
                gdf = gpd.read_file(_COUNTRY_TOPOJSON, driver="TopoJSON")[
                    ["geometry"]
                ]
            else:
                gdf = ent.geo()
            rdi = rdi_by_id.get(ent.id, 0.0)
            gdf["ent_id"] = ent.id
            gdf["ent_name"] = ent.name
            gdf["rdi"] = rdi
            gdf["color"] = _rdi_color(rdi)
            frames.append(gdf)

        combined = gpd.GeoDataFrame(pd.concat(frames, ignore_index=True))

        fig, ax = plt.subplots(figsize=(10, 8))
        fig.patch.set_facecolor("#f5f0e8")
        ax.set_facecolor("#f5f0e8")

        combined.plot(
            ax=ax, color=combined["color"], edgecolor="#333333", linewidth=0.4
        )

        if len(ents) < 30:
            combined["geometry"] = combined["geometry"].buffer(0)
            labels = combined.dissolve(
                by="ent_id",
                aggfunc={
                    "ent_name": "first",
                    "rdi": "first",
                },
            )
            for _, row in labels.iterrows():
                pt = row.geometry.representative_point()
                label = f"{row['ent_name']}\n{row['rdi']:.1f}"
                ax.annotate(
                    label,
                    xy=(pt.x, pt.y),
                    ha="center",
                    va="center",
                    fontsize=6.5,
                    color="white",
                )

        # Legend — include per-band region counts
        rdi_values = list(rdi_by_id.values())
        legend_patches = [
            mpatches.Patch(
                color=color,
                label=f"{label}  [{sum(lo <= v <= hi for v in rdi_values)}]",
            )
            for lo, hi, color, label in RDI_BANDS
        ]
        ax.legend(
            handles=legend_patches,
            title="Religious Diversity Index",
            loc="center left",
            bbox_to_anchor=(1.02, 0.5),
            fontsize=8,
            title_fontsize=9,
            framealpha=0.85,
            borderaxespad=0,
        )

        ent_type_label = ENT_TYPE_LABELS.get(
            self.ent_type.name, self.ent_type.name.title()
        )
        ax.set_title(
            f"Religious Diversity Index — Sri Lanka\n"
            f"by {ent_type_label} ({len(ents)} regions)",
            fontsize=14,
            fontweight="bold",
            pad=12,
        )
        ax.axis("off")

        fig.text(
            0.5,
            0.01,
            "Methodology based on Pew Research Center's Religious Diversity Index.",
            ha="center",
            fontsize=7,
            color="#555555",
            style="italic",
        )

        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches="tight")
        plt.close()
        log.info(f"Map saved to {output_path}")
        subprocess.run(["open", output_path])


if __name__ == "__main__":
    for ent_type in [
        EntType.COUNTRY,
        EntType.PROVINCE,
        EntType.DISTRICT,
        EntType.DSD,
        EntType.ED,
        EntType.PD,
    ]:
        diversity = Diversity(ent_type)
        diversity.save_hs()
        diversity.plot()
        diversity = Diversity(ent_type)
        diversity.plot()
