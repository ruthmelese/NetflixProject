import pandas as pd

def clean_users(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)
    original_len = len(df)
    print(f"Loaded {original_len} rows")

    # 1. Drop fully duplicate rows, keep first occurrence
    df = df.drop_duplicates(keep="first")
    print(f"After dedup:          {len(df)} rows (-{original_len - len(df)})")

    # 2. Set invalid ages (negative or > 100) to NaN
    invalid_age_mask = (df["age"] < 0) | (df["age"] > 100)
    df.loc[invalid_age_mask, "age"] = float("nan")
    print(f"Invalid ages -> NaN:  {invalid_age_mask.sum()} rows")

    # 3. Drop rows with any remaining missing values
    before_dropna = len(df)
    df = df.dropna()
    print(f"After dropping nulls: {len(df)} rows (-{before_dropna - len(df)})")

    # 4. Fix dtypes
    df["age"] = df["age"].astype(int)
    df["household_size"] = df["household_size"].astype(int)
    df["subscription_start_date"] = pd.to_datetime(df["subscription_start_date"])
    df["created_at"] = pd.to_datetime(df["created_at"])

    print(f"Final row count:      {len(df)}")
    df.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")
    return df


if __name__ == "__main__":
    clean_users(
        input_path="data/raw/users.csv",
        output_path="data/clean/users_clean.csv",
    )
