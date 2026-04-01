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

def clean_users(input_path: str, output_path: str) -> pd.DataFrame:
    """Clean user-level data and save the result."""
    try:
        logger.info(f"Starting users cleaning: {input_path}")

        df = pd.read_csv(input_path)
        original_len = len(df)
        logger.info(f"Loaded {original_len} rows")

        # Remove duplicate rows
        df = df.drop_duplicates(keep="first")
        logger.info(f"After dedup: {len(df)} rows")

        # Mark invalid ages as missing
        invalid_age_mask = (df["age"] < 0) | (df["age"] > 100)
        df.loc[invalid_age_mask, "age"] = float("nan")
        logger.info(f"Invalid ages set to NaN: {invalid_age_mask.sum()} rows")

        # Drop rows with missing values
        before_dropna = len(df)
        df = df.dropna()
        logger.info(f"After dropping nulls: {len(df)} rows (removed {before_dropna - len(df)})")

        # Fix data types
        df["age"] = df["age"].astype(int)
        df["household_size"] = df["household_size"].astype(int)
        df["subscription_start_date"] = pd.to_datetime(df["subscription_start_date"])
        df["created_at"] = pd.to_datetime(df["created_at"])

        df.to_csv(output_path, index=False)
        logger.info(f"Saved cleaned users data to {output_path}")
        logger.info("Users cleaning completed successfully")

        return df

    except FileNotFoundError:
        logger.exception(f"Users file not found: {input_path}")
        raise
    except KeyError as e:
        logger.exception(f"Missing expected column in users data: {e}")
        raise
    except Exception:
        logger.exception("Unexpected error while cleaning users data")
        raise

if __name__ == "__main__":
    clean_users(
        input_path="data/raw/users.csv",
        output_path="data/clean/users_clean.csv",
    )
