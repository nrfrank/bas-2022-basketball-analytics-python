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

from bas.data.season import get_season_schedule
from bas.data.shots import get_game_shots

# %%
season_df = get_season_schedule(2021)

# %%
print(season_df.shape)
season_df.sample(15)

# %%
sample_game = season_df.sample(1).iloc[0]

# %%
shot_df = get_game_shots(sample_game)

# %%
g = sns.relplot(
    x='x', 
    y='y', 
    hue='make_miss', 
    col='team', 
    data=shot_df, 
    palette=dict(MAKE=sns.color_palette()[2], MISS=sns.color_palette()[3])
)
g.set(
    xlim=(0, 50), 
    ylim=(0, 42)
)
g.fig.suptitle(f"{sample_game.HOME_ABBREV} v {sample_game.VISITOR_ABBREV} - {sample_game.DATE.date()}", y=1.05)

# %%
