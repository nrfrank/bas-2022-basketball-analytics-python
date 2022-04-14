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
