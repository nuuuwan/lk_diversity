# One Island, Many Maps: The Hidden Geography of Religious Diversity in Sri Lanka

### Pew Research ranks Sri Lanka 39th in the world for religious diversity. But that single number conceals a country of extraordinary contrasts; from districts that rival the world's most pluralist places to corners that are almost entirely monocultural

---

## Why This Matters

In February 2026 the Pew Research Center published its updated [Religious Diversity Index](https://www.pewresearch.org/religion/2026/02/12/religious-diversity-around-the-world/), ranking 198 countries by how evenly their populations are spread across eight major faith traditions. Sri Lanka; a country of 22 million people and four major religions; earned a score of **5.6 out of 10**, placing it in the "High" diversity band alongside nations like Singapore and Switzerland. The Voronoi visualisation below puts that in global context:

[![Global Religious Diversity Index; Voronoi](https://www.voronoiapp.com/_next/image?url=https%3A%2F%2Fcdn.voronoiapp.com%2Fpublic%2Fimages%2F569b3be9-d493-498d-b76e-5b5a36201950.webp&w=1080&q=85)](https://www.voronoiapp.com/category/Religious-Diversity-Around-the-World--8143)

A single national score, however, is an aggregation over an island that is anything but average. Sri Lanka's ethnic and religious communities are not randomly distributed; they are geographically concentrated in patterns shaped by centuries of history, colonial policy, and one of Asia's longest civil wars. This analysis breaks the national RDI down to province, district, and sub-region levels using Sri Lanka's 2012 Census of Population and Housing, asking a simple question: *where* is Sri Lanka diverse, and where is it not?

---

## The Metric: How the RDI Is Computed

The Religious Diversity Index uses the **Herfindahl-Simpson concentration measure**; the same statistic used in economics to measure market concentration; applied to religious population shares. Intuitively, it answers the question: *if you picked two Sri Lankans at random, what is the probability they belong to different faiths?*

For a region with population shares $s_1, s_2, \ldots, s_n$ across $n$ faith categories:

$$\text{RDI} = \frac{10 \times (1 - \sum s_i^2)}{1 - \frac{1}{n}}$$

The denominator $1 - \frac{1}{n}$ rescales the result so that a perfectly even split across all $n$ categories yields exactly 10, regardless of how many categories are used. The sum $\sum s_i^2$ is the probability that two randomly chosen people share the same faith; subtracting it from 1 gives the probability they differ.

**Walking through Sri Lanka as a whole** (5 census categories: Buddhist, Hindu, Muslim, Christian, Other):

| Religion | Share | $s_i^2$ |
|---|---|---|
| Buddhist | 70.2% | 0.4928 |
| Hindu | 12.6% | 0.0159 |
| Muslim | 9.7% | 0.0094 |
| Christian | 7.4% | 0.0055 |
| Other | 0.1% | 0.0000 |
| **Total** | | **0.5236** |

$$\text{RDI} = \frac{10 \times (1 - 0.5236)}{1 - \frac{1}{5}} = \frac{10 \times 0.4764}{0.8} = \mathbf{5.6}$$

This matches Pew's published figure precisely. The country earns its "High" rating because no single group is completely dominant; Buddhists form a strong majority, but a meaningful quarter of the population belongs to three other traditions.

![Sri Lanka; national RDI 5.6](output/images/diversity_map_country.png)

Sri Lanka's published score and full country-level data are available in [Pew's Appendix B](https://www.pewresearch.org/wp-content/uploads/sites/20/2026/02/PR_2026.02.12_religious-diversity-around-the-world_appendix-b.pdf).

---

## Provinces: A Country of Extremes

The provincial map immediately dissolves the illusion of a uniformly diverse nation.

![Provinces](output/images/diversity_map_province.png)

- **Eastern Province (7.9; Very High)** — The most religiously diverse province by a significant margin. Its population is roughly divided three ways between Sinhalese Buddhists, Sri Lankan Tamils (Hindu), and Sri Lankan Muslims; no single group holds more than about 40%.

- **Central Province (6.1; High)** — Diversity driven almost entirely by the Indian Tamil plantation community brought by the British to work the hill-country tea estates. They are predominantly Hindu, creating a substantial counterweight to the Sinhalese Buddhist majority.

- **Western and Northern Provinces (5.0 and 5.1; Moderate)** — Both land in the Moderate band but for different reasons. Western reaches it via a large urban Muslim and Christian minority concentrated in Colombo; Northern via the Tamil Muslim community that adds religious variety to an otherwise near-entirely Hindu Tamil province.

- **North Western Province (4.9; Moderate)** — A case where one district defines the story: inland Kurunegala is decidedly Low, but coastal Puttalam (7.7; Very High) pulls the provincial average up by itself.

- **North Central and Southern Provinces (2.2 and 1.2; Low)** — The two most homogeneously Buddhist provinces, for complementary reasons. North Central is ancient Sinhalese Buddhist heartland centred on Anuradhapura; Southern's coast has seen historically little Tamil or Muslim settlement, a pattern reinforced over generations.

---

## Districts: Where the Diversity Lives

The district map reveals sub-provincial patterns that the provincial view obscures.

![Districts](output/images/diversity_map_district.png)

- **Trincomalee (7.7) and Ampara (7.3; Very High)** — The two standout east-coast districts, both products of centuries of interleaved Muslim, Tamil, and Sinhalese settlement. Trincomalee's famous natural harbour brought traders and colonisers of every background; that history is now encoded in its demographics.

- **Puttalam (7.7; Very High)** — The highest-scoring district outside the east, and the surprise of the map. A large Sri Lankan Moor (Muslim) community concentrated in coastal fishing towns sits alongside a Sinhalese Buddhist hinterland; together they produce a balance the inland north-west does not.

- **Mannar (7.2; Very High)** — A small north-western district whose large Catholic Tamil population — a direct legacy of Portuguese missionary activity — pushes it into the Very High band alongside the east-coast districts.

- **Nuwara Eliya (6.7; High)** — The heart of the estate Tamil community. In some divisions Indian Tamils are the outright majority, making it the most ethnically complex district in the hill country.

- **Hambantota (0.7; Very Low)** — The only district in the Very Low band. Over 95% of its population is Sinhalese Buddhist. The contrast with Trincomalee, just two provinces away on the same island, is the starkest illustration of how profoundly geography has shaped community composition.

---

## A Note on the DSD Level

![DS Divisions](output/images/diversity_map_dsd.png)

At the Divisional Secretariat level; over 300 administrative units; the variation becomes even starker. Many DSDs along the east coast and in the hill country plantation belt remain Very High, while large swathes of the south, north-central, and parts of the Western Province dry zone appear as solid orange and red. The finer the lens, the more clearly Sri Lanka's communities resolve into distinct geographic concentrations.

---

## Caveats: What the Index Does Not Tell You

The RDI is a useful summary statistic, but it has genuine weaknesses; and Sri Lanka provides vivid illustrations of each.

**High diversity does not mean peaceful coexistence.** Eastern Province scores 7.9; the highest in the country; yet the east was also one of the most heavily contested theatres of Sri Lanka's thirty-year civil war. Trincomalee and Ampara districts experienced some of the worst inter-communal violence of the 1980s. The index measures how mixed a population is, not how harmoniously it lives together. A score of 7.9 could describe a genuinely integrated community or a patchwork of segregated enclaves occupying the same district.

**The index is scale-sensitive.** A district that scores "Moderate" may contain GN divisions that are almost entirely composed of a single community living alongside other GN divisions of a different community. The diversity registered at district level is partly an artefact of drawing a boundary around two adjacent monocultural villages. This effect is visible when comparing the district and DSD maps: several districts that appear moderate at the district level show a mosaic of Very High and Very Low at the DSD level.

**Treating the 2024 baseline as fixed.** The 2024 census was the 2nd conducted across all of Sri Lanka following the end of the civil war in 2009. Large-scale displacement and post-war resettlement in the north and east mean the demographic landscape in those regions could still be in flux. Districts like Mullaitivu (5.1) and Kilinochchi (3.7) had seen massive population movements in the preceding decade; their 2024 figures reflect a transitional moment rather than a settled pattern.

**Near-zero categories inflate the score under normalisation.** Because the formula divides by $1 - 1/n$, adding a category that is nearly empty (like "Jews" or "religiously unaffiliated" in Sri Lanka) still increases $n$ and therefore the denominator. This effectively raises every region's score slightly relative to a 4-category formulation. This analysis uses $n = 5$ census categories; Pew's global analysis uses $n = 7$, which is part of why direct score comparisons require care.

**The index treats all groups symmetrically regardless of size.** A district split 50/50 between two groups scores identically to one split 50/50 between two different groups, regardless of the social or political significance of those groups. In Sri Lanka, where ethnicity, language, and religion are deeply intertwined, a Buddhist-Muslim balance carries different social weight than a Buddhist-Christian balance would in another context; distinctions the index cannot capture.

---

*Data: Sri Lanka Census of Population and Housing, 2024. Methodology follows the Pew Research Center's Religious Diversity Index. Analysis and maps produced using Python, GeoPandas, and Matplotlib.*
