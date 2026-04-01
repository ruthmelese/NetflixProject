import logging
from pathlib import Path

import pandas as pd

# Set up logging
Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
    filename="logs/data_cleaning.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

def clean_movies(input_path: str, output_path: str) -> pd.DataFrame:
    """Clean movie metadata and save the result."""
    try:
        logger.info(f"Starting movies cleaning: {input_path}")

        df = pd.read_csv(input_path)
        original_len = len(df)
        logger.info(f"Loaded {original_len} rows")

        # Remove duplicate rows
        df = df.drop_duplicates(keep="first")
        logger.info(f"After dedup: {len(df)} rows")

        # Remove invalid runtime values
        before = len(df)
        df = df[df["duration_minutes"] > 0]
        logger.info(f"After dropping duration_minutes <= 0: {len(df)} rows (removed {before - len(df)})")

        # Remove invalid or missing IMDb ratings
        before = len(df)
        df = df[~(df["imdb_rating"] < 1)]
        logger.info(f"After dropping imdb_rating < 1: {len(df)} rows (removed {before - len(df)})")

        before = len(df)
        df = df.dropna(subset=["imdb_rating"])
        logger.info(f"After dropping missing imdb_rating: {len(df)} rows (removed {before - len(df)})")

        # Fix data types
        df["added_to_platform"] = pd.to_datetime(df["added_to_platform"])
        df["duration_minutes"] = df["duration_minutes"].astype(int)
        df["number_of_seasons"] = df["number_of_seasons"].astype("Int64")
        df["number_of_episodes"] = df["number_of_episodes"].astype("Int64")

        # Structural nulls are left as-is for secondary genre, budget, revenue, and series fields
        df.to_csv(output_path, index=False)
        logger.info(f"Saved cleaned movies data to {output_path}")
        logger.info("Movies cleaning completed successfully")

        return df

    except FileNotFoundError:
        logger.exception(f"Movies file not found: {input_path}")
        raise
    except KeyError as e:
        logger.exception(f"Missing expected column in movies data: {e}")
        raise
    except Exception:
        logger.exception("Unexpected error while cleaning movies data")
        raise

if __name__ == "__main__":
    clean_movies(
        input_path="data/raw/movies.csv",
        output_path="data/clean/movies_clean.csv",
    )
