from gig import Ent, EntType, GIGTable
from utils import Log

log = Log("Diversity")


class Diversity:
    def __init__(self, ent_type: EntType):
        self.ent_type = ent_type

    def computer_hhcm(self) -> dict[str, float]:
        ents = Ent.list_from_type(self.ent_type)
        n_ents = len(ents)
        log.info(f"Found {n_ents} {self.ent_type.name} entities")

        gig_table_religion = GIGTable("population-religion", "regions", "2012")
        d = {}
        for ent in ents:
            religion = ent.gig(gig_table_religion).dict
            buddhist = religion.get("buddhist", 0)
            hindu = religion.get("hindu", 0)
            islamic = religion.get("islam", 0)
            roman_catholic = religion.get("roman_catholic", 0)
            other_christian = religion.get("other_christian", 0)
            other = religion.get("other", 0)

            counts = [
                buddhist,
                hindu,
                islamic,
                roman_catholic,
                other_christian,
                other,
            ]
            total = sum(counts)
            if total == 0:
                rdi = 0.0
            else:
                shares = [c / total for c in counts]
                rdi = 10 * (1 - sum(s**2 for s in shares))

            d[ent.id] = rdi
        return d


if __name__ == "__main__":
    print(Diversity(EntType.COUNTRY).computer_hhcm())
