# DS 4320 Project 1: Personalized Content Recommendation

**Ruth Melese (cup6cd)**

---

## Executive Summary

This repository contains the data, cleaning pipeline, and proof-of-concept recommendation system for a personalized content recommendation system built on streaming platform data. The project uses four interrelated datasets — users, watch history, reviews, and movies — to score and rank unwatched titles for a given user based on IMDb ratings, community completion rates, review sentiment, and individual genre affinity. The pipeline demonstrates how structured relational data can be used to generate personalized recommendations that improve content discovery and reduce search time.

---

## Project Information

- **DOI:** [Insert DOI after publishing to Zenodo]
- **Press Release:** [Tired of Searching? A Recommendation System That Finds What You Want Faster](press_release.md)
- **Data:** [[OneDrive Folder Link](https://myuva-my.sharepoint.com/:f:/g/personal/cup6cd_virginia_edu/IgAjhQzKwslGR7JxSBBK85FaAeGtPGEIYve6gsApg2Y2YDw?e=zrpke6)]
- **Pipeline:** [pipeline/pipeline.ipynb](pipeline/pipeline.ipynb)
- **License:** MIT (see LICENSE)

---

## Problem Definition

### Initial General Problem and Refined Specific Problem Statement

Modern streaming platforms face a broader challenge of helping users navigate extremely large content libraries. As the volume of available media grows, users can become overwhelmed by the number of choices, leading to difficulty in discovering content that matches their interests. This problem extends beyond recommendation systems and includes platform design, search functionality, and content organization.

This project refines that broader challenge into a specific problem: building a recommendation system that predicts which movies or shows a user is most likely to prefer based on prior user-item interactions. Using historical interaction data, the system generates personalized recommendations in the form of ranked content suggestions. The goal is to improve relevance and reduce the time users spend searching for content.

### Rationale for the Refinement

The general problem of content discovery is too broad to address directly because it includes many overlapping factors. Narrowing the problem to personalized recommendations makes it measurable and actionable. User preferences can be inferred from interaction data such as watch history, completion behavior, and ratings. This allows the problem to be framed as a ranking task, where the goal is to order content by predicted relevance.

### Representative User Context

Consider Sarah J., a typical streaming platform user who has watched 15 titles. Her viewing history shows a consistent preference for Horror and Sci-Fi, and she tends to complete most of what she starts. Despite this clear pattern, the platform surfaces largely generic or globally popular recommendations that do not reflect her preferences.

As a result, Sarah spends a disproportionate amount of time searching for content, even though her interests are well-defined in the data. This gap between available behavioral signals and the recommendations produced highlights the need for a system that better translates user interaction data into relevant suggestions.

### Motivation

Recommendation systems shape how users experience digital platforms. Without personalization, users may struggle to find relevant content in large catalogs. Improving recommendation quality can reduce search time and increase engagement. This project explores how structured relational data and user behavior signals can be used to generate more relevant recommendations.

---

## Domain Exposition

### Terminology

| Term | Definition |
|---|---|
| Recommender System | A system that predicts which items a user is likely to prefer and presents them in a ranked order. |
| Personalization | Tailoring content suggestions to an individual user based on their behavior or preferences. |
| Collaborative Filtering | A recommendation method that uses patterns in user-item interactions to suggest items. |
| Content-Based Filtering | A recommendation method that suggests items similar to those a user already liked. |
| User-Item Interaction | Any signal connecting a user to an item, such as a rating, click, watch, or purchase. |
| Ranking | The process of ordering candidate items from most relevant to least relevant. |
| Candidate Generation | The stage where a system narrows a very large catalog to a smaller set of possible recommendations. |
| Matrix Factorization | A collaborative filtering technique that represents users and items as low-dimensional embeddings. |
| Embedding | A learned numerical representation of a user or item in a latent feature space. |
| Relevance Metric | A metric used to evaluate how useful recommendations are, such as precision, recall, or NDCG. |
| Cold Start Problem | The challenge of making recommendations for new users or new items with little to no interaction data. |
| Data Sparsity | A situation where most users have interacted with only a small fraction of available items, making it harder to learn preferences. |
| Latent Factors | Hidden features learned from data that represent underlying patterns in user preferences and item characteristics. |
| Top-N Recommendation | A list of the top N items predicted to be most relevant to a user. |
Source: https://developers.google.com/machine-learning/recommendation/overview/candidate-generation

### Domain Overview

This project falls within the domain of recommender systems, which is a branch of machine learning and information retrieval focused on helping users discover relevant items from large catalogs. Recommendation systems are widely used by streaming services, online stores, and social media platforms to personalize what each user sees. In practice, these systems often rely on collaborative filtering, content-based methods, or hybrid approaches that combine multiple signals. Large-scale platforms also structure recommendations as a pipeline that includes candidate generation, scoring, and ranking. The domain is centered on predicting user preference and presenting results in a way that improves relevance, discovery, and user engagement.

### Background Reading

| Title | Description | Link to file in folder |
|---|---|---|
| Evaluating Recommender Systems | Recommender systems are typically evaluated using ranking and relevance metrics such as precision and recall. These metrics provide a clearer picture of how useful recommendations are beyond simple accuracy. | [evaluating_recommender_systems.pdf](https://myuva-my.sharepoint.com/:b:/g/personal/cup6cd_virginia_edu/IQBBH1fCWuE4RZsqA54qXhsXAXfkSVPzkk9crTc4knY-iz4?e=ecMFK0) |
| Matrix Factorization for Recommendations | Matrix factorization models user-item interactions by mapping both users and items into a shared latent space. This approach allows systems to uncover hidden patterns in preferences and generate personalized recommendations. | [matrix_factorization.pdf](https://myuva-my.sharepoint.com/:b:/g/personal/cup6cd_virginia_edu/IQCD1KEe8c7mQ43zsfVAHgPRAQT69sfRUEIzHXN0wODqENM?e=Lkzvdk) |
| Neural Collaborative Filtering | Neural collaborative filtering extends traditional methods by using neural networks to learn complex user-item relationships. This approach can improve recommendation quality by capturing non-linear patterns in the data. | [neural_collaborative_filtering.pdf](https://myuva-my.sharepoint.com/:b:/g/personal/cup6cd_virginia_edu/IQCgX1dIVenTQ6mqp-ZOmaOuAf0STnvPUvaD3JeYor09gls?e=Ozw1Eu) |
| Limitations of Collaborative Filtering | Collaborative filtering methods often struggle with issues like cold start and sparse data. These limitations can reduce recommendation quality, especially for new users or less popular items. | [collaborative_filtering_limitations.pdf](https://myuva-my.sharepoint.com/:b:/g/personal/cup6cd_virginia_edu/IQBFD0GAQVaeQZUuBXJHqKUTAY_6JKnsuFzmtLW2zJxdl_I?e=6P6TDV) |
| System Architectures for Personalization and Recommendation | Large-scale recommendation systems are typically built as pipelines that include candidate generation, ranking, and filtering stages. These components work together to efficiently deliver personalized content to users. | [recommendation_system_architecture.pdf](https://myuva-my.sharepoint.com/:b:/g/personal/cup6cd_virginia_edu/IQCJ_eIKu7wpTpaHmBU7YmebAUUe4umNSHjE5btBuRdaYJM?e=wHKS2r) |

---

## Data Creation

### Data Acquisition (Provenance)

The dataset used in this project was sourced from a publicly available Kaggle dataset containing user interaction and media metadata. The raw data included user profiles, viewing history, movie attributes, and review information. These datasets were initially stored in separate files with inconsistent formats and varying levels of completeness.

The data was cleaned and transformed into a structured relational format using Python scripts. This process included removing invalid entries, standardizing identifiers, and organizing the data into separate tables representing users, movies, watch history, and reviews.

### Code Used to Create Data

| File | Description | Link |
|------|-------------|------|
| users_clean.py | Cleans and standardizes user-level data, including handling missing values and ensuring consistent user identifiers for downstream joins | https://github.com/ruthmelese/NetflixProject/blob/main/pipeline/users_clean.py |
| watch_history_clean.py | Processes raw viewing session data, deriving completion metrics and structuring user–content interactions for analysis | https://github.com/ruthmelese/NetflixProject/blob/main/pipeline/watch_history_clean.py |
| reviews_clean.py | Cleans review and rating data, normalizing user feedback and preparing sentiment and rating signals for modeling | https://github.com/ruthmelese/NetflixProject/blob/main/pipeline/reviews_clean.py |
| movies_clean.py | Cleans and organizes movie metadata, including genres and external ratings, to support feature engineering and recommendation scoring | https://github.com/ruthmelese/NetflixProject/blob/main/pipeline/movies_clean.py |

### Bias Identification

The dataset may not fully represent real-world streaming behavior. It is limited to a sample of users and may reflect popularity bias, where widely viewed or highly rated content is overrepresented. Additionally, user interaction data may be incomplete, which can distort preference signals.

### Bias Mitigation

Bias is addressed by incorporating multiple signals rather than relying on a single metric. The model combines ratings, completion behavior, and genre preferences to reduce reliance on any one biased feature. Results are interpreted cautiously and framed as illustrative rather than definitive.

### Rationale and Uncertainty

The dataset was structured into relational tables to support efficient querying and modeling. Features such as completion rate and genre affinity were selected because they provide interpretable signals of user preference. Uncertainty arises from missing data, subjective ratings, and variability in user behavior, which may affect the reliability of predictions.

---

## Metadata

### Schema (ER Diagram)

[Insert ER diagram image here]

### Data Tables

| Table | Description | Link |
|------|-------------|------|
| Users | User-level information | [users_clean.csv](https://myuva-my.sharepoint.com/:x:/g/personal/cup6cd_virginia_edu/IQA28B07xeZ6S67kSPG6l3oMAfP3mKQrtl0-A8uC-mXjfNo?e=I1CQQb) |
| Movies | Movie metadata | [movies_clean.csv](https://myuva-my.sharepoint.com/:x:/g/personal/cup6cd_virginia_edu/IQDEHxo6M-YwRrY2xktXA8omASj1VLhVXSMnUrnjruEUxj8?e=8OlPay) |
| Watch History | Viewing sessions | [watch_history_clean.csv](https://myuva-my.sharepoint.com/:x:/g/personal/cup6cd_virginia_edu/IQAYhtJwd6agSqN8i7rPL4R5ASvwOE8PtPXNW_KO_maZ5H4?e=vaDYR4) |
| Reviews | User reviews and ratings | [reviews_clean.csv](https://myuva-my.sharepoint.com/:x:/g/personal/cup6cd_virginia_edu/IQDvOiXLZzPtQKbH2ImqqbB5AQa5w4R7Qv-UHQVvj7UhwL4?e=b2WZDJ) |

### Item 3. Data Dictionary

users_clean (6,175 rows)

| Feature | Type | Description | Example |
|---|---|---|---|
| `user_id` | string | Unique identifier for each user | `user_00001` |
| `email` | string | User email address | `figueroajohn@example.org` |
| `first_name` | string | User's first name | `Erica` |
| `last_name` | string | User's last name | `Garza` |
| `age` | integer | User's age in years | `43` |
| `gender` | string | User's reported gender (`Male`, `Female`, `Other`, `Prefer not to say`) | `Male` |
| `country` | string | Country of residence | `USA` |
| `state_province` | string | State or province of residence | `Massachusetts` |
| `city` | string | City of residence | `North Jefferyhaven` |
| `subscription_plan` | string | Current subscription tier (`Basic`, `Standard`, `Premium`, `Premium+`) | `Basic` |
| `subscription_start_date` | date | Date the user's current subscription began | `2024-04-08` |
| `is_active` | boolean | Whether the user's account is currently active | `True` |
| `monthly_spend` | float | Monthly spend in USD | `36.06` |
| `primary_device` | string | Device most used for viewing (`Laptop`, `Desktop`, `Tablet`, `Mobile`, `Gaming Console`) | `Laptop` |
| `household_size` | integer | Number of people in the user's household | `1` |
| `created_at` | datetime | Timestamp when the account was created | `2023-04-01 14:40:50` |

watch_history_clean (100,000 rows)

| Feature | Type | Description | Example |
|---|---|---|---|
| `session_id` | string | Unique identifier for each viewing session | `session_000001` |
| `user_id` | string | Identifier of the user who watched (foreign key → `users_clean`) | `user_07271` |
| `movie_id` | string | Identifier of the title watched (foreign key → `movies_clean`) | `movie_0511` |
| `watch_date` | date | Date the session occurred | `2025-11-13` |
| `device_type` | string | Device used during the session (`Tablet`, `Laptop`, `Desktop`, `Mobile`, `Smart TV`) | `Tablet` |
| `watch_duration_minutes` | float | Total minutes watched in the session; nulls filled with median (51.2) | `63.9` |
| `progress_percentage` | float | Percentage of the title completed; nulls filled with median (49.8) | `34.6` |
| `action` | string | Last recorded playback action (`started`, `paused`, `stopped`, `completed`) | `completed` |
| `quality` | string | Streaming quality selected (`SD`, `HD`, `4K`, `Ultra HD`) | `HD` |
| `location_country` | string | Country where the session occurred | `USA` |
| `is_download` | boolean | Whether the content was downloaded for offline viewing | `False` |
| `user_rating` | float | In-session rating given by user (1–5); ~80% null as most users do not rate | `4.0` |

reviews_clean (12,204 rows)

| Feature | Type | Description | Example |
|---|---|---|---|
| `review_id` | string | Unique identifier for each review | `review_000001` |
| `user_id` | string | Identifier of the reviewing user (foreign key → `users_clean`) | `user_07066` |
| `movie_id` | string | Identifier of the reviewed title (foreign key → `movies_clean`) | `movie_0360` |
| `rating` | integer | Star rating given by the user (1–5) | `4` |
| `review_date` | date | Date the review was submitted | `2025-03-29` |
| `device_type` | string | Device used when submitting the review | `Mobile` |
| `is_verified_watch` | boolean | Whether the user has a verified watch session for this title | `False` |
| `helpful_votes` | integer | Number of users who marked the review as helpful | `3` |
| `total_votes` | integer | Total number of votes the review received | `5` |
| `review_text` | string | Free-text body of the review; 636 rows null | `Fantastic cinematography and plot twists.` |
| `sentiment` | string | Predicted sentiment label (`positive`, `neutral`, `negative`) | `positive` |
| `sentiment_score` | float | Confidence score for the sentiment prediction (0–1) | `0.711` |

movies_clean (843 rows)

| Feature | Type | Description | Example |
|---|---|---|---|
| `movie_id` | string | Unique identifier for each title | `movie_0002` |
| `title` | string | Title of the movie or series | `Storm Warrior` |
| `content_type` | string | Type of content (`Movie`, `TV Series`, `Limited Series`, `Documentary`, `Stand-up Comedy`) | `Stand-up Comedy` |
| `genre_primary` | string | Primary genre | `Sci-Fi` |
| `genre_secondary` | string | Secondary genre; null for ~64% of titles that have only one genre | `Mystery` |
| `release_year` | integer | Year the title was originally released | `2017` |
| `duration_minutes` | integer | Runtime in minutes (per episode for series) | `37` |
| `rating` | string | Content rating (`G`, `PG`, `PG-13`, `R`, `NC-17`, `TV-Y`, `TV-Y7`, `TV-G`, `TV-PG`, `TV-14`, `TV-MA`) | `PG` |
| `language` | string | Primary language of the title | `Japanese` |
| `country_of_origin` | string | Country where the title was produced | `USA` |
| `imdb_rating` | float | IMDb rating (1–10) | `3.3` |
| `production_budget` | float | Production budget in USD; null for non-Movie content types | `2114120` |
| `box_office_revenue` | float | Box office revenue in USD; null for non-Movie content types | `792291` |
| `number_of_seasons` | integer | Number of seasons; null for Movies, Documentaries, and Stand-up Comedy | `12` |
| `number_of_episodes` | integer | Total number of episodes; null for Movies, Documentaries, and Stand-up Comedy | `32` |
| `is_netflix_original` | boolean | Whether the title is a platform original | `False` |
| `added_to_platform` | date | Date the title was made available on the platform | `2022-01-28` |
| `content_warning` | boolean | Whether the title carries a content warning | `True` |

### Item 4. Uncertainty Quantification (Numerical Features)

| Table | Feature | Min | Max | Mean | Std Dev | Notes |
|---|---|---|---|---|---|---|
| `users_clean` | `age` | 1 | 97 | 35.04 | 12.15 | Ages outside 0–100 set to null and dropped; small values (1–12) may still be erroneous |
| `users_clean` | `monthly_spend` | 0.11 | 997.80 | 21.85 | 64.89 | High std dev driven by outliers near $998; median ($13.53) is a more reliable central estimate |
| `users_clean` | `household_size` | 1 | 8 | 2.87 | 1.56 | Self-reported; may not reflect actual household composition |
| `watch_history_clean` | `watch_duration_minutes` | 0.2 | 799.3 | 63.99 | 64.30 | ~12% of values filled with median (51.2); sessions >600 min retained but may reflect idle playback |
| `watch_history_clean` | `progress_percentage` | 0.0 | 100.0 | 49.95 | 27.65 | ~8% of values filled with median (49.8); introduces artificial clustering near 49.8 |
| `watch_history_clean` | `user_rating` | 1.0 | 5.0 | 3.36 | 1.24 | ~80% null; only users who actively rated are represented — subject to strong self-selection bias |
| `reviews_clean` | `rating` | 1 | 5 | 3.66 | 1.11 | Subject to self-selection bias; reviewers tend toward stronger opinions than average viewers |
| `reviews_clean` | `helpful_votes` | 0 | 13 | 3.00 | 1.73 | Low-engagement reviews may be systematically under-rated |
| `reviews_clean` | `total_votes` | 0 | 16 | 5.36 | 2.02 | Reviews with 0 total votes carry no helpfulness signal |
| `reviews_clean` | `sentiment_score` | 0.0 | 1.0 | 0.64 | 0.25 | Scores near 0.5 indicate high uncertainty in sentiment classification |
| `movies_clean` | `release_year` | 1953 | 2024 | 2006.39 | 11.45 | Older titles may have incomplete metadata (budget, IMDb rating) |
| `movies_clean` | `duration_minutes` | 6 | 586 | 90.51 | 70.80 | Represents per-episode runtime for series; not directly comparable to Movie runtime |
| `movies_clean` | `imdb_rating` | 1.0 | 10.0 | 6.37 | 1.68 | Ratings below 1.0 dropped as invalid; missing ratings (~14%) also dropped |
| `movies_clean` | `production_budget` | 68,373 | 197,326,642 | 11,037,097 | 24,303,599 | ~63% null (non-Movie types); high std dev reflects blockbuster outliers |
| `movies_clean` | `box_office_revenue` | 28,637 | 2,032,055,569 | 61,476,590 | 162,596,158 | ~67% null; dominated by a small number of high-grossing titles |
| `movies_clean` | `number_of_seasons` | 1 | 14 | 7.34 | 4.04 | Null for all non-series content types by design |
| `movies_clean` | `number_of_episodes` | 6 | 199 | 101.01 | 56.44 | Null for all non-series content types by design |

### Uncertainty in Numerical Features

Numerical features such as ratings and completion rates contain inherent uncertainty. Ratings are subjective and vary across users, while completion rates may be influenced by external factors unrelated to preference. Missing or sparse data may reduce reliability for less active users or less popular titles.

---

## Press Release

See [press-release.md](press-release.md)

---

## Pipeline

The full pipeline is implemented in:

[pipeline/pipeline.ipynb](pipeline/pipeline.ipynb)

### Case Study: Recommendation for Sarah J.

To evaluate the system, the pipeline is applied to the representative user described earlier. Sarah’s interaction history is used to construct features such as genre affinity, completion behavior, and exposure to highly rated content.

The model scores all unseen titles and ranks them based on predicted relevance. Titles aligned with her preferred genres and strong engagement metrics receive higher scores. Compared to generic recommendations, this approach produces suggestions that better reflect her viewing behavior and reduces the need for extended browsing.

---

## License

MIT — see LICENSE
