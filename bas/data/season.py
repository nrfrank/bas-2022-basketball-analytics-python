import pandas as pd
from basketball_reference_scraper.seasons import get_schedule

from bas.data import TEAM_NAME_TO_ABBREV


def get_season_schedule(season: int, include_playoffs: bool = False) -> pd.DataFrame:
    sdf = get_schedule(season, playoffs=include_playoffs)
    sdf['HOME_ABBREV'] = sdf['HOME'].map(TEAM_NAME_TO_ABBREV)
    sdf['VISITOR_ABBREV'] = sdf['VISITOR'].map(TEAM_NAME_TO_ABBREV)
    return sdf

