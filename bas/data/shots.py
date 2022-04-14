import pandas as pd
from basketball_reference_scraper.shot_charts import get_shot_chart


def get_game_shots(game) -> pd.DataFrame:
    shots = get_shot_chart(game.DATE, game.HOME_ABBREV, game.VISITOR_ABBREV)
    shot_df_home = process_shot_df(shots[game.HOME_ABBREV], game.DATE, game.HOME_ABBREV, game.VISITOR_ABBREV)
    shot_df_away = process_shot_df(shots[game.VISITOR_ABBREV], game.DATE, game.VISITOR_ABBREV, game.HOME_ABBREV)
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
