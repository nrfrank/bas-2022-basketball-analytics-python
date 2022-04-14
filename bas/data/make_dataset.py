# -*- coding: utf-8 -*-
import argparse

import logging
import sys
from pathlib import Path

import pandas as pd

from bas.data.shots import get_game_shots

from bas.data.season import get_season_schedule


def main(cli_args):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('Generating full season shot dataset.')

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "season",
        type=int,
        help="The season to generate data for."
    )
    args = parser.parse_args(cli_args)
    logger.info(f'Getting schedule for season {args.season}.')
    season_df = get_season_schedule(args.season)

    logger.info(f'Generating shot data for all games in season {args.season}.')
    all_shots = []
    for row in season_df.itertuples():
        shot_df = get_game_shots(row)
        all_shots.append(shot_df)

    logger.info('Compiling game level shot data.')
    all_shots_df = pd.concat(all_shots, ignore_index=True)

    project_dir = Path(__file__).resolve().parents[2]
    save_path = project_dir / 'data' / f'shot_data_{args.season}.csv'
    logger.info(f'Writing shot data to {save_path}.')
    all_shots_df.to_csv(save_path, index=False)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main(sys.argv[1:])
