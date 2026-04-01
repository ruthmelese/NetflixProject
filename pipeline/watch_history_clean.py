import pandas as pd


def clean_watch_history(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)
    original_len = len(df)
    print(f"Loaded {original_len} rows")

    # 1. Drop fully duplicate rows, keep first occurrence
    df = df.drop_duplicates(keep="first")
    print(f"After dedup:          {len(df)} rows (-{original_len - len(df)})")

    # 2. Fill missing watch_duration_minutes and progress_percentage with median
    dur_median = df["watch_duration_minutes"].median()
    prog_median = df["progress_percentage"].median()
    df["watch_duration_minutes"] = df["watch_duration_minutes"].fillna(dur_median)
    df["progress_percentage"] = df["progress_percentage"].fillna(prog_median)
    print(f"Filled watch_duration_minutes nulls with median: {dur_median}")
    print(f"Filled progress_percentage nulls with median:    {prog_median}")

    # 3. Fix dtypes
    df["watch_date"] = pd.to_datetime(df["watch_date"])
    df["watch_duration_minutes"] = df["watch_duration_minutes"].round(1)
    df["progress_percentage"] = df["progress_percentage"].round(1)

    print(f"Final row count:      {len(df)}")
    df.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")
    return df


if __name__ == "__main__":
    clean_watch_history(
        input_path="data/raw/watch_history.csv",
        output_path="data/clean/watch_history_clean.csv",
    )
