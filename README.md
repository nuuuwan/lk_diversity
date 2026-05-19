# lk_diversity

Attempts to Replicate the Pew Research Center's Religious Diversity Index (RDI) analysis for Sri Lanka, extended to sub-national units: provinces, districts, DS divisions, GN divisions, and polling divisions.

## Background

The original global analysis was published by Pew Research Center and visualised by Voronoi:

- Voronoi article: <https://www.voronoiapp.com/category/Religious-Diversity-Around-the-World--8143>
- Pew Research: <https://www.pewresearch.org/religion/2026/02/12/religious-diversity-around-the-world/>

Sri Lanka ranks 39th globally with an RDI of 5.61 ("High"). This repo asks: how does that figure vary inside the country?

## Methodology

The Religious Diversity Index applies the Herfindahl-Hirschman concentration measure to population shares across eight religious categories used by Pew: Buddhists, Hindus, Muslims, Christians, Jews, folk religionists, other religions, and the religiously unaffiliated.

For a region with share `s_i` in category `i`:

```bash

RDI = 10 × (1 − Σ s_i²)

```

- Score ranges from 0 (one group dominates entirely) to ~8.75 (perfectly even split across 8 groups; rescaled so 10 is the theoretical max).
- Pew's bands: Very Low (<1.6), Low (1.6–3.5), Moderate (3.6–5.5), High (5.6–7.1), Very High (>7.1).

### Intuition

`Σ s_i²` is the probability that two people drawn at random from the region belong to the same group. If one group dominates, this probability is close to 1 and diversity is low. If groups are evenly mixed, the probability of a match is low and diversity is high. RDI flips and rescales this so larger numbers mean more diversity.

The measure is sensitive to evenness, not just the number of groups present. A region with 95% Buddhists and tiny slivers of four other faiths scores low; a region split 40/30/20/10 scores much higher even with fewer groups represented.
