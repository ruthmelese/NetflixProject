# DS 4320 Project 1: Personalized Content Recommendation
 
#### Ruth Melese: cup6cd
 
---
 
## Executive Summary
 
This repository contains the data, cleaning pipeline, and proof-of-concept recommendation code for a personalized content recommendation system built on streaming platform data. The project uses four interrelated datasets — users, watch history, reviews, and movies — to score and rank unwatched titles for a given user based on IMDb ratings, community completion rates, review sentiment, and individual genre affinity. The pipeline is demonstrated as a case study through Sarah J., a real user profile whose viewing history, preferences, and recommendations are traced end-to-end through the system. All raw data has been cleaned and documented, with full data dictionaries, bias identification, and uncertainty quantification provided for reproducibility and transparency.
 
---
 
## DOI
 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
 
> Replace the badge above after publishing to [Zenodo](https://zenodo.org): log in with GitHub → New Upload → link `ruthmelese/NetflixProject` → Publish.
 
---
 
## Press Release
 
📰 [Tired of Searching? A Recommendation System That Finds What You Want Faster](press_release.md)
 
---
 
## Problem Definition
 
### Initial General Problem and Refined Specific Problem Statement
 
Modern streaming platforms face a broader challenge of helping users navigate extremely large content libraries. As the volume of available media grows, users can become overwhelmed by the number of choices, leading to difficulty in discovering content that matches their interests. This problem is not limited to recommendation systems, but also involves platform design, search functionality, and how content is presented to users.
 
This project refines that broader challenge into a specific problem: building a recommendation system that predicts which movies or shows a user is most likely to prefer based on prior user-item interactions. Using historical interaction data, the system generates personalized recommendations in the form of ranked content suggestions. The goal is to improve relevance and reduce the time users spend searching for content.
 
Consider Sarah J., a typical subscriber who has watched 15 titles on the platform. She tends to gravitate toward Horror and Sci-Fi, finishes most of what she starts, and browses on a laptop. Despite a clear viewing profile, the platform's generic recommendations surface popular titles that don't align with her history — leaving her to scroll through hundreds of options before finding something worth watching. Sarah is the user this system is designed for.
 
### Rationale for the Refinement
 
The general problem of content discovery is too broad to address directly because it includes many overlapping issues, such as catalog size, user behavior, and platform design. Narrowing the problem to personalized recommendations makes it more measurable, since user preferences can be inferred from interaction data such as ratings, clicks, or watch history. Recommendation systems are a central part of modern content platforms. They provide a clear way to connect user behavior to a specific output, like a ranked list of suggested items. This refinement creates a problem that can be approached with existing recommendation methods and evaluated using ranking metrics.
 
### Motivation
 
The motivation for this project comes from how much recommendation systems influence the way people interact with large content platforms. With so many options available, it's easy for users to feel overwhelmed and struggle to find something they actually want to watch. Personalization helps narrow those choices by surfacing content that better matches individual preferences. When recommendations are more relevant, users can spend less time searching and more time engaging with content they enjoy. Improving recommendation systems can play an important role in shaping the overall user experience.
 
---
 
## Data
 
[Data Folder](data/clean/)
 
| Table | Description | File |
|---|---|---|
| `users_clean` | User demographic and account information, one row per user | [users_clean.csv](data/clean/users_clean.csv) |
| `watch_history_clean` | Per-session viewing activity, one row per viewing session | [watch_history_clean.csv](data/clean/watch_history_clean.csv) |
| `reviews_clean` | User-submitted movie reviews and sentiment scores, one row per review | [reviews_clean.csv](data/clean/reviews_clean.csv) |
| `movies_clean` | Movie and series metadata including genre, ratings, and platform info, one row per title | [movies_clean.csv](data/clean/movies_clean.csv) |
 
---
 
## Pipeline
 
[Pipeline Files](pipeline/)
 
| File | Description | Code |
|---|---|---|
| `users_clean.csv` | Cleaned user demographic and account data | [users_clean.py](pipeline/users_clean.py) |
| `watch_history_clean.csv` | Cleaned per-session viewing activity | [watch_history_clean.py](pipeline/watch_history_clean.py) |
| `reviews_clean.csv` | Cleaned movie reviews and sentiment scores | [reviews_clean.py](pipeline/reviews_clean.py) |
| `movies_clean.csv` | Cleaned movie metadata and ratings | [movies_clean.py](pipeline/movies_clean.py) |
 
The full problem solution pipeline is in [`pipeline/pipeline.ipynb`](pipeline/pipeline.ipynb).
 
---
 
## License
 
MIT — see [LICENSE](LICENSE)
