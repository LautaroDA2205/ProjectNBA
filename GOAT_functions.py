import pandas as pd
from nba_api.stats.endpoints import playercareerstats

def load_csvs(players_path, teams_path, finals_path):
    players = pd.read_csv(players_path)
    teams = pd.read_csv(teams_path)
    finals = pd.read_csv(finals_path)
    return players, teams, finals


GOATS_IDS = {
    "Michael Jordan": 893,
    "Kobe Bryant": 977,
    "LeBron James": 2544
    }


def get_player_career(player_name, player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df = career.get_data_frames()[0]
    df["PLAYER_NAME"] = player_name
    return df


def build_career_df(goats_ids: dict):
    dfs = []
    for name, pid in goats_ids.items():
        dfs.append(get_player_career(name, pid))
    return pd.concat(dfs, ignore_index=True)


def add_per_minute_stats(df, stats):
    for stat in stats:
        df[f"{stat}_PER_MIN"] = df[stat] / df["MIN"]
    return df


def add_per_36_stats(df, stats):
    for stat in stats:
        df[f"{stat}_PER_36"] = df[f"{stat}_PER_MIN"] * 36
    return df


def prepare_metrics_df(df):
    return df[
        [
            "PLAYER_NAME", "SEASON_ID",
            "PTS_PER_36", "REB_PER_36", "AST_PER_36",
            "STL_PER_36", "BLK_PER_36",
            "FG_PCT", "FG3_PCT", "FT_PCT"
        ]
    ].copy()

from sklearn.preprocessing import MinMaxScaler

def scale_metrics(df, cols):
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[cols] = scaler.fit_transform(df_scaled[cols])
    return df_scaled


def compute_goat_index(df, weights: dict):
    df["GOAT_INDEX"] = sum(df[col] * w for col, w in weights.items())
    return df


def add_championships(df, championships_df):
    championships_df["CHAMPIONSHIPS_NORM"] = (
        championships_df["CHAMPIONSHIPS"] /
        championships_df["CHAMPIONSHIPS"].max()
    )
    return df.merge(
        championships_df[["PLAYER_NAME", "CHAMPIONSHIPS_NORM"]],
        on="PLAYER_NAME",
        how="left"
    )


def compute_final_index(df, alpha=0.9):
    df["GOAT_INDEX_FINAL"] = (
        df["GOAT_INDEX"] * alpha +
        df["CHAMPIONSHIPS_NORM"] * (1 - alpha)
    )
    return df


def career_ranking(df):
    ranking = (
        df.groupby("PLAYER_NAME", as_index=False)
        .mean(numeric_only=True)
        .sort_values("GOAT_INDEX_FINAL", ascending=False)
    )
    ranking.index += 1
    ranking.index.name = "RANK"
    return ranking

