import pandas as pd

try:
    df = pd.read_csv("athlete_events.csv")
except pd.errors.EmptyDataError:
    df = pd.DataFrame()

try:
    region_df = pd.read_csv("noc_regions.csv")
except pd.errors.EmptyDataError:
    region_df = pd.DataFrame()


def preprocess():
    global df, region_df

    if df.empty or region_df.empty:
        return pd.DataFrame()

    df_filtered = df[df["Season"] == "Summer"]

    df_merged = df_filtered.merge(region_df, how="left", on="NOC")

    df_merged.drop_duplicates(inplace=True)

    medal_dummies = pd.get_dummies(df_merged["Medal"])

    df_final = pd.concat([df_merged, medal_dummies], axis=1)

    return df_final