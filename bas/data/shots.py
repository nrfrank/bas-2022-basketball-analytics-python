import pandas as pd
from basketball_reference_scraper.shot_charts import get_shot_chart


def get_game_shots(date: str, home: str, visitor: str) -> pd.DataFrame:
    """Retrieve all shots for a given NBA game.

    Args:
        date (str): The date of the NBA game.
        home (str): Abbreviation of the home team. See allowed values in bas.data.TEAM_NAME_TO_ABBREV
        visitor (str): Abbreviation of the away (visiting) team. See allowed values in bas.data.TEAM_NAME_TO_ABBREV

    Returns:
        pandas.DataFrame of all shots for both teams

    """
    shots = get_shot_chart(date, home, visitor)
    shot_df_home = process_shot_df(
        shots[home],
        date,
        home,
        visitor
    )
    shot_df_away = process_shot_df(
        shots[visitor],
        date,
        visitor,
        home
    )
    return pd.concat([shot_df_home, shot_df_away], ignore_index=True)


def process_shot_df(shot_df: pd.DataFrame, date: str, team: str, opponent: str) -> pd.DataFrame:
    shot_df.columns = [c.lower() for c in shot_df.columns]
    shot_df['x'] = shot_df['x'].str.replace(' ft', '').astype(float)
    shot_df['y'] = shot_df['y'].str.replace(' ft', '').astype(float)
    shot_df['distance'] = shot_df['distance'].str.replace(' ft', '').astype(float)
    shot_df['label'] = shot_df['make_miss'].map({'MAKE': 1, 'MISS': 0})
    shot_df['date'] = date
    shot_df['team'] = team
    shot_df['opponent'] = opponent
    return shot_df
