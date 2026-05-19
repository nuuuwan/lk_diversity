# lk_diversity

Attempts to Replicate the Pew Research Center's Religious Diversity Index (RDI) analysis for Sri Lanka, extended to sub-national units: provinces, districts, DS divisions, GN divisions, and polling divisions.

## Background

The original global analysis was published by Pew Research Center and visualised by Voronoi:

- Voronoi article: <https://www.voronoiapp.com/category/Religious-Diversity-Around-the-World--8143>
- Voronoi visualization: <https://www.voronoiapp.com/_next/image?url=https%3A%2F%2Fcdn.voronoiapp.com%2Fpublic%2Fimages%2F569b3be9-d493-498d-b76e-5b5a36201950.webp&w=1080&q=85>
- Pew Research: <https://www.pewresearch.org/religion/2026/02/12/religious-diversity-around-the-world/>

Sri Lanka has an RDI of 5.6 ("High") as of 2020, unchanged from 2010. This repo asks: how does that figure vary inside the country?

## Methodology

The Religious Diversity Index is a normalised Herfindahl-Simpson concentration measure applied to population shares across the seven religious categories used by Pew: Christians, Muslims, Hindus, Buddhists, Jews, adherents of all other religions, and the religiously unaffiliated.

For a region with share `s_i` in each of `n` categories:

```

RDI = 10 × (1 − Σ s_i²) / (1 − 1/n)

```

The `(1 − 1/n)` denominator rescales so a perfectly even split across all `n` categories scores exactly 10, regardless of how many categories are used. With Pew's `n = 7`, the scaling factor is `10 / (1 − 1/7) ≈ 11.67`.

- Score ranges from 0 (one group dominates entirely) to 10 (perfectly even split across all categories).
- Pew's bands: Very Low (<1.0), Low (1.0–2.9), Moderate (3.0–5.4), High (5.5–6.9), Very High (≥7.0).

### Verification against Pew

Pew's 2020 shares for Sri Lanka: Buddhists 69.6%, Hindus 14.5%, Muslims 10.2%, Christians 5.6%, others <0.1%.

```

Σ s_i² = 0.696² + 0.145² + 0.102² + 0.056² ≈ 0.5189
RDI = 10 × (1 − 0.5189) / (1 − 1/7) ≈ 11.67 × 0.4811 ≈ 5.6 

```

### Intuition

`Σ s_i²` is the probability that two people drawn at random from the region belong to the same group. If one group dominates, this probability is close to 1 and diversity is low. If groups are evenly mixed, the probability of a match is low and diversity is high. RDI flips and rescales this so larger numbers mean more diversity.

The measure is sensitive to evenness, not just the number of groups present. A region with 95% Buddhists and tiny slivers of four other faiths scores low; a region split 40/30/20/10 scores much higher even with fewer groups represented.
