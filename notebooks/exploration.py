# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Basketball Analytics Summit (Python 3.9)
#     language: python
#     name: basketball-analytics-summit
# ---

# %%
import pandas as pd
import seaborn as sns

from basketball_reference_scraper.seasons import get_schedule
from basketball_reference_scraper.shot_charts import get_shot_chart

# %%
TEAM_NAME_TO_ABBREV = {
    'Atlanta Hawks': 'ATL',
    'Boston Celtics': 'BOS',
    'Brooklyn Nets': 'BRK',
    'Charlotte Bobcats': 'CHA',
    'Charlotte Hornets': 'CHO',
    'Chicago Bulls': 'CHI',
    'Cleveland Cavaliers': 'CLE',
    'Dallas Mavericks': 'DAL',
    'Denver Nuggets': 'DEN',
    'Detroit Pistons': 'DET',
    'Golden State Warriors': 'GSW',
    'Houston Rockets': 'HOU',
    'Indiana Pacers': 'IND',
    'Los Angeles Clippers': 'LAC',
    'Los Angeles Lakers': 'LAL',
    'Memphis Grizzlies': 'MEM',
    'Miami Heat': 'MIA',
    'Milwaukee Bucks': 'MIL',
    'Minnesota Timberwolves': 'MIN',
    'New Jersey Nets': 'NJN',
    'New Orleans Hornets': 'NOH',
    'New Orleans Pelicans': 'NOP',
    'New Orleans/Oklahoma City Hornets': 'NOK',
    'New York Knicks': 'NYK',
    'Oklahoma City Thunder': 'OKC',
    'Orlando Magic': 'ORL',
    'Philadelphia 76ers': 'PHI',
    'Phoenix Suns': 'PHO',
    'Portland Trail Blazers': 'POR',
    'Sacramento Kings': 'SAC',
    'San Antonio Spurs': 'SAS',
    'Seattle SuperSonics': 'SEA',
    'Toronto Raptors': 'TOR',
    'Utah Jazz': 'UTA',
    'Vancouver Grizzlies': 'VAN',
    'Washington Wizards': 'WAS'
}

# %%
sdf = get_schedule(2021, playoffs=False)
sdf['HOME_ABBREV'] = sdf['HOME'].map(TEAM_NAME_TO_ABBREV)
sdf['VISITOR_ABBREV'] = sdf['VISITOR'].map(TEAM_NAME_TO_ABBREV)

# %%
sdf.sample(15)

# %%
sample_game = sdf.sample(1).iloc[0]

# %%
sample_game

# %%
for row in sdf.itertuples():
    print(row.DATE)

# %%
type(row)


# %%

# %%
def get_game_shots(game) -> pd.DataFrame:
    shots = get_shot_chart(game.DATE, game.HOME_ABBREV, game.VISITOR_ABBREV)
    shot_df_home = process_shot_df(shots[game.HOME_ABBREV], game.HOME_ABBREV, game.DATE)
    shot_df_away = process_shot_df(shots[game.VISITOR_ABBREV], game.VISITOR_ABBREV, game.DATE)
    return pd.concat([shot_df_home, shot_df_away], ignore_index=True)


def process_shot_df(shot_df: pd.DataFrame, team: str, date: str) -> pd.DataFrame:
    shot_df.columns = [c.lower() for c in shot_df.columns]
    shot_df['x'] = shot_df['x'].str.replace(' ft', '').astype(float)
    shot_df['y'] = shot_df['y'].str.replace(' ft', '').astype(float)
    shot_df['distance'] = shot_df['distance'].str.replace(' ft', '').astype(float)
    shot_df['label'] = shot_df['make_miss'].map({'MAKE': 1, 'MISS': 0})
    shot_df['team'] = team
    shot_df['date'] = date
    return shot_df


# %%
shot_df = get_game_shots(row)

# %%
g = sns.relplot(
    x='x', 
    y='y', 
    hue='make_miss', 
    col='team', 
    data=shot_df, 
    palette=dict(MAKE=sns.color_palette()[2], MISS=sns.color_palette()[3])
)
g.set(xlim=(0, 50), ylim=(0, 42))

# %%
