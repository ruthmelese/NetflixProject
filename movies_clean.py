import pandas as pd


def clean_movies(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)
    original_len = len(df)
    print(f"Loaded {original_len} rows")

    # 1. Drop fully duplicate rows
    df = df.drop_duplicates(keep="first")
    print(f"After dedup:            {len(df)} rows (-{original_len - len(df)})")

    # 2. Drop rows where duration_minutes == 0
    before = len(df)
    df = df[df["duration_minutes"] > 0]
    print(f"After dropping dur=0:   {len(df)} rows (-{before - len(df)})")

    # 3. Drop rows where imdb_rating < 1 
    before = len(df)
    df = df[~(df["imdb_rating"] < 1)]
    print(f"After dropping imdb<1:  {len(df)} rows (-{before - len(df)})")

    # 4. Drop rows where imdb_rating is null
    before = len(df)
    df = df.dropna(subset=["imdb_rating"])
    print(f"After dropping imdb NaN:{len(df)} rows (-{before - len(df)})")

    # 5. Fix dtypes
    df["added_to_platform"] = pd.to_datetime(df["added_to_platform"])
    df["duration_minutes"] = df["duration_minutes"].astype(int)
    df["number_of_seasons"] = df["number_of_seasons"].astype("Int64")
    df["number_of_episodes"] = df["number_of_episodes"].astype("Int64")

    # genre_secondary, production_budget, box_office_revenue,
    # number_of_seasons, number_of_episodes nulls are structural

    print(f"Final row count:        {len(df)}")
    df.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")
    return df


if __name__ == "__main__":
    clean_movies(
        input_path="data/raw/movies.csv",
        output_path="data/clean/movies_clean.csv",
    )
