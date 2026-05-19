# lk_diversity

Attempts to Replicate the Pew Research Center's Religious Diversity Index (RDI) analysis for Sri Lanka, extended to sub-national units: provinces, districts, DS divisions, GN divisions, and polling divisions.

## Background

The original global analysis was published by Pew Research Center and visualised by Voronoi:

- Voronoi article: <https://www.voronoiapp.com/category/Religious-Diversity-Around-the-World--8143>
- Voronoi visualization: <https://www.voronoiapp.com/_next/image?url=https%3A%2F%2Fcdn.voronoiapp.com%2Fpublic%2Fimages%2F569b3be9-d493-498d-b76e-5b5a36201950.webp&w=1080&q=85>
- Pew Research: <https://www.pewresearch.org/religion/2026/02/12/religious-diversity-around-the-world/>
- Pew's score (5.6) for Sri Lanka: <https://www.pewresearch.org/wp-content/uploads/sites/20/2026/02/PR_2026.02.12_religious-diversity-around-the-world_appendix-b.pdf>

Sri Lanka has an RDI of 5.6 ("High") as of 2020, unchanged from 2010. This repo asks: how does that figure vary inside the country?

## Methodology

The Religious Diversity Index is a normalised Herfindahl-Simpson concentration measure applied to population shares across the seven religious categories used by Pew: Christians, Muslims, Hindus, Buddhists, Jews, adherents of all other religions, and the religiously unaffiliated.

For a region with share `s_i` in each of `n` categories:

```bash
RDI = 10 × (1 − Σ s_i²) / (1 − 1/n)
```

## Analysis

See [ANALYSIS.md](ANALYSIS.md).
