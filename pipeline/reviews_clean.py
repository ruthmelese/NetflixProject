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

def clean_reviews(input_path: str, output_path: str) -> pd.DataFrame:
    """Clean review data and save the result."""
    try:
        logger.info(f"Starting reviews cleaning: {input_path}")

        df = pd.read_csv(input_path)
        original_len = len(df)
        logger.info(f"Loaded {original_len} rows")

        # Remove duplicate rows
        df = df.drop_duplicates(keep="first")
        logger.info(f"After dedup: {len(df)} rows")

        # Drop rows missing key numeric review fields
        before_dropna = len(df)
        df = df.dropna(subset=["helpful_votes", "total_votes", "sentiment_score"])
        logger.info(f"After dropping nulls: {len(df)} rows (removed {before_dropna - len(df)})")

        # Fix data types
        df["review_date"] = pd.to_datetime(df["review_date"])
        df["helpful_votes"] = df["helpful_votes"].astype(int)
        df["total_votes"] = df["total_votes"].astype(int)

        # review_text nulls are left intentionally
        df.to_csv(output_path, index=False)
        logger.info(f"Saved cleaned reviews data to {output_path}")
        logger.info("Reviews cleaning completed successfully")

        return df

    except FileNotFoundError:
        logger.exception(f"Reviews file not found: {input_path}")
        raise
    except KeyError as e:
        logger.exception(f"Missing expected column in reviews data: {e}")
        raise
    except Exception:
        logger.exception("Unexpected error while cleaning reviews data")
        raise

if __name__ == "__main__":
    clean_reviews(
        input_path="data/raw/reviews.csv",
        output_path="data/clean/reviews_clean.csv",
    )
