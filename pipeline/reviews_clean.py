import pandas as pd


def clean_reviews(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)
    original_len = len(df)
    print(f"Loaded {original_len} rows")

    # 1. Drop duplicate rows
    df = df.drop_duplicates(keep="first")
    print(f"After dedup:          {len(df)} rows (-{original_len - len(df)})")

    # 2. Drop rows missing helpful_votes, total_votes, or sentiment_score
    before_dropna = len(df)
    df = df.dropna(subset=["helpful_votes", "total_votes", "sentiment_score"])
    print(f"After dropping nulls: {len(df)} rows (-{before_dropna - len(df)})")

    # 3. Fix dtypes
    df["review_date"] = pd.to_datetime(df["review_date"])
    df["helpful_votes"] = df["helpful_votes"].astype(int)
    df["total_votes"] = df["total_votes"].astype(int)

    # review_text nulls left as NaN intentionally

    print(f"Final row count:      {len(df)}")
    df.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")
    return df


if __name__ == "__main__":
    clean_reviews(
        input_path="data/raw/reviews.csv",
        output_path="data/clean/reviews_clean.csv",
    )
