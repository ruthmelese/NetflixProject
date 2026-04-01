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

def clean_watch_history(input_path: str, output_path: str) -> pd.DataFrame:
    """Clean watch history data and save the result."""
    try:
        logger.info(f"Starting watch history cleaning: {input_path}")

        df = pd.read_csv(input_path)
        original_len = len(df)
        logger.info(f"Loaded {original_len} rows")

        # Remove duplicate rows
        df = df.drop_duplicates(keep="first")
        logger.info(f"After dedup: {len(df)} rows")

        # Fill missing numeric values with medians
        dur_median = df["watch_duration_minutes"].median()
        prog_median = df["progress_percentage"].median()

        df["watch_duration_minutes"] = df["watch_duration_minutes"].fillna(dur_median)
        df["progress_percentage"] = df["progress_percentage"].fillna(prog_median)

        logger.info(f"Filled watch_duration_minutes nulls with median: {dur_median}")
        logger.info(f"Filled progress_percentage nulls with median: {prog_median}")

        # Fix data types / formatting
        df["watch_date"] = pd.to_datetime(df["watch_date"])
        df["watch_duration_minutes"] = df["watch_duration_minutes"].round(1)
        df["progress_percentage"] = df["progress_percentage"].round(1)

        df.to_csv(output_path, index=False)
        logger.info(f"Saved cleaned watch history data to {output_path}")
        logger.info("Watch history cleaning completed successfully")

        return df

    except FileNotFoundError:
        logger.exception(f"Watch history file not found: {input_path}")
        raise
    except KeyError as e:
        logger.exception(f"Missing expected column in watch history data: {e}")
        raise
    except Exception:
        logger.exception("Unexpected error while cleaning watch history data")
        raise

if __name__ == "__main__":
    clean_watch_history(
        input_path="data/raw/watch_history.csv",
        output_path="data/clean/watch_history_clean.csv",
    )
