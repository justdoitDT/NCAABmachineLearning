import pandas as pd
import numpy as np
from datetime import datetime

# UNTESTED

startingSeason = 2006
rootDirectory = '/Users/dthomas/Desktop/Coding/NCAAB/testing9-29-2023'

# initialize DataFrame to contain input data
emptyInputDF = pd.DataFrame(columns=[
    'Labels',  # True if Team A wins, False if Team B wins
    'TeamID A',  # not a feature
    'TeamID B',  # not a feature

    # home-court advantage
    'HomeAdv A',  # +1 if Team A is Home, 0 if neutral site, -1 if Team A is Away

    # Team A season totals

    'NumGamesPlayedThisSeason A',  # the number of games Team A has played during the current season

    'WinPctThisSeason A',  # win percentage for Team A during the current season
    'WinPctLastSeason A',  # win percentage for Team A during the previous season
    'WinPct2SeasonsAgo A',  # win percentage for Team A during the season 2 years prior
    'WinPct3SeasonsAgo A',  # win percentage for Team A during the season 3 years prior

    'FlipCloseWinPctThisSeason A',  # win percentage for Team A during the current season (had the results of all of their close games been flipped)
    'FlipCloseWinPctLastSeason A',  # win percentage for Team A during the previous season (had the results of all of their close games been flipped)
    'FlipCloseWinPct2SeasonsAgo A',  # win percentage for Team A during the season 2 years prior (had the results of all of their close games been flipped)
    'FlipCloseWinPct3SeasonsAgo A',  # win percentage for Team A during the season 3 years prior (had the results of all of their close games been flipped)

    'WinCloseWinPctThisSeason A',  # win percentage for Team A during the current season (had they won all of their close games)
    'WinCloseWinPctLastSeason A',  # win percentage for Team A during the previous season (had they won all of their close games)
    'WinCloseWinPct2SeasonsAgo A',  # win percentage for Team A during the season 2 years prior (had they won all of their close games)
    'WinCloseWinPct3SeasonsAgo A',  # win percentage for Team A during the season 3 years prior (had they won all of their close games)

    'LoseCloseWinPctThisSeason A',  # win percentage for Team A during the current season (had they lost all of their close games)
    'LoseCloseWinPctLastSeason A',  # win percentage for Team A during the previous season (had they lost all of their close games)
    'LoseCloseWinPct2SeasonsAgo A',  # win percentage for Team A during the season 2 years prior (had they lost all of their close games)
    'LoseCloseWinPct3SeasonsAgo A',  # win percentage for Team A during the season 3 years prior (had they lost all of their close games)

    'PointsPerGameThisSeason A',  # average points scored by Team A per game during the current season
    'PointsPerGameLastSeason A',  # average points scored by Team A per game during the previous season
    'PointsPerGame2SeasonsAgo A',  # average points scored by Team A per game during the season 2 years prior
    'PointsPerGame3SeasonsAgo A',  # average points scored by Team A per game during the season 3 years prior

    'PointsAllowedPerGameThisSeason A',  # average points allowed by Team A per game during the current season
    'PointsAllowedPerGameLastSeason A',  # average points allowed by Team A per game during the previous season
    'PointsAllowedPerGame2SeasonsAgo A',  # average points allowed by Team A per game during the season 2 years prior
    'PointsAllowedPerGame3SeasonsAgo A',  # average points allowed by Team A per game during the season 3 years prior

    'PointsMarginPerGameThisSeason A',  # average difference between points scored by Team A and points allowed by Team A per game during the current season
    'PointsMarginPerGameLastSeason A',  # average difference between points scored by Team A and points allowed by Team A per game during the previous season
    'PointsMarginPerGame2SeasonsAgo A',  # average difference between points scored by Team A and points allowed by Team A per game during the season 2 years prior
    'PointsMarginPerGame3SeasonsAgo A',  # average difference between points scored by Team A and points allowed by Team A per game during the season 3 years prior

    'FGMPerGameThisSeason A',  # average number of field goals made by Team A per game during the current season
    'FGMPerGameLastSeason A',  # average number of field goals made by Team A per game during the previous season
    'FGMPerGame2SeasonsAgo A',  # average number of field goals made by Team A per game during the season 2 years prior
    'FGMPerGame3SeasonsAgo A',  # average number of field goals made by Team A per game during the season 3 years prior

    'FGMAllowedPerGameThisSeason A',  # average number of field goals allowed by Team A per game during the current season
    'FGMAllowedPerGameLastSeason A',  # average number of field goals allowed by Team A per game during the previous season
    'FGMAllowedPerGame2SeasonsAgo A',  # average number of field goals allowed by Team A per game during the season 2 years prior
    'FGMAllowedPerGame3SeasonsAgo A',  # average number of field goals allowed by Team A per game during the season 3 years prior

    'FGMMarginPerGameThisSeason A',  # average difference between field goals made by Team A and field goals allowed by Team A per game during the current season
    'FGMMarginPerGameLastSeason A',  # average difference between field goals made by Team A and field goals allowed by Team A per game during the previous season
    'FGMMarginPerGame2SeasonsAgo A',  # average difference between field goals made by Team A and field goals allowed by Team A per game during the season 2 years prior
    'FGMMarginPerGame3SeasonsAgo A',  # average difference between field goals made by Team A and field goals allowed by Team A per game during the season 3 years prior

    'FGAPerGameThisSeason A',  # average number of field goals attempted by Team A per game during the current season
    'FGAPerGameLastSeason A',  # average number of field goals attempted by Team A per game during the previous season
    'FGAPerGame2SeasonsAgo A',  # average number of field goals attempted by Team A per game during the season 2 years prior
    'FGAPerGame3SeasonsAgo A',  # average number of field goals attempted by Team A per game during the season 3 years prior

    'FGAAllowedPerGameThisSeason A',  # average number of field goal attempts allowed by Team A per game during the current season
    'FGAAllowedPerGameLastSeason A',  # average number of field goal attempts allowed by Team A per game during the previous season
    'FGAAllowedPerGame2SeasonsAgo A',  # average number of field goal attempts allowed by Team A per game during the season 2 years prior
    'FGAAllowedPerGame3SeasonsAgo A',  # average number of field goal attempts allowed by Team A per game during the season 3 years prior

    'FGAMarginPerGameThisSeason A',  # average difference between number of field goals attempted by Team A and number of field goal attempts allowed by Team A per game during the current season
    'FGAMarginPerGameLastSeason A',  # average difference between number of field goals attempted by Team A and number of field goal attempts allowed by Team A per game during the previous season
    'FGAMarginPerGame2SeasonsAgo A',  # average difference between number of field goals attempted by Team A and number of field goal attempts allowed by Team A per game during the season 2 years prior
    'FGAMarginPerGame3SeasonsAgo A',  # average difference between number of field goals attempted by Team A and number of field goal attempts allowed by Team A per game during the season 3 years prior

    'FGPctThisSeason A',  # Team A's field goal percentage during the current season
    'FGPctLastSeason A',  # Team A's field goal percentage during the previous season
    'FGPct2SeasonsAgo A',  # Team A's field goal percentage during the season 2 years prior
    'FGPct3SeasonsAgo A',  # Team A's field goal percentage during the season 3 years prior

    'FGPctAllowedThisSeason A',  # Team A's field goal percentage allowed during the current season
    'FGPctAllowedLastSeason A',  # Team A's field goal percentage allowed during the previous season
    'FGPctAllowed2SeasonsAgo A',  # Team A's field goal percentage allowed during the season 2 years prior
    'FGPctAllowed3SeasonsAgo A',  # Team A's field goal percentage allowed during the season 3 years prior

    'FGPctMarginThisSeason A',  # difference between Team A's field goal percentage and Team A's field goal percentage allowed during the current season
    'FGPctMarginLastSeason A',  # difference between Team A's field goal percentage and Team A's field goal percentage allowed during the previous season
    'FGPctMargin2SeasonsAgo A',  # difference between Team A's field goal percentage and Team A's field goal percentage allowed during the season 2 years prior
    'FGPctMargin3SeasonsAgo A',  # difference between Team A's field goal percentage and Team A's field goal percentage allowed during the season 3 years prior

    'FGM3PerGameThisSeason A',  # average number of 3-point field goals made by Team A per game during the current season
    'FGM3PerGameLastSeason A',  # average number of 3-point field goals made by Team A per game during the previous season
    'FGM3PerGame2SeasonsAgo A',  # average number of 3-point field goals made by Team A per game during the season 2 years prior
    'FGM3PerGame3SeasonsAgo A',  # average number of 3-point field goals made by Team A per game during the season 3 years prior

    'FGM3AllowedPerGameThisSeason A',  # average number of 3-point field goals allowed by Team A per game during the current season
    'FGM3AllowedPerGameLastSeason A',  # average number of 3-point field goals allowed by Team A per game during the previous season
    'FGM3AllowedPerGame2SeasonsAgo A',  # average number of 3-point field goals allowed by Team A per game during the season 2 years prior
    'FGM3AllowedPerGame3SeasonsAgo A',  # average number of 3-point field goals allowed by Team A per game during the season 3 years prior

    'FGM3MarginPerGameThisSeason A',  # average difference between number of 3-point field goals made by Team A and number of 3-point field goals allowed by Team A per game during the current season
    'FGM3MarginPerGameLastSeason A',  # average difference between number of 3-point field goals made by Team A and number of 3-point field goals allowed by Team A per game during the previous season
    'FGM3MarginPerGame2SeasonsAgo A',  # average difference between number of 3-point field goals made by Team A and number of 3-point field goals allowed by Team A per game during the season 2 years prior
    'FGM3MarginPerGame3SeasonsAgo A',  # average difference between number of 3-point field goals made by Team A and number of 3-point field goals allowed by Team A per game during the season 3 years prior

    'FGA3PerGameThisSeason A',  # average number of 3-point field goal attempts made by Team A per game during the current season
    'FGA3PerGameLastSeason A',  # average number of 3-point field goal attempts made by Team A per game during the previous season
    'FGA3PerGame2SeasonsAgo A',  # average number of 3-point field goal attempts made by Team A per game during the season 2 years prior
    'FGA3PerGame3SeasonsAgo A',  # average number of 3-point field goal attempts made by Team A per game during the season 3 years prior

    'FGA3AllowedPerGameThisSeason A',  # average number of 3-point field goal attempts allowed by Team A per game during the current season
    'FGA3AllowedPerGameLastSeason A',  # average number of 3-point field goal attempts allowed by Team A per game during the previous season
    'FGA3AllowedPerGame2SeasonsAgo A',  # average number of 3-point field goal attempts allowed by Team A per game during the season 2 years prior
    'FGA3AllowedPerGame3SeasonsAgo A',  # average number of 3-point field goal attempts allowed by Team A per game during the season 3 years prior

    'FGA3MarginPerGameThisSeason A',  # average difference between number of 3-point field goals attempted by Team A and number of 3-point field goal attempts allowed by Team A per game during the current season
    'FGA3MarginPerGameLastSeason A',  # average difference between number of 3-point field goals attempted by Team A and number of 3-point field goal attempts allowed by Team A per game during the previous season
    'FGA3MarginPerGame2SeasonsAgo A',  # average difference between number of 3-point field goals attempted by Team A and number of 3-point field goal attempts allowed by Team A per game during the season 2 years prior
    'FGA3MarginPerGame3SeasonsAgo A',  # average difference between number of 3-point field goals attempted by Team A and number of 3-point field goal attempts allowed by Team A per game during the season 3 years prior

    'FG3PctThisSeason A',  # Team A's 3-point field goal percentage during the current season
    'FG3PctLastSeason A',  # Team A's 3-point field goal percentage during the previous season
    'FG3Pct2SeasonsAgo A',  # Team A's 3-point field goal percentage during the season 2 years prior
    'FG3Pct3SeasonsAgo A',  # Team A's 3-point field goal percentage during the season 3 years prior

    'FG3PctAllowedThisSeason A',  # Team A's 3-point field goal percentage allowed during the current season
    'FG3PctAllowedLastSeason A',  # Team A's 3-point field goal percentage allowed during the previous season
    'FG3PctAllowed2SeasonsAgo A',  # Team A's 3-point field goal percentage allowed during the season 2 years prior
    'FG3PctAllowed3SeasonsAgo A',  # Team A's 3-point field goal percentage allowed during the season 3 years prior

    'FG3PctMarginThisSeason A',  # difference between Team A's 3-point field goal percentage and Team A's 3-point field goal percentage allowed during the current season
    'FG3PctMarginLastSeason A',  # difference between Team A's 3-point field goal percentage and Team A's 3-point field goal percentage allowed during the previous season
    'FG3PctMargin2SeasonsAgo A',  # difference between Team A's 3-point field goal percentage and Team A's 3-point field goal percentage allowed during the season 2 years prior
    'FG3PctMargin3SeasonsAgo A',  # difference between Team A's 3-point field goal percentage and Team A's 3-point field goal percentage allowed during the season 3 years prior

    'FTMPerGameThisSeason A',  # average number of free-throws made by Team A per game during the current season
    'FTMPerGameLastSeason A',  # average number of free-throws made by Team A per game during the previous season
    'FTMPerGame2SeasonsAgo A',  # average number of free-throws made by Team A per game during the season 2 years prior
    'FTMPerGame3SeasonsAgo A',  # average number of free-throws made by Team A per game during the season 3 years prior

    'FTMAllowedPerGameThisSeason A',  # average number of successful free-throws allowed by Team A per game during the current season
    'FTMAllowedPerGameLastSeason A',  # average number of successful free-throws allowed by Team A per game during the previous season
    'FTMAllowedPerGame2SeasonsAgo A',  # average number of successful free-throws allowed by Team A per game during the season 2 years prior
    'FTMAllowedPerGame3SeasonsAgo A',  # average number of successful free-throws allowed by Team A per game during the season 3 years prior

    'FTMMarginPerGameThisSeason A',  # average difference between number of free-throws made by Team A and number of successful free-throws allowed by Team A per game during the current season
    'FTMMarginPerGameLastSeason A',  # average difference between number of free-throws made by Team A and number of successful free-throws allowed by Team A per game during the previous season
    'FTMMarginPerGame2SeasonsAgo A',  # average difference between number of free-throws made by Team A and number of successful free-throws allowed by Team A per game during the season 2 years prior
    'FTMMarginPerGame3SeasonsAgo A',  # average difference between number of free-throws made by Team A and number of successful free-throws allowed by Team A per game during the season 3 years prior

    'FTAPerGameThisSeason A',  # average number of free-throws attempted by Team A per game during the current season
    'FTAPerGameLastSeason A',  # average number of free-throws attempted by Team A per game during the previous season
    'FTAPerGame2SeasonsAgo A',  # average number of free-throws attempted by Team A per game during the season 2 years prior
    'FTAPerGame3SeasonsAgo A',  # average number of free-throws attempted by Team A per game during the season 3 years prior

    'FTAAllowedPerGameThisSeason A',  # average number of free-throw attempts allowed by Team A per game during the current season
    'FTAAllowedPerGameLastSeason A',  # average number of free-throw attempts allowed by Team A per game during the previous season
    'FTAAllowedPerGame2SeasonsAgo A',  # average number of free-throw attempts allowed by Team A per game during the season 2 years prior
    'FTAAllowedPerGame3SeasonsAgo A',  # average number of free-throw attempts allowed by Team A per game during the season 3 years prior

    'FTAMarginPerGameThisSeason A',  # average difference between number of free-throws attempted by Team A and number of free-throw attempts allowed by Team A per game during the current season
    'FTAMarginPerGameLastSeason A',  # average difference between number of free-throws attempted by Team A and number of free-throw attempts allowed by Team A per game during the previous season
    'FTAMarginPerGame2SeasonsAgo A',  # average difference between number of free-throws attempted by Team A and number of free-throw attempts allowed by Team A per game during the season 2 years prior
    'FTAMarginPerGame3SeasonsAgo A',  # average difference between number of free-throws attempted by Team A and number of free-throw attempts allowed by Team A per game during the season 3 years prior

    'FTPctThisSeason A',  # Team A's free-throw percentage during the current season
    'FTPctLastSeason A',  # Team A's free-throw percentage during the previous season
    'FTPct2SeasonsAgo A',  # Team A's free-throw percentage during the season 2 years prior
    'FTPct3SeasonsAgo A',  # Team A's free-throw percentage during the season 3 years prior

    'FTPctAllowedThisSeason A',  # Team A's free-throw percentage allowed during the current season
    'FTPctAllowedLastSeason A',  # Team A's free-throw percentage allowed during the previous season
    'FTPctAllowed2SeasonsAgo A',  # Team A's free-throw percentage allowed during the season 2 years prior
    'FTPctAllowed3SeasonsAgo A',  # Team A's free-throw percentage allowed during the season 3 years prior

    'FTPctMarginThisSeason A',  # difference between Team A's free-throw percentage and Team A's free-throw percentage allowed during the current season
    'FTPctMarginLastSeason A',  # difference between Team A's free-throw percentage and Team A's free-throw percentage allowed during the previous season
    'FTPctMargin2SeasonsAgo A',  # difference between Team A's free-throw percentage and Team A's free-throw percentage allowed during the season 2 years prior
    'FTPctMargin3SeasonsAgo A',  # difference between Team A's free-throw percentage and Team A's free-throw percentage allowed during the season 3 years prior

    'RebPerGameThisSeason A',  # average number of rebounds by Team A per game during the current season
    'RebPerGameLastSeason A',  # average number of rebounds by Team A per game during the previous season
    'RebPerGame2SeasonsAgo A',  # average number of rebounds by Team A per game during the season 2 years prior
    'RebPerGame3SeasonsAgo A',  # average number of rebounds by Team A per game during the season 3 years prior

    'RebAllowedPerGameThisSeason A',  # average number of rebounds allowed by Team A per game during the current season
    'RebAllowedPerGameLastSeason A',  # average number of rebounds allowed by Team A per game during the previous season
    'RebAllowedPerGame2SeasonsAgo A',  # average number of rebounds allowed by Team A per game during the season 2 years prior
    'RebAllowedPerGame3SeasonsAgo A',  # average number of rebounds allowed by Team A per game during the season 3 years prior

    'RebMarginPerGameThisSeason A',  # average difference between number of rebounds by Team A and number of rebounds allowed by Team A per game during the current season
    'RebMarginPerGameLastSeason A',  # average difference between number of rebounds by Team A and number of rebounds allowed by Team A per game during the previous season
    'RebMarginPerGame2SeasonsAgo A',  # average difference between number of rebounds by Team A and number of rebounds allowed by Team A per game during the season 2 years prior
    'RebMarginPerGame3SeasonsAgo A',  # average difference between number of rebounds by Team A and number of rebounds allowed by Team A per game during the season 3 years prior

    'ORebPerGameThisSeason A',  # average number of offensive rebounds by Team A per game during the current season
    'ORebPerGameLastSeason A',  # average number of offensive rebounds by Team A per game during the previous season
    'ORebPerGame2SeasonsAgo A',  # average number of offensive rebounds by Team A per game during the season 2 years prior
    'ORebPerGame3SeasonsAgo A',  # average number of offensive rebounds by Team A per game during the season 3 years prior

    'ORebAllowedPerGameThisSeason A',  # average number of offensive rebounds allowed by Team A per game during the current season
    'ORebAllowedPerGameLastSeason A',  # average number of offensive rebounds allowed by Team A per game during the previous season
    'ORebAllowedPerGame2SeasonsAgo A',  # average number of offensive rebounds allowed by Team A per game during the season 2 years prior
    'ORebAllowedPerGame3SeasonsAgo A',  # average number of offensive rebounds allowed by Team A per game during the season 3 years prior

    'ORebMarginPerGameThisSeason A',  # average difference between number of offensive rebounds by Team A and number of rebounds allowed by Team A per game during the current season
    'ORebMarginPerGameLastSeason A',  # average difference between number of offensive rebounds by Team A and number of rebounds allowed by Team A per game during the previous season
    'ORebMarginPerGame2SeasonsAgo A',  # average difference between number of offensive rebounds by Team A and number of rebounds allowed by Team A per game during the season 2 years prior
    'ORebMarginPerGame3SeasonsAgo A',  # average difference between number of offensive rebounds by Team A and number of rebounds allowed by Team A per game during the season 3 years prior

    'DRebPerGameThisSeason A',  # average number of defensive rebounds by Team A per game during the current season
    'DRebPerGameLastSeason A',  # average number of defensive rebounds by Team A per game during the previous season
    'DRebPerGame2SeasonsAgo A',  # average number of defensive rebounds by Team A per game during the season 2 years prior
    'DRebPerGame3SeasonsAgo A',  # average number of defensive rebounds by Team A per game during the season 3 years prior

    'DRebAllowedPerGameThisSeason A',  # average number of defensive rebounds allowed by Team A per game during the current season
    'DRebAllowedPerGameLastSeason A',  # average number of defensive rebounds allowed by Team A per game during the previous season
    'DRebAllowedPerGame2SeasonsAgo A',  # average number of defensive rebounds allowed by Team A per game during the season 2 years prior
    'DRebAllowedPerGame3SeasonsAgo A',  # average number of defensive rebounds allowed by Team A per game during the season 3 years prior

    'DRebMarginPerGameThisSeason A',  # average difference between number of defensive rebounds by Team A and number of rebounds allowed by Team A per game during the current season
    'DRebMarginPerGameLastSeason A',  # average difference between number of defensive rebounds by Team A and number of rebounds allowed by Team A per game during the previous season
    'DRebMarginPerGame2SeasonsAgo A',  # average difference between number of defensive rebounds by Team A and number of rebounds allowed by Team A per game during the season 2 years prior
    'DRebMarginPerGame3SeasonsAgo A',  # average difference between number of defensive rebounds by Team A and number of rebounds allowed by Team A per game during the season 3 years prior

    'AstPerGameThisSeason A',  # average number of assists by Team A per game during the current season
    'AstPerGameLastSeason A',  # average number of assists by Team A per game during the previous season
    'AstPerGame2SeasonsAgo A',  # average number of assists by Team A per game during the season 2 years prior
    'AstPerGame3SeasonsAgo A',  # average number of assists by Team A per game during the season 3 years prior

    'AstAllowedPerGameThisSeason A',  # average number of assists allowed by Team A per game during the current season
    'AstAllowedPerGameLastSeason A',  # average number of assists allowed by Team A per game during the previous season
    'AstAllowedPerGame2SeasonsAgo A',  # average number of assists allowed by Team A per game during the season 2 years prior
    'AstAllowedPerGame3SeasonsAgo A',  # average number of assists allowed by Team A per game during the season 3 years prior

    'AstMarginPerGameThisSeason A',  # average difference between number of assists by Team A and number of assists allowed by Team A per game during the current season
    'AstMarginPerGameLastSeason A',  # average difference between number of assists by Team A and number of assists allowed by Team A per game during the previous season
    'AstMarginPerGame2SeasonsAgo A',  # average difference between number of assists by Team A and number of assists allowed by Team A per game during the season 2 years prior
    'AstMarginPerGame3SeasonsAgo A',  # average difference between number of assists by Team A and number of assists allowed by Team A per game during the season 3 years prior

    'TOPerGameThisSeason A',  # average number of turnovers by Team A per game during the current season
    'TOPerGameLastSeason A',  # average number of turnovers by Team A per game during the previous season
    'TOPerGame2SeasonsAgo A',  # average number of turnovers by Team A per game during the season 2 years prior
    'TOPerGame3SeasonsAgo A',  # average number of turnovers by Team A per game during the season 3 years prior

    'TOAllowedPerGameThisSeason A',  # average number of turnovers forced by Team A per game during the current season
    'TOAllowedPerGameLastSeason A',  # average number of turnovers forced by Team A per game during the previous season
    'TOAllowedPerGame2SeasonsAgo A',  # average number of turnovers forced by Team A per game during the season 2 years prior
    'TOAllowedPerGame3SeasonsAgo A',  # average number of turnovers forced by Team A per game during the season 3 years prior

    'TOMarginPerGameThisSeason A',  # average difference between number of turnovers by Team A and number of turnovers forced by Team A per game during the current season
    'TOMarginPerGameLastSeason A',  # average difference between number of turnovers by Team A and number of turnovers forced by Team A per game during the previous season
    'TOMarginPerGame2SeasonsAgo A',  # average difference between number of turnovers by Team A and number of turnovers forced by Team A per game during the season 2 years prior
    'TOMarginPerGame3SeasonsAgo A',  # average difference between number of turnovers by Team A and number of turnovers forced by Team A per game during the season 3 years prior

    'AvgAst/TORatioThisSeason A',  # Team A's season total assists divided by Team A's season total turnovers during the current season
    'AvgAst/TORatioLastSeason A',  # Team A's season total assists divided by Team A's season total turnovers during the previous season
    'AvgAst/TORatio2SeasonsAgo A',  # Team A's season total assists divided by Team A's season total turnovers during the season 2 years prior
    'AvgAst/TORatio3SeasonsAgo A',  # Team A's season total assists divided by Team A's season total turnovers during the season 3 years prior

    'AvgAst/TORatioAllowedThisSeason A',  # Team A's season total assists allowed divided by Team A's season total turnovers forced during the current season
    'AvgAst/TORatioAllowedLastSeason A',  # Team A's season total assists allowed divided by Team A's season total turnovers forced during the previous season
    'AvgAst/TORatioAllowed2SeasonsAgo A',  # Team A's season total assists allowed divided by Team A's season total turnovers forced during the season 2 years prior
    'AvgAst/TORatioAllowed3SeasonsAgo A',  # Team A's season total assists allowed divided by Team A's season total turnovers forced during the season 3 years prior

    'AvgAst/TORatioMarginThisSeason A',  # (Team A's season total assists divided by Team A's season total turnovers) minus (Team A's season total assists allowed divided by Team A's season total turnovers forced) during the current season
    'AvgAst/TORatioMarginLastSeason A',  # (Team A's season total assists divided by Team A's season total turnovers) minus (Team A's season total assists allowed divided by Team A's season total turnovers forced) during the previous season
    'AvgAst/TORatioMargin2SeasonsAgo A',  # (Team A's season total assists divided by Team A's season total turnovers) minus (Team A's season total assists allowed divided by Team A's season total turnovers forced) during the season 2 years prior
    'AvgAst/TORatioMargin3SeasonsAgo A',  # (Team A's season total assists divided by Team A's season total turnovers) minus (Team A's season total assists allowed divided by Team A's season total turnovers forced) during the season 3 years prior

    'AvgAst/TORatio(alt)ThisSeason A',  # average of Team A's assist/turnover ratios for each game Team A has played during the current season (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)LastSeason A',  # average of Team A's assist/turnover ratios for each game Team A played during the previous season (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)2SeasonsAgo A',  # average of Team A's assist/turnover ratios for each game Team A played during the season 2 years prior (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)3SeasonsAgo A',  # average of Team A's assist/turnover ratios for each game Team A played during the season 3 years prior (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)

    'AvgAst/TORatio(alt)AllowedThisSeason A',  # average of Team A's opponent's assist/turnover ratios for each game Team A has played during the current season (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)AllowedLastSeason A',  # average of Team A's opponent's assist/turnover ratios for each game Team A has played during the previous season (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)Allowed2SeasonsAgo A',  # average of Team A's opponent's assist/turnover ratios for each game Team A has played during the season 2 years prior (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)Allowed3SeasonsAgo A',  # average of Team A's opponent's assist/turnover ratios for each game Team A has played during the season 3 years prior (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)

    'AvgAst/TORatio(alt)MarginThisSeason A',  # average of the differences between Team A's assist/turnover ratio and Team A's opponent's assist/turnover ratio for each game Team A has played during the current season (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)MarginLastSeason A',  # average of the differences between Team A's assist/turnover ratio and Team A's opponent's assist/turnover ratio for each game Team A played during the previous season (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)Margin2SeasonsAgo A',  # average of the differences between Team A's assist/turnover ratio and Team A's opponent's assist/turnover ratio for each game Team A played during the season 2 years prior (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)Margin3SeasonsAgo A',  # average of the differences between Team A's assist/turnover ratio and Team A's opponent's assist/turnover ratio for each game Team A played during the season 3 years prior (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)

    'StlPerGameThisSeason A',  # average number of steals by Team A per game during the current season
    'StlPerGameLastSeason A',  # average number of steals by Team A per game during the previous season
    'StlPerGame2SeasonsAgo A',  # average number of steals by Team A per game during the season 2 years prior
    'StlPerGame3SeasonsAgo A',  # average number of steals by Team A per game during the season 3 years prior

    'StlAllowedPerGameThisSeason A',  # average number of steals allowed by Team A per game during the current season
    'StlAllowedPerGameLastSeason A',  # average number of steals allowed by Team A per game during the previous season
    'StlAllowedPerGame2SeasonsAgo A',  # average number of steals allowed by Team A per game during the season 2 years prior
    'StlAllowedPerGame3SeasonsAgo A',  # average number of steals allowed by Team A per game during the season 3 years prior

    'StlMarginPerGameThisSeason A',  # average difference between number of steals by Team A and number of steals allowed by Team A per game during the current season
    'StlMarginPerGameLastSeason A',  # average difference between number of steals by Team A and number of steals allowed by Team A per game during the previous season
    'StlMarginPerGame2SeasonsAgo A',  # average difference between number of steals by Team A and number of steals allowed by Team A per game during the season 2 years prior
    'StlMarginPerGame3SeasonsAgo A',  # average difference between number of steals by Team A and number of steals allowed by Team A per game during the season 3 years prior

    'BlkPerGameThisSeason A',  # average number of blocks by Team A per game during the current season
    'BlkPerGameLastSeason A',  # average number of blocks by Team A per game during the previous season
    'BlkPerGame2SeasonsAgo A',  # average number of blocks by Team A per game during the season 2 years prior
    'BlkPerGame3SeasonsAgo A',  # average number of blocks by Team A per game during the season 3 years prior

    'BlkAllowedPerGameThisSeason A',  # average number of blocks allowed by Team A per game during the current season
    'BlkAllowedPerGameLastSeason A',  # average number of blocks allowed by Team A per game during the previous season
    'BlkAllowedPerGame2SeasonsAgo A',  # average number of blocks allowed by Team A per game during the season 2 years prior
    'BlkAllowedPerGame3SeasonsAgo A',  # average number of blocks allowed by Team A per game during the season 3 years prior

    'BlkMarginPerGameThisSeason A',  # average difference between number of blocks by Team A and number of blocks allowed by Team A per game during the current season
    'BlkMarginPerGameLastSeason A',  # average difference between number of blocks by Team A and number of blocks allowed by Team A per game during the previous season
    'BlkMarginPerGame2SeasonsAgo A',  # average difference between number of blocks by Team A and number of blocks allowed by Team A per game during the season 2 years prior
    'BlkMarginPerGame3SeasonsAgo A',  # average difference between number of blocks by Team A and number of blocks allowed by Team A per game during the season 3 years prior

    'PFPerGameThisSeason A',  # average number of fouls committed by Team A per game during the current season
    'PFPerGameLastSeason A',  # average number of fouls committed by Team A per game during the previous season
    'PFPerGame2SeasonsAgo A',  # average number of fouls committed by Team A per game during the season 2 years prior
    'PFPerGame3SeasonsAgo A',  # average number of fouls committed by Team A per game during the season 3 years prior

    'PFAllowedPerGameThisSeason A',  # average number of fouls absorbed by Team A per game during the current season
    'PFAllowedPerGameLastSeason A',  # average number of fouls absorbed by Team A per game during the previous season
    'PFAllowedPerGame2SeasonsAgo A',  # average number of fouls absorbed by Team A per game during the season 2 years prior
    'PFAllowedPerGame3SeasonsAgo A',  # average number of fouls absorbed by Team A per game during the season 3 years prior

    'PFMarginPerGameThisSeason A',  # average difference between number of fouls committed by Team A and number of fouls absorbed by Team A per game during the current season
    'PFMarginPerGameLastSeason A',  # average difference between number of fouls committed by Team A and number of fouls absorbed by Team A per game during the previous season
    'PFMarginPerGame2SeasonsAgo A',  # average difference between number of fouls committed by Team A and number of fouls absorbed by Team A per game during the season 2 years prior
    'PFMarginPerGame3SeasonsAgo A',  # average difference between number of fouls committed by Team A and number of fouls absorbed by Team A per game during the season 3 years prior

    # Team A strength of schedule

    'CurrentSoSWeightedAvgOppWinPctThenThisSeason A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the current season
    'PastSoSWeightedAvgOppWinPctThenLastSeason A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the
    'PastSoSWeightedAvgOppWinPctThen2SeasonsAgo A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the
    'PastSoSWeightedAvgOppWinPctThen3SeasonsAgo A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the
    'CurrentSoSAvgOppWinPctNowThisSeason A',  # average up-to-date win percentage (counting only the current season) of the teams which Team A has played during the current season
    'CurrentSoSAvgOppWinPctNowLastSeason A',  # average end-of-season win percentage (counting only the previous season) of the teams which Team A has played during the current season
    'CurrentSoSAvgOppWinPctNow2SeasonsAgo A',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team A has played during the current season
    'CurrentSoSAvgOppWinPctNow3SeasonsAgo A',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team A has played during the current season
    'PastSoSAvgOppWinPctNowLastSeason A',  # average end-of-season win percentage (counting only the previous season) of the teams which Team A played during the previous season
    'PastSoSAvgOppWinPctNow2SeasonsAgo A',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team A played during the season 2 years prior
    'PastSoSAvgOppWinPctNow3SeasonsAgo A',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team A played during the season 3 years prior

    'CurrentSoSWeightedAvgOppFlipCloseWinPctThenThisSeason A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the current season (had the results of all of their close games been flipped)
    'PastSoSWeightedAvgOppFlipCloseWinPctThenLastSeason A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the previous season (had the results of all of their close games been flipped)
    'PastSoSWeightedAvgOppFlipCloseWinPctThen2SeasonsAgo A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the season 2 years prior (had the results of all of their close games been flipped)
    'PastSoSWeightedAvgOppFlipCloseWinPctThen3SeasonsAgo A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the season 3 years prior (had the results of all of their close games been flipped)
    'CurrentSoSAvgOppFlipCloseWinPctNowThisSeason A',  # average up-to-date win percentage (counting only the current season) of the teams which Team A has played during the current season (had the results of all of their close games been flipped)
    'CurrentSoSAvgOppFlipCloseWinPctNowLastSeason A',  # average end-of-season win percentage (counting only the previous season) of the teams which Team A has played during the current season (had the results of all of their close games been flipped)
    'CurrentSoSAvgOppFlipCloseWinPctNow2SeasonsAgo A',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team A has played during the current season (had the results of all of their close games been flipped)
    'CurrentSoSAvgOppFlipCloseWinPctNow3SeasonsAgo A',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team A has played during the current season (had the results of all of their close games been flipped)
    'PastSoSAvgOppFlipCloseWinPctNowLastSeason A',  # average end-of-season win percentage (counting only the previous season) of the teams which Team A played during the previous season (had the results of all of their close games been flipped)
    'PastSoSAvgOppFlipCloseWinPctNow2SeasonsAgo A',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team A played during the season 2 years prior (had the results of all of their close games been flipped)
    'PastSoSAvgOppFlipCloseWinPctNow3SeasonsAgo A',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team A played during the season 3 years prior (had the results of all of their close games been flipped)

    'CurrentSoSWeightedAvgOppWinCloseWinPctThenThisSeason A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the current season (had they won all of their close games)
    'PastSoSWeightedAvgOppWinCloseWinPctThenLastSeason A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the previous season (had they won all of their close games)
    'PastSoSWeightedAvgOppWinCloseWinPctThen2SeasonsAgo A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the season 2 years prior (had they won all of their close games)
    'PastSoSWeightedAvgOppWinCloseWinPctThen3SeasonsAgo A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the season 3 years prior (had they won all of their close games)
    'CurrentSoSAvgOppWinCloseWinPctNowThisSeason A',  # average up-to-date win percentage (counting only the current season) of the teams which Team A has played during the current season (had they won all of their close games)
    'CurrentSoSAvgOppWinCloseWinPctNowLastSeason A',  # average end-of-season win percentage (counting only the previous season) of the teams which Team A has played during the current season (had they won all of their close games)
    'CurrentSoSAvgOppWinCloseWinPctNow2SeasonsAgo A',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team A has played during the current season (had they won all of their close games)
    'CurrentSoSAvgOppWinCloseWinPctNow3SeasonsAgo A',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team A has played during the current season (had they won all of their close games)
    'PastSoSAvgOppWinCloseWinPctNowLastSeason A',  # average end-of-season win percentage (counting only the previous season) of the teams which Team A played during the previous season (had they won all of their close games)
    'PastSoSAvgOppWinCloseWinPctNow2SeasonsAgo A',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team A played during the season 2 years prior (had they won all of their close games)
    'PastSoSAvgOppWinCloseWinPctNow3SeasonsAgo A',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team A played during the season 3 years prior (had they won all of their close games)

    'CurrentSoSWeightedAvgOppLoseCloseWinPctThenThisSeason A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the current season (had they lost all of their close games)
    'PastSoSWeightedAvgOppLoseCloseWinPctThenLastSeason A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the previous season (had they lost all of their close games)
    'PastSoSWeightedAvgOppLoseCloseWinPctThen2SeasonsAgo A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the season 2 years prior (had they lost all of their close games)
    'PastSoSWeightedAvgOppLoseCloseWinPctThen3SeasonsAgo A',  # average win percentage of Team A's opponents at the time when they played Team A, weighted by number of games played by opponent going into the game against Team A, during the season 3 years prior (had they lost all of their close games)
    'CurrentSoSAvgOppLoseCloseWinPctNowThisSeason A',  # average up-to-date win percentage (counting only the current season) of the teams which Team A has played during the current season (had they lost all of their close games)
    'CurrentSoSAvgOppLoseCloseWinPctNowLastSeason A',  # average end-of-season win percentage (counting only the previous season) of the teams which Team A has played during the current season (had they lost all of their close games)
    'CurrentSoSAvgOppLoseCloseWinPctNow2SeasonsAgo A',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team A has played during the current season (had they lost all of their close games)
    'CurrentSoSAvgOppLoseCloseWinPctNow3SeasonsAgo A',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team A has played during the current season (had they lost all of their close games)
    'PastSoSAvgOppLoseCloseWinPctNowLastSeason A',  # average end-of-season win percentage (counting only the previous season) of the teams which Team A played during the previous season (had they lost all of their close games)
    'PastSoSAvgOppLoseCloseWinPctNow2SeasonsAgo A',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team A played during the season 2 years prior (had they lost all of their close games)
    'PastSoSAvgOppLoseCloseWinPctNow3SeasonsAgo A',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team A played during the season 3 years prior (had they lost all of their close games)

    'CurrentSoSWeightedAvgOppPointsPerGameThenThisSeason A',  # average of Team A's current-season opponents' average points scored per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average points scored per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average points scored per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average points scored per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppPointsPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average points scored per game during the current season
    'CurrentSoSAvgOppPointsPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average points scored per game during the previous season
    'CurrentSoSAvgOppPointsPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average points scored per game during the season 2 years prior
    'CurrentSoSAvgOppPointsPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average points scored per game during the season 3 years prior
    'PastSoSAvgOppPointsPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average points scored per game during the previous season
    'PastSoSAvgOppPointsPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average points scored per game during the season 2 years prior
    'PastSoSAvgOppPointsPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average points scored per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppPointsAllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average points allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsAllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average points allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsAllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average points allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsAllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average points allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppPointsAllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average points allowed per game during the current season
    'CurrentSoSAvgOppPointsAllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average points allowed per game during the previous season
    'CurrentSoSAvgOppPointsAllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average points allowed per game during the season 2 years prior
    'CurrentSoSAvgOppPointsAllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average points allowed per game during the season 3 years prior
    'PastSoSAvgOppPointsAllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average points allowed per game during the previous season
    'PastSoSAvgOppPointsAllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average points allowed per game during the season 2 years prior
    'PastSoSAvgOppPointsAllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average points allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppPointsMarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between points scored and points allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsMarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between points scored and points allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsMarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between points scored and points allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsMarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between points scored and points allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppPointsMarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between points scored and points allowed per game during the current season
    'CurrentSoSAvgOppPointsMarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between points scored and points allowed per game during the previous season
    'CurrentSoSAvgOppPointsMarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between points scored and points allowed per game during the season 2 years prior
    'CurrentSoSAvgOppPointsMarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between points scored and points allowed per game during the season 3 years prior
    'PastSoSAvgOppPointsMarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between points scored and points allowed per game during the previous season
    'PastSoSAvgOppPointsMarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between points scored and points allowed per game during the season 2 years prior
    'PastSoSAvgOppPointsMarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between points scored and points allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGMPerGameThenThisSeason A',  # average of Team A's current-season opponents' average number of field goals made per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average number of field goals made per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average number of field goals made per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average number of field goals made per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGMPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average number of field goals made per game during the current season
    'CurrentSoSAvgOppFGMPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average number of field goals made per game during the previous season
    'CurrentSoSAvgOppFGMPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average number of field goals made per game during the season 2 years prior
    'CurrentSoSAvgOppFGMPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average number of field goals made per game during the season 3 years prior
    'PastSoSAvgOppFGMPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average number of field goals made per game during the previous season
    'PastSoSAvgOppFGMPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average number of field goals made per game during the season 2 years prior
    'PastSoSAvgOppFGMPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average number of field goals made per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGMAllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average number of field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMAllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average number of field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMAllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average number of field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMAllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average number of field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGMAllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average number of field goals allowed per game during the current season
    'CurrentSoSAvgOppFGMAllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average number of field goals allowed per game during the previous season
    'CurrentSoSAvgOppFGMAllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average number of field goals allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGMAllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average number of field goals allowed per game during the season 3 years prior
    'PastSoSAvgOppFGMAllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average number of field goals allowed per game during the previous season
    'PastSoSAvgOppFGMAllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average number of field goals allowed per game during the season 2 years prior
    'PastSoSAvgOppFGMAllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average number of field goals allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGMMarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between number of field goals made and number of field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMMarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between number of field goals made and number of field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMMarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between number of field goals made and number of field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMMarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between number of field goals made and number of field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGMMarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between number of field goals made and number of field goals allowed per game during the current season
    'CurrentSoSAvgOppFGMMarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between number of field goals made and number of field goals allowed per game during the previous season
    'CurrentSoSAvgOppFGMMarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between number of field goals made and number of field goals allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGMMarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between number of field goals made and number of field goals allowed per game during the season 3 years prior
    'PastSoSAvgOppFGMMarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between number of field goals made and number of field goals allowed per game during the previous season
    'PastSoSAvgOppFGMMarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between number of field goals made and number of field goals allowed per game during the season 2 years prior
    'PastSoSAvgOppFGMMarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between number of field goals made and number of field goals allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGAPerGameThenThisSeason A',  # average of Team A's current-season opponents' average number of field goal attempts per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average number of field goal attempts per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average number of field goal attempts per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average number of field goal attempts per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGAPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average number of field goal attempts per game during the current season
    'CurrentSoSAvgOppFGAPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average number of field goal attempts per game during the previous season
    'CurrentSoSAvgOppFGAPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average number of field goal attempts per game during the season 2 years prior
    'CurrentSoSAvgOppFGAPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average number of field goal attempts per game during the season 3 years prior
    'PastSoSAvgOppFGAPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average number of field goal attempts per game during the previous season
    'PastSoSAvgOppFGAPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average number of field goal attempts per game during the season 2 years prior
    'PastSoSAvgOppFGAPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average number of field goal attempts per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGAAllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average number of field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAAllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average number of field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAAllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average number of field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAAllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average number of field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGAAllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average number of field goal attempts allowed per game during the current season
    'CurrentSoSAvgOppFGAAllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average number of field goal attempts allowed per game during the previous season
    'CurrentSoSAvgOppFGAAllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average number of field goal attempts allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGAAllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average number of field goal attempts allowed per game during the season 3 years prior
    'PastSoSAvgOppFGAAllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average number of field goal attempts allowed per game during the previous season
    'PastSoSAvgOppFGAAllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average number of field goal attempts allowed per game during the season 2 years prior
    'PastSoSAvgOppFGAAllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average number of field goal attempts allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGAMarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between number of field goal attempts and number of field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAMarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between number of field goal attempts and number of field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAMarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between number of field goal attempts and number of field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAMarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between number of field goal attempts and number of field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGAMarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between number of field goal attempts and number of field goal attempts allowed per game during the current season
    'CurrentSoSAvgOppFGAMarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between number of field goal attempts and number of field goal attempts allowed per game during the previous season
    'CurrentSoSAvgOppFGAMarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between number of field goal attempts and number of field goal attempts allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGAMarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between number of field goal attempts and number of field goal attempts allowed per game during the season 3 years prior
    'PastSoSAvgOppFGAMarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between number of field goal attempts and number of field goal attempts allowed per game during the previous season
    'PastSoSAvgOppFGAMarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between number of field goal attempts and number of field goal attempts allowed per game during the season 2 years prior
    'PastSoSAvgOppFGAMarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between number of field goal attempts and number of field goal attempts allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGPctThenThisSeason A',  # average of Team A's current-season opponents' season-long field goal percentage, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctThenLastSeason A',  # average of Team A's previous-season opponents' season-long field goal percentage, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season-long field goal percentage, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season-long field goal percentage, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGPctNowThisSeason A',  # average of Team A's current-season opponents' up-to-date season-long field goal percentage during the current season
    'CurrentSoSAvgOppFGPctNowLastSeason A',  # average of Team A's current-season opponents' season-long field goal percentage during the previous season
    'CurrentSoSAvgOppFGPctNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long field goal percentage during the season 2 years prior
    'CurrentSoSAvgOppFGPctNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long field goal percentage during the season 3 years prior
    'PastSoSAvgOppFGPctNowLastSeason A',  # average of Team A's previous-season opponents' season-long field goal percentage during the previous season
    'PastSoSAvgOppFGPctNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season-long field goal percentage during the season 2 years prior
    'PastSoSAvgOppFGPctNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season-long field goal percentage during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGPctAllowedThenThisSeason A',  # average of Team A's current-season opponents' season-long field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctAllowedThenLastSeason A',  # average of Team A's previous-season opponents' season-long field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctAllowedThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season-long field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctAllowedThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season-long field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGPctAllowedNowThisSeason A',  # average of Team A's current-season opponents' up-to-date season-long field goal percentage allowed during the current season
    'CurrentSoSAvgOppFGPctAllowedNowLastSeason A',  # average of Team A's current-season opponents' season-long field goal percentage allowed during the previous season
    'CurrentSoSAvgOppFGPctAllowedNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long field goal percentage allowed during the season 2 years prior
    'CurrentSoSAvgOppFGPctAllowedNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long field goal percentage allowed during the season 3 years prior
    'PastSoSAvgOppFGPctAllowedNowLastSeason A',  # average of Team A's previous-season opponents' season-long field goal percentage allowed during the previous season
    'PastSoSAvgOppFGPctAllowedNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season-long field goal percentage allowed during the season 2 years prior
    'PastSoSAvgOppFGPctAllowedNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season-long field goal percentage allowed during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGPctMarginThenThisSeason A',  # average of Team A's current-season opponents' differences between season-long field goal percentage and season-long field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctMarginThenLastSeason A',  # average of Team A's previous-season opponents' differences between previous-season-long field goal percentage and previous-season-long field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctMarginThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' differences between 2-seasons-prior season-long field goal percentage and 2-seasons-prior season-long field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctMarginThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' differences between 3 seasons-prior season-long field goal percentage and 3-seasons-prior season-long field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGPctMarginNowThisSeason A',  # average of Team A's current-season opponents' up-to-date differences between season-long field goal percentage and season-long field goal percentage allowed during the current season
    'CurrentSoSAvgOppFGPctMarginNowLastSeason A',  # average of Team A's current-season opponents' up-to-date differences between season-long field goal percentage and season-long field goal percentage allowed during the previous season
    'CurrentSoSAvgOppFGPctMarginNow2SeasonsAgo A',  # average of Team A's current-season opponents' up-to-date differences between season-long field goal percentage and season-long field goal percentage allowed during the season 2 years prior
    'CurrentSoSAvgOppFGPctMarginNow3SeasonsAgo A',  # average of Team A's current-season opponents' up-to-date differences between season-long field goal percentage and season-long field goal percentage allowed during the season 3 years prior
    'PastSoSAvgOppFGPctMarginNowLastSeason A',  # average of Team A's previous-season opponents' differences between season-long field goal percentage and season-long field goal percentage allowed during the previous season
    'PastSoSAvgOppFGPctMarginNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' differences between season-long field goal percentage and season-long field goal percentage allowed during the previous season
    'PastSoSAvgOppFGPctMarginNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' differences between season-long field goal percentage and season-long field goal percentage allowed during the previous season 3 years prior

    'CurrentSoSWeightedAvgOppFGM3PerGameThenThisSeason A',  # average of Team A's current-season opponents' average number of 3-point field goals made per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3PerGameThenLastSeason A',  # average of Team A's previous-season opponents' average number of 3-point field goals made per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3PerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average number of 3-point field goals made per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3PerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average number of 3-point field goals made per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGM3PerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average number of 3-point field goals made per game during the current season
    'CurrentSoSAvgOppFGM3PerGameNowLastSeason A',  # average of Team A's current-season opponents' season average number of 3-point field goals made per game during the previous season
    'CurrentSoSAvgOppFGM3PerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average number of 3-point field goals made per game during the season 2 years prior
    'CurrentSoSAvgOppFGM3PerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average number of 3-point field goals made per game during the season 3 years prior
    'PastSoSAvgOppFGM3PerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average number of 3-point field goals made per game during the previous season
    'PastSoSAvgOppFGM3PerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average number of 3-point field goals made per game during the season 2 years prior
    'PastSoSAvgOppFGM3PerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average number of 3-point field goals made per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGM3AllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average number of 3-point field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3AllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average number of 3-point field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3AllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average number of 3-point field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3AllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average number of 3-point field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGM3AllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average number of 3-point field goals allowed per game during the current season
    'CurrentSoSAvgOppFGM3AllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average number of 3-point field goals allowed per game during the previous season
    'CurrentSoSAvgOppFGM3AllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average number of 3-point field goals allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGM3AllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average number of 3-point field goals allowed per game during the season 3 years prior
    'PastSoSAvgOppFGM3AllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average number of 3-point field goals allowed per game during the previous season
    'PastSoSAvgOppFGM3AllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average number of 3-point field goals allowed per game during the season 2 years prior
    'PastSoSAvgOppFGM3AllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average number of 3-point field goals allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGM3MarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between number of 3-point field goals made and number of 3-point field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3MarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between number of 3-point field goals made and number of 3-point field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3MarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between number of 3-point field goals made and number of 3-point field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3MarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between number of 3-point field goals made and number of 3-point field goals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGM3MarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the current season
    'CurrentSoSAvgOppFGM3MarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the previous season
    'CurrentSoSAvgOppFGM3MarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGM3MarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the season 3 years prior
    'PastSoSAvgOppFGM3MarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the previous season
    'PastSoSAvgOppFGM3MarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the season 2 years prior
    'PastSoSAvgOppFGM3MarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGA3PerGameThenThisSeason A',  # average of Team A's current-season opponents' average number of 3-point field goal attempts per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3PerGameThenLastSeason A',  # average of Team A's previous-season opponents' average number of 3-point field goal attempts per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3PerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average number of 3-point field goal attempts per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3PerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average number of 3-point field goal attempts per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGA3PerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average number of 3-point field goal attempts per game during the current season
    'CurrentSoSAvgOppFGA3PerGameNowLastSeason A',  # average of Team A's current-season opponents' season average number of 3-point field goal attempts per game during the previous season
    'CurrentSoSAvgOppFGA3PerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average number of 3-point field goal attempts per game during the season 2 years prior
    'CurrentSoSAvgOppFGA3PerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average number of 3-point field goal attempts per game during the season 3 years prior
    'PastSoSAvgOppFGA3PerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average number of 3-point field goal attempts per game during the previous season
    'PastSoSAvgOppFGA3PerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average number of 3-point field goal attempts per game during the season 2 years prior
    'PastSoSAvgOppFGA3PerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average number of 3-point field goal attempts per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGA3AllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3AllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3AllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3AllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGA3AllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average number of 3-point field goal attempts allowed per game during the current season
    'CurrentSoSAvgOppFGA3AllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average number of 3-point field goal attempts allowed per game during the previous season
    'CurrentSoSAvgOppFGA3AllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average number of 3-point field goal attempts allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGA3AllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average number of 3-point field goal attempts allowed per game during the season 3 years prior
    'PastSoSAvgOppFGA3AllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average number of 3-point field goal attempts allowed per game during the previous season
    'PastSoSAvgOppFGA3AllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average number of 3-point field goal attempts allowed per game during the season 2 years prior
    'PastSoSAvgOppFGA3AllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average number of 3-point field goal attempts allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGA3MarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3MarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3MarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3MarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGA3MarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the current season
    'CurrentSoSAvgOppFGA3MarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the previous season
    'CurrentSoSAvgOppFGA3MarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGA3MarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the season 3 years prior
    'PastSoSAvgOppFGA3MarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the previous season
    'PastSoSAvgOppFGA3MarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the season 2 years prior
    'PastSoSAvgOppFGA3MarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFG3PctThenThisSeason A',  # average of Team A's current-season opponents' season-long 3-point field goal percentage, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctThenLastSeason A',  # average of Team A's previous-season opponents' season-long 3-point field goal percentage, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season-long 3-point field goal percentage, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season-long 3-point field goal percentage, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFG3PctNowThisSeason A',  # average of Team A's current-season opponents' up-to-date season-long 3-point field goal percentage during the current season
    'CurrentSoSAvgOppFG3PctNowLastSeason A',  # average of Team A's current-season opponents' season-long 3-point field goal percentage during the previous season
    'CurrentSoSAvgOppFG3PctNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long 3-point field goal percentage during the season 2 years prior
    'CurrentSoSAvgOppFG3PctNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long 3-point field goal percentage during the season 3 years prior
    'PastSoSAvgOppFG3PctNowLastSeason A',  # average of Team A's previous-season opponents' season-long 3-point field goal percentage during the previous season
    'PastSoSAvgOppFG3PctNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season-long 3-point field goal percentage during the season 2 years prior
    'PastSoSAvgOppFG3PctNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season-long 3-point field goal percentage during the season 3 years prior

    'CurrentSoSWeightedAvgOppFG3PctAllowedThenThisSeason A',  # average of Team A's current-season opponents' season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctAllowedThenLastSeason A',  # average of Team A's previous-season opponents' season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctAllowedThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctAllowedThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFG3PctAllowedNowThisSeason A',  # average of Team A's current-season opponents' up-to-date season-long 3-point field goal percentage allowed during the current season
    'CurrentSoSAvgOppFG3PctAllowedNowLastSeason A',  # average of Team A's current-season opponents' season-long 3-point field goal percentage allowed during the previous season
    'CurrentSoSAvgOppFG3PctAllowedNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long 3-point field goal percentage allowed during the season 2 years prior
    'CurrentSoSAvgOppFG3PctAllowedNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long 3-point field goal percentage allowed during the season 3 years prior
    'PastSoSAvgOppFG3PctAllowedNowLastSeason A',  # average of Team A's previous-season opponents' season-long 3-point field goal percentage allowed during the previous season
    'PastSoSAvgOppFG3PctAllowedNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season-long 3-point field goal percentage allowed during the season 2 years prior
    'PastSoSAvgOppFG3PctAllowedNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season-long 3-point field goal percentage allowed during the season 3 years prior

    'CurrentSoSWeightedAvgOppFG3PctMarginThenThisSeason A',  # average of Team A's current-season opponents' differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctMarginThenLastSeason A',  # average of Team A's previous-season opponents' differences between previous-season-long 3-point field goal percentage and previous-season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctMarginThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' differences between 2-seasons-prior season-long 3-point field goal percentage and 2-seasons-prior season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctMarginThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' differences between 3 seasons-prior season-long 3-point field goal percentage and 3-seasons-prior season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFG3PctMarginNowThisSeason A',  # average of Team A's current-season opponents' up-to-date differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the current season
    'CurrentSoSAvgOppFG3PctMarginNowLastSeason A',  # average of Team A's current-season opponents' up-to-date differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the previous season
    'CurrentSoSAvgOppFG3PctMarginNow2SeasonsAgo A',  # average of Team A's current-season opponents' up-to-date differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the season 2 years prior
    'CurrentSoSAvgOppFG3PctMarginNow3SeasonsAgo A',  # average of Team A's current-season opponents' up-to-date differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the season 3 years prior
    'PastSoSAvgOppFG3PctMarginNowLastSeason A',  # average of Team A's previous-season opponents' differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the previous season
    'PastSoSAvgOppFG3PctMarginNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the previous season
    'PastSoSAvgOppFG3PctMarginNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the previous season 3 years prior

    'CurrentSoSWeightedAvgOppFTMPerGameThenThisSeason A',  # average of Team A's current-season opponents' average number of free-throws made per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average number of free-throws made per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average number of free-throws made per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average number of free-throws made per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTMPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average number of free-throws made per game during the current season
    'CurrentSoSAvgOppFTMPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average number of free-throws made per game during the previous season
    'CurrentSoSAvgOppFTMPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average number of free-throws made per game during the season 2 years prior
    'CurrentSoSAvgOppFTMPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average number of free-throws made per game during the season 3 years prior
    'PastSoSAvgOppFTMPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average number of free-throws made per game during the previous season
    'PastSoSAvgOppFTMPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average number of free-throws made per game during the season 2 years prior
    'PastSoSAvgOppFTMPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average number of free-throws made per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTMAllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average number of successful free-throws allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMAllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average number of successful free-throws allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMAllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average number of successful free-throws allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMAllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average number of successful free-throws allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTMAllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average number of successful free-throws allowed per game during the current season
    'CurrentSoSAvgOppFTMAllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average number of successful free-throws allowed per game during the previous season
    'CurrentSoSAvgOppFTMAllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average number of successful free-throws allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFTMAllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average number of successful free-throws allowed per game during the season 3 years prior
    'PastSoSAvgOppFTMAllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average number of successful free-throws allowed per game during the previous season
    'PastSoSAvgOppFTMAllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average number of successful free-throws allowed per game during the season 2 years prior
    'PastSoSAvgOppFTMAllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average number of successful free-throws allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTMMarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between number of free-throws made and number of successful free-throws allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMMarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between number of free-throws made and number of successful free-throws allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMMarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between number of free-throws made and number of successful free-throws allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMMarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between number of free-throws made and number of successful free-throws allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTMMarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between number of free-throws made and number of successful free-throws allowed per game during the current season
    'CurrentSoSAvgOppFTMMarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between number of free-throws made and number of successful free-throws allowed per game during the previous season
    'CurrentSoSAvgOppFTMMarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between number of free-throws made and number of successful free-throws allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFTMMarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between number of free-throws made and number of successful free-throws allowed per game during the season 3 years prior
    'PastSoSAvgOppFTMMarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between number of free-throws made and number of successful free-throws allowed per game during the previous season
    'PastSoSAvgOppFTMMarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between number of free-throws made and number of successful free-throws allowed per game during the season 2 years prior
    'PastSoSAvgOppFTMMarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between number of free-throws made and number of successful free-throws allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTAPerGameThenThisSeason A',  # average of Team A's current-season opponents' average number of free-throw attempts per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average number of free-throw attempts per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average number of free-throw attempts per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average number of free-throw attempts per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTAPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average number of free-throw attempts per game during the current season
    'CurrentSoSAvgOppFTAPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average number of free-throw attempts per game during the previous season
    'CurrentSoSAvgOppFTAPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average number of free-throw attempts per game during the season 2 years prior
    'CurrentSoSAvgOppFTAPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average number of free-throw attempts per game during the season 3 years prior
    'PastSoSAvgOppFTAPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average number of free-throw attempts per game during the previous season
    'PastSoSAvgOppFTAPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average number of free-throw attempts per game during the season 2 years prior
    'PastSoSAvgOppFTAPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average number of free-throw attempts per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTAAllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average number of free-throw attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAAllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average number of free-throw attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAAllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average number of free-throw attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAAllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average number of free-throw attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTAAllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average number of free-throw attempts allowed per game during the current season
    'CurrentSoSAvgOppFTAAllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average number of free-throw attempts allowed per game during the previous season
    'CurrentSoSAvgOppFTAAllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average number of free-throw attempts allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFTAAllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average number of free-throw attempts allowed per game during the season 3 years prior
    'PastSoSAvgOppFTAAllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average number of free-throw attempts allowed per game during the previous season
    'PastSoSAvgOppFTAAllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average number of free-throw attempts allowed per game during the season 2 years prior
    'PastSoSAvgOppFTAAllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average number of free-throw attempts allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTAMarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between number of free-throw attempts and number of free-throw attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAMarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between number of free-throw attempts and number of free-throw attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAMarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between number of free-throw attempts and number of free-throw attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAMarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between number of free-throw attempts and number of free-throw attempts allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTAMarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the current season
    'CurrentSoSAvgOppFTAMarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the previous season
    'CurrentSoSAvgOppFTAMarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFTAMarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the season 3 years prior
    'PastSoSAvgOppFTAMarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the previous season
    'PastSoSAvgOppFTAMarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the season 2 years prior
    'PastSoSAvgOppFTAMarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTPctThenThisSeason A',  # average of Team A's current-season opponents' season-long free-throw percentage, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctThenLastSeason A',  # average of Team A's previous-season opponents' season-long free-throw percentage, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season-long free-throw percentage, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season-long free-throw percentage, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTPctNowThisSeason A',  # average of Team A's current-season opponents' up-to-date season-long free-throw percentage during the current season
    'CurrentSoSAvgOppFTPctNowLastSeason A',  # average of Team A's current-season opponents' season-long free-throw percentage during the previous season
    'CurrentSoSAvgOppFTPctNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long free-throw percentage during the season 2 years prior
    'CurrentSoSAvgOppFTPctNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long free-throw percentage during the season 3 years prior
    'PastSoSAvgOppFTPctNowLastSeason A',  # average of Team A's previous-season opponents' season-long free-throw percentage during the previous season
    'PastSoSAvgOppFTPctNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season-long free-throw percentage during the season 2 years prior
    'PastSoSAvgOppFTPctNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season-long free-throw percentage during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTPctAllowedThenThisSeason A',  # average of Team A's current-season opponents' season-long free-throw percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctAllowedThenLastSeason A',  # average of Team A's previous-season opponents' season-long free-throw percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctAllowedThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season-long free-throw percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctAllowedThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season-long free-throw percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTPctAllowedNowThisSeason A',  # average of Team A's current-season opponents' up-to-date season-long free-throw percentage allowed during the current season
    'CurrentSoSAvgOppFTPctAllowedNowLastSeason A',  # average of Team A's current-season opponents' season-long free-throw percentage allowed during the previous season
    'CurrentSoSAvgOppFTPctAllowedNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long free-throw percentage allowed during the season 2 years prior
    'CurrentSoSAvgOppFTPctAllowedNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long free-throw percentage allowed during the season 3 years prior
    'PastSoSAvgOppFTPctAllowedNowLastSeason A',  # average of Team A's previous-season opponents' season-long free-throw percentage allowed during the previous season
    'PastSoSAvgOppFTPctAllowedNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season-long free-throw percentage allowed during the season 2 years prior
    'PastSoSAvgOppFTPctAllowedNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season-long free-throw percentage allowed during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTPctMarginThenThisSeason A',  # average of Team A's current-season opponents' differences between season-long free-throw percentage and season-long free-throw percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctMarginThenLastSeason A',  # average of Team A's previous-season opponents' differences between previous-season-long free-throw percentage and previous-season-long free-throw percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctMarginThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' differences between 2-seasons-prior season-long free-throw percentage and 2-seasons-prior season-long free-throw percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctMarginThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' differences between 3 seasons-prior season-long free-throw percentage and 3-seasons-prior season-long free-throw percentage allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTPctMarginNowThisSeason A',  # average of Team A's current-season opponents' up-to-date differences between season-long free-throw percentage and season-long free-throw percentage allowed during the current season
    'CurrentSoSAvgOppFTPctMarginNowLastSeason A',  # average of Team A's current-season opponents' up-to-date differences between season-long free-throw percentage and season-long free-throw percentage allowed during the previous season
    'CurrentSoSAvgOppFTPctMarginNow2SeasonsAgo A',  # average of Team A's current-season opponents' up-to-date differences between season-long free-throw percentage and season-long free-throw percentage allowed during the season 2 years prior
    'CurrentSoSAvgOppFTPctMarginNow3SeasonsAgo A',  # average of Team A's current-season opponents' up-to-date differences between season-long free-throw percentage and season-long free-throw percentage allowed during the season 3 years prior
    'PastSoSAvgOppFTPctMarginNowLastSeason A',  # average of Team A's previous-season opponents' differences between season-long free-throw percentage and season-long free-throw percentage allowed during the previous season
    'PastSoSAvgOppFTPctMarginNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' differences between season-long free-throw percentage and season-long free-throw percentage allowed during the previous season
    'PastSoSAvgOppFTPctMarginNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' differences between season-long free-throw percentage and season-long free-throw percentage allowed during the previous season 3 years prior

    'CurrentSoSWeightedAvgOppRebPerGameThenThisSeason A',  # average of Team A's current-season opponents' average rebounds per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average rebounds per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average rebounds per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average rebounds per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppRebPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average rebounds per game during the current season
    'CurrentSoSAvgOppRebPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average rebounds per game during the previous season
    'CurrentSoSAvgOppRebPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average rebounds per game during the season 2 years prior
    'CurrentSoSAvgOppRebPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average rebounds per game during the season 3 years prior
    'PastSoSAvgOppRebPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average rebounds per game during the previous season
    'PastSoSAvgOppRebPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average rebounds per game during the season 2 years prior
    'PastSoSAvgOppRebPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average rebounds per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppRebAllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebAllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebAllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebAllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppRebAllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average rebounds allowed per game during the current season
    'CurrentSoSAvgOppRebAllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average rebounds allowed per game during the previous season
    'CurrentSoSAvgOppRebAllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average rebounds allowed per game during the season 2 years prior
    'CurrentSoSAvgOppRebAllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average rebounds allowed per game during the season 3 years prior
    'PastSoSAvgOppRebAllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average rebounds allowed per game during the previous season
    'PastSoSAvgOppRebAllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average rebounds allowed per game during the season 2 years prior
    'PastSoSAvgOppRebAllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average rebounds allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppRebMarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between rebounds and rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebMarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between rebounds and rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebMarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between rebounds and rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebMarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between rebounds and rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppRebMarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between rebounds and rebounds allowed per game during the current season
    'CurrentSoSAvgOppRebMarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between rebounds and rebounds allowed per game during the previous season
    'CurrentSoSAvgOppRebMarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between rebounds and rebounds allowed per game during the season 2 years prior
    'CurrentSoSAvgOppRebMarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between rebounds and rebounds allowed per game during the season 3 years prior
    'PastSoSAvgOppRebMarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between rebounds and rebounds allowed per game during the previous season
    'PastSoSAvgOppRebMarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between rebounds and rebounds allowed per game during the season 2 years prior
    'PastSoSAvgOppRebMarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between rebounds and rebounds allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppORebPerGameThenThisSeason A',  # average of Team A's current-season opponents' average offensive rebounds per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average offensive rebounds per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average offensive rebounds per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average offensive rebounds per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppORebPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average offensive rebounds per game during the current season
    'CurrentSoSAvgOppORebPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average offensive rebounds per game during the previous season
    'CurrentSoSAvgOppORebPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average offensive rebounds per game during the season 2 years prior
    'CurrentSoSAvgOppORebPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average offensive rebounds per game during the season 3 years prior
    'PastSoSAvgOppORebPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average offensive rebounds per game during the previous season
    'PastSoSAvgOppORebPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average offensive rebounds per game during the season 2 years prior
    'PastSoSAvgOppORebPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average offensive rebounds per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppORebAllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average offensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebAllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average offensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebAllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average offensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebAllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average offensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppORebAllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average offensive rebounds allowed per game during the current season
    'CurrentSoSAvgOppORebAllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average offensive rebounds allowed per game during the previous season
    'CurrentSoSAvgOppORebAllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average offensive rebounds allowed per game during the season 2 years prior
    'CurrentSoSAvgOppORebAllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average offensive rebounds allowed per game during the season 3 years prior
    'PastSoSAvgOppORebAllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average offensive rebounds allowed per game during the previous season
    'PastSoSAvgOppORebAllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average offensive rebounds allowed per game during the season 2 years prior
    'PastSoSAvgOppORebAllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average offensive rebounds allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppORebMarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between offensive rebounds and offensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebMarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between offensive rebounds and offensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebMarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between offensive rebounds and offensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebMarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between offensive rebounds and offensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppORebMarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between offensive rebounds and offensive rebounds allowed per game during the current season
    'CurrentSoSAvgOppORebMarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between offensive rebounds and offensive rebounds allowed per game during the previous season
    'CurrentSoSAvgOppORebMarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between offensive rebounds and offensive rebounds allowed per game during the season 2 years prior
    'CurrentSoSAvgOppORebMarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between offensive rebounds and offensive rebounds allowed per game during the season 3 years prior
    'PastSoSAvgOppORebMarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between offensive rebounds and offensive rebounds allowed per game during the previous season
    'PastSoSAvgOppORebMarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between offensive rebounds and offensive rebounds allowed per game during the season 2 years prior
    'PastSoSAvgOppORebMarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between offensive rebounds and offensive rebounds allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppDRebPerGameThenThisSeason A',  # average of Team A's current-season opponents' average defensive rebounds per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average defensive rebounds per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average defensive rebounds per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average defensive rebounds per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppDRebPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average defensive rebounds per game during the current season
    'CurrentSoSAvgOppDRebPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average defensive rebounds per game during the previous season
    'CurrentSoSAvgOppDRebPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average defensive rebounds per game during the season 2 years prior
    'CurrentSoSAvgOppDRebPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average defensive rebounds per game during the season 3 years prior
    'PastSoSAvgOppDRebPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average defensive rebounds per game during the previous season
    'PastSoSAvgOppDRebPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average defensive rebounds per game during the season 2 years prior
    'PastSoSAvgOppDRebPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average defensive rebounds per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppDRebAllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average defensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebAllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average defensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebAllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average defensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebAllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average defensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppDRebAllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average defensive rebounds allowed per game during the current season
    'CurrentSoSAvgOppDRebAllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average defensive rebounds allowed per game during the previous season
    'CurrentSoSAvgOppDRebAllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average defensive rebounds allowed per game during the season 2 years prior
    'CurrentSoSAvgOppDRebAllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average defensive rebounds allowed per game during the season 3 years prior
    'PastSoSAvgOppDRebAllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average defensive rebounds allowed per game during the previous season
    'PastSoSAvgOppDRebAllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average defensive rebounds allowed per game during the season 2 years prior
    'PastSoSAvgOppDRebAllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average defensive rebounds allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppDRebMarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between defensive rebounds and defensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebMarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between defensive rebounds and defensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebMarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between defensive rebounds and defensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebMarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between defensive rebounds and defensive rebounds allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppDRebMarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between defensive rebounds and defensive rebounds allowed per game during the current season
    'CurrentSoSAvgOppDRebMarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between defensive rebounds and defensive rebounds allowed per game during the previous season
    'CurrentSoSAvgOppDRebMarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between defensive rebounds and defensive rebounds allowed per game during the season 2 years prior
    'CurrentSoSAvgOppDRebMarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between defensive rebounds and defensive rebounds allowed per game during the season 3 years prior
    'PastSoSAvgOppDRebMarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between defensive rebounds and defensive rebounds allowed per game during the previous season
    'PastSoSAvgOppDRebMarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between defensive rebounds and defensive rebounds allowed per game during the season 2 years prior
    'PastSoSAvgOppDRebMarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between defensive rebounds and defensive rebounds allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppAstPerGameThenThisSeason A',  # average of Team A's current-season opponents' average assists per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average assists per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average assists per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average assists per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppAstPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average assists per game during the current season
    'CurrentSoSAvgOppAstPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average assists per game during the previous season
    'CurrentSoSAvgOppAstPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average assists per game during the season 2 years prior
    'CurrentSoSAvgOppAstPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average assists per game during the season 3 years prior
    'PastSoSAvgOppAstPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average assists per game during the previous season
    'PastSoSAvgOppAstPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average assists per game during the season 2 years prior
    'PastSoSAvgOppAstPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average assists per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppAstAllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average assists allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstAllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average assists allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstAllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average assists allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstAllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average assists allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppAstAllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average assists allowed per game during the current season
    'CurrentSoSAvgOppAstAllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average assists allowed per game during the previous season
    'CurrentSoSAvgOppAstAllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average assists allowed per game during the season 2 years prior
    'CurrentSoSAvgOppAstAllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average assists allowed per game during the season 3 years prior
    'PastSoSAvgOppAstAllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average assists allowed per game during the previous season
    'PastSoSAvgOppAstAllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average assists allowed per game during the season 2 years prior
    'PastSoSAvgOppAstAllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average assists allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppAstMarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between assists and assists allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstMarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between assists and assists allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstMarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between assists and assists allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstMarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between assists and assists allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppAstMarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between assists and assists allowed per game during the current season
    'CurrentSoSAvgOppAstMarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between assists and assists allowed per game during the previous season
    'CurrentSoSAvgOppAstMarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between assists and assists allowed per game during the season 2 years prior
    'CurrentSoSAvgOppAstMarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between assists and assists allowed per game during the season 3 years prior
    'PastSoSAvgOppAstMarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between assists and assists allowed per game during the previous season
    'PastSoSAvgOppAstMarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between assists and assists allowed per game during the season 2 years prior
    'PastSoSAvgOppAstMarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between assists and assists allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppTOPerGameThenThisSeason A',  # average of Team A's current-season opponents' average turnovers per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average turnovers per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average turnovers per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average turnovers per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppTOPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average turnovers per game during the current season
    'CurrentSoSAvgOppTOPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average turnovers per game during the previous season
    'CurrentSoSAvgOppTOPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average turnovers per game during the season 2 years prior
    'CurrentSoSAvgOppTOPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average turnovers per game during the season 3 years prior
    'PastSoSAvgOppTOPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average turnovers per game during the previous season
    'PastSoSAvgOppTOPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average turnovers per game during the season 2 years prior
    'PastSoSAvgOppTOPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average turnovers per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppTOAllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average turnovers forced per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOAllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average turnovers forced per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOAllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average turnovers forced per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOAllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average turnovers forced per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppTOAllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average turnovers forced per game during the current season
    'CurrentSoSAvgOppTOAllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average turnovers forced per game during the previous season
    'CurrentSoSAvgOppTOAllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average turnovers forced per game during the season 2 years prior
    'CurrentSoSAvgOppTOAllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average turnovers forced per game during the season 3 years prior
    'PastSoSAvgOppTOAllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average turnovers forced per game during the previous season
    'PastSoSAvgOppTOAllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average turnovers forced per game during the season 2 years prior
    'PastSoSAvgOppTOAllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average turnovers forced per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppTOMarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between turnovers and turnovers forced per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOMarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between turnovers and turnovers forced per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOMarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between turnovers and turnovers forced per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOMarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between turnovers and turnovers forced per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppTOMarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between turnovers and turnovers forced per game during the current season
    'CurrentSoSAvgOppTOMarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between turnovers and turnovers forced per game during the previous season
    'CurrentSoSAvgOppTOMarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between turnovers and turnovers forced per game during the season 2 years prior
    'CurrentSoSAvgOppTOMarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between turnovers and turnovers forced per game during the season 3 years prior
    'PastSoSAvgOppTOMarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between turnovers and turnovers forced per game during the previous season
    'PastSoSAvgOppTOMarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between turnovers and turnovers forced per game during the season 2 years prior
    'PastSoSAvgOppTOMarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between turnovers and turnovers forced per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppAvgAst/TORatioThenThisSeason A',  # average of Team A's current-season opponents' current-season-long assist/turnover ratios (total assists / total turnovers), recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioThenLastSeason A',  # average of Team A's previous-season opponents' previous-season-long assist/turnover ratios (total assists / total turnovers), recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioThen2SeasonsAgo A',  # average of Team A's 2-seasons-prior opponents' 2-seasons-prior season-long assist/turnover ratios (total assists / total turnovers), recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioThen3SeasonsAgo A',  # average of Team A's 3-seasons-prior opponents' 3-seasons-prior season-long assist/turnover ratios (total assists / total turnovers), recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppAvgAst/TORatioNowThisSeason A',  # average of Team A's current-season opponents' up-to-date assist/turnover ratios (total assists / total turnovers) during the current season
    'CurrentSoSAvgOppAvgAst/TORatioNowLastSeason A',  # average of Team A's current-season opponents' season-long assist/turnover ratios (total assists / total turnovers) during the previous season
    'CurrentSoSAvgOppAvgAst/TORatioNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long assist/turnover ratios (total assists / total turnovers) during the season 2 years prior
    'CurrentSoSAvgOppAvgAst/TORatioNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long assist/turnover ratios (total assists / total turnovers) during the season 3 years prior
    'PastSoSAvgOppAvgAst/TORatioNowLastSeason A',  # average of Team A's previous-season opponents' season-long assist/turnover ratios (total assists / total turnovers) during the previous season
    'PastSoSAvgOppAvgAst/TORatioNow2SeasonsAgo A',  # average of Team A's 2-seasons-prior opponents' season-long assist/turnover ratios (total assists / total turnovers) during the season 2 years prior
    'PastSoSAvgOppAvgAst/TORatioNow3SeasonsAgo A',  # average of Team A's 3-seasons-prior opponents' season-long assist/turnover ratios (total assists / total turnovers) during the season 3 years prior

    'CurrentSoSWeightedAvgOppAvgAst/TORatioAllowedThenThisSeason A',  # average of Team A's current-season opponents' current-season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioAllowedThenLastSeason A',  # average of Team A's previous-season opponents' previous-season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioAllowedThen2SeasonsAgo A',  # average of Team A's 2-seasons-prior opponents' 2-seasons-prior season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioAllowedThen3SeasonsAgo A',  # average of Team A's 3-seasons-prior opponents' 3-seasons-prior season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppAvgAst/TORatioAllowedNowThisSeason A',  # average of Team A's current-season opponents' up-to-date assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the current season
    'CurrentSoSAvgOppAvgAst/TORatioAllowedNowLastSeason A',  # average of Team A's current-season opponents' season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the previous season
    'CurrentSoSAvgOppAvgAst/TORatioAllowedNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the season 2 years prior
    'CurrentSoSAvgOppAvgAst/TORatioAllowedNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the season 3 years prior
    'PastSoSAvgOppAvgAst/TORatioAllowedNowLastSeason A',  # average of Team A's previous-season opponents' season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the previous season
    'PastSoSAvgOppAvgAst/TORatioAllowedNow2SeasonsAgo A',  # average of Team A's 2-seasons-prior opponents' season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the season 2 years prior
    'PastSoSAvgOppAvgAst/TORatioAllowedNow3SeasonsAgo A',  # average of Team A's 3-seasons-prior opponents' season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the season 3 years prior

    'CurrentSoSWeightedAvgOppAvgAst/TORatioMarginThenThisSeason A',  # average of Team A's current-season opponents' current-season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioMarginThenLastSeason A',  # average of Team A's previous-season opponents' previous-season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioMarginThen2SeasonsAgo A',  # average of Team A's 2-seasons-prior opponents' 2-seasons-prior season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioMarginThen3SeasonsAgo A',  # average of Team A's 3-seasons-prior opponents' 3-seasons-prior season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppAvgAst/TORatioMarginNowThisSeason A',  # average of Team A's current-season opponents' up-to-date differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the current season
    'CurrentSoSAvgOppAvgAst/TORatioMarginNowLastSeason A',  # average of Team A's current-season opponents' season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the previous season
    'CurrentSoSAvgOppAvgAst/TORatioMarginNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the season 2 years prior
    'CurrentSoSAvgOppAvgAst/TORatioMarginNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the season 3 years prior
    'PastSoSAvgOppAvgAst/TORatioMarginNowLastSeason A',  # average of Team A's previous-season opponents' season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the previous season
    'PastSoSAvgOppAvgAst/TORatioMarginNow2SeasonsAgo A',  # average of Team A's 2-seasons-prior opponents' season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the season 2 years prior
    'PastSoSAvgOppAvgAst/TORatioMarginNow3SeasonsAgo A',  # average of Team A's 3-seasons-prior opponents' season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the season 3 years prior

    'CurrentSoSWeightedAvgOppAvgAst/TORatio(alt)ThenThisSeason A',  # average of Team A's current-season opponents' current-season-long assist/turnover ratios, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)ThenLastSeason A',  # average of Team A's previous-season opponents' previous-season-long assist/turnover ratios, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)Then2SeasonsAgo A',  # average of Team A's 2-seasons-prior opponents' 2-seasons-prior season-long assist/turnover ratios, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)Then3SeasonsAgo A',  # average of Team A's 3-seasons-prior opponents' 3-seasons-prior season-long assist/turnover ratios, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)NowThisSeason A',  # average of Team A's current-season opponents' up-to-date assist/turnover ratios during the current season (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)NowLastSeason A',  # average of Team A's current-season opponents' season-long assist/turnover ratios during the previous season (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)Now2SeasonsAgo A',  # average of Team A's current-season opponents' season-long assist/turnover ratios during the season 2 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)Now3SeasonsAgo A',  # average of Team A's current-season opponents' season-long assist/turnover ratios during the season 3 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSAvgOppAvgAst/TORatio(alt)NowLastSeason A',  # average of Team A's previous-season opponents' season-long assist/turnover ratios during the previous season (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSAvgOppAvgAst/TORatio(alt)Now2SeasonsAgo A',  # average of Team A's 2-seasons-prior opponents' season-long assist/turnover ratios during the season 2 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSAvgOppAvgAst/TORatio(alt)Now3SeasonsAgo A',  # average of Team A's 3-seasons-prior opponents' season-long assist/turnover ratios during the season 3 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)

    'CurrentSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThenThisSeason A',  # average of Team A's current-season opponents' current-season-long assist/turnover ratios allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThenLastSeason A',  # average of Team A's previous-season opponents' previous-season-long assist/turnover ratios allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThen2SeasonsAgo A',  # average of Team A's 2-seasons-prior opponents' 2-seasons-prior season-long assist/turnover ratios allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThen3SeasonsAgo A',  # average of Team A's 3-seasons-prior opponents' 3-seasons-prior season-long assist/turnover ratios allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNowThisSeason A',  # average of Team A's current-season opponents' up-to-date assist/turnover ratios allowed during the current season (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNowLastSeason A',  # average of Team A's current-season opponents' season-long assist/turnover ratios allowed during the previous season (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long assist/turnover ratios allowed during the season 2 years prior (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long assist/turnover ratios allowed during the season 3 years prior (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'PastSoSAvgOppAvgAst/TORatio(alt)AllowedNowLastSeason A',  # average of Team A's previous-season opponents' season-long assist/turnover ratios allowed during the previous season (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'PastSoSAvgOppAvgAst/TORatio(alt)AllowedNow2SeasonsAgo A',  # average of Team A's 2-seasons-prior opponents' season-long assist/turnover ratios allowed during the season 2 years prior (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'PastSoSAvgOppAvgAst/TORatio(alt)AllowedNow3SeasonsAgo A',  # average of Team A's 3-seasons-prior opponents' season-long assist/turnover ratios allowed during the season 3 years prior (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)

    'CurrentSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThenThisSeason A',  # average of Team A's current-season opponents' current-season-long differences between assist/turnover ratio and assist/turnover ratio allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThenLastSeason A',  # average of Team A's previous-season opponents' previous-season-long differences between assist/turnover ratio and assist/turnover ratio allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThen2SeasonsAgo A',  # average of Team A's 2-seasons-prior opponents' 2-seasons-prior season-long differences between assist/turnover ratio and assist/turnover ratio allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThen3SeasonsAgo A',  # average of Team A's 3-seasons-prior opponents' 3-seasons-prior season-long differences between assist/turnover ratio and assist/turnover ratio allowed, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNowThisSeason A',  # average of Team A's current-season opponents' up-to-date differences between assist/turnover ratio and assist/turnover ratio allowed during the current season (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNowLastSeason A',  # average of Team A's current-season opponents' season-long differences between assist/turnover ratio and assist/turnover ratio allowed during the previous season (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long differences between assist/turnover ratio and assist/turnover ratio allowed during the season 2 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long differences between assist/turnover ratio and assist/turnover ratio allowed during the season 3 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSAvgOppAvgAst/TORatio(alt)MarginNowLastSeason A',  # average of Team A's previous-season opponents' season-long differences between assist/turnover ratio and assist/turnover ratio allowed during the previous season (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSAvgOppAvgAst/TORatio(alt)MarginNow2SeasonsAgo A',  # average of Team A's 2-seasons-prior opponents' season-long differences between assist/turnover ratio and assist/turnover ratio allowed during the season 2 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSAvgOppAvgAst/TORatio(alt)MarginNow3SeasonsAgo A',  # average of Team A's 3-seasons-prior opponents' season-long differences between assist/turnover ratio and assist/turnover ratio allowed during the season 3 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)

    'CurrentSoSWeightedAvgOppStlPerGameThenThisSeason A',  # average of Team A's current-season opponents' average steals per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average steals per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average steals per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average steals per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppStlPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average steals per game during the current season
    'CurrentSoSAvgOppStlPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average steals per game during the previous season
    'CurrentSoSAvgOppStlPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average steals per game during the season 2 years prior
    'CurrentSoSAvgOppStlPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average steals per game during the season 3 years prior
    'PastSoSAvgOppStlPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average steals per game during the previous season
    'PastSoSAvgOppStlPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average steals per game during the season 2 years prior
    'PastSoSAvgOppStlPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average steals per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppStlAllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average steals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlAllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average steals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlAllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average steals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlAllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average steals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppStlAllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average steals allowed per game during the current season
    'CurrentSoSAvgOppStlAllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average steals allowed per game during the previous season
    'CurrentSoSAvgOppStlAllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average steals allowed per game during the season 2 years prior
    'CurrentSoSAvgOppStlAllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average steals allowed per game during the season 3 years prior
    'PastSoSAvgOppStlAllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average steals allowed per game during the previous season
    'PastSoSAvgOppStlAllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average steals allowed per game during the season 2 years prior
    'PastSoSAvgOppStlAllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average steals allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppStlMarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between steals and steals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlMarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between steals and steals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlMarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between steals and steals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlMarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between steals and steals allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppStlMarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between steals and steals allowed per game during the current season
    'CurrentSoSAvgOppStlMarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between steals and steals allowed per game during the previous season
    'CurrentSoSAvgOppStlMarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between steals and steals allowed per game during the season 2 years prior
    'CurrentSoSAvgOppStlMarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between steals and steals allowed per game during the season 3 years prior
    'PastSoSAvgOppStlMarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between steals and steals allowed per game during the previous season
    'PastSoSAvgOppStlMarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between steals and steals allowed per game during the season 2 years prior
    'PastSoSAvgOppStlMarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between steals and steals allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppBlkPerGameThenThisSeason A',  # average of Team A's current-season opponents' average blocks per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average blocks per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average blocks per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average blocks per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppBlkPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average blocks per game during the current season
    'CurrentSoSAvgOppBlkPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average blocks per game during the previous season
    'CurrentSoSAvgOppBlkPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average blocks per game during the season 2 years prior
    'CurrentSoSAvgOppBlkPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average blocks per game during the season 3 years prior
    'PastSoSAvgOppBlkPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average blocks per game during the previous season
    'PastSoSAvgOppBlkPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average blocks per game during the season 2 years prior
    'PastSoSAvgOppBlkPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average blocks per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppBlkAllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average blocks allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkAllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average blocks allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkAllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average blocks allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkAllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average blocks allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppBlkAllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average blocks allowed per game during the current season
    'CurrentSoSAvgOppBlkAllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average blocks allowed per game during the previous season
    'CurrentSoSAvgOppBlkAllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average blocks allowed per game during the season 2 years prior
    'CurrentSoSAvgOppBlkAllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average blocks allowed per game during the season 3 years prior
    'PastSoSAvgOppBlkAllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average blocks allowed per game during the previous season
    'PastSoSAvgOppBlkAllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average blocks allowed per game during the season 2 years prior
    'PastSoSAvgOppBlkAllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average blocks allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppBlkMarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between blocks and blocks allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkMarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between blocks and blocks allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkMarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between blocks and blocks allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkMarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between blocks and blocks allowed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppBlkMarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between blocks and blocks allowed per game during the current season
    'CurrentSoSAvgOppBlkMarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between blocks and blocks allowed per game during the previous season
    'CurrentSoSAvgOppBlkMarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between blocks and blocks allowed per game during the season 2 years prior
    'CurrentSoSAvgOppBlkMarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between blocks and blocks allowed per game during the season 3 years prior
    'PastSoSAvgOppBlkMarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between blocks and blocks allowed per game during the previous season
    'PastSoSAvgOppBlkMarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between blocks and blocks allowed per game during the season 2 years prior
    'PastSoSAvgOppBlkMarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between blocks and blocks allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppPFPerGameThenThisSeason A',  # average of Team A's current-season opponents' average fouls committed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average fouls committed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average fouls committed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average fouls committed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppPFPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average fouls committed per game during the current season
    'CurrentSoSAvgOppPFPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average fouls committed per game during the previous season
    'CurrentSoSAvgOppPFPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average fouls committed per game during the season 2 years prior
    'CurrentSoSAvgOppPFPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average fouls committed per game during the season 3 years prior
    'PastSoSAvgOppPFPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average fouls committed per game during the previous season
    'PastSoSAvgOppPFPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average fouls committed per game during the season 2 years prior
    'PastSoSAvgOppPFPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average fouls committed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppPFAllowedPerGameThenThisSeason A',  # average of Team A's current-season opponents' average fouls absorbed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFAllowedPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average fouls absorbed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFAllowedPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average fouls absorbed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFAllowedPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average fouls absorbed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppPFAllowedPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average fouls absorbed per game during the current season
    'CurrentSoSAvgOppPFAllowedPerGameNowLastSeason A',  # average of Team A's current-season opponents' season average fouls absorbed per game during the previous season
    'CurrentSoSAvgOppPFAllowedPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season average fouls absorbed per game during the season 2 years prior
    'CurrentSoSAvgOppPFAllowedPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season average fouls absorbed per game during the season 3 years prior
    'PastSoSAvgOppPFAllowedPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average fouls absorbed per game during the previous season
    'PastSoSAvgOppPFAllowedPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average fouls absorbed per game during the season 2 years prior
    'PastSoSAvgOppPFAllowedPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average fouls absorbed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppPFMarginPerGameThenThisSeason A',  # average of Team A's current-season opponents' average difference between fouls committed and fouls absorbed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFMarginPerGameThenLastSeason A',  # average of Team A's previous-season opponents' average difference between fouls committed and fouls absorbed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFMarginPerGameThen2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' average difference between fouls committed and fouls absorbed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFMarginPerGameThen3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' average difference between fouls committed and fouls absorbed per game, recorded immediately prior to playing Team A, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppPFMarginPerGameNowThisSeason A',  # average of Team A's current-season opponents' up-to-date average difference between fouls committed and fouls absorbed per game during the current season
    'CurrentSoSAvgOppPFMarginPerGameNowLastSeason A',  # average of Team A's current-season opponents' season-long average difference between fouls committed and fouls absorbed per game during the previous season
    'CurrentSoSAvgOppPFMarginPerGameNow2SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between fouls committed and fouls absorbed per game during the season 2 years prior
    'CurrentSoSAvgOppPFMarginPerGameNow3SeasonsAgo A',  # average of Team A's current-season opponents' season-long average difference between fouls committed and fouls absorbed per game during the season 3 years prior
    'PastSoSAvgOppPFMarginPerGameNowLastSeason A',  # average of Team A's previous-season opponents' season average difference between fouls committed and fouls absorbed per game during the previous season
    'PastSoSAvgOppPFMarginPerGameNow2SeasonsAgo A',  # average of Team A's 2-years-prior-season opponents' season average difference between fouls committed and fouls absorbed per game during the season 2 years prior
    'PastSoSAvgOppPFMarginPerGameNow3SeasonsAgo A',  # average of Team A's 3-years-prior-season opponents' season average difference between fouls committed and fouls absorbed per game during the season 3 years prior

    # Team B season totals

    'NumGamesPlayedThisSeason B',  # the number of games Team B has played during the current season

    'WinPctThisSeason B',  # win percentage for Team B during the current season
    'WinPctLastSeason B',  # win percentage for Team B during the previous season
    'WinPct2SeasonsAgo B',  # win percentage for Team B during the season 2 years prior
    'WinPct3SeasonsAgo B',  # win percentage for Team B during the season 3 years prior

    'FlipCloseWinPctThisSeason B',  # win percentage for Team B during the current season (had the results of all of their close games been flipped)
    'FlipCloseWinPctLastSeason B',  # win percentage for Team B during the previous season (had the results of all of their close games been flipped)
    'FlipCloseWinPct2SeasonsAgo B',  # win percentage for Team B during the season 2 years prior (had the results of all of their close games been flipped)
    'FlipCloseWinPct3SeasonsAgo B',  # win percentage for Team B during the season 3 years prior (had the results of all of their close games been flipped)

    'WinCloseWinPctThisSeason B',  # win percentage for Team B during the current season (had they won all of their close games)
    'WinCloseWinPctLastSeason B',  # win percentage for Team B during the previous season (had they won all of their close games)
    'WinCloseWinPct2SeasonsAgo B',  # win percentage for Team B during the season 2 years prior (had they won all of their close games)
    'WinCloseWinPct3SeasonsAgo B',  # win percentage for Team B during the season 3 years prior (had they won all of their close games)

    'LoseCloseWinPctThisSeason B',  # win percentage for Team B during the current season (had they lost all of their close games)
    'LoseCloseWinPctLastSeason B',  # win percentage for Team B during the previous season (had they lost all of their close games)
    'LoseCloseWinPct2SeasonsAgo B',  # win percentage for Team B during the season 2 years prior (had they lost all of their close games)
    'LoseCloseWinPct3SeasonsAgo B',  # win percentage for Team B during the season 3 years prior (had they lost all of their close games)

    'PointsPerGameThisSeason B',  # average points scored by Team B per game during the current season
    'PointsPerGameLastSeason B',  # average points scored by Team B per game during the previous season
    'PointsPerGame2SeasonsAgo B',  # average points scored by Team B per game during the season 2 years prior
    'PointsPerGame3SeasonsAgo B',  # average points scored by Team B per game during the season 3 years prior

    'PointsAllowedPerGameThisSeason B',  # average points allowed by Team B per game during the current season
    'PointsAllowedPerGameLastSeason B',  # average points allowed by Team B per game during the previous season
    'PointsAllowedPerGame2SeasonsAgo B',  # average points allowed by Team B per game during the season 2 years prior
    'PointsAllowedPerGame3SeasonsAgo B',  # average points allowed by Team B per game during the season 3 years prior

    'PointsMarginPerGameThisSeason B',  # average difference between points scored by Team B and points allowed by Team B per game during the current season
    'PointsMarginPerGameLastSeason B',  # average difference between points scored by Team B and points allowed by Team B per game during the previous season
    'PointsMarginPerGame2SeasonsAgo B',  # average difference between points scored by Team B and points allowed by Team B per game during the season 2 years prior
    'PointsMarginPerGame3SeasonsAgo B',  # average difference between points scored by Team B and points allowed by Team B per game during the season 3 years prior

    'FGMPerGameThisSeason B',  # average number of field goals made by Team B per game during the current season
    'FGMPerGameLastSeason B',  # average number of field goals made by Team B per game during the previous season
    'FGMPerGame2SeasonsAgo B',  # average number of field goals made by Team B per game during the season 2 years prior
    'FGMPerGame3SeasonsAgo B',  # average number of field goals made by Team B per game during the season 3 years prior

    'FGMAllowedPerGameThisSeason B',  # average number of field goals allowed by Team B per game during the current season
    'FGMAllowedPerGameLastSeason B',  # average number of field goals allowed by Team B per game during the previous season
    'FGMAllowedPerGame2SeasonsAgo B',  # average number of field goals allowed by Team B per game during the season 2 years prior
    'FGMAllowedPerGame3SeasonsAgo B',  # average number of field goals allowed by Team B per game during the season 3 years prior

    'FGMMarginPerGameThisSeason B',  # average difference between field goals made by Team B and field goals allowed by Team B per game during the current season
    'FGMMarginPerGameLastSeason B',  # average difference between field goals made by Team B and field goals allowed by Team B per game during the previous season
    'FGMMarginPerGame2SeasonsAgo B',  # average difference between field goals made by Team B and field goals allowed by Team B per game during the season 2 years prior
    'FGMMarginPerGame3SeasonsAgo B',  # average difference between field goals made by Team B and field goals allowed by Team B per game during the season 3 years prior

    'FGAPerGameThisSeason B',  # average number of field goals attempted by Team B per game during the current season
    'FGAPerGameLastSeason B',  # average number of field goals attempted by Team B per game during the previous season
    'FGAPerGame2SeasonsAgo B',  # average number of field goals attempted by Team B per game during the season 2 years prior
    'FGAPerGame3SeasonsAgo B',  # average number of field goals attempted by Team B per game during the season 3 years prior

    'FGAAllowedPerGameThisSeason B',  # average number of field goal attempts allowed by Team B per game during the current season
    'FGAAllowedPerGameLastSeason B',  # average number of field goal attempts allowed by Team B per game during the previous season
    'FGAAllowedPerGame2SeasonsAgo B',  # average number of field goal attempts allowed by Team B per game during the season 2 years prior
    'FGAAllowedPerGame3SeasonsAgo B',  # average number of field goal attempts allowed by Team B per game during the season 3 years prior

    'FGAMarginPerGameThisSeason B',  # average difference between number of field goals attempted by Team B and number of field goal attempts allowed by Team B per game during the current season
    'FGAMarginPerGameLastSeason B',  # average difference between number of field goals attempted by Team B and number of field goal attempts allowed by Team B per game during the previous season
    'FGAMarginPerGame2SeasonsAgo B',  # average difference between number of field goals attempted by Team B and number of field goal attempts allowed by Team B per game during the season 2 years prior
    'FGAMarginPerGame3SeasonsAgo B',  # average difference between number of field goals attempted by Team B and number of field goal attempts allowed by Team B per game during the season 3 years prior

    'FGPctThisSeason B',  # Team B's field goal percentage during the current season
    'FGPctLastSeason B',  # Team B's field goal percentage during the previous season
    'FGPct2SeasonsAgo B',  # Team B's field goal percentage during the season 2 years prior
    'FGPct3SeasonsAgo B',  # Team B's field goal percentage during the season 3 years prior

    'FGPctAllowedThisSeason B',  # Team B's field goal percentage allowed during the current season
    'FGPctAllowedLastSeason B',  # Team B's field goal percentage allowed during the previous season
    'FGPctAllowed2SeasonsAgo B',  # Team B's field goal percentage allowed during the season 2 years prior
    'FGPctAllowed3SeasonsAgo B',  # Team B's field goal percentage allowed during the season 3 years prior

    'FGPctMarginThisSeason B',  # difference between Team B's field goal percentage and Team B's field goal percentage allowed during the current season
    'FGPctMarginLastSeason B',  # difference between Team B's field goal percentage and Team B's field goal percentage allowed during the previous season
    'FGPctMargin2SeasonsAgo B',  # difference between Team B's field goal percentage and Team B's field goal percentage allowed during the season 2 years prior
    'FGPctMargin3SeasonsAgo B',  # difference between Team B's field goal percentage and Team B's field goal percentage allowed during the season 3 years prior

    'FGM3PerGameThisSeason B',  # average number of 3-point field goals made by Team B per game during the current season
    'FGM3PerGameLastSeason B',  # average number of 3-point field goals made by Team B per game during the previous season
    'FGM3PerGame2SeasonsAgo B',  # average number of 3-point field goals made by Team B per game during the season 2 years prior
    'FGM3PerGame3SeasonsAgo B',  # average number of 3-point field goals made by Team B per game during the season 3 years prior

    'FGM3AllowedPerGameThisSeason B',  # average number of 3-point field goals allowed by Team B per game during the current season
    'FGM3AllowedPerGameLastSeason B',  # average number of 3-point field goals allowed by Team B per game during the previous season
    'FGM3AllowedPerGame2SeasonsAgo B',  # average number of 3-point field goals allowed by Team B per game during the season 2 years prior
    'FGM3AllowedPerGame3SeasonsAgo B',  # average number of 3-point field goals allowed by Team B per game during the season 3 years prior

    'FGM3MarginPerGameThisSeason B',  # average difference between number of 3-point field goals made by Team B and number of 3-point field goals allowed by Team B per game during the current season
    'FGM3MarginPerGameLastSeason B',  # average difference between number of 3-point field goals made by Team B and number of 3-point field goals allowed by Team B per game during the previous season
    'FGM3MarginPerGame2SeasonsAgo B',  # average difference between number of 3-point field goals made by Team B and number of 3-point field goals allowed by Team B per game during the season 2 years prior
    'FGM3MarginPerGame3SeasonsAgo B',  # average difference between number of 3-point field goals made by Team B and number of 3-point field goals allowed by Team B per game during the season 3 years prior

    'FGA3PerGameThisSeason B',  # average number of 3-point field goal attempts made by Team B per game during the current season
    'FGA3PerGameLastSeason B',  # average number of 3-point field goal attempts made by Team B per game during the previous season
    'FGA3PerGame2SeasonsAgo B',  # average number of 3-point field goal attempts made by Team B per game during the season 2 years prior
    'FGA3PerGame3SeasonsAgo B',  # average number of 3-point field goal attempts made by Team B per game during the season 3 years prior

    'FGA3AllowedPerGameThisSeason B',  # average number of 3-point field goal attempts allowed by Team B per game during the current season
    'FGA3AllowedPerGameLastSeason B',  # average number of 3-point field goal attempts allowed by Team B per game during the previous season
    'FGA3AllowedPerGame2SeasonsAgo B',  # average number of 3-point field goal attempts allowed by Team B per game during the season 2 years prior
    'FGA3AllowedPerGame3SeasonsAgo B',  # average number of 3-point field goal attempts allowed by Team B per game during the season 3 years prior

    'FGA3MarginPerGameThisSeason B',  # average difference between number of 3-point field goals attempted by Team B and number of 3-point field goal attempts allowed by Team B per game during the current season
    'FGA3MarginPerGameLastSeason B',  # average difference between number of 3-point field goals attempted by Team B and number of 3-point field goal attempts allowed by Team B per game during the previous season
    'FGA3MarginPerGame2SeasonsAgo B',  # average difference between number of 3-point field goals attempted by Team B and number of 3-point field goal attempts allowed by Team B per game during the season 2 years prior
    'FGA3MarginPerGame3SeasonsAgo B',  # average difference between number of 3-point field goals attempted by Team B and number of 3-point field goal attempts allowed by Team B per game during the season 3 years prior

    'FG3PctThisSeason B',  # Team B's 3-point field goal percentage during the current season
    'FG3PctLastSeason B',  # Team B's 3-point field goal percentage during the previous season
    'FG3Pct2SeasonsAgo B',  # Team B's 3-point field goal percentage during the season 2 years prior
    'FG3Pct3SeasonsAgo B',  # Team B's 3-point field goal percentage during the season 3 years prior

    'FG3PctAllowedThisSeason B',  # Team B's 3-point field goal percentage allowed during the current season
    'FG3PctAllowedLastSeason B',  # Team B's 3-point field goal percentage allowed during the previous season
    'FG3PctAllowed2SeasonsAgo B',  # Team B's 3-point field goal percentage allowed during the season 2 years prior
    'FG3PctAllowed3SeasonsAgo B',  # Team B's 3-point field goal percentage allowed during the season 3 years prior

    'FG3PctMarginThisSeason B',  # difference between Team B's 3-point field goal percentage and Team B's 3-point field goal percentage allowed during the current season
    'FG3PctMarginLastSeason B',  # difference between Team B's 3-point field goal percentage and Team B's 3-point field goal percentage allowed during the previous season
    'FG3PctMargin2SeasonsAgo B',  # difference between Team B's 3-point field goal percentage and Team B's 3-point field goal percentage allowed during the season 2 years prior
    'FG3PctMargin3SeasonsAgo B',  # difference between Team B's 3-point field goal percentage and Team B's 3-point field goal percentage allowed during the season 3 years prior

    'FTMPerGameThisSeason B',  # average number of free-throws made by Team B per game during the current season
    'FTMPerGameLastSeason B',  # average number of free-throws made by Team B per game during the previous season
    'FTMPerGame2SeasonsAgo B',  # average number of free-throws made by Team B per game during the season 2 years prior
    'FTMPerGame3SeasonsAgo B',  # average number of free-throws made by Team B per game during the season 3 years prior

    'FTMAllowedPerGameThisSeason B',  # average number of successful free-throws allowed by Team B per game during the current season
    'FTMAllowedPerGameLastSeason B',  # average number of successful free-throws allowed by Team B per game during the previous season
    'FTMAllowedPerGame2SeasonsAgo B',  # average number of successful free-throws allowed by Team B per game during the season 2 years prior
    'FTMAllowedPerGame3SeasonsAgo B',  # average number of successful free-throws allowed by Team B per game during the season 3 years prior

    'FTMMarginPerGameThisSeason B',  # average difference between number of free-throws made by Team B and number of successful free-throws allowed by Team B per game during the current season
    'FTMMarginPerGameLastSeason B',  # average difference between number of free-throws made by Team B and number of successful free-throws allowed by Team B per game during the previous season
    'FTMMarginPerGame2SeasonsAgo B',  # average difference between number of free-throws made by Team B and number of successful free-throws allowed by Team B per game during the season 2 years prior
    'FTMMarginPerGame3SeasonsAgo B',  # average difference between number of free-throws made by Team B and number of successful free-throws allowed by Team B per game during the season 3 years prior

    'FTAPerGameThisSeason B',  # average number of free-throws attempted by Team B per game during the current season
    'FTAPerGameLastSeason B',  # average number of free-throws attempted by Team B per game during the previous season
    'FTAPerGame2SeasonsAgo B',  # average number of free-throws attempted by Team B per game during the season 2 years prior
    'FTAPerGame3SeasonsAgo B',  # average number of free-throws attempted by Team B per game during the season 3 years prior

    'FTAAllowedPerGameThisSeason B',  # average number of free-throw attempts allowed by Team B per game during the current season
    'FTAAllowedPerGameLastSeason B',  # average number of free-throw attempts allowed by Team B per game during the previous season
    'FTAAllowedPerGame2SeasonsAgo B',  # average number of free-throw attempts allowed by Team B per game during the season 2 years prior
    'FTAAllowedPerGame3SeasonsAgo B',  # average number of free-throw attempts allowed by Team B per game during the season 3 years prior

    'FTAMarginPerGameThisSeason B',  # average difference between number of free-throws attempted by Team B and number of free-throw attempts allowed by Team B per game during the current season
    'FTAMarginPerGameLastSeason B',  # average difference between number of free-throws attempted by Team B and number of free-throw attempts allowed by Team B per game during the previous season
    'FTAMarginPerGame2SeasonsAgo B',  # average difference between number of free-throws attempted by Team B and number of free-throw attempts allowed by Team B per game during the season 2 years prior
    'FTAMarginPerGame3SeasonsAgo B',  # average difference between number of free-throws attempted by Team B and number of free-throw attempts allowed by Team B per game during the season 3 years prior

    'FTPctThisSeason B',  # Team B's free-throw percentage during the current season
    'FTPctLastSeason B',  # Team B's free-throw percentage during the previous season
    'FTPct2SeasonsAgo B',  # Team B's free-throw percentage during the season 2 years prior
    'FTPct3SeasonsAgo B',  # Team B's free-throw percentage during the season 3 years prior

    'FTPctAllowedThisSeason B',  # Team B's free-throw percentage allowed during the current season
    'FTPctAllowedLastSeason B',  # Team B's free-throw percentage allowed during the previous season
    'FTPctAllowed2SeasonsAgo B',  # Team B's free-throw percentage allowed during the season 2 years prior
    'FTPctAllowed3SeasonsAgo B',  # Team B's free-throw percentage allowed during the season 3 years prior

    'FTPctMarginThisSeason B',  # difference between Team B's free-throw percentage and Team B's free-throw percentage allowed during the current season
    'FTPctMarginLastSeason B',  # difference between Team B's free-throw percentage and Team B's free-throw percentage allowed during the previous season
    'FTPctMargin2SeasonsAgo B',  # difference between Team B's free-throw percentage and Team B's free-throw percentage allowed during the season 2 years prior
    'FTPctMargin3SeasonsAgo B',  # difference between Team B's free-throw percentage and Team B's free-throw percentage allowed during the season 3 years prior

    'RebPerGameThisSeason B',  # average number of rebounds by Team B per game during the current season
    'RebPerGameLastSeason B',  # average number of rebounds by Team B per game during the previous season
    'RebPerGame2SeasonsAgo B',  # average number of rebounds by Team B per game during the season 2 years prior
    'RebPerGame3SeasonsAgo B',  # average number of rebounds by Team B per game during the season 3 years prior

    'RebAllowedPerGameThisSeason B',  # average number of rebounds allowed by Team B per game during the current season
    'RebAllowedPerGameLastSeason B',  # average number of rebounds allowed by Team B per game during the previous season
    'RebAllowedPerGame2SeasonsAgo B',  # average number of rebounds allowed by Team B per game during the season 2 years prior
    'RebAllowedPerGame3SeasonsAgo B',  # average number of rebounds allowed by Team B per game during the season 3 years prior

    'RebMarginPerGameThisSeason B',  # average difference between number of rebounds by Team B and number of rebounds allowed by Team B per game during the current season
    'RebMarginPerGameLastSeason B',  # average difference between number of rebounds by Team B and number of rebounds allowed by Team B per game during the previous season
    'RebMarginPerGame2SeasonsAgo B',  # average difference between number of rebounds by Team B and number of rebounds allowed by Team B per game during the season 2 years prior
    'RebMarginPerGame3SeasonsAgo B',  # average difference between number of rebounds by Team B and number of rebounds allowed by Team B per game during the season 3 years prior

    'ORebPerGameThisSeason B',  # average number of offensive rebounds by Team B per game during the current season
    'ORebPerGameLastSeason B',  # average number of offensive rebounds by Team B per game during the previous season
    'ORebPerGame2SeasonsAgo B',  # average number of offensive rebounds by Team B per game during the season 2 years prior
    'ORebPerGame3SeasonsAgo B',  # average number of offensive rebounds by Team B per game during the season 3 years prior

    'ORebAllowedPerGameThisSeason B',  # average number of offensive rebounds allowed by Team B per game during the current season
    'ORebAllowedPerGameLastSeason B',  # average number of offensive rebounds allowed by Team B per game during the previous season
    'ORebAllowedPerGame2SeasonsAgo B',  # average number of offensive rebounds allowed by Team B per game during the season 2 years prior
    'ORebAllowedPerGame3SeasonsAgo B',  # average number of offensive rebounds allowed by Team B per game during the season 3 years prior

    'ORebMarginPerGameThisSeason B',  # average difference between number of offensive rebounds by Team B and number of rebounds allowed by Team B per game during the current season
    'ORebMarginPerGameLastSeason B',  # average difference between number of offensive rebounds by Team B and number of rebounds allowed by Team B per game during the previous season
    'ORebMarginPerGame2SeasonsAgo B',  # average difference between number of offensive rebounds by Team B and number of rebounds allowed by Team B per game during the season 2 years prior
    'ORebMarginPerGame3SeasonsAgo B',  # average difference between number of offensive rebounds by Team B and number of rebounds allowed by Team B per game during the season 3 years prior

    'DRebPerGameThisSeason B',  # average number of defensive rebounds by Team B per game during the current season
    'DRebPerGameLastSeason B',  # average number of defensive rebounds by Team B per game during the previous season
    'DRebPerGame2SeasonsAgo B',  # average number of defensive rebounds by Team B per game during the season 2 years prior
    'DRebPerGame3SeasonsAgo B',  # average number of defensive rebounds by Team B per game during the season 3 years prior

    'DRebAllowedPerGameThisSeason B',  # average number of defensive rebounds allowed by Team B per game during the current season
    'DRebAllowedPerGameLastSeason B',  # average number of defensive rebounds allowed by Team B per game during the previous season
    'DRebAllowedPerGame2SeasonsAgo B',  # average number of defensive rebounds allowed by Team B per game during the season 2 years prior
    'DRebAllowedPerGame3SeasonsAgo B',  # average number of defensive rebounds allowed by Team B per game during the season 3 years prior

    'DRebMarginPerGameThisSeason B',  # average difference between number of defensive rebounds by Team B and number of rebounds allowed by Team B per game during the current season
    'DRebMarginPerGameLastSeason B',  # average difference between number of defensive rebounds by Team B and number of rebounds allowed by Team B per game during the previous season
    'DRebMarginPerGame2SeasonsAgo B',  # average difference between number of defensive rebounds by Team B and number of rebounds allowed by Team B per game during the season 2 years prior
    'DRebMarginPerGame3SeasonsAgo B',  # average difference between number of defensive rebounds by Team B and number of rebounds allowed by Team B per game during the season 3 years prior

    'AstPerGameThisSeason B',  # average number of assists by Team B per game during the current season
    'AstPerGameLastSeason B',  # average number of assists by Team B per game during the previous season
    'AstPerGame2SeasonsAgo B',  # average number of assists by Team B per game during the season 2 years prior
    'AstPerGame3SeasonsAgo B',  # average number of assists by Team B per game during the season 3 years prior

    'AstAllowedPerGameThisSeason B',  # average number of assists allowed by Team B per game during the current season
    'AstAllowedPerGameLastSeason B',  # average number of assists allowed by Team B per game during the previous season
    'AstAllowedPerGame2SeasonsAgo B',  # average number of assists allowed by Team B per game during the season 2 years prior
    'AstAllowedPerGame3SeasonsAgo B',  # average number of assists allowed by Team B per game during the season 3 years prior

    'AstMarginPerGameThisSeason B',  # average difference between number of assists by Team B and number of assists allowed by Team B per game during the current season
    'AstMarginPerGameLastSeason B',  # average difference between number of assists by Team B and number of assists allowed by Team B per game during the previous season
    'AstMarginPerGame2SeasonsAgo B',  # average difference between number of assists by Team B and number of assists allowed by Team B per game during the season 2 years prior
    'AstMarginPerGame3SeasonsAgo B',  # average difference between number of assists by Team B and number of assists allowed by Team B per game during the season 3 years prior

    'TOPerGameThisSeason B',  # average number of turnovers by Team B per game during the current season
    'TOPerGameLastSeason B',  # average number of turnovers by Team B per game during the previous season
    'TOPerGame2SeasonsAgo B',  # average number of turnovers by Team B per game during the season 2 years prior
    'TOPerGame3SeasonsAgo B',  # average number of turnovers by Team B per game during the season 3 years prior

    'TOAllowedPerGameThisSeason B',  # average number of turnovers forced by Team B per game during the current season
    'TOAllowedPerGameLastSeason B',  # average number of turnovers forced by Team B per game during the previous season
    'TOAllowedPerGame2SeasonsAgo B',  # average number of turnovers forced by Team B per game during the season 2 years prior
    'TOAllowedPerGame3SeasonsAgo B',  # average number of turnovers forced by Team B per game during the season 3 years prior

    'TOMarginPerGameThisSeason B',  # average difference between number of turnovers by Team B and number of turnovers forced by Team B per game during the current season
    'TOMarginPerGameLastSeason B',  # average difference between number of turnovers by Team B and number of turnovers forced by Team B per game during the previous season
    'TOMarginPerGame2SeasonsAgo B',  # average difference between number of turnovers by Team B and number of turnovers forced by Team B per game during the season 2 years prior
    'TOMarginPerGame3SeasonsAgo B',  # average difference between number of turnovers by Team B and number of turnovers forced by Team B per game during the season 3 years prior

    'AvgAst/TORatioThisSeason B',  # Team B's season total assists divided by Team B's season total turnovers during the current season
    'AvgAst/TORatioLastSeason B',  # Team B's season total assists divided by Team B's season total turnovers during the previous season
    'AvgAst/TORatio2SeasonsAgo B',  # Team B's season total assists divided by Team B's season total turnovers during the season 2 years prior
    'AvgAst/TORatio3SeasonsAgo B',  # Team B's season total assists divided by Team B's season total turnovers during the season 3 years prior

    'AvgAst/TORatioAllowedThisSeason B',  # Team B's season total assists allowed divided by Team B's season total turnovers forced during the current season
    'AvgAst/TORatioAllowedLastSeason B',  # Team B's season total assists allowed divided by Team B's season total turnovers forced during the previous season
    'AvgAst/TORatioAllowed2SeasonsAgo B',  # Team B's season total assists allowed divided by Team B's season total turnovers forced during the season 2 years prior
    'AvgAst/TORatioAllowed3SeasonsAgo B',  # Team B's season total assists allowed divided by Team B's season total turnovers forced during the season 3 years prior

    'AvgAst/TORatioMarginThisSeason B',  # (Team B's season total assists divided by Team B's season total turnovers) minus (Team B's season total assists allowed divided by Team B's season total turnovers forced) during the current season
    'AvgAst/TORatioMarginLastSeason B',  # (Team B's season total assists divided by Team B's season total turnovers) minus (Team B's season total assists allowed divided by Team B's season total turnovers forced) during the previous season
    'AvgAst/TORatioMargin2SeasonsAgo B',  # (Team B's season total assists divided by Team B's season total turnovers) minus (Team B's season total assists allowed divided by Team B's season total turnovers forced) during the season 2 years prior
    'AvgAst/TORatioMargin3SeasonsAgo B',  # (Team B's season total assists divided by Team B's season total turnovers) minus (Team B's season total assists allowed divided by Team B's season total turnovers forced) during the season 3 years prior

    'AvgAst/TORatio(alt)ThisSeason B',  # average of Team B's assist/turnover ratios for each game Team B has played during the current season (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)LastSeason B',  # average of Team B's assist/turnover ratios for each game Team B played during the previous season (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)2SeasonsAgo B',  # average of Team B's assist/turnover ratios for each game Team B played during the season 2 years prior (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)3SeasonsAgo B',  # average of Team B's assist/turnover ratios for each game Team B played during the season 3 years prior (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)

    'AvgAst/TORatio(alt)AllowedThisSeason B',  # average of Team B's opponent's assist/turnover ratios for each game Team B has played during the current season (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)AllowedLastSeason B',  # average of Team B's opponent's assist/turnover ratios for each game Team B has played during the previous season (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)Allowed2SeasonsAgo B',  # average of Team B's opponent's assist/turnover ratios for each game Team B has played during the season 2 years prior (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)Allowed3SeasonsAgo B',  # average of Team B's opponent's assist/turnover ratios for each game Team B has played during the season 3 years prior (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)

    'AvgAst/TORatio(alt)MarginThisSeason B',  # average of the differences between Team B's assist/turnover ratio and Team B's opponent's assist/turnover ratio for each game Team B has played during the current season (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)MarginLastSeason B',  # average of the differences between Team B's assist/turnover ratio and Team B's opponent's assist/turnover ratio for each game Team B played during the previous season (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)Margin2SeasonsAgo B',  # average of the differences between Team B's assist/turnover ratio and Team B's opponent's assist/turnover ratio for each game Team B played during the season 2 years prior (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'AvgAst/TORatio(alt)Margin3SeasonsAgo B',  # average of the differences between Team B's assist/turnover ratio and Team B's opponent's assist/turnover ratio for each game Team B played during the season 3 years prior (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)

    'StlPerGameThisSeason B',  # average number of steals by Team B per game during the current season
    'StlPerGameLastSeason B',  # average number of steals by Team B per game during the previous season
    'StlPerGame2SeasonsAgo B',  # average number of steals by Team B per game during the season 2 years prior
    'StlPerGame3SeasonsAgo B',  # average number of steals by Team B per game during the season 3 years prior

    'StlAllowedPerGameThisSeason B',  # average number of steals allowed by Team B per game during the current season
    'StlAllowedPerGameLastSeason B',  # average number of steals allowed by Team B per game during the previous season
    'StlAllowedPerGame2SeasonsAgo B',  # average number of steals allowed by Team B per game during the season 2 years prior
    'StlAllowedPerGame3SeasonsAgo B',  # average number of steals allowed by Team B per game during the season 3 years prior

    'StlMarginPerGameThisSeason B',  # average difference between number of steals by Team B and number of steals allowed by Team B per game during the current season
    'StlMarginPerGameLastSeason B',  # average difference between number of steals by Team B and number of steals allowed by Team B per game during the previous season
    'StlMarginPerGame2SeasonsAgo B',  # average difference between number of steals by Team B and number of steals allowed by Team B per game during the season 2 years prior
    'StlMarginPerGame3SeasonsAgo B',  # average difference between number of steals by Team B and number of steals allowed by Team B per game during the season 3 years prior

    'BlkPerGameThisSeason B',  # average number of blocks by Team B per game during the current season
    'BlkPerGameLastSeason B',  # average number of blocks by Team B per game during the previous season
    'BlkPerGame2SeasonsAgo B',  # average number of blocks by Team B per game during the season 2 years prior
    'BlkPerGame3SeasonsAgo B',  # average number of blocks by Team B per game during the season 3 years prior

    'BlkAllowedPerGameThisSeason B',  # average number of blocks allowed by Team B per game during the current season
    'BlkAllowedPerGameLastSeason B',  # average number of blocks allowed by Team B per game during the previous season
    'BlkAllowedPerGame2SeasonsAgo B',  # average number of blocks allowed by Team B per game during the season 2 years prior
    'BlkAllowedPerGame3SeasonsAgo B',  # average number of blocks allowed by Team B per game during the season 3 years prior

    'BlkMarginPerGameThisSeason B',  # average difference between number of blocks by Team B and number of blocks allowed by Team B per game during the current season
    'BlkMarginPerGameLastSeason B',  # average difference between number of blocks by Team B and number of blocks allowed by Team B per game during the previous season
    'BlkMarginPerGame2SeasonsAgo B',  # average difference between number of blocks by Team B and number of blocks allowed by Team B per game during the season 2 years prior
    'BlkMarginPerGame3SeasonsAgo B',  # average difference between number of blocks by Team B and number of blocks allowed by Team B per game during the season 3 years prior

    'PFPerGameThisSeason B',  # average number of fouls committed by Team B per game during the current season
    'PFPerGameLastSeason B',  # average number of fouls committed by Team B per game during the previous season
    'PFPerGame2SeasonsAgo B',  # average number of fouls committed by Team B per game during the season 2 years prior
    'PFPerGame3SeasonsAgo B',  # average number of fouls committed by Team B per game during the season 3 years prior

    'PFAllowedPerGameThisSeason B',  # average number of fouls absorbed by Team B per game during the current season
    'PFAllowedPerGameLastSeason B',  # average number of fouls absorbed by Team B per game during the previous season
    'PFAllowedPerGame2SeasonsAgo B',  # average number of fouls absorbed by Team B per game during the season 2 years prior
    'PFAllowedPerGame3SeasonsAgo B',  # average number of fouls absorbed by Team B per game during the season 3 years prior

    'PFMarginPerGameThisSeason B',  # average difference between number of fouls committed by Team B and number of fouls absorbed by Team B per game during the current season
    'PFMarginPerGameLastSeason B',  # average difference between number of fouls committed by Team B and number of fouls absorbed by Team B per game during the previous season
    'PFMarginPerGame2SeasonsAgo B',  # average difference between number of fouls committed by Team B and number of fouls absorbed by Team B per game during the season 2 years prior
    'PFMarginPerGame3SeasonsAgo B',  # average difference between number of fouls committed by Team B and number of fouls absorbed by Team B per game during the season 3 years prior

    # Team B strength of schedule

    'CurrentSoSWeightedAvgOppWinPctThenThisSeason B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the current season
    'PastSoSWeightedAvgOppWinPctThenLastSeason B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the
    'PastSoSWeightedAvgOppWinPctThen2SeasonsAgo B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the
    'PastSoSWeightedAvgOppWinPctThen3SeasonsAgo B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the
    'CurrentSoSAvgOppWinPctNowThisSeason B',  # average up-to-date win percentage (counting only the current season) of the teams which Team B has played during the current season
    'CurrentSoSAvgOppWinPctNowLastSeason B',  # average end-of-season win percentage (counting only the previous season) of the teams which Team B has played during the current season
    'CurrentSoSAvgOppWinPctNow2SeasonsAgo B',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team B has played during the current season
    'CurrentSoSAvgOppWinPctNow3SeasonsAgo B',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team B has played during the current season
    'PastSoSAvgOppWinPctNowLastSeason B',  # average end-of-season win percentage (counting only the previous season) of the teams which Team B played during the previous season
    'PastSoSAvgOppWinPctNow2SeasonsAgo B',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team B played during the season 2 years prior
    'PastSoSAvgOppWinPctNow3SeasonsAgo B',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team B played during the season 3 years prior

    'CurrentSoSWeightedAvgOppFlipCloseWinPctThenThisSeason B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the current season (had the results of all of their close games been flipped)
    'PastSoSWeightedAvgOppFlipCloseWinPctThenLastSeason B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the previous season (had the results of all of their close games been flipped)
    'PastSoSWeightedAvgOppFlipCloseWinPctThen2SeasonsAgo B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the season 2 years prior (had the results of all of their close games been flipped)
    'PastSoSWeightedAvgOppFlipCloseWinPctThen3SeasonsAgo B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the season 3 years prior (had the results of all of their close games been flipped)
    'CurrentSoSAvgOppFlipCloseWinPctNowThisSeason B',  # average up-to-date win percentage (counting only the current season) of the teams which Team B has played during the current season (had the results of all of their close games been flipped)
    'CurrentSoSAvgOppFlipCloseWinPctNowLastSeason B',  # average end-of-season win percentage (counting only the previous season) of the teams which Team B has played during the current season (had the results of all of their close games been flipped)
    'CurrentSoSAvgOppFlipCloseWinPctNow2SeasonsAgo B',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team B has played during the current season (had the results of all of their close games been flipped)
    'CurrentSoSAvgOppFlipCloseWinPctNow3SeasonsAgo B',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team B has played during the current season (had the results of all of their close games been flipped)
    'PastSoSAvgOppFlipCloseWinPctNowLastSeason B',  # average end-of-season win percentage (counting only the previous season) of the teams which Team B played during the previous season (had the results of all of their close games been flipped)
    'PastSoSAvgOppFlipCloseWinPctNow2SeasonsAgo B',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team B played during the season 2 years prior (had the results of all of their close games been flipped)
    'PastSoSAvgOppFlipCloseWinPctNow3SeasonsAgo B',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team B played during the season 3 years prior (had the results of all of their close games been flipped)

    'CurrentSoSWeightedAvgOppWinCloseWinPctThenThisSeason B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the current season (had they won all of their close games)
    'PastSoSWeightedAvgOppWinCloseWinPctThenLastSeason B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the previous season (had they won all of their close games)
    'PastSoSWeightedAvgOppWinCloseWinPctThen2SeasonsAgo B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the season 2 years prior (had they won all of their close games)
    'PastSoSWeightedAvgOppWinCloseWinPctThen3SeasonsAgo B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the season 3 years prior (had they won all of their close games)
    'CurrentSoSAvgOppWinCloseWinPctNowThisSeason B',  # average up-to-date win percentage (counting only the current season) of the teams which Team B has played during the current season (had they won all of their close games)
    'CurrentSoSAvgOppWinCloseWinPctNowLastSeason B',  # average end-of-season win percentage (counting only the previous season) of the teams which Team B has played during the current season (had they won all of their close games)
    'CurrentSoSAvgOppWinCloseWinPctNow2SeasonsAgo B',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team B has played during the current season (had they won all of their close games)
    'CurrentSoSAvgOppWinCloseWinPctNow3SeasonsAgo B',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team B has played during the current season (had they won all of their close games)
    'PastSoSAvgOppWinCloseWinPctNowLastSeason B',  # average end-of-season win percentage (counting only the previous season) of the teams which Team B played during the previous season (had they won all of their close games)
    'PastSoSAvgOppWinCloseWinPctNow2SeasonsAgo B',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team B played during the season 2 years prior (had they won all of their close games)
    'PastSoSAvgOppWinCloseWinPctNow3SeasonsAgo B',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team B played during the season 3 years prior (had they won all of their close games)

    'CurrentSoSWeightedAvgOppLoseCloseWinPctThenThisSeason B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the current season (had they lost all of their close games)
    'PastSoSWeightedAvgOppLoseCloseWinPctThenLastSeason B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the previous season (had they lost all of their close games)
    'PastSoSWeightedAvgOppLoseCloseWinPctThen2SeasonsAgo B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the season 2 years prior (had they lost all of their close games)
    'PastSoSWeightedAvgOppLoseCloseWinPctThen3SeasonsAgo B',  # average win percentage of Team B's opponents at the time when they played Team B, weighted by number of games played by opponent going into the game against Team B, during the season 3 years prior (had they lost all of their close games)
    'CurrentSoSAvgOppLoseCloseWinPctNowThisSeason B',  # average up-to-date win percentage (counting only the current season) of the teams which Team B has played during the current season (had they lost all of their close games)
    'CurrentSoSAvgOppLoseCloseWinPctNowLastSeason B',  # average end-of-season win percentage (counting only the previous season) of the teams which Team B has played during the current season (had they lost all of their close games)
    'CurrentSoSAvgOppLoseCloseWinPctNow2SeasonsAgo B',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team B has played during the current season (had they lost all of their close games)
    'CurrentSoSAvgOppLoseCloseWinPctNow3SeasonsAgo B',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team B has played during the current season (had they lost all of their close games)
    'PastSoSAvgOppLoseCloseWinPctNowLastSeason B',  # average end-of-season win percentage (counting only the previous season) of the teams which Team B played during the previous season (had they lost all of their close games)
    'PastSoSAvgOppLoseCloseWinPctNow2SeasonsAgo B',  # average end-of-season win percentage (counting only the season 2 years prior) of the teams which Team B played during the season 2 years prior (had they lost all of their close games)
    'PastSoSAvgOppLoseCloseWinPctNow3SeasonsAgo B',  # average end-of-season win percentage (counting only the season 3 years prior) of the teams which Team B played during the season 3 years prior (had they lost all of their close games)

    'CurrentSoSWeightedAvgOppPointsPerGameThenThisSeason B',  # average of Team B's current-season opponents' average points scored per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average points scored per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average points scored per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average points scored per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppPointsPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average points scored per game during the current season
    'CurrentSoSAvgOppPointsPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average points scored per game during the previous season
    'CurrentSoSAvgOppPointsPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average points scored per game during the season 2 years prior
    'CurrentSoSAvgOppPointsPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average points scored per game during the season 3 years prior
    'PastSoSAvgOppPointsPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average points scored per game during the previous season
    'PastSoSAvgOppPointsPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average points scored per game during the season 2 years prior
    'PastSoSAvgOppPointsPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average points scored per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppPointsAllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average points allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsAllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average points allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsAllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average points allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsAllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average points allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppPointsAllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average points allowed per game during the current season
    'CurrentSoSAvgOppPointsAllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average points allowed per game during the previous season
    'CurrentSoSAvgOppPointsAllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average points allowed per game during the season 2 years prior
    'CurrentSoSAvgOppPointsAllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average points allowed per game during the season 3 years prior
    'PastSoSAvgOppPointsAllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average points allowed per game during the previous season
    'PastSoSAvgOppPointsAllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average points allowed per game during the season 2 years prior
    'PastSoSAvgOppPointsAllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average points allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppPointsMarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between points scored and points allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsMarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between points scored and points allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsMarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between points scored and points allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPointsMarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between points scored and points allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppPointsMarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between points scored and points allowed per game during the current season
    'CurrentSoSAvgOppPointsMarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between points scored and points allowed per game during the previous season
    'CurrentSoSAvgOppPointsMarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between points scored and points allowed per game during the season 2 years prior
    'CurrentSoSAvgOppPointsMarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between points scored and points allowed per game during the season 3 years prior
    'PastSoSAvgOppPointsMarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between points scored and points allowed per game during the previous season
    'PastSoSAvgOppPointsMarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between points scored and points allowed per game during the season 2 years prior
    'PastSoSAvgOppPointsMarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between points scored and points allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGMPerGameThenThisSeason B',  # average of Team B's current-season opponents' average number of field goals made per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average number of field goals made per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average number of field goals made per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average number of field goals made per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGMPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average number of field goals made per game during the current season
    'CurrentSoSAvgOppFGMPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average number of field goals made per game during the previous season
    'CurrentSoSAvgOppFGMPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average number of field goals made per game during the season 2 years prior
    'CurrentSoSAvgOppFGMPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average number of field goals made per game during the season 3 years prior
    'PastSoSAvgOppFGMPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average number of field goals made per game during the previous season
    'PastSoSAvgOppFGMPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average number of field goals made per game during the season 2 years prior
    'PastSoSAvgOppFGMPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average number of field goals made per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGMAllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average number of field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMAllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average number of field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMAllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average number of field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMAllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average number of field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGMAllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average number of field goals allowed per game during the current season
    'CurrentSoSAvgOppFGMAllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average number of field goals allowed per game during the previous season
    'CurrentSoSAvgOppFGMAllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average number of field goals allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGMAllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average number of field goals allowed per game during the season 3 years prior
    'PastSoSAvgOppFGMAllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average number of field goals allowed per game during the previous season
    'PastSoSAvgOppFGMAllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average number of field goals allowed per game during the season 2 years prior
    'PastSoSAvgOppFGMAllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average number of field goals allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGMMarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between number of field goals made and number of field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMMarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between number of field goals made and number of field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMMarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between number of field goals made and number of field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGMMarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between number of field goals made and number of field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGMMarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between number of field goals made and number of field goals allowed per game during the current season
    'CurrentSoSAvgOppFGMMarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between number of field goals made and number of field goals allowed per game during the previous season
    'CurrentSoSAvgOppFGMMarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between number of field goals made and number of field goals allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGMMarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between number of field goals made and number of field goals allowed per game during the season 3 years prior
    'PastSoSAvgOppFGMMarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between number of field goals made and number of field goals allowed per game during the previous season
    'PastSoSAvgOppFGMMarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between number of field goals made and number of field goals allowed per game during the season 2 years prior
    'PastSoSAvgOppFGMMarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between number of field goals made and number of field goals allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGAPerGameThenThisSeason B',  # average of Team B's current-season opponents' average number of field goal attempts per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average number of field goal attempts per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average number of field goal attempts per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average number of field goal attempts per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGAPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average number of field goal attempts per game during the current season
    'CurrentSoSAvgOppFGAPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average number of field goal attempts per game during the previous season
    'CurrentSoSAvgOppFGAPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average number of field goal attempts per game during the season 2 years prior
    'CurrentSoSAvgOppFGAPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average number of field goal attempts per game during the season 3 years prior
    'PastSoSAvgOppFGAPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average number of field goal attempts per game during the previous season
    'PastSoSAvgOppFGAPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average number of field goal attempts per game during the season 2 years prior
    'PastSoSAvgOppFGAPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average number of field goal attempts per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGAAllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average number of field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAAllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average number of field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAAllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average number of field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAAllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average number of field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGAAllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average number of field goal attempts allowed per game during the current season
    'CurrentSoSAvgOppFGAAllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average number of field goal attempts allowed per game during the previous season
    'CurrentSoSAvgOppFGAAllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average number of field goal attempts allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGAAllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average number of field goal attempts allowed per game during the season 3 years prior
    'PastSoSAvgOppFGAAllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average number of field goal attempts allowed per game during the previous season
    'PastSoSAvgOppFGAAllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average number of field goal attempts allowed per game during the season 2 years prior
    'PastSoSAvgOppFGAAllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average number of field goal attempts allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGAMarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between number of field goal attempts and number of field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAMarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between number of field goal attempts and number of field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAMarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between number of field goal attempts and number of field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGAMarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between number of field goal attempts and number of field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGAMarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between number of field goal attempts and number of field goal attempts allowed per game during the current season
    'CurrentSoSAvgOppFGAMarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between number of field goal attempts and number of field goal attempts allowed per game during the previous season
    'CurrentSoSAvgOppFGAMarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between number of field goal attempts and number of field goal attempts allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGAMarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between number of field goal attempts and number of field goal attempts allowed per game during the season 3 years prior
    'PastSoSAvgOppFGAMarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between number of field goal attempts and number of field goal attempts allowed per game during the previous season
    'PastSoSAvgOppFGAMarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between number of field goal attempts and number of field goal attempts allowed per game during the season 2 years prior
    'PastSoSAvgOppFGAMarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between number of field goal attempts and number of field goal attempts allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGPctThenThisSeason B',  # average of Team B's current-season opponents' season-long field goal percentage, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctThenLastSeason B',  # average of Team B's previous-season opponents' season-long field goal percentage, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season-long field goal percentage, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season-long field goal percentage, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGPctNowThisSeason B',  # average of Team B's current-season opponents' up-to-date season-long field goal percentage during the current season
    'CurrentSoSAvgOppFGPctNowLastSeason B',  # average of Team B's current-season opponents' season-long field goal percentage during the previous season
    'CurrentSoSAvgOppFGPctNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long field goal percentage during the season 2 years prior
    'CurrentSoSAvgOppFGPctNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long field goal percentage during the season 3 years prior
    'PastSoSAvgOppFGPctNowLastSeason B',  # average of Team B's previous-season opponents' season-long field goal percentage during the previous season
    'PastSoSAvgOppFGPctNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season-long field goal percentage during the season 2 years prior
    'PastSoSAvgOppFGPctNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season-long field goal percentage during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGPctAllowedThenThisSeason B',  # average of Team B's current-season opponents' season-long field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctAllowedThenLastSeason B',  # average of Team B's previous-season opponents' season-long field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctAllowedThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season-long field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctAllowedThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season-long field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGPctAllowedNowThisSeason B',  # average of Team B's current-season opponents' up-to-date season-long field goal percentage allowed during the current season
    'CurrentSoSAvgOppFGPctAllowedNowLastSeason B',  # average of Team B's current-season opponents' season-long field goal percentage allowed during the previous season
    'CurrentSoSAvgOppFGPctAllowedNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long field goal percentage allowed during the season 2 years prior
    'CurrentSoSAvgOppFGPctAllowedNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long field goal percentage allowed during the season 3 years prior
    'PastSoSAvgOppFGPctAllowedNowLastSeason B',  # average of Team B's previous-season opponents' season-long field goal percentage allowed during the previous season
    'PastSoSAvgOppFGPctAllowedNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season-long field goal percentage allowed during the season 2 years prior
    'PastSoSAvgOppFGPctAllowedNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season-long field goal percentage allowed during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGPctMarginThenThisSeason B',  # average of Team B's current-season opponents' differences between season-long field goal percentage and season-long field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctMarginThenLastSeason B',  # average of Team B's previous-season opponents' differences between previous-season-long field goal percentage and previous-season-long field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctMarginThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' differences between 2-seasons-prior season-long field goal percentage and 2-seasons-prior season-long field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGPctMarginThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' differences between 3 seasons-prior season-long field goal percentage and 3-seasons-prior season-long field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGPctMarginNowThisSeason B',  # average of Team B's current-season opponents' up-to-date differences between season-long field goal percentage and season-long field goal percentage allowed during the current season
    'CurrentSoSAvgOppFGPctMarginNowLastSeason B',  # average of Team B's current-season opponents' up-to-date differences between season-long field goal percentage and season-long field goal percentage allowed during the previous season
    'CurrentSoSAvgOppFGPctMarginNow2SeasonsAgo B',  # average of Team B's current-season opponents' up-to-date differences between season-long field goal percentage and season-long field goal percentage allowed during the season 2 years prior
    'CurrentSoSAvgOppFGPctMarginNow3SeasonsAgo B',  # average of Team B's current-season opponents' up-to-date differences between season-long field goal percentage and season-long field goal percentage allowed during the season 3 years prior
    'PastSoSAvgOppFGPctMarginNowLastSeason B',  # average of Team B's previous-season opponents' differences between season-long field goal percentage and season-long field goal percentage allowed during the previous season
    'PastSoSAvgOppFGPctMarginNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' differences between season-long field goal percentage and season-long field goal percentage allowed during the previous season
    'PastSoSAvgOppFGPctMarginNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' differences between season-long field goal percentage and season-long field goal percentage allowed during the previous season 3 years prior

    'CurrentSoSWeightedAvgOppFGM3PerGameThenThisSeason B',  # average of Team B's current-season opponents' average number of 3-point field goals made per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3PerGameThenLastSeason B',  # average of Team B's previous-season opponents' average number of 3-point field goals made per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3PerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average number of 3-point field goals made per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3PerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average number of 3-point field goals made per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGM3PerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average number of 3-point field goals made per game during the current season
    'CurrentSoSAvgOppFGM3PerGameNowLastSeason B',  # average of Team B's current-season opponents' season average number of 3-point field goals made per game during the previous season
    'CurrentSoSAvgOppFGM3PerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average number of 3-point field goals made per game during the season 2 years prior
    'CurrentSoSAvgOppFGM3PerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average number of 3-point field goals made per game during the season 3 years prior
    'PastSoSAvgOppFGM3PerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average number of 3-point field goals made per game during the previous season
    'PastSoSAvgOppFGM3PerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average number of 3-point field goals made per game during the season 2 years prior
    'PastSoSAvgOppFGM3PerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average number of 3-point field goals made per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGM3AllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average number of 3-point field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3AllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average number of 3-point field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3AllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average number of 3-point field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3AllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average number of 3-point field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGM3AllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average number of 3-point field goals allowed per game during the current season
    'CurrentSoSAvgOppFGM3AllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average number of 3-point field goals allowed per game during the previous season
    'CurrentSoSAvgOppFGM3AllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average number of 3-point field goals allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGM3AllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average number of 3-point field goals allowed per game during the season 3 years prior
    'PastSoSAvgOppFGM3AllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average number of 3-point field goals allowed per game during the previous season
    'PastSoSAvgOppFGM3AllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average number of 3-point field goals allowed per game during the season 2 years prior
    'PastSoSAvgOppFGM3AllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average number of 3-point field goals allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGM3MarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between number of 3-point field goals made and number of 3-point field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3MarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between number of 3-point field goals made and number of 3-point field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3MarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between number of 3-point field goals made and number of 3-point field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGM3MarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between number of 3-point field goals made and number of 3-point field goals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGM3MarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the current season
    'CurrentSoSAvgOppFGM3MarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the previous season
    'CurrentSoSAvgOppFGM3MarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGM3MarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the season 3 years prior
    'PastSoSAvgOppFGM3MarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the previous season
    'PastSoSAvgOppFGM3MarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the season 2 years prior
    'PastSoSAvgOppFGM3MarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between number of 3-point field goals made and number of 3-point field goals allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGA3PerGameThenThisSeason B',  # average of Team B's current-season opponents' average number of 3-point field goal attempts per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3PerGameThenLastSeason B',  # average of Team B's previous-season opponents' average number of 3-point field goal attempts per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3PerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average number of 3-point field goal attempts per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3PerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average number of 3-point field goal attempts per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGA3PerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average number of 3-point field goal attempts per game during the current season
    'CurrentSoSAvgOppFGA3PerGameNowLastSeason B',  # average of Team B's current-season opponents' season average number of 3-point field goal attempts per game during the previous season
    'CurrentSoSAvgOppFGA3PerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average number of 3-point field goal attempts per game during the season 2 years prior
    'CurrentSoSAvgOppFGA3PerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average number of 3-point field goal attempts per game during the season 3 years prior
    'PastSoSAvgOppFGA3PerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average number of 3-point field goal attempts per game during the previous season
    'PastSoSAvgOppFGA3PerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average number of 3-point field goal attempts per game during the season 2 years prior
    'PastSoSAvgOppFGA3PerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average number of 3-point field goal attempts per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGA3AllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3AllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3AllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3AllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGA3AllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average number of 3-point field goal attempts allowed per game during the current season
    'CurrentSoSAvgOppFGA3AllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average number of 3-point field goal attempts allowed per game during the previous season
    'CurrentSoSAvgOppFGA3AllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average number of 3-point field goal attempts allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGA3AllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average number of 3-point field goal attempts allowed per game during the season 3 years prior
    'PastSoSAvgOppFGA3AllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average number of 3-point field goal attempts allowed per game during the previous season
    'PastSoSAvgOppFGA3AllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average number of 3-point field goal attempts allowed per game during the season 2 years prior
    'PastSoSAvgOppFGA3AllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average number of 3-point field goal attempts allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFGA3MarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3MarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3MarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFGA3MarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFGA3MarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the current season
    'CurrentSoSAvgOppFGA3MarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the previous season
    'CurrentSoSAvgOppFGA3MarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFGA3MarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the season 3 years prior
    'PastSoSAvgOppFGA3MarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the previous season
    'PastSoSAvgOppFGA3MarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the season 2 years prior
    'PastSoSAvgOppFGA3MarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between number of 3-point field goal attempts and number of 3-point field goal attempts allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFG3PctThenThisSeason B',  # average of Team B's current-season opponents' season-long 3-point field goal percentage, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctThenLastSeason B',  # average of Team B's previous-season opponents' season-long 3-point field goal percentage, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season-long 3-point field goal percentage, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season-long 3-point field goal percentage, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFG3PctNowThisSeason B',  # average of Team B's current-season opponents' up-to-date season-long 3-point field goal percentage during the current season
    'CurrentSoSAvgOppFG3PctNowLastSeason B',  # average of Team B's current-season opponents' season-long 3-point field goal percentage during the previous season
    'CurrentSoSAvgOppFG3PctNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long 3-point field goal percentage during the season 2 years prior
    'CurrentSoSAvgOppFG3PctNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long 3-point field goal percentage during the season 3 years prior
    'PastSoSAvgOppFG3PctNowLastSeason B',  # average of Team B's previous-season opponents' season-long 3-point field goal percentage during the previous season
    'PastSoSAvgOppFG3PctNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season-long 3-point field goal percentage during the season 2 years prior
    'PastSoSAvgOppFG3PctNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season-long 3-point field goal percentage during the season 3 years prior

    'CurrentSoSWeightedAvgOppFG3PctAllowedThenThisSeason B',  # average of Team B's current-season opponents' season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctAllowedThenLastSeason B',  # average of Team B's previous-season opponents' season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctAllowedThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctAllowedThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFG3PctAllowedNowThisSeason B',  # average of Team B's current-season opponents' up-to-date season-long 3-point field goal percentage allowed during the current season
    'CurrentSoSAvgOppFG3PctAllowedNowLastSeason B',  # average of Team B's current-season opponents' season-long 3-point field goal percentage allowed during the previous season
    'CurrentSoSAvgOppFG3PctAllowedNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long 3-point field goal percentage allowed during the season 2 years prior
    'CurrentSoSAvgOppFG3PctAllowedNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long 3-point field goal percentage allowed during the season 3 years prior
    'PastSoSAvgOppFG3PctAllowedNowLastSeason B',  # average of Team B's previous-season opponents' season-long 3-point field goal percentage allowed during the previous season
    'PastSoSAvgOppFG3PctAllowedNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season-long 3-point field goal percentage allowed during the season 2 years prior
    'PastSoSAvgOppFG3PctAllowedNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season-long 3-point field goal percentage allowed during the season 3 years prior

    'CurrentSoSWeightedAvgOppFG3PctMarginThenThisSeason B',  # average of Team B's current-season opponents' differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctMarginThenLastSeason B',  # average of Team B's previous-season opponents' differences between previous-season-long 3-point field goal percentage and previous-season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctMarginThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' differences between 2-seasons-prior season-long 3-point field goal percentage and 2-seasons-prior season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFG3PctMarginThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' differences between 3 seasons-prior season-long 3-point field goal percentage and 3-seasons-prior season-long 3-point field goal percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFG3PctMarginNowThisSeason B',  # average of Team B's current-season opponents' up-to-date differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the current season
    'CurrentSoSAvgOppFG3PctMarginNowLastSeason B',  # average of Team B's current-season opponents' up-to-date differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the previous season
    'CurrentSoSAvgOppFG3PctMarginNow2SeasonsAgo B',  # average of Team B's current-season opponents' up-to-date differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the season 2 years prior
    'CurrentSoSAvgOppFG3PctMarginNow3SeasonsAgo B',  # average of Team B's current-season opponents' up-to-date differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the season 3 years prior
    'PastSoSAvgOppFG3PctMarginNowLastSeason B',  # average of Team B's previous-season opponents' differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the previous season
    'PastSoSAvgOppFG3PctMarginNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the previous season
    'PastSoSAvgOppFG3PctMarginNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' differences between season-long 3-point field goal percentage and season-long 3-point field goal percentage allowed during the previous season 3 years prior

    'CurrentSoSWeightedAvgOppFTMPerGameThenThisSeason B',  # average of Team B's current-season opponents' average number of free-throws made per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average number of free-throws made per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average number of free-throws made per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average number of free-throws made per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTMPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average number of free-throws made per game during the current season
    'CurrentSoSAvgOppFTMPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average number of free-throws made per game during the previous season
    'CurrentSoSAvgOppFTMPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average number of free-throws made per game during the season 2 years prior
    'CurrentSoSAvgOppFTMPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average number of free-throws made per game during the season 3 years prior
    'PastSoSAvgOppFTMPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average number of free-throws made per game during the previous season
    'PastSoSAvgOppFTMPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average number of free-throws made per game during the season 2 years prior
    'PastSoSAvgOppFTMPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average number of free-throws made per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTMAllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average number of successful free-throws allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMAllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average number of successful free-throws allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMAllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average number of successful free-throws allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMAllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average number of successful free-throws allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTMAllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average number of successful free-throws allowed per game during the current season
    'CurrentSoSAvgOppFTMAllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average number of successful free-throws allowed per game during the previous season
    'CurrentSoSAvgOppFTMAllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average number of successful free-throws allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFTMAllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average number of successful free-throws allowed per game during the season 3 years prior
    'PastSoSAvgOppFTMAllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average number of successful free-throws allowed per game during the previous season
    'PastSoSAvgOppFTMAllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average number of successful free-throws allowed per game during the season 2 years prior
    'PastSoSAvgOppFTMAllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average number of successful free-throws allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTMMarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between number of free-throws made and number of successful free-throws allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMMarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between number of free-throws made and number of successful free-throws allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMMarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between number of free-throws made and number of successful free-throws allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTMMarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between number of free-throws made and number of successful free-throws allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTMMarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between number of free-throws made and number of successful free-throws allowed per game during the current season
    'CurrentSoSAvgOppFTMMarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between number of free-throws made and number of successful free-throws allowed per game during the previous season
    'CurrentSoSAvgOppFTMMarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between number of free-throws made and number of successful free-throws allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFTMMarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between number of free-throws made and number of successful free-throws allowed per game during the season 3 years prior
    'PastSoSAvgOppFTMMarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between number of free-throws made and number of successful free-throws allowed per game during the previous season
    'PastSoSAvgOppFTMMarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between number of free-throws made and number of successful free-throws allowed per game during the season 2 years prior
    'PastSoSAvgOppFTMMarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between number of free-throws made and number of successful free-throws allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTAPerGameThenThisSeason B',  # average of Team B's current-season opponents' average number of free-throw attempts per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average number of free-throw attempts per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average number of free-throw attempts per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average number of free-throw attempts per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTAPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average number of free-throw attempts per game during the current season
    'CurrentSoSAvgOppFTAPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average number of free-throw attempts per game during the previous season
    'CurrentSoSAvgOppFTAPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average number of free-throw attempts per game during the season 2 years prior
    'CurrentSoSAvgOppFTAPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average number of free-throw attempts per game during the season 3 years prior
    'PastSoSAvgOppFTAPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average number of free-throw attempts per game during the previous season
    'PastSoSAvgOppFTAPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average number of free-throw attempts per game during the season 2 years prior
    'PastSoSAvgOppFTAPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average number of free-throw attempts per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTAAllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average number of free-throw attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAAllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average number of free-throw attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAAllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average number of free-throw attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAAllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average number of free-throw attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTAAllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average number of free-throw attempts allowed per game during the current season
    'CurrentSoSAvgOppFTAAllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average number of free-throw attempts allowed per game during the previous season
    'CurrentSoSAvgOppFTAAllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average number of free-throw attempts allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFTAAllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average number of free-throw attempts allowed per game during the season 3 years prior
    'PastSoSAvgOppFTAAllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average number of free-throw attempts allowed per game during the previous season
    'PastSoSAvgOppFTAAllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average number of free-throw attempts allowed per game during the season 2 years prior
    'PastSoSAvgOppFTAAllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average number of free-throw attempts allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTAMarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between number of free-throw attempts and number of free-throw attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAMarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between number of free-throw attempts and number of free-throw attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAMarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between number of free-throw attempts and number of free-throw attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTAMarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between number of free-throw attempts and number of free-throw attempts allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTAMarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the current season
    'CurrentSoSAvgOppFTAMarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the previous season
    'CurrentSoSAvgOppFTAMarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the season 2 years prior
    'CurrentSoSAvgOppFTAMarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the season 3 years prior
    'PastSoSAvgOppFTAMarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the previous season
    'PastSoSAvgOppFTAMarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the season 2 years prior
    'PastSoSAvgOppFTAMarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between number of free-throw attempts and number of free-throw attempts allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTPctThenThisSeason B',  # average of Team B's current-season opponents' season-long free-throw percentage, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctThenLastSeason B',  # average of Team B's previous-season opponents' season-long free-throw percentage, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season-long free-throw percentage, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season-long free-throw percentage, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTPctNowThisSeason B',  # average of Team B's current-season opponents' up-to-date season-long free-throw percentage during the current season
    'CurrentSoSAvgOppFTPctNowLastSeason B',  # average of Team B's current-season opponents' season-long free-throw percentage during the previous season
    'CurrentSoSAvgOppFTPctNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long free-throw percentage during the season 2 years prior
    'CurrentSoSAvgOppFTPctNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long free-throw percentage during the season 3 years prior
    'PastSoSAvgOppFTPctNowLastSeason B',  # average of Team B's previous-season opponents' season-long free-throw percentage during the previous season
    'PastSoSAvgOppFTPctNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season-long free-throw percentage during the season 2 years prior
    'PastSoSAvgOppFTPctNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season-long free-throw percentage during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTPctAllowedThenThisSeason B',  # average of Team B's current-season opponents' season-long free-throw percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctAllowedThenLastSeason B',  # average of Team B's previous-season opponents' season-long free-throw percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctAllowedThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season-long free-throw percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctAllowedThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season-long free-throw percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTPctAllowedNowThisSeason B',  # average of Team B's current-season opponents' up-to-date season-long free-throw percentage allowed during the current season
    'CurrentSoSAvgOppFTPctAllowedNowLastSeason B',  # average of Team B's current-season opponents' season-long free-throw percentage allowed during the previous season
    'CurrentSoSAvgOppFTPctAllowedNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long free-throw percentage allowed during the season 2 years prior
    'CurrentSoSAvgOppFTPctAllowedNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long free-throw percentage allowed during the season 3 years prior
    'PastSoSAvgOppFTPctAllowedNowLastSeason B',  # average of Team B's previous-season opponents' season-long free-throw percentage allowed during the previous season
    'PastSoSAvgOppFTPctAllowedNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season-long free-throw percentage allowed during the season 2 years prior
    'PastSoSAvgOppFTPctAllowedNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season-long free-throw percentage allowed during the season 3 years prior

    'CurrentSoSWeightedAvgOppFTPctMarginThenThisSeason B',  # average of Team B's current-season opponents' differences between season-long free-throw percentage and season-long free-throw percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctMarginThenLastSeason B',  # average of Team B's previous-season opponents' differences between previous-season-long free-throw percentage and previous-season-long free-throw percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctMarginThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' differences between 2-seasons-prior season-long free-throw percentage and 2-seasons-prior season-long free-throw percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppFTPctMarginThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' differences between 3 seasons-prior season-long free-throw percentage and 3-seasons-prior season-long free-throw percentage allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppFTPctMarginNowThisSeason B',  # average of Team B's current-season opponents' up-to-date differences between season-long free-throw percentage and season-long free-throw percentage allowed during the current season
    'CurrentSoSAvgOppFTPctMarginNowLastSeason B',  # average of Team B's current-season opponents' up-to-date differences between season-long free-throw percentage and season-long free-throw percentage allowed during the previous season
    'CurrentSoSAvgOppFTPctMarginNow2SeasonsAgo B',  # average of Team B's current-season opponents' up-to-date differences between season-long free-throw percentage and season-long free-throw percentage allowed during the season 2 years prior
    'CurrentSoSAvgOppFTPctMarginNow3SeasonsAgo B',  # average of Team B's current-season opponents' up-to-date differences between season-long free-throw percentage and season-long free-throw percentage allowed during the season 3 years prior
    'PastSoSAvgOppFTPctMarginNowLastSeason B',  # average of Team B's previous-season opponents' differences between season-long free-throw percentage and season-long free-throw percentage allowed during the previous season
    'PastSoSAvgOppFTPctMarginNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' differences between season-long free-throw percentage and season-long free-throw percentage allowed during the previous season
    'PastSoSAvgOppFTPctMarginNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' differences between season-long free-throw percentage and season-long free-throw percentage allowed during the previous season 3 years prior

    'CurrentSoSWeightedAvgOppRebPerGameThenThisSeason B',  # average of Team B's current-season opponents' average rebounds per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average rebounds per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average rebounds per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average rebounds per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppRebPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average rebounds per game during the current season
    'CurrentSoSAvgOppRebPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average rebounds per game during the previous season
    'CurrentSoSAvgOppRebPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average rebounds per game during the season 2 years prior
    'CurrentSoSAvgOppRebPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average rebounds per game during the season 3 years prior
    'PastSoSAvgOppRebPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average rebounds per game during the previous season
    'PastSoSAvgOppRebPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average rebounds per game during the season 2 years prior
    'PastSoSAvgOppRebPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average rebounds per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppRebAllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebAllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebAllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebAllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppRebAllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average rebounds allowed per game during the current season
    'CurrentSoSAvgOppRebAllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average rebounds allowed per game during the previous season
    'CurrentSoSAvgOppRebAllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average rebounds allowed per game during the season 2 years prior
    'CurrentSoSAvgOppRebAllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average rebounds allowed per game during the season 3 years prior
    'PastSoSAvgOppRebAllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average rebounds allowed per game during the previous season
    'PastSoSAvgOppRebAllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average rebounds allowed per game during the season 2 years prior
    'PastSoSAvgOppRebAllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average rebounds allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppRebMarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between rebounds and rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebMarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between rebounds and rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebMarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between rebounds and rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppRebMarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between rebounds and rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppRebMarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between rebounds and rebounds allowed per game during the current season
    'CurrentSoSAvgOppRebMarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between rebounds and rebounds allowed per game during the previous season
    'CurrentSoSAvgOppRebMarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between rebounds and rebounds allowed per game during the season 2 years prior
    'CurrentSoSAvgOppRebMarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between rebounds and rebounds allowed per game during the season 3 years prior
    'PastSoSAvgOppRebMarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between rebounds and rebounds allowed per game during the previous season
    'PastSoSAvgOppRebMarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between rebounds and rebounds allowed per game during the season 2 years prior
    'PastSoSAvgOppRebMarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between rebounds and rebounds allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppORebPerGameThenThisSeason B',  # average of Team B's current-season opponents' average offensive rebounds per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average offensive rebounds per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average offensive rebounds per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average offensive rebounds per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppORebPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average offensive rebounds per game during the current season
    'CurrentSoSAvgOppORebPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average offensive rebounds per game during the previous season
    'CurrentSoSAvgOppORebPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average offensive rebounds per game during the season 2 years prior
    'CurrentSoSAvgOppORebPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average offensive rebounds per game during the season 3 years prior
    'PastSoSAvgOppORebPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average offensive rebounds per game during the previous season
    'PastSoSAvgOppORebPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average offensive rebounds per game during the season 2 years prior
    'PastSoSAvgOppORebPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average offensive rebounds per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppORebAllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average offensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebAllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average offensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebAllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average offensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebAllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average offensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppORebAllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average offensive rebounds allowed per game during the current season
    'CurrentSoSAvgOppORebAllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average offensive rebounds allowed per game during the previous season
    'CurrentSoSAvgOppORebAllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average offensive rebounds allowed per game during the season 2 years prior
    'CurrentSoSAvgOppORebAllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average offensive rebounds allowed per game during the season 3 years prior
    'PastSoSAvgOppORebAllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average offensive rebounds allowed per game during the previous season
    'PastSoSAvgOppORebAllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average offensive rebounds allowed per game during the season 2 years prior
    'PastSoSAvgOppORebAllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average offensive rebounds allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppORebMarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between offensive rebounds and offensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebMarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between offensive rebounds and offensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebMarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between offensive rebounds and offensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppORebMarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between offensive rebounds and offensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppORebMarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between offensive rebounds and offensive rebounds allowed per game during the current season
    'CurrentSoSAvgOppORebMarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between offensive rebounds and offensive rebounds allowed per game during the previous season
    'CurrentSoSAvgOppORebMarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between offensive rebounds and offensive rebounds allowed per game during the season 2 years prior
    'CurrentSoSAvgOppORebMarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between offensive rebounds and offensive rebounds allowed per game during the season 3 years prior
    'PastSoSAvgOppORebMarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between offensive rebounds and offensive rebounds allowed per game during the previous season
    'PastSoSAvgOppORebMarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between offensive rebounds and offensive rebounds allowed per game during the season 2 years prior
    'PastSoSAvgOppORebMarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between offensive rebounds and offensive rebounds allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppDRebPerGameThenThisSeason B',  # average of Team B's current-season opponents' average defensive rebounds per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average defensive rebounds per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average defensive rebounds per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average defensive rebounds per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppDRebPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average defensive rebounds per game during the current season
    'CurrentSoSAvgOppDRebPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average defensive rebounds per game during the previous season
    'CurrentSoSAvgOppDRebPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average defensive rebounds per game during the season 2 years prior
    'CurrentSoSAvgOppDRebPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average defensive rebounds per game during the season 3 years prior
    'PastSoSAvgOppDRebPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average defensive rebounds per game during the previous season
    'PastSoSAvgOppDRebPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average defensive rebounds per game during the season 2 years prior
    'PastSoSAvgOppDRebPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average defensive rebounds per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppDRebAllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average defensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebAllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average defensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebAllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average defensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebAllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average defensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppDRebAllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average defensive rebounds allowed per game during the current season
    'CurrentSoSAvgOppDRebAllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average defensive rebounds allowed per game during the previous season
    'CurrentSoSAvgOppDRebAllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average defensive rebounds allowed per game during the season 2 years prior
    'CurrentSoSAvgOppDRebAllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average defensive rebounds allowed per game during the season 3 years prior
    'PastSoSAvgOppDRebAllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average defensive rebounds allowed per game during the previous season
    'PastSoSAvgOppDRebAllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average defensive rebounds allowed per game during the season 2 years prior
    'PastSoSAvgOppDRebAllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average defensive rebounds allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppDRebMarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between defensive rebounds and defensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebMarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between defensive rebounds and defensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebMarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between defensive rebounds and defensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppDRebMarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between defensive rebounds and defensive rebounds allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppDRebMarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between defensive rebounds and defensive rebounds allowed per game during the current season
    'CurrentSoSAvgOppDRebMarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between defensive rebounds and defensive rebounds allowed per game during the previous season
    'CurrentSoSAvgOppDRebMarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between defensive rebounds and defensive rebounds allowed per game during the season 2 years prior
    'CurrentSoSAvgOppDRebMarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between defensive rebounds and defensive rebounds allowed per game during the season 3 years prior
    'PastSoSAvgOppDRebMarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between defensive rebounds and defensive rebounds allowed per game during the previous season
    'PastSoSAvgOppDRebMarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between defensive rebounds and defensive rebounds allowed per game during the season 2 years prior
    'PastSoSAvgOppDRebMarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between defensive rebounds and defensive rebounds allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppAstPerGameThenThisSeason B',  # average of Team B's current-season opponents' average assists per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average assists per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average assists per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average assists per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppAstPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average assists per game during the current season
    'CurrentSoSAvgOppAstPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average assists per game during the previous season
    'CurrentSoSAvgOppAstPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average assists per game during the season 2 years prior
    'CurrentSoSAvgOppAstPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average assists per game during the season 3 years prior
    'PastSoSAvgOppAstPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average assists per game during the previous season
    'PastSoSAvgOppAstPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average assists per game during the season 2 years prior
    'PastSoSAvgOppAstPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average assists per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppAstAllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average assists allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstAllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average assists allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstAllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average assists allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstAllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average assists allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppAstAllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average assists allowed per game during the current season
    'CurrentSoSAvgOppAstAllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average assists allowed per game during the previous season
    'CurrentSoSAvgOppAstAllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average assists allowed per game during the season 2 years prior
    'CurrentSoSAvgOppAstAllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average assists allowed per game during the season 3 years prior
    'PastSoSAvgOppAstAllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average assists allowed per game during the previous season
    'PastSoSAvgOppAstAllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average assists allowed per game during the season 2 years prior
    'PastSoSAvgOppAstAllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average assists allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppAstMarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between assists and assists allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstMarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between assists and assists allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstMarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between assists and assists allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAstMarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between assists and assists allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppAstMarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between assists and assists allowed per game during the current season
    'CurrentSoSAvgOppAstMarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between assists and assists allowed per game during the previous season
    'CurrentSoSAvgOppAstMarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between assists and assists allowed per game during the season 2 years prior
    'CurrentSoSAvgOppAstMarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between assists and assists allowed per game during the season 3 years prior
    'PastSoSAvgOppAstMarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between assists and assists allowed per game during the previous season
    'PastSoSAvgOppAstMarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between assists and assists allowed per game during the season 2 years prior
    'PastSoSAvgOppAstMarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between assists and assists allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppTOPerGameThenThisSeason B',  # average of Team B's current-season opponents' average turnovers per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average turnovers per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average turnovers per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average turnovers per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppTOPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average turnovers per game during the current season
    'CurrentSoSAvgOppTOPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average turnovers per game during the previous season
    'CurrentSoSAvgOppTOPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average turnovers per game during the season 2 years prior
    'CurrentSoSAvgOppTOPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average turnovers per game during the season 3 years prior
    'PastSoSAvgOppTOPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average turnovers per game during the previous season
    'PastSoSAvgOppTOPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average turnovers per game during the season 2 years prior
    'PastSoSAvgOppTOPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average turnovers per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppTOAllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average turnovers forced per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOAllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average turnovers forced per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOAllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average turnovers forced per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOAllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average turnovers forced per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppTOAllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average turnovers forced per game during the current season
    'CurrentSoSAvgOppTOAllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average turnovers forced per game during the previous season
    'CurrentSoSAvgOppTOAllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average turnovers forced per game during the season 2 years prior
    'CurrentSoSAvgOppTOAllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average turnovers forced per game during the season 3 years prior
    'PastSoSAvgOppTOAllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average turnovers forced per game during the previous season
    'PastSoSAvgOppTOAllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average turnovers forced per game during the season 2 years prior
    'PastSoSAvgOppTOAllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average turnovers forced per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppTOMarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between turnovers and turnovers forced per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOMarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between turnovers and turnovers forced per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOMarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between turnovers and turnovers forced per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppTOMarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between turnovers and turnovers forced per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppTOMarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between turnovers and turnovers forced per game during the current season
    'CurrentSoSAvgOppTOMarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between turnovers and turnovers forced per game during the previous season
    'CurrentSoSAvgOppTOMarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between turnovers and turnovers forced per game during the season 2 years prior
    'CurrentSoSAvgOppTOMarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between turnovers and turnovers forced per game during the season 3 years prior
    'PastSoSAvgOppTOMarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between turnovers and turnovers forced per game during the previous season
    'PastSoSAvgOppTOMarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between turnovers and turnovers forced per game during the season 2 years prior
    'PastSoSAvgOppTOMarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between turnovers and turnovers forced per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppAvgAst/TORatioThenThisSeason B',  # average of Team B's current-season opponents' current-season-long assist/turnover ratios (total assists / total turnovers), recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioThenLastSeason B',  # average of Team B's previous-season opponents' previous-season-long assist/turnover ratios (total assists / total turnovers), recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioThen2SeasonsAgo B',  # average of Team B's 2-seasons-prior opponents' 2-seasons-prior season-long assist/turnover ratios (total assists / total turnovers), recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioThen3SeasonsAgo B',  # average of Team B's 3-seasons-prior opponents' 3-seasons-prior season-long assist/turnover ratios (total assists / total turnovers), recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppAvgAst/TORatioNowThisSeason B',  # average of Team B's current-season opponents' up-to-date assist/turnover ratios (total assists / total turnovers) during the current season
    'CurrentSoSAvgOppAvgAst/TORatioNowLastSeason B',  # average of Team B's current-season opponents' season-long assist/turnover ratios (total assists / total turnovers) during the previous season
    'CurrentSoSAvgOppAvgAst/TORatioNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long assist/turnover ratios (total assists / total turnovers) during the season 2 years prior
    'CurrentSoSAvgOppAvgAst/TORatioNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long assist/turnover ratios (total assists / total turnovers) during the season 3 years prior
    'PastSoSAvgOppAvgAst/TORatioNowLastSeason B',  # average of Team B's previous-season opponents' season-long assist/turnover ratios (total assists / total turnovers) during the previous season
    'PastSoSAvgOppAvgAst/TORatioNow2SeasonsAgo B',  # average of Team B's 2-seasons-prior opponents' season-long assist/turnover ratios (total assists / total turnovers) during the season 2 years prior
    'PastSoSAvgOppAvgAst/TORatioNow3SeasonsAgo B',  # average of Team B's 3-seasons-prior opponents' season-long assist/turnover ratios (total assists / total turnovers) during the season 3 years prior

    'CurrentSoSWeightedAvgOppAvgAst/TORatioAllowedThenThisSeason B',  # average of Team B's current-season opponents' current-season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioAllowedThenLastSeason B',  # average of Team B's previous-season opponents' previous-season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioAllowedThen2SeasonsAgo B',  # average of Team B's 2-seasons-prior opponents' 2-seasons-prior season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioAllowedThen3SeasonsAgo B',  # average of Team B's 3-seasons-prior opponents' 3-seasons-prior season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppAvgAst/TORatioAllowedNowThisSeason B',  # average of Team B's current-season opponents' up-to-date assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the current season
    'CurrentSoSAvgOppAvgAst/TORatioAllowedNowLastSeason B',  # average of Team B's current-season opponents' season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the previous season
    'CurrentSoSAvgOppAvgAst/TORatioAllowedNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the season 2 years prior
    'CurrentSoSAvgOppAvgAst/TORatioAllowedNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the season 3 years prior
    'PastSoSAvgOppAvgAst/TORatioAllowedNowLastSeason B',  # average of Team B's previous-season opponents' season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the previous season
    'PastSoSAvgOppAvgAst/TORatioAllowedNow2SeasonsAgo B',  # average of Team B's 2-seasons-prior opponents' season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the season 2 years prior
    'PastSoSAvgOppAvgAst/TORatioAllowedNow3SeasonsAgo B',  # average of Team B's 3-seasons-prior opponents' season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced) during the season 3 years prior

    'CurrentSoSWeightedAvgOppAvgAst/TORatioMarginThenThisSeason B',  # average of Team B's current-season opponents' current-season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioMarginThenLastSeason B',  # average of Team B's previous-season opponents' previous-season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioMarginThen2SeasonsAgo B',  # average of Team B's 2-seasons-prior opponents' 2-seasons-prior season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppAvgAst/TORatioMarginThen3SeasonsAgo B',  # average of Team B's 3-seasons-prior opponents' 3-seasons-prior season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced), recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppAvgAst/TORatioMarginNowThisSeason B',  # average of Team B's current-season opponents' up-to-date differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the current season
    'CurrentSoSAvgOppAvgAst/TORatioMarginNowLastSeason B',  # average of Team B's current-season opponents' season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the previous season
    'CurrentSoSAvgOppAvgAst/TORatioMarginNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the season 2 years prior
    'CurrentSoSAvgOppAvgAst/TORatioMarginNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the season 3 years prior
    'PastSoSAvgOppAvgAst/TORatioMarginNowLastSeason B',  # average of Team B's previous-season opponents' season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the previous season
    'PastSoSAvgOppAvgAst/TORatioMarginNow2SeasonsAgo B',  # average of Team B's 2-seasons-prior opponents' season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the season 2 years prior
    'PastSoSAvgOppAvgAst/TORatioMarginNow3SeasonsAgo B',  # average of Team B's 3-seasons-prior opponents' season-long differences between assist/turnover ratio (total assists / total turnovers) and assist/turnover ratio allowed (total assists allowed / total turnovers forced) during the season 3 years prior

    'CurrentSoSWeightedAvgOppAvgAst/TORatio(alt)ThenThisSeason B',  # average of Team B's current-season opponents' current-season-long assist/turnover ratios, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)ThenLastSeason B',  # average of Team B's previous-season opponents' previous-season-long assist/turnover ratios, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)Then2SeasonsAgo B',  # average of Team B's 2-seasons-prior opponents' 2-seasons-prior season-long assist/turnover ratios, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)Then3SeasonsAgo B',  # average of Team B's 3-seasons-prior opponents' 3-seasons-prior season-long assist/turnover ratios, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)NowThisSeason B',  # average of Team B's current-season opponents' up-to-date assist/turnover ratios during the current season (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)NowLastSeason B',  # average of Team B's current-season opponents' season-long assist/turnover ratios during the previous season (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)Now2SeasonsAgo B',  # average of Team B's current-season opponents' season-long assist/turnover ratios during the season 2 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)Now3SeasonsAgo B',  # average of Team B's current-season opponents' season-long assist/turnover ratios during the season 3 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSAvgOppAvgAst/TORatio(alt)NowLastSeason B',  # average of Team B's previous-season opponents' season-long assist/turnover ratios during the previous season (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSAvgOppAvgAst/TORatio(alt)Now2SeasonsAgo B',  # average of Team B's 2-seasons-prior opponents' season-long assist/turnover ratios during the season 2 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSAvgOppAvgAst/TORatio(alt)Now3SeasonsAgo B',  # average of Team B's 3-seasons-prior opponents' season-long assist/turnover ratios during the season 3 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)

    'CurrentSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThenThisSeason B',  # average of Team B's current-season opponents' current-season-long assist/turnover ratios allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThenLastSeason B',  # average of Team B's previous-season opponents' previous-season-long assist/turnover ratios allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThen2SeasonsAgo B',  # average of Team B's 2-seasons-prior opponents' 2-seasons-prior season-long assist/turnover ratios allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThen3SeasonsAgo B',  # average of Team B's 3-seasons-prior opponents' 3-seasons-prior season-long assist/turnover ratios allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNowThisSeason B',  # average of Team B's current-season opponents' up-to-date assist/turnover ratios allowed during the current season (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNowLastSeason B',  # average of Team B's current-season opponents' season-long assist/turnover ratios allowed during the previous season (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long assist/turnover ratios allowed during the season 2 years prior (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long assist/turnover ratios allowed during the season 3 years prior (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'PastSoSAvgOppAvgAst/TORatio(alt)AllowedNowLastSeason B',  # average of Team B's previous-season opponents' season-long assist/turnover ratios allowed during the previous season (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'PastSoSAvgOppAvgAst/TORatio(alt)AllowedNow2SeasonsAgo B',  # average of Team B's 2-seasons-prior opponents' season-long assist/turnover ratios allowed during the season 2 years prior (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)
    'PastSoSAvgOppAvgAst/TORatio(alt)AllowedNow3SeasonsAgo B',  # average of Team B's 3-seasons-prior opponents' season-long assist/turnover ratios allowed during the season 3 years prior (ratios calculated by averaging the assist/turnover ratios allowed from each game, not by dividing total assists allowed / total turnovers forced)

    'CurrentSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThenThisSeason B',  # average of Team B's current-season opponents' current-season-long differences between assist/turnover ratio and assist/turnover ratio allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThenLastSeason B',  # average of Team B's previous-season opponents' previous-season-long differences between assist/turnover ratio and assist/turnover ratio allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThen2SeasonsAgo B',  # average of Team B's 2-seasons-prior opponents' 2-seasons-prior season-long differences between assist/turnover ratio and assist/turnover ratio allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThen3SeasonsAgo B',  # average of Team B's 3-seasons-prior opponents' 3-seasons-prior season-long differences between assist/turnover ratio and assist/turnover ratio allowed, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNowThisSeason B',  # average of Team B's current-season opponents' up-to-date differences between assist/turnover ratio and assist/turnover ratio allowed during the current season (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNowLastSeason B',  # average of Team B's current-season opponents' season-long differences between assist/turnover ratio and assist/turnover ratio allowed during the previous season (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long differences between assist/turnover ratio and assist/turnover ratio allowed during the season 2 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long differences between assist/turnover ratio and assist/turnover ratio allowed during the season 3 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSAvgOppAvgAst/TORatio(alt)MarginNowLastSeason B',  # average of Team B's previous-season opponents' season-long differences between assist/turnover ratio and assist/turnover ratio allowed during the previous season (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSAvgOppAvgAst/TORatio(alt)MarginNow2SeasonsAgo B',  # average of Team B's 2-seasons-prior opponents' season-long differences between assist/turnover ratio and assist/turnover ratio allowed during the season 2 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
    'PastSoSAvgOppAvgAst/TORatio(alt)MarginNow3SeasonsAgo B',  # average of Team B's 3-seasons-prior opponents' season-long differences between assist/turnover ratio and assist/turnover ratio allowed during the season 3 years prior (ratios calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)

    'CurrentSoSWeightedAvgOppStlPerGameThenThisSeason B',  # average of Team B's current-season opponents' average steals per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average steals per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average steals per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average steals per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppStlPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average steals per game during the current season
    'CurrentSoSAvgOppStlPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average steals per game during the previous season
    'CurrentSoSAvgOppStlPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average steals per game during the season 2 years prior
    'CurrentSoSAvgOppStlPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average steals per game during the season 3 years prior
    'PastSoSAvgOppStlPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average steals per game during the previous season
    'PastSoSAvgOppStlPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average steals per game during the season 2 years prior
    'PastSoSAvgOppStlPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average steals per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppStlAllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average steals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlAllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average steals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlAllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average steals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlAllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average steals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppStlAllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average steals allowed per game during the current season
    'CurrentSoSAvgOppStlAllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average steals allowed per game during the previous season
    'CurrentSoSAvgOppStlAllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average steals allowed per game during the season 2 years prior
    'CurrentSoSAvgOppStlAllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average steals allowed per game during the season 3 years prior
    'PastSoSAvgOppStlAllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average steals allowed per game during the previous season
    'PastSoSAvgOppStlAllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average steals allowed per game during the season 2 years prior
    'PastSoSAvgOppStlAllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average steals allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppStlMarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between steals and steals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlMarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between steals and steals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlMarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between steals and steals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppStlMarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between steals and steals allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppStlMarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between steals and steals allowed per game during the current season
    'CurrentSoSAvgOppStlMarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between steals and steals allowed per game during the previous season
    'CurrentSoSAvgOppStlMarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between steals and steals allowed per game during the season 2 years prior
    'CurrentSoSAvgOppStlMarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between steals and steals allowed per game during the season 3 years prior
    'PastSoSAvgOppStlMarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between steals and steals allowed per game during the previous season
    'PastSoSAvgOppStlMarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between steals and steals allowed per game during the season 2 years prior
    'PastSoSAvgOppStlMarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between steals and steals allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppBlkPerGameThenThisSeason B',  # average of Team B's current-season opponents' average blocks per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average blocks per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average blocks per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average blocks per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppBlkPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average blocks per game during the current season
    'CurrentSoSAvgOppBlkPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average blocks per game during the previous season
    'CurrentSoSAvgOppBlkPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average blocks per game during the season 2 years prior
    'CurrentSoSAvgOppBlkPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average blocks per game during the season 3 years prior
    'PastSoSAvgOppBlkPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average blocks per game during the previous season
    'PastSoSAvgOppBlkPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average blocks per game during the season 2 years prior
    'PastSoSAvgOppBlkPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average blocks per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppBlkAllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average blocks allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkAllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average blocks allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkAllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average blocks allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkAllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average blocks allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppBlkAllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average blocks allowed per game during the current season
    'CurrentSoSAvgOppBlkAllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average blocks allowed per game during the previous season
    'CurrentSoSAvgOppBlkAllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average blocks allowed per game during the season 2 years prior
    'CurrentSoSAvgOppBlkAllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average blocks allowed per game during the season 3 years prior
    'PastSoSAvgOppBlkAllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average blocks allowed per game during the previous season
    'PastSoSAvgOppBlkAllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average blocks allowed per game during the season 2 years prior
    'PastSoSAvgOppBlkAllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average blocks allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppBlkMarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between blocks and blocks allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkMarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between blocks and blocks allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkMarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between blocks and blocks allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppBlkMarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between blocks and blocks allowed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppBlkMarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between blocks and blocks allowed per game during the current season
    'CurrentSoSAvgOppBlkMarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between blocks and blocks allowed per game during the previous season
    'CurrentSoSAvgOppBlkMarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between blocks and blocks allowed per game during the season 2 years prior
    'CurrentSoSAvgOppBlkMarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between blocks and blocks allowed per game during the season 3 years prior
    'PastSoSAvgOppBlkMarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between blocks and blocks allowed per game during the previous season
    'PastSoSAvgOppBlkMarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between blocks and blocks allowed per game during the season 2 years prior
    'PastSoSAvgOppBlkMarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between blocks and blocks allowed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppPFPerGameThenThisSeason B',  # average of Team B's current-season opponents' average fouls committed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average fouls committed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average fouls committed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average fouls committed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppPFPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average fouls committed per game during the current season
    'CurrentSoSAvgOppPFPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average fouls committed per game during the previous season
    'CurrentSoSAvgOppPFPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average fouls committed per game during the season 2 years prior
    'CurrentSoSAvgOppPFPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average fouls committed per game during the season 3 years prior
    'PastSoSAvgOppPFPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average fouls committed per game during the previous season
    'PastSoSAvgOppPFPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average fouls committed per game during the season 2 years prior
    'PastSoSAvgOppPFPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average fouls committed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppPFAllowedPerGameThenThisSeason B',  # average of Team B's current-season opponents' average fouls absorbed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFAllowedPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average fouls absorbed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFAllowedPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average fouls absorbed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFAllowedPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average fouls absorbed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppPFAllowedPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average fouls absorbed per game during the current season
    'CurrentSoSAvgOppPFAllowedPerGameNowLastSeason B',  # average of Team B's current-season opponents' season average fouls absorbed per game during the previous season
    'CurrentSoSAvgOppPFAllowedPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season average fouls absorbed per game during the season 2 years prior
    'CurrentSoSAvgOppPFAllowedPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season average fouls absorbed per game during the season 3 years prior
    'PastSoSAvgOppPFAllowedPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average fouls absorbed per game during the previous season
    'PastSoSAvgOppPFAllowedPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average fouls absorbed per game during the season 2 years prior
    'PastSoSAvgOppPFAllowedPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average fouls absorbed per game during the season 3 years prior

    'CurrentSoSWeightedAvgOppPFMarginPerGameThenThisSeason B',  # average of Team B's current-season opponents' average difference between fouls committed and fouls absorbed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFMarginPerGameThenLastSeason B',  # average of Team B's previous-season opponents' average difference between fouls committed and fouls absorbed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFMarginPerGameThen2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' average difference between fouls committed and fouls absorbed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'PastSoSWeightedAvgOppPFMarginPerGameThen3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' average difference between fouls committed and fouls absorbed per game, recorded immediately prior to playing Team B, and weighted by number of games each opponent had played at that time
    'CurrentSoSAvgOppPFMarginPerGameNowThisSeason B',  # average of Team B's current-season opponents' up-to-date average difference between fouls committed and fouls absorbed per game during the current season
    'CurrentSoSAvgOppPFMarginPerGameNowLastSeason B',  # average of Team B's current-season opponents' season-long average difference between fouls committed and fouls absorbed per game during the previous season
    'CurrentSoSAvgOppPFMarginPerGameNow2SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between fouls committed and fouls absorbed per game during the season 2 years prior
    'CurrentSoSAvgOppPFMarginPerGameNow3SeasonsAgo B',  # average of Team B's current-season opponents' season-long average difference between fouls committed and fouls absorbed per game during the season 3 years prior
    'PastSoSAvgOppPFMarginPerGameNowLastSeason B',  # average of Team B's previous-season opponents' season average difference between fouls committed and fouls absorbed per game during the previous season
    'PastSoSAvgOppPFMarginPerGameNow2SeasonsAgo B',  # average of Team B's 2-years-prior-season opponents' season average difference between fouls committed and fouls absorbed per game during the season 2 years prior
    'PastSoSAvgOppPFMarginPerGameNow3SeasonsAgo B',  # average of Team B's 3-years-prior-season opponents' season average difference between fouls committed and fouls absorbed per game during the season 3 years prior
])

inputData = emptyInputDF.copy()

# read in raw game data
rawGamesDF = pd.read_csv(rootDirectory + '/MRegularSeasonDetailedResults.csv')

# identify close games
rawGamesDF['Close'] = np.logical_or(rawGamesDF.loc[:, 'NumOT'], rawGamesDF.loc[:, 'WScore'] - rawGamesDF.loc[:, 'LScore'] <= 3)

# to prevent division by zero, set a small positive minimum for field goal attempts, 3-point field goal attempts, free-throw attempts, and turnovers
rawGamesDF.loc[:, 'WFGA'] = rawGamesDF.loc[:, 'WFGA'].map(lambda x: max(x, 2 ** -64))
rawGamesDF.loc[:, 'LFGA'] = rawGamesDF.loc[:, 'LFGA'].map(lambda x: max(x, 2 ** -64))
rawGamesDF.loc[:, 'WFGA3'] = rawGamesDF.loc[:, 'WFGA3'].map(lambda x: max(x, 2 ** -64))
rawGamesDF.loc[:, 'LFGA3'] = rawGamesDF.loc[:, 'LFGA3'].map(lambda x: max(x, 2 ** -64))
rawGamesDF.loc[:, 'WFTA'] = rawGamesDF.loc[:, 'WFTA'].map(lambda x: max(x, 2 ** -64))
rawGamesDF.loc[:, 'LFTA'] = rawGamesDF.loc[:, 'LFTA'].map(lambda x: max(x, 2 ** -64))
rawGamesDF.loc[:, 'WTO'] = rawGamesDF.loc[:, 'WTO'].map(lambda x: max(x, 2 ** -64))
rawGamesDF.loc[:, 'LTO'] = rawGamesDF.loc[:, 'LTO'].map(lambda x: max(x, 2 ** -64))

# add stop-sign row at the end of rawGamesDF
rawGamesDF.loc[len(rawGamesDF), 'Season'] = 9999

# read in set of all teams
teams = pd.read_csv(rootDirectory + '/MTeams.csv')
teams.set_index('TeamID', inplace=True)

# initialize weights for strength of schedule calculations (increase from 0 to an upper limit of 1)
GamesPlayedWeights = .00390625 * (((np.array(list(range(45)))) * (np.array(list(range(45)))) * (np.array(list(range(45)))) * (np.array(list(range(45))))) / (((.0625 * (np.array(list(range(45)))) * (np.array(list(range(45))))) + 1) * ((.0625 * (np.array(list(range(45)))) * (np.array(list(range(45))))) + 1)))  # used to weight the importance of opponents' records by the number of games they've played

# define dictionary of numerical values for home-court advantage
HomeAdvDict = {'H': 1, 'N': 0, 'A': -1}

# initialize dictionary to store refined data for each season, read in pre-refined data from the first 3 seasons
seasonTotalsDict = {startingSeason - 3: pd.read_csv(rootDirectory + '/SeasonTotals' + '/SeasonTotals' + str(startingSeason - 3) + '.csv'),
                    startingSeason - 2: pd.read_csv(rootDirectory + '/SeasonTotals' + '/SeasonTotals' + str(startingSeason - 2) + '.csv'),
                    startingSeason - 1: pd.read_csv(rootDirectory + '/SeasonTotals' + '/SeasonTotals' + str(startingSeason - 1) + '.csv')}

# set indexes of season total dataframes to the teams' four-digit identification numbers
for season in seasonTotalsDict:
    seasonTotalsDict[season].set_index('Team ID', inplace=True)

# set starting season and day before first season and day
season = 1891  # set to arbitrary year prior to 2003 (start of data)
dayNum = -1
upToMinuteSeasonTotals = pd.DataFrame({})
TeamAWins = True
startTime = datetime.now()

# iterate through each game in rawGamesDF, starting from startingSeason
for index in range((rawGamesDF['Season'] == startingSeason).idxmax(), len(rawGamesDF)):

    # if this is the first game of a new season
    if rawGamesDF.iloc[index, 0] != season:

        # if at least 1 season's worth of games have been processed
        if season > 1891:
            # make end-of-season calculations
            upToMinuteSeasonTotals.loc[:, 'WinPct'] = upToMinuteSeasonTotals.loc[:, 'Wins'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'FlipCloseWinPct'] = upToMinuteSeasonTotals.loc[:, 'FlipCloseWins'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'WinCloseWinPct'] = upToMinuteSeasonTotals.loc[:, 'WinCloseWins'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'LoseCloseWinPct'] = upToMinuteSeasonTotals.loc[:, 'LoseCloseWins'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'PointsPerGame'] = upToMinuteSeasonTotals.loc[:, 'Points'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'PointsAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'PointsAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'PointsMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'PointsPerGame'] - upToMinuteSeasonTotals.loc[:, 'PointsAllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'FGMPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGM'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'FGMAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGMAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'FGMMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGMPerGame'] - upToMinuteSeasonTotals.loc[:, 'FGMAllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'FGAPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGA'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'FGAAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGAAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'FGAMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGAPerGame'] - upToMinuteSeasonTotals.loc[:, 'FGAAllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'FGPctMargin'] = upToMinuteSeasonTotals.loc[:, 'FGPct'] - upToMinuteSeasonTotals.loc[:, 'FGPctAllowed']
            upToMinuteSeasonTotals.loc[:, 'FGM3PerGame'] = upToMinuteSeasonTotals.loc[:, 'FGM3'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'FGM3AllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGM3Allowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'FGM3MarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGM3PerGame'] - upToMinuteSeasonTotals.loc[:, 'FGM3AllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'FGA3PerGame'] = upToMinuteSeasonTotals.loc[:, 'FGA3'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'FGA3AllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGA3Allowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'FGA3MarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGA3PerGame'] - upToMinuteSeasonTotals.loc[:, 'FGA3AllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'FG3PctMargin'] = upToMinuteSeasonTotals.loc[:, 'FG3Pct'] - upToMinuteSeasonTotals.loc[:, 'FG3PctAllowed']
            upToMinuteSeasonTotals.loc[:, 'FTMPerGame'] = upToMinuteSeasonTotals.loc[:, 'FTM'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'FTMAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'FTMAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'FTMMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'FTMPerGame'] - upToMinuteSeasonTotals.loc[:, 'FTMAllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'FTAPerGame'] = upToMinuteSeasonTotals.loc[:, 'FTA'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'FTAAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'FTAAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'FTAMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'FTAPerGame'] - upToMinuteSeasonTotals.loc[:, 'FTAAllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'FTPctMargin'] = upToMinuteSeasonTotals.loc[:, 'FTPct'] - upToMinuteSeasonTotals.loc[:, 'FTPctAllowed']
            upToMinuteSeasonTotals.loc[:, 'RebPerGame'] = (upToMinuteSeasonTotals.loc[:, 'OReb'] + upToMinuteSeasonTotals.loc[:, 'DReb']) / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'RebAllowedPerGame'] = (upToMinuteSeasonTotals.loc[:, 'ORebAllowed'] + upToMinuteSeasonTotals.loc[:, 'DRebAllowed']) / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'RebMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'RebPerGame'] - upToMinuteSeasonTotals.loc[:, 'RebAllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'ORebPerGame'] = upToMinuteSeasonTotals.loc[:, 'OReb'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'ORebAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'ORebAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'ORebMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'ORebPerGame'] - upToMinuteSeasonTotals.loc[:, 'ORebAllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'DRebPerGame'] = upToMinuteSeasonTotals.loc[:, 'DReb'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'DRebAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'DRebAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'DRebMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'DRebPerGame'] - upToMinuteSeasonTotals.loc[:, 'DRebAllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'AstPerGame'] = upToMinuteSeasonTotals.loc[:, 'Ast'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'AstAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'AstAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'AstMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'AstPerGame'] - upToMinuteSeasonTotals.loc[:, 'AstAllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'TOPerGame'] = upToMinuteSeasonTotals.loc[:, 'TO'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'TOAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'TOAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'TOMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'TOPerGame'] - upToMinuteSeasonTotals.loc[:, 'TOAllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'AvgAst/TORatioMargin'] = upToMinuteSeasonTotals.loc[:, 'AvgAst/TORatio'] - upToMinuteSeasonTotals.loc[:, 'AvgAst/TORatioAllowed']
            upToMinuteSeasonTotals.loc[:, 'AvgAst/TORatio(alt)Margin'] = upToMinuteSeasonTotals.loc[:, 'AvgAst/TORatio(alt)'] - upToMinuteSeasonTotals.loc[:, 'AvgAst/TORatio(alt)Allowed']
            upToMinuteSeasonTotals.loc[:, 'StlPerGame'] = upToMinuteSeasonTotals.loc[:, 'Stl'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'StlAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'StlAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'StlMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'StlPerGame'] - upToMinuteSeasonTotals.loc[:, 'StlAllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'BlkPerGame'] = upToMinuteSeasonTotals.loc[:, 'Blk'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'BlkAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'BlkAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'BlkMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'BlkPerGame'] - upToMinuteSeasonTotals.loc[:, 'BlkAllowedPerGame']
            upToMinuteSeasonTotals.loc[:, 'PFPerGame'] = upToMinuteSeasonTotals.loc[:, 'PF'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'PFAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'PFAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            upToMinuteSeasonTotals.loc[:, 'PFMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'PFPerGame'] - upToMinuteSeasonTotals.loc[:, 'PFAllowedPerGame']
            # strength of schedule
            for teamID in upToMinuteSeasonTotals.index:
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppWinPctNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'WinPct'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFlipCloseWinPctNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FlipCloseWinPct'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppWinCloseWinPctNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'WinCloseWinPct'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppLoseCloseWinPctNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'LoseCloseWinPct'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppPointsPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'PointsPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppPointsAllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'PointsAllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppPointsMarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'PointsMarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGMPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGMPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGMAllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGMAllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGMMarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGMMarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGAPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGAPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGAAllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGAAllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGAMarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGAMarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGPctNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGPct'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGPctAllowedNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGPctAllowed'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGPctMarginNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGPctMargin'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGM3PerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGM3PerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGM3AllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGM3AllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGM3MarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGM3MarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGA3PerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGA3PerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGA3AllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGA3AllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFGA3MarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FGA3MarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFG3PctNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FG3Pct'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFG3PctAllowedNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FG3PctAllowed'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFG3PctMarginNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FG3PctMargin'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFTMPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FTMPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFTMAllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FTMAllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFTMMarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FTMMarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFTAPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FTAPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFTAAllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FTAAllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFTAMarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FTAMarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFTPctNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FTPct'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFTPctAllowedNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FTPctAllowed'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppFTPctMarginNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'FTPctMargin'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppRebPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'RebPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppRebAllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'RebAllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppRebMarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'RebMarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppORebPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'ORebPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppORebAllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'ORebAllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppORebMarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'ORebMarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppDRebPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'DRebPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppDRebAllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'DRebAllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppDRebMarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'DRebMarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppAstPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'AstPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppAstAllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'AstAllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppAstMarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'AstMarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppTOPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'TOPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppTOAllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'TOAllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppTOMarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'TOMarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppAvgAst/TORatioNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'AvgAst/TORatio'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppAvgAst/TORatioAllowedNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppAvgAst/TORatioMarginNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'AvgAst/TORatioMargin'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppAvgAst/TORatio(alt)Now'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppAvgAst/TORatio(alt)AllowedNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppAvgAst/TORatio(alt)MarginNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Margin'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppStlPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'StlPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppStlAllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'StlAllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppStlMarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'StlMarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppBlkPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'BlkPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppBlkAllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'BlkAllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppBlkMarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'BlkMarginPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppPFPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'PFPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppPFAllowedPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'PFAllowedPerGame'].mean()
                upToMinuteSeasonTotals.loc[teamID, 'SoSAvgOppPFMarginPerGameNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[teamID, 'ListOpponentsTeamID'], 'PFMarginPerGame'].mean()

            # # make end-of-season calculations
            # upToMinuteSeasonTotals.loc[:, 'WinPct'] = upToMinuteSeasonTotals.loc[:, 'Wins'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'FlipCloseWinPct'] = upToMinuteSeasonTotals.loc[:, 'FlipCloseWins'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'WinCloseWinPct'] = upToMinuteSeasonTotals.loc[:, 'WinCloseWins'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'LoseCloseWinPct'] = upToMinuteSeasonTotals.loc[:, 'LoseCloseWins'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'PointsPerGame'] = upToMinuteSeasonTotals.loc[:, 'Points'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'PointsAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'PointsAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'PointsMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'PointsPerGame'] - upToMinuteSeasonTotals.loc[:, 'PointsAllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'FGMPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGM'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'FGMAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGMAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'FGMMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGMPerGame'] - upToMinuteSeasonTotals.loc[:, 'FGMAllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'FGAPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGA'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'FGAAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGAAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'FGAMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGAPerGame'] - upToMinuteSeasonTotals.loc[:, 'FGAAllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'FGPctMargin'] = upToMinuteSeasonTotals.loc[:, 'FGPct'] - upToMinuteSeasonTotals.loc[:, 'FGPctAllowed']
            # upToMinuteSeasonTotals.loc[:, 'FGM3PerGame'] = upToMinuteSeasonTotals.loc[:, 'FGM3'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'FGM3AllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGM3Allowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'FGM3MarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGM3PerGame'] - upToMinuteSeasonTotals.loc[:, 'FGM3AllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'FGA3PerGame'] = upToMinuteSeasonTotals.loc[:, 'FGA3'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'FGA3AllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGA3Allowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'FGA3MarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'FGA3PerGame'] - upToMinuteSeasonTotals.loc[:, 'FGA3AllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'FGPctMargin'] = upToMinuteSeasonTotals.loc[:, 'FGPct'] - upToMinuteSeasonTotals.loc[:, 'FGPctAllowed']
            # upToMinuteSeasonTotals.loc[:, 'FTMPerGame'] = upToMinuteSeasonTotals.loc[:, 'FTM'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'FTMAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'FTMAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'FTMMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'FTMPerGame'] - upToMinuteSeasonTotals.loc[:, 'FTMAllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'FTAPerGame'] = upToMinuteSeasonTotals.loc[:, 'FTA'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'FTAAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'FTAAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'FTAMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'FTAPerGame'] - upToMinuteSeasonTotals.loc[:, 'FTAAllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'FTPctMargin'] = upToMinuteSeasonTotals.loc[:, 'FTPct'] - upToMinuteSeasonTotals.loc[:, 'FTPctAllowed']
            # upToMinuteSeasonTotals.loc[:, 'RebPerGame'] = (upToMinuteSeasonTotals.loc[:, 'OReb'] + upToMinuteSeasonTotals.loc[:, 'DReb']) / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'RebAllowedPerGame'] = (upToMinuteSeasonTotals.loc[:, 'ORebAllowed'] + upToMinuteSeasonTotals.loc[:, 'DRebAllowed']) / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'RebMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'RebPerGame'] - upToMinuteSeasonTotals.loc[:, 'RebAllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'ORebPerGame'] = upToMinuteSeasonTotals.loc[:, 'OReb'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'ORebAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'ORebAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'ORebMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'ORebPerGame'] - upToMinuteSeasonTotals.loc[:, 'ORebAllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'DRebPerGame'] = upToMinuteSeasonTotals.loc[:, 'DReb'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'DRebAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'DRebAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'DRebMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'DRebPerGame'] - upToMinuteSeasonTotals.loc[:, 'DRebAllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'AstPerGame'] = upToMinuteSeasonTotals.loc[:, 'Ast'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'AstAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'AstAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'AstMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'AstPerGame'] - upToMinuteSeasonTotals.loc[:, 'AstAllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'TOPerGame'] = upToMinuteSeasonTotals.loc[:, 'TO'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'TOAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'TOAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'TOMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'TOPerGame'] - upToMinuteSeasonTotals.loc[:, 'TOAllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'AvgAst/TORatioMargin'] = upToMinuteSeasonTotals.loc[:, 'AvgAst/TORatio'] - upToMinuteSeasonTotals.loc[:, 'AvgAst/TORatioAllowed']
            # upToMinuteSeasonTotals.loc[:, 'AvgAst/TORatio(alt)Margin'] = upToMinuteSeasonTotals.loc[:, 'AvgAst/TORatio(alt)'] - upToMinuteSeasonTotals.loc[:, 'AvgAst/TORatio(alt)Allowed']
            # upToMinuteSeasonTotals.loc[:, 'StlPerGame'] = upToMinuteSeasonTotals.loc[:, 'Stl'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'StlAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'StlAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'StlMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'StlPerGame'] - upToMinuteSeasonTotals.loc[:, 'StlAllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'BlkPerGame'] = upToMinuteSeasonTotals.loc[:, 'Blk'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'BlkAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'BlkAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'BlkMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'BlkPerGame'] - upToMinuteSeasonTotals.loc[:, 'BlkAllowedPerGame']
            # upToMinuteSeasonTotals.loc[:, 'PFPerGame'] = upToMinuteSeasonTotals.loc[:, 'PF'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'PFAllowedPerGame'] = upToMinuteSeasonTotals.loc[:, 'PFAllowed'] / upToMinuteSeasonTotals.loc[:, 'GamesPlayed']
            # upToMinuteSeasonTotals.loc[:, 'PFMarginPerGame'] = upToMinuteSeasonTotals.loc[:, 'PFPerGame'] - upToMinuteSeasonTotals.loc[:, 'PFAllowedPerGame']
            # # strength of schedule
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppWinPctNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'Wins'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFlipCloseWinPctNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FlipCloseWins'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppWinCloseWinPctNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'WinCloseWins'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppLoseCloseWinPctNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'LoseCloseWins'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppPointsPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'Points'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppPointsAllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'PointsAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppPointsMarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'Points'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'PointsAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGMPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGM'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGMAllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGMAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGMMarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGM'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGMAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGAPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGA'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGAAllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGAAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGAMarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGA'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGAAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGPctNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGM'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGA']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGPctAllowedNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGMAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGAAllowed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGPctMarginNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGPct'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGPctAllowed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGM3PerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGM3'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGM3AllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGM3Allowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGM3MarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGM3'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGM3Allowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGA3PerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGA3'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGA3AllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGA3Allowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFGA3MarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGA3'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGA3Allowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFG3PctNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGM3'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGA3']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFG3PctAllowedNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGM3Allowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FGA3Allowed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFG3PctMarginNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FG3Pct'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FG3PctAllowed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFTMPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTM'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFTMAllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTMAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFTMMarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTM'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTMAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFTAPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTA'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFTAAllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTAAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFTAMarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTA'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTAAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFTPctNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTM'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTA']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFTPctAllowedNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTMAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTAAllowed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppFTPctMarginNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTPct'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'FTPctAllowed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppRebPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'OReb'] + upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'DReb']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppRebAllowedPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'ORebAllowed'] + upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'DRebAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppRebMarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'OReb'] + upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'DReb'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'ORebAllowed'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'DRebAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppORebPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'OReb'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppORebAllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'ORebAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppORebMarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'OReb'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'ORebAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppDRebPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'DReb'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppDRebAllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'DRebAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppDRebMarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'DReb'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'DRebAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppAstPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'Ast'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppAstAllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'AstAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppAstMarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'Ast'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'AstAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppTOPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'TO'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppTOAllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'TOAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppTOMarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'TO'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'TOAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppAvgAst/TORatioNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'AvgAst/TORatio'].mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppAvgAst/TORatioAllowedNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed'].mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppAvgAst/TORatioMarginNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'AvgAst/TORatio'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppAvgAst/TORatio(alt)Now'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'].mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppAvgAst/TORatio(alt)AllowedNow'] = upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed'].mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppAvgAst/TORatio(alt)MarginNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppStlPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'Stl'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppStlAllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'StlAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppStlMarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'Stl'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'StlAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppBlkPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'Blk'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppBlkAllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'BlkAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppBlkMarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'Blk'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'BlkAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppPFPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'PF'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppPFAllowedPerGameNow'] = (upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'PFAllowed'] / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
            # upToMinuteSeasonTotals.loc[:, 'SoSAvgOppPFMarginPerGameNow'] = ((upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'PF'] - upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'PFAllowed']) / upToMinuteSeasonTotals.loc[upToMinuteSeasonTotals.loc[:, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()

            # memoize end-of-season totals
            seasonTotalsDict[season] = upToMinuteSeasonTotals.copy()
            # write previous season totals
            seasonTotalsDict[int(season)].to_csv(rootDirectory + '/SeasonTotals' + '/SeasonTotals' + str(int(season)) + '.csv')
            print(rootDirectory + '/SeasonTotals' + '/SeasonTotals' + str(int(season)) + '.csv written')
            # write input data
            inputData.to_csv(rootDirectory + '/InputData' + '/InputData' + str(int(season)) + '.csv')
            print(rootDirectory + '/InputData' + '/InputData' + str(int(season)) + '.csv written')
        # advance to next season
        season = rawGamesDF.iloc[index, 0]
        if season == 9999:
            break
        print('Season:', int(season), '   Current time:', str(datetime.now())[:-7])
        # reset day number
        dayNum = -1
        # reset input dataframe
        inputData = emptyInputDF.copy()
        # reset season totals
        upToMinuteSeasonTotals = pd.DataFrame(columns=['Team ID',  # 4-digit numerical team identification number
                                                       # season totals
                                                       'GamesPlayed',  # total games played during the current season
                                                       'Wins',  # total wins during the current season
                                                       'CloseGames',  # total close games played during the current season
                                                       'FlipCloseWins',  # total wins during the current season (had the results of all of their close games been flipped)
                                                       'WinCloseWins',  # total wins during the current season (had they won all of their close games)
                                                       'LoseCloseWins',  # total wins during the current season (had they lost all of their close games)
                                                       'Points',  # total points scored during the current season
                                                       'PointsAllowed',  # total points allowed during the current season
                                                       'FGM',  # total field goals made during the current season
                                                       'FGMAllowed',  # total field goals allowed during the current season
                                                       'FGA',  # total field goal attempts during the current season
                                                       'FGAAllowed',  # total field goal attempts allowed during the current season
                                                       'FGPct',  # total field goals made divided by total field goal attempts during the current season
                                                       'FGPctAllowed',  # total field goals allowed divided by total field goal attempts allowed during the current season
                                                       'FGM3',  # total 3-point field goals made during the current season
                                                       'FGM3Allowed',  # total 3-point field goals allowed during the current season
                                                       'FGA3',  # total 3 point field goal attempts during the current season
                                                       'FGA3Allowed',  # total 3-point field goal attempts allowed during the current season
                                                       'FG3Pct',  # total 3-point field goals made divided by total 3-point field goal attempts during the current season
                                                       'FG3PctAllowed',  # total 3-point field goals allowed divided by total 3-point field goal attempts allowed during the current season
                                                       'FTM',  # total free-throws made during the current season
                                                       'FTMAllowed',  # total successful free-throws allowed during the current season
                                                       'FTA',  # total free-throw attempts during the current season
                                                       'FTAAllowed',  # total free-throw attempts allowed during the current season
                                                       'FTPct',  # total free-throws made divided by total free-throw attempts during the current season
                                                       'FTPctAllowed',  # total successful free-throws allowed divided by total free-throw attempts allowed during the current season
                                                       'OReb',  # total offensive rebounds during the current season
                                                       'ORebAllowed',  # total offensive rebounds allowed during the current season
                                                       'DReb',  # total defensive rebounds during the current season
                                                       'DRebAllowed',  # total defensive rebounds allowed during the current season
                                                       'Ast',  # total assists during the current season
                                                       'AstAllowed',  # total assists allowed during the current season
                                                       'TO',  # total turnovers during the current season
                                                       'TOAllowed',  # total turnovers forced during the current season
                                                       'AvgAst/TORatio',  # total assists divided by total turnovers during the current season
                                                       'AvgAst/TORatioAllowed',  # total assists allowed divided by total turnovers forced during the current season
                                                       'AvgAst/TORatio(alt)',  # average of assist/turnover ratios during the current season (calculated by averaging each game's assist/turnover ratio, not by dividing total assists / total turnovers)
                                                       'AvgAst/TORatio(alt)Allowed',  # average of opposing assist/turnover ratios during the current season (calculated by averaging each game's assist/turnover ratio, not by dividing total assists / total turnovers)
                                                       'Stl',  # total steals during the current season
                                                       'StlAllowed',  # total steals allowed during the current season
                                                       'Blk',  # total blocks during the current season
                                                       'BlkAllowed',  # total blocks allowed during the current season
                                                       'PF',  # total fouls committed during the current season
                                                       'PFAllowed',  # total fouls absorbed during the current season
                                                       # strength of schedule
                                                       'ListOpponentsTeamID',  # list of opponents' 4-digit team identification numbers
                                                       'SoSSumOppGamesPlayedWeightsDenominator',  # sum of weights applied to opponents' stats based on number of games they'd played prior to their contest against this team
                                                       'SoSWeightedAvgOpponentsWinPct',  # weighted average of opponents' win percentages entering contest against this team
                                                       'SoSWeightedAvgOpponentsFlipCloseWinPct',  # weighted average of opponents' win percentages (had the results of all of their close games been flipped) entering contest against this team
                                                       'SoSWeightedAvgOpponentsWinCloseWinPct',  # weighted average of opponents' win percentages (had they won all of their close games) entering contest against this team
                                                       'SoSWeightedAvgOpponentsLoseCloseWinPct',  # weighted average of opponents' win percentages (had they lost all of their close games) entering contest against this team
                                                       'SoSWeightedAvgOpponentsPointsPerGame',  # weighted average of opponents' average points per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsPointsAllowedPerGame',  # weighted average of opponents' average points per game allowed entering contest against this team
                                                       'SoSWeightedAvgOpponentsFGMPerGame',  # weighted average of opponents' average field goals made per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsFGMAllowedPerGame',  # weighted average of opponents' average field goals allowed per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsFGAPerGame',  # weighted average of opponents' average field goal attempts per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsFGAAllowedPerGame',  # weighted average of opponents' average field goal attempts allowed per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsFGPct',  # weighted average of opponents' season-long field goal percentage entering contest against this team
                                                       'SoSWeightedAvgOpponentsFGPctAllowed',  # weighted average of opponents' season-long field goal percentage allowed entering contest against this team
                                                       'SoSWeightedAvgOpponentsFGM3PerGame',  # weighted average of opponents' average 3-point field goals made per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsFGM3AllowedPerGame',  # weighted average of opponents' average 3-point field goals allowed per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsFGA3PerGame',  # weighted average of opponents' average 3-point field goal attempts per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsFGA3AllowedPerGame',  # weighted average of opponents' average 3-point field goal attempts allowed per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsFG3Pct',  # weighted average of opponents' season-long 3-point field goal percentage entering contest against this team
                                                       'SoSWeightedAvgOpponentsFG3PctAllowed',  # weighted average of opponents' season-long 3-point field goal percentage allowed entering contest against this team
                                                       'SoSWeightedAvgOpponentsFTMPerGame',  # weighted average of opponents' average free throws made per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsFTMAllowedPerGame',  # weighted average of opponents' average successful free throws allowed per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsFTAPerGame',  # weighted average of opponents' average free throw attempts per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsFTAAllowedPerGame',  # weighted average of opponents' average free throw attempts allowed per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsFTPct',  # weighted average of opponents' season-long free-throw percentage entering contest against this team
                                                       'SoSWeightedAvgOpponentsFTPctAllowed',  # weighted average of opponents' season-long free-throw percentage allowed entering contest against this team
                                                       'SoSWeightedAvgOpponentsORebPerGame',  # weighted average of opponents' average offensive rebounds per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsORebAllowedPerGame',  # weighted average of opponents' average offensive rebounds allowed per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsDRebPerGame',  # weighted average of opponents' average defensive rebounds per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsDRebAllowedPerGame',  # weighted average of opponents' average defensive rebounds allowed per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsAstPerGame',  # weighted average of opponents' average assists per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsAstAllowedPerGame',  # weighted average of opponents' average assists allowed per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsTOPerGame',  # weighted average of opponents' average turnovers per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsTOAllowedPerGame',  # weighted average of opponents' average turnovers forced per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsAst/TORatio',  # weighted average of opponents' season-long assist/turnover ratios (total assists / total turnovers) entering contest against this team
                                                       'SoSWeightedAvgOpponentsAst/TORatioAllowed',  # weighted average of opponents' season-long assist/turnover ratios allowed (total assists allowed / total turnovers forced) entering contest against this team (calculated by averaging each team's total assists allowed divided by that team's total turnovers forced)
                                                       'SoSWeightedAvgOpponentsAst/TORatio(alt)',  # weighted average of opponents' average of assist/turnover ratios entering contest against this team (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
                                                       'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed',  # weighted average of opponents' average of assist/turnover ratios allowed entering contest against this team (calculated by averaging the assist/turnover ratios from each game, not by dividing total assists / total turnovers)
                                                       'SoSWeightedAvgOpponentsStlPerGame',  # weighted average of opponents' average steals per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsStlAllowedPerGame',  # weighted average of opponents' average steals allowed per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsBlkPerGame',  # weighted average of opponents' average blocks per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsBlkAllowedPerGame',  # weighted average of opponents' average blocks allowed per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsPFPerGame',  # weighted average of opponents' average fouls committed per game entering contest against this team
                                                       'SoSWeightedAvgOpponentsPFAllowedPerGame'])  # weighted average of opponents' average fouls absorbed per game entering contest against this team
        upToMinuteSeasonTotals.set_index('Team ID', inplace=True)
        for team in teams.index:
            upToMinuteSeasonTotals.loc[team] = {'GamesPlayed': 0, 'Wins': 0, 'CloseGames': 0, 'FlipCloseWins': 0, 'WinCloseWins': 0, 'LoseCloseWins': 0, 'Points': 0, 'PointsAllowed': 0, 'FGM': 0, 'FGMAllowed': 0,
                                                'FGA': 0, 'FGAAllowed': 0, 'FGPct': 0, 'FGPctAllowed': 0, 'FGM3': 0, 'FGM3Allowed': 0, 'FGA3': 0, 'FGA3Allowed': 0, 'FG3Pct': 0, 'FG3PctAllowed': 0, 'FTM': 0, 'FTMAllowed': 0, 'FTA': 0, 'FTAAllowed': 0, 'FTPct': 0, 'FTPctAllowed': 0, 'OReb': 0, 'ORebAllowed': 0,
                                                'DReb': 0, 'DRebAllowed': 0, 'Ast': 0, 'AstAllowed': 0, 'TO': 0, 'TOAllowed': 0, 'AvgAst/TORatio': 0, 'AvgAst/TORatioAllowed': 0, 'AvgAst/TORatio(alt)': 0, 'AvgAst/TORatio(alt)Allowed': 0,
                                                'Stl': 0, 'StlAllowed': 0, 'Blk': 0, 'BlkAllowed': 0, 'PF': 0, 'PFAllowed': 0, 'ListOpponentsTeamID': [], 'SoSSumOppGamesPlayedWeightsDenominator': 0, 'SoSWeightedAvgOpponentsWinPct': 0,
                                                'SoSWeightedAvgOpponentsFlipCloseWinPct': 0, 'SoSWeightedAvgOpponentsWinCloseWinPct': 0, 'SoSWeightedAvgOpponentsLoseCloseWinPct': 0, 'SoSWeightedAvgOpponentsPointsPerGame': 0,
                                                'SoSWeightedAvgOpponentsPointsAllowedPerGame': 0, 'SoSWeightedAvgOpponentsFGMPerGame': 0, 'SoSWeightedAvgOpponentsFGMAllowedPerGame': 0, 'SoSWeightedAvgOpponentsFGAPerGame': 0,
                                                'SoSWeightedAvgOpponentsFGAAllowedPerGame': 0, 'SoSWeightedAvgOpponentsFGPct': 0, 'SoSWeightedAvgOpponentsFGPctAllowed': 0, 'SoSWeightedAvgOpponentsFGM3PerGame': 0, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame': 0, 'SoSWeightedAvgOpponentsFGA3PerGame': 0,
                                                'SoSWeightedAvgOpponentsFGA3AllowedPerGame': 0, 'SoSWeightedAvgOpponentsFG3Pct': 0, 'SoSWeightedAvgOpponentsFG3PctAllowed': 0, 'SoSWeightedAvgOpponentsFTMPerGame': 0, 'SoSWeightedAvgOpponentsFTMAllowedPerGame': 0, 'SoSWeightedAvgOpponentsFTAPerGame': 0,
                                                'SoSWeightedAvgOpponentsFTAAllowedPerGame': 0, 'SoSWeightedAvgOpponentsFTPct': 0, 'SoSWeightedAvgOpponentsFTPctAllowed': 0, 'SoSWeightedAvgOpponentsORebPerGame': 0, 'SoSWeightedAvgOpponentsORebAllowedPerGame': 0, 'SoSWeightedAvgOpponentsDRebPerGame': 0,
                                                'SoSWeightedAvgOpponentsDRebAllowedPerGame': 0, 'SoSWeightedAvgOpponentsAstPerGame': 0, 'SoSWeightedAvgOpponentsAstAllowedPerGame': 0, 'SoSWeightedAvgOpponentsTOPerGame': 0,
                                                'SoSWeightedAvgOpponentsTOAllowedPerGame': 0, 'SoSWeightedAvgOpponentsAst/TORatio': 0, 'SoSWeightedAvgOpponentsAst/TORatioAllowed': 0, 'SoSWeightedAvgOpponentsAst/TORatio(alt)': 0, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed': 0,
                                                'SoSWeightedAvgOpponentsStlPerGame': 0, 'SoSWeightedAvgOpponentsStlAllowedPerGame': 0, 'SoSWeightedAvgOpponentsBlkPerGame': 0, 'SoSWeightedAvgOpponentsBlkAllowedPerGame': 0,
                                                'SoSWeightedAvgOpponentsPFPerGame': 0, 'SoSWeightedAvgOpponentsPFAllowedPerGame': 0}

    # if this is the first game of a new day
    if rawGamesDF.iloc[index, 1] > dayNum:
        dayNum = rawGamesDF.iloc[index, 1]
        print('Season:', int(season), '   Day Number:', int(dayNum), '   Current Time:', str(datetime.now())[:-7])
        # update season totals
        startOfDaySeasonTotals = upToMinuteSeasonTotals.copy()

    # update winning team's up-to-the-minute season totals with results of game
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] += 1
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'Wins'] += 1
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'CloseGames'] += rawGamesDF.loc[index, 'Close']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FlipCloseWins'] += 1 - rawGamesDF.loc[index, 'Close']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'WinCloseWins'] += 1
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'LoseCloseWins'] += 1 - rawGamesDF.loc[index, 'Close']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'Points'] += rawGamesDF.loc[index, 'WScore']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'PointsAllowed'] += rawGamesDF.loc[index, 'LScore']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGM'] += rawGamesDF.loc[index, 'WFGM']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGMAllowed'] += rawGamesDF.loc[index, 'LFGM']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGA'] += rawGamesDF.loc[index, 'WFGA']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGAAllowed'] += rawGamesDF.loc[index, 'LFGA']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGM'] + rawGamesDF.loc[index, 'WFGM']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGA'] + rawGamesDF.loc[index, 'WFGA'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGPctAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGMAllowed'] + rawGamesDF.loc[index, 'LFGM']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGAAllowed'] + rawGamesDF.loc[index, 'LFGA'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGM3'] += rawGamesDF.loc[index, 'WFGM3']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGM3Allowed'] += rawGamesDF.loc[index, 'LFGM3']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGA3'] += rawGamesDF.loc[index, 'WFGA3']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGA3Allowed'] += rawGamesDF.loc[index, 'LFGA3']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FG3Pct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGM3'] + rawGamesDF.loc[index, 'WFGM3']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGA3'] + rawGamesDF.loc[index, 'WFGA3'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FG3PctAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGM3Allowed'] + rawGamesDF.loc[index, 'LFGM3']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGA3Allowed'] + rawGamesDF.loc[index, 'LFGA3'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTM'] += rawGamesDF.loc[index, 'WFTM']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTMAllowed'] += rawGamesDF.loc[index, 'LFTM']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTA'] += rawGamesDF.loc[index, 'WFTA']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTAAllowed'] += rawGamesDF.loc[index, 'LFTA']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTM'] + rawGamesDF.loc[index, 'WFTM']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTA'] + rawGamesDF.loc[index, 'WFTA'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTPctAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTMAllowed'] + rawGamesDF.loc[index, 'LFTM']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTAAllowed'] + rawGamesDF.loc[index, 'LFTA'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'OReb'] += rawGamesDF.loc[index, 'WOR']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'ORebAllowed'] += rawGamesDF.loc[index, 'LOR']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'DReb'] += rawGamesDF.loc[index, 'WDR']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'DRebAllowed'] += rawGamesDF.loc[index, 'LDR']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'Ast'] += rawGamesDF.loc[index, 'WAst']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'AstAllowed'] += rawGamesDF.loc[index, 'LAst']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'TO'] += rawGamesDF.loc[index, 'WTO']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'TOAllowed'] += rawGamesDF.loc[index, 'LTO']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'AvgAst/TORatio'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'Ast'] + rawGamesDF.loc[index, 'WAst']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'TO'] + rawGamesDF.loc[index, 'WTO'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'AvgAst/TORatioAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'AstAllowed'] + rawGamesDF.loc[index, 'LAst']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'TOAllowed'] + rawGamesDF.loc[index, 'LTO'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'AvgAst/TORatio(alt)'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'AvgAst/TORatio(alt)'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] + rawGamesDF.loc[index, 'WAst'] / rawGamesDF.loc[index, 'WTO']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] + 1)
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'AvgAst/TORatio(alt)Allowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'AvgAst/TORatio(alt)Allowed'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] + rawGamesDF.loc[index, 'LAst'] / rawGamesDF.loc[index, 'LTO']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] + 1)
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'Stl'] += rawGamesDF.loc[index, 'WStl']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'StlAllowed'] += rawGamesDF.loc[index, 'LStl']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'Blk'] += rawGamesDF.loc[index, 'WBlk']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'BlkAllowed'] += rawGamesDF.loc[index, 'LBlk']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'PF'] += rawGamesDF.loc[index, 'WPF']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'PFAllowed'] += rawGamesDF.loc[index, 'LPF']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'ListOpponentsTeamID'].append(rawGamesDF.loc[index, 'LTeamID'])
    if startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']:
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] += GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsWinPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsWinPct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'Wins'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFlipCloseWinPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFlipCloseWinPct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FlipCloseWins'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsWinCloseWinPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsWinCloseWinPct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'WinCloseWins'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsLoseCloseWinPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsLoseCloseWinPct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'LoseCloseWins'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsPointsPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsPointsPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'Points'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsPointsAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsPointsAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'PointsAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGMPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGMPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGM'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGMAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGMAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGMAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGAPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGAPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGA'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGAAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGAAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGAAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGPct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGM'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGA'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGPctAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGPctAllowed'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGMAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGAAllowed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGM3PerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGM3PerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGM3'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGM3AllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGM3AllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGM3Allowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGA3PerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGA3PerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGA3'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGA3AllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFGA3AllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGA3Allowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFG3Pct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFG3Pct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGM3'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGA3'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFG3PctAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFG3PctAllowed'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGM3Allowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGA3Allowed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFTMPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFTMPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTM'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFTMAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFTMAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTMAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFTAPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFTAPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTA'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFTAAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFTAAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTAAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFTPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFTPct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTM'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTA'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFTPctAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsFTPctAllowed'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTMAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTAAllowed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsORebPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsORebPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'OReb'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsORebAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsORebAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'ORebAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsDRebPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsDRebPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'DReb'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsDRebAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsDRebAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'DRebAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsAstPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsAstPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'Ast'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsAstAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsAstAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'AstAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsTOPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsTOPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'TO'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsTOAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsTOAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'TOAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsAst/TORatio'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsAst/TORatio'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'Ast'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'TO'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsAst/TORatioAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsAst/TORatioAllowed'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'AstAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'TOAllowed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsAst/TORatio(alt)'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsAst/TORatio(alt)'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'AvgAst/TORatio(alt)'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'AvgAst/TORatio(alt)Allowed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsStlPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsStlPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'Stl'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsStlAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsStlAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'StlAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsBlkPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsBlkPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'Blk'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsBlkAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsBlkAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'BlkAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsPFPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsPFPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'PF'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsPFAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSWeightedAvgOpponentsPFAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'PFAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed']])
    # update losing team's up-to-the-minute season totals with results of game
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] += 1
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'CloseGames'] += rawGamesDF.loc[index, 'Close']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FlipCloseWins'] += rawGamesDF.loc[index, 'Close']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'WinCloseWins'] += rawGamesDF.loc[index, 'Close']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'Points'] += rawGamesDF.loc[index, 'LScore']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'PointsAllowed'] += rawGamesDF.loc[index, 'WScore']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGM'] += rawGamesDF.loc[index, 'LFGM']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGMAllowed'] += rawGamesDF.loc[index, 'WFGM']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGA'] += rawGamesDF.loc[index, 'LFGA']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGAAllowed'] += rawGamesDF.loc[index, 'WFGA']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGM'] + rawGamesDF.loc[index, 'LFGM']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGA'] + rawGamesDF.loc[index, 'LFGA'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGPctAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGMAllowed'] + rawGamesDF.loc[index, 'WFGM']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGAAllowed'] + rawGamesDF.loc[index, 'WFGA'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGM3'] += rawGamesDF.loc[index, 'LFGM3']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGM3Allowed'] += rawGamesDF.loc[index, 'WFGM3']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGA3'] += rawGamesDF.loc[index, 'LFGA3']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGA3Allowed'] += rawGamesDF.loc[index, 'WFGA3']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FG3Pct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGM3'] + rawGamesDF.loc[index, 'LFGM3']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGA3'] + rawGamesDF.loc[index, 'LFGA3'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FG3PctAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGM3Allowed'] + rawGamesDF.loc[index, 'WFGM3']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FGA3Allowed'] + rawGamesDF.loc[index, 'WFGA3'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTM'] += rawGamesDF.loc[index, 'LFTM']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTMAllowed'] += rawGamesDF.loc[index, 'WFTM']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTA'] += rawGamesDF.loc[index, 'LFTA']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTAAllowed'] += rawGamesDF.loc[index, 'WFTA']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTM'] + rawGamesDF.loc[index, 'LFTM']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTA'] + rawGamesDF.loc[index, 'LFTA'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTPctAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTMAllowed'] + rawGamesDF.loc[index, 'WFTM']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'FTAAllowed'] + rawGamesDF.loc[index, 'WFTA'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'OReb'] += rawGamesDF.loc[index, 'LOR']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'ORebAllowed'] += rawGamesDF.loc[index, 'WOR']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'DReb'] += rawGamesDF.loc[index, 'LDR']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'DRebAllowed'] += rawGamesDF.loc[index, 'WDR']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'Ast'] += rawGamesDF.loc[index, 'LAst']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'AstAllowed'] += rawGamesDF.loc[index, 'WAst']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'TO'] += rawGamesDF.loc[index, 'LTO']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'TOAllowed'] += rawGamesDF.loc[index, 'WTO']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'AvgAst/TORatio'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'Ast'] + rawGamesDF.loc[index, 'LAst']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'TO'] + rawGamesDF.loc[index, 'LTO'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'AvgAst/TORatioAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'AstAllowed'] + rawGamesDF.loc[index, 'WAst']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'TOAllowed'] + rawGamesDF.loc[index, 'WTO'])
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'AvgAst/TORatio(alt)'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'AvgAst/TORatio(alt)'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] + rawGamesDF.loc[index, 'LAst'] / rawGamesDF.loc[index, 'LTO']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] + 1)
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'AvgAst/TORatio(alt)Allowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'AvgAst/TORatio(alt)Allowed'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] + rawGamesDF.loc[index, 'WAst'] / rawGamesDF.loc[index, 'WTO']) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] + 1)
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'Stl'] += rawGamesDF.loc[index, 'LStl']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'StlAllowed'] += rawGamesDF.loc[index, 'WStl']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'Blk'] += rawGamesDF.loc[index, 'LBlk']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'BlkAllowed'] += rawGamesDF.loc[index, 'WBlk']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'PF'] += rawGamesDF.loc[index, 'LPF']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'PFAllowed'] += rawGamesDF.loc[index, 'WPF']
    upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'ListOpponentsTeamID'].append(rawGamesDF.loc[index, 'WTeamID'])
    if startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']:
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] += GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsWinPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsWinPct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'Wins'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFlipCloseWinPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFlipCloseWinPct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FlipCloseWins'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsWinCloseWinPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsWinCloseWinPct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'WinCloseWins'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsLoseCloseWinPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsLoseCloseWinPct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'LoseCloseWins'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsPointsPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsPointsPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'Points'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsPointsAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsPointsAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'PointsAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGMPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGMPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGM'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGMAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGMAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGMAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGAPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGAPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGA'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGAAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGAAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGAAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGPct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGM'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGA'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGPctAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGPctAllowed'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGMAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGAAllowed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGM3PerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGM3PerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGM3'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGM3AllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGM3AllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGM3Allowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGA3PerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGA3PerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGA3'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGA3AllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFGA3AllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGA3Allowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFG3Pct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFG3Pct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGM3'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGA3'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFG3PctAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFG3PctAllowed'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGM3Allowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FGA3Allowed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFTMPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFTMPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTM'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFTMAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFTMAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTMAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFTAPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFTAPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTA'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFTAAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFTAAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTAAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFTPct'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFTPct'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTM'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTA'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFTPctAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsFTPctAllowed'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTMAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'FTAAllowed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsORebPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsORebPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'OReb'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsORebAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsORebAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'ORebAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsDRebPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsDRebPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'DReb'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsDRebAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsDRebAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'DRebAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsAstPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsAstPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'Ast'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsAstAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsAstAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'AstAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsTOPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsTOPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'TO'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsTOAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsTOAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'TOAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsAst/TORatio'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsAst/TORatio'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'Ast'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'TO'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsAst/TORatioAllowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsAst/TORatioAllowed'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'AstAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'TOAllowed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsAst/TORatio(alt)'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsAst/TORatio(alt)'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'AvgAst/TORatio(alt)'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'AvgAst/TORatio(alt)Allowed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsStlPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsStlPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'Stl'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsStlAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsStlAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'StlAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsBlkPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsBlkPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'Blk'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsBlkAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsBlkAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'BlkAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsPFPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsPFPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'PF'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])
        upToMinuteSeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsPFAllowedPerGame'] = (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSWeightedAvgOpponentsPFAllowedPerGame'] * startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'PFAllowed'] / startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] * GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']]) / (startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'SoSSumOppGamesPlayedWeightsDenominator'] + GamesPlayedWeights[startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed']])

    # if both teams have played at least 5 games prior to this one during the current season, and both teams have at least 3 seasons of historical data
    if startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'WTeamID']), 'GamesPlayed'] >= 5 and startOfDaySeasonTotals.loc[int(rawGamesDF.loc[index, 'LTeamID']), 'GamesPlayed'] >= 5 \
            and seasonTotalsDict[season - 3].loc[rawGamesDF.loc[index, 'WTeamID'], 'GamesPlayed'] and seasonTotalsDict[season - 2].loc[rawGamesDF.loc[index, 'WTeamID'], 'GamesPlayed'] and seasonTotalsDict[season - 1].loc[rawGamesDF.loc[index, 'WTeamID'], 'GamesPlayed'] \
            and seasonTotalsDict[season - 3].loc[rawGamesDF.loc[index, 'LTeamID'], 'GamesPlayed'] and seasonTotalsDict[season - 2].loc[rawGamesDF.loc[index, 'LTeamID'], 'GamesPlayed'] and seasonTotalsDict[season - 1].loc[rawGamesDF.loc[index, 'LTeamID'], 'GamesPlayed']:

        # create input tensor for game

        # flip flag to alternate winning team between Team A and Team B each game
        TeamAWins = not TeamAWins
        if TeamAWins:
            teamA = rawGamesDF.loc[index, 'WTeamID']
            teamB = rawGamesDF.loc[index, 'LTeamID']
        else:
            teamA = rawGamesDF.loc[index, 'LTeamID']
            teamB = rawGamesDF.loc[index, 'WTeamID']

        # assign labels (True if Team A wins, False if Team B wins)
        inputData.loc[index, 'Labels'] = TeamAWins

        # use teams' four-digit identification numbers as pseudo-indexes
        inputData.loc[index, 'TeamID A'] = teamA
        inputData.loc[index, 'TeamID B'] = teamB

        # Team A's features
        inputData.loc[index, 'HomeAdv A'] = (2 * TeamAWins - 1) * HomeAdvDict[rawGamesDF.loc[index, 'WLoc']]
        inputData.loc[index, 'NumGamesPlayedThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']

        inputData.loc[index, 'WinPctThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'Wins'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'WinPctLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'WinPct']
        inputData.loc[index, 'WinPct2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'WinPct']
        inputData.loc[index, 'WinPct3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'WinPct']

        inputData.loc[index, 'FlipCloseWinPctThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FlipCloseWins'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FlipCloseWinPctLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FlipCloseWinPct']
        inputData.loc[index, 'FlipCloseWinPct2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FlipCloseWinPct']
        inputData.loc[index, 'FlipCloseWinPct3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FlipCloseWinPct']

        inputData.loc[index, 'WinCloseWinPctThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'WinCloseWins'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'WinCloseWinPctLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'WinCloseWinPct']
        inputData.loc[index, 'WinCloseWinPct2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'WinCloseWinPct']
        inputData.loc[index, 'WinCloseWinPct3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'WinCloseWinPct']

        inputData.loc[index, 'LoseCloseWinPctThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'LoseCloseWins'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'LoseCloseWinPctLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'LoseCloseWinPct']
        inputData.loc[index, 'LoseCloseWinPct2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'LoseCloseWinPct']
        inputData.loc[index, 'LoseCloseWinPct3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'LoseCloseWinPct']

        inputData.loc[index, 'PointsPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'Points'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'PointsPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'PointsPerGame']
        inputData.loc[index, 'PointsPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'PointsPerGame']
        inputData.loc[index, 'PointsPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'PointsPerGame']

        inputData.loc[index, 'PointsAllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'PointsAllowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'PointsAllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'PointsAllowedPerGame']
        inputData.loc[index, 'PointsAllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'PointsAllowedPerGame']
        inputData.loc[index, 'PointsAllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'PointsAllowedPerGame']

        inputData.loc[index, 'PointsMarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'Points'] - startOfDaySeasonTotals.loc[teamA, 'PointsAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'PointsMarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'PointsMarginPerGame']
        inputData.loc[index, 'PointsMarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'PointsMarginPerGame']
        inputData.loc[index, 'PointsMarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'PointsMarginPerGame']

        inputData.loc[index, 'FGMPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGM'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FGMPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGMPerGame']
        inputData.loc[index, 'FGMPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGMPerGame']
        inputData.loc[index, 'FGMPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGMPerGame']

        inputData.loc[index, 'FGMAllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGMAllowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FGMAllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGMAllowedPerGame']
        inputData.loc[index, 'FGMAllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGMAllowedPerGame']
        inputData.loc[index, 'FGMAllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGMAllowedPerGame']

        inputData.loc[index, 'FGMMarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'FGM'] - startOfDaySeasonTotals.loc[teamA, 'FGMAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FGMMarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGMMarginPerGame']
        inputData.loc[index, 'FGMMarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGMMarginPerGame']
        inputData.loc[index, 'FGMMarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGMMarginPerGame']

        inputData.loc[index, 'FGAPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGA'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FGAPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGAPerGame']
        inputData.loc[index, 'FGAPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGAPerGame']
        inputData.loc[index, 'FGAPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGAPerGame']

        inputData.loc[index, 'FGAAllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGAAllowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FGAAllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGAAllowedPerGame']
        inputData.loc[index, 'FGAAllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGAAllowedPerGame']
        inputData.loc[index, 'FGAAllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGAAllowedPerGame']

        inputData.loc[index, 'FGAMarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'FGA'] - startOfDaySeasonTotals.loc[teamA, 'FGAAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FGAMarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGAMarginPerGame']
        inputData.loc[index, 'FGAMarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGAMarginPerGame']
        inputData.loc[index, 'FGAMarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGAMarginPerGame']

        inputData.loc[index, 'FGPctThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGM'] / startOfDaySeasonTotals.loc[teamA, 'FGA']
        inputData.loc[index, 'FGPctLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGPct']
        inputData.loc[index, 'FGPct2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGPct']
        inputData.loc[index, 'FGPct3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGPct']

        inputData.loc[index, 'FGPctAllowedThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGMAllowed'] / startOfDaySeasonTotals.loc[teamA, 'FGAAllowed']
        inputData.loc[index, 'FGPctAllowedLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGPctAllowed']
        inputData.loc[index, 'FGPctAllowed2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGPctAllowed']
        inputData.loc[index, 'FGPctAllowed3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGPctAllowed']

        inputData.loc[index, 'FGPctMarginThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGM'] / startOfDaySeasonTotals.loc[teamA, 'FGA'] - startOfDaySeasonTotals.loc[teamA, 'FGMAllowed'] / startOfDaySeasonTotals.loc[teamA, 'FGAAllowed']
        inputData.loc[index, 'FGPctMarginLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGPctMargin']
        inputData.loc[index, 'FGPctMargin2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGPctMargin']
        inputData.loc[index, 'FGPctMargin3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGPctMargin']

        inputData.loc[index, 'FGM3PerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGM3'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FGM3PerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGM3PerGame']
        inputData.loc[index, 'FGM3PerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGM3PerGame']
        inputData.loc[index, 'FGM3PerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGM3PerGame']

        inputData.loc[index, 'FGM3AllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGM3Allowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FGM3AllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGM3AllowedPerGame']
        inputData.loc[index, 'FGM3AllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGM3AllowedPerGame']
        inputData.loc[index, 'FGM3AllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGM3AllowedPerGame']

        inputData.loc[index, 'FGM3MarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'FGM3'] - startOfDaySeasonTotals.loc[teamA, 'FGM3Allowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FGM3MarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGM3MarginPerGame']
        inputData.loc[index, 'FGM3MarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGM3MarginPerGame']
        inputData.loc[index, 'FGM3MarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGM3MarginPerGame']

        inputData.loc[index, 'FGA3PerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGA3'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FGA3PerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGA3PerGame']
        inputData.loc[index, 'FGA3PerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGA3PerGame']
        inputData.loc[index, 'FGA3PerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGA3PerGame']

        inputData.loc[index, 'FGA3AllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGA3Allowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FGA3AllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGA3AllowedPerGame']
        inputData.loc[index, 'FGA3AllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGA3AllowedPerGame']
        inputData.loc[index, 'FGA3AllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGA3AllowedPerGame']

        inputData.loc[index, 'FGA3MarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'FGA3'] - startOfDaySeasonTotals.loc[teamA, 'FGA3Allowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FGA3MarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FGA3MarginPerGame']
        inputData.loc[index, 'FGA3MarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FGA3MarginPerGame']
        inputData.loc[index, 'FGA3MarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FGA3MarginPerGame']

        inputData.loc[index, 'FG3PctThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGM3'] / startOfDaySeasonTotals.loc[teamA, 'FGA3']
        inputData.loc[index, 'FG3PctLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FG3Pct']
        inputData.loc[index, 'FG3Pct2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FG3Pct']
        inputData.loc[index, 'FG3Pct3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FG3Pct']

        inputData.loc[index, 'FG3PctAllowedThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGM3Allowed'] / startOfDaySeasonTotals.loc[teamA, 'FGA3Allowed']
        inputData.loc[index, 'FG3PctAllowedLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FG3PctAllowed']
        inputData.loc[index, 'FG3PctAllowed2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FG3PctAllowed']
        inputData.loc[index, 'FG3PctAllowed3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FG3PctAllowed']

        inputData.loc[index, 'FG3PctMarginThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FGM3'] / startOfDaySeasonTotals.loc[teamA, 'FGA3'] - startOfDaySeasonTotals.loc[teamA, 'FGM3Allowed'] / startOfDaySeasonTotals.loc[teamA, 'FGA3Allowed']
        inputData.loc[index, 'FG3PctMarginLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FG3PctMargin']
        inputData.loc[index, 'FG3PctMargin2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FG3PctMargin']
        inputData.loc[index, 'FG3PctMargin3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FG3PctMargin']

        inputData.loc[index, 'FTMPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FTM'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FTMPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FTMPerGame']
        inputData.loc[index, 'FTMPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FTMPerGame']
        inputData.loc[index, 'FTMPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FTMPerGame']

        inputData.loc[index, 'FTMAllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FTMAllowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FTMAllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FTMAllowedPerGame']
        inputData.loc[index, 'FTMAllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FTMAllowedPerGame']
        inputData.loc[index, 'FTMAllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FTMAllowedPerGame']

        inputData.loc[index, 'FTMMarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'FTM'] - startOfDaySeasonTotals.loc[teamA, 'FTMAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FTMMarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FTMMarginPerGame']
        inputData.loc[index, 'FTMMarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FTMMarginPerGame']
        inputData.loc[index, 'FTMMarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FTMMarginPerGame']

        inputData.loc[index, 'FTAPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FTA'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FTAPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FTAPerGame']
        inputData.loc[index, 'FTAPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FTAPerGame']
        inputData.loc[index, 'FTAPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FTAPerGame']

        inputData.loc[index, 'FTAAllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FTAAllowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FTAAllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FTAAllowedPerGame']
        inputData.loc[index, 'FTAAllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FTAAllowedPerGame']
        inputData.loc[index, 'FTAAllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FTAAllowedPerGame']

        inputData.loc[index, 'FTAMarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'FTA'] - startOfDaySeasonTotals.loc[teamA, 'FTAAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'FTAMarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FTAMarginPerGame']
        inputData.loc[index, 'FTAMarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FTAMarginPerGame']
        inputData.loc[index, 'FTAMarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FTAMarginPerGame']

        inputData.loc[index, 'FTPctThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FTM'] / startOfDaySeasonTotals.loc[teamA, 'FTA']
        inputData.loc[index, 'FTPctLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FTPct']
        inputData.loc[index, 'FTPct2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FTPct']
        inputData.loc[index, 'FTPct3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FTPct']

        inputData.loc[index, 'FTPctAllowedThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FTMAllowed'] / startOfDaySeasonTotals.loc[teamA, 'FTAAllowed']
        inputData.loc[index, 'FTPctAllowedLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FTPctAllowed']
        inputData.loc[index, 'FTPctAllowed2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FTPctAllowed']
        inputData.loc[index, 'FTPctAllowed3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FTPctAllowed']

        inputData.loc[index, 'FTPctMarginThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'FTM'] / startOfDaySeasonTotals.loc[teamA, 'FTA'] - startOfDaySeasonTotals.loc[teamA, 'FTMAllowed'] / startOfDaySeasonTotals.loc[teamA, 'FTAAllowed']
        inputData.loc[index, 'FTPctMarginLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'FTPctMargin']
        inputData.loc[index, 'FTPctMargin2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'FTPctMargin']
        inputData.loc[index, 'FTPctMargin3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'FTPctMargin']

        inputData.loc[index, 'RebPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'OReb'] + startOfDaySeasonTotals.loc[teamA, 'DReb']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'RebPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'RebPerGame']
        inputData.loc[index, 'RebPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'RebPerGame']
        inputData.loc[index, 'RebPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'RebPerGame']

        inputData.loc[index, 'RebAllowedPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'ORebAllowed'] + startOfDaySeasonTotals.loc[teamA, 'DRebAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'RebAllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'RebAllowedPerGame']
        inputData.loc[index, 'RebAllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'RebAllowedPerGame']
        inputData.loc[index, 'RebAllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'RebAllowedPerGame']

        inputData.loc[index, 'RebMarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'OReb'] + startOfDaySeasonTotals.loc[teamA, 'DReb'] - startOfDaySeasonTotals.loc[teamA, 'ORebAllowed'] - startOfDaySeasonTotals.loc[teamA, 'DRebAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'RebMarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'RebMarginPerGame']
        inputData.loc[index, 'RebMarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'RebMarginPerGame']
        inputData.loc[index, 'RebMarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'RebMarginPerGame']

        inputData.loc[index, 'ORebPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'OReb'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'ORebPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'ORebPerGame']
        inputData.loc[index, 'ORebPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'ORebPerGame']
        inputData.loc[index, 'ORebPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'ORebPerGame']

        inputData.loc[index, 'ORebAllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'ORebAllowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'ORebAllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'ORebAllowedPerGame']
        inputData.loc[index, 'ORebAllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'ORebAllowedPerGame']
        inputData.loc[index, 'ORebAllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'ORebAllowedPerGame']

        inputData.loc[index, 'ORebMarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'OReb'] - startOfDaySeasonTotals.loc[teamA, 'ORebAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'ORebMarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'ORebMarginPerGame']
        inputData.loc[index, 'ORebMarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'ORebMarginPerGame']
        inputData.loc[index, 'ORebMarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'ORebMarginPerGame']

        inputData.loc[index, 'DRebPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'DReb'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'DRebPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'DRebPerGame']
        inputData.loc[index, 'DRebPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'DRebPerGame']
        inputData.loc[index, 'DRebPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'DRebPerGame']

        inputData.loc[index, 'DRebAllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'DRebAllowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'DRebAllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'DRebAllowedPerGame']
        inputData.loc[index, 'DRebAllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'DRebAllowedPerGame']
        inputData.loc[index, 'DRebAllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'DRebAllowedPerGame']

        inputData.loc[index, 'DRebMarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'DReb'] - startOfDaySeasonTotals.loc[teamA, 'DRebAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'DRebMarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'DRebMarginPerGame']
        inputData.loc[index, 'DRebMarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'DRebMarginPerGame']
        inputData.loc[index, 'DRebMarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'DRebMarginPerGame']

        inputData.loc[index, 'AstPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'Ast'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'AstPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'AstPerGame']
        inputData.loc[index, 'AstPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'AstPerGame']
        inputData.loc[index, 'AstPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'AstPerGame']

        inputData.loc[index, 'AstAllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'AstAllowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'AstAllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'AstAllowedPerGame']
        inputData.loc[index, 'AstAllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'AstAllowedPerGame']
        inputData.loc[index, 'AstAllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'AstAllowedPerGame']

        inputData.loc[index, 'AstMarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'Ast'] - startOfDaySeasonTotals.loc[teamA, 'AstAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'AstMarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'AstMarginPerGame']
        inputData.loc[index, 'AstMarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'AstMarginPerGame']
        inputData.loc[index, 'AstMarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'AstMarginPerGame']

        inputData.loc[index, 'TOPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'TO'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'TOPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'TOPerGame']
        inputData.loc[index, 'TOPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'TOPerGame']
        inputData.loc[index, 'TOPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'TOPerGame']

        inputData.loc[index, 'TOAllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'TOAllowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'TOAllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'TOAllowedPerGame']
        inputData.loc[index, 'TOAllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'TOAllowedPerGame']
        inputData.loc[index, 'TOAllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'TOAllowedPerGame']

        inputData.loc[index, 'TOMarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'TO'] - startOfDaySeasonTotals.loc[teamA, 'TOAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'TOMarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'TOMarginPerGame']
        inputData.loc[index, 'TOMarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'TOMarginPerGame']
        inputData.loc[index, 'TOMarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'TOMarginPerGame']

        inputData.loc[index, 'AvgAst/TORatioThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'AvgAst/TORatio']
        inputData.loc[index, 'AvgAst/TORatioLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'AvgAst/TORatio']
        inputData.loc[index, 'AvgAst/TORatio2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'AvgAst/TORatio']
        inputData.loc[index, 'AvgAst/TORatio3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'AvgAst/TORatio']

        inputData.loc[index, 'AvgAst/TORatioAllowedThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'AvgAst/TORatioAllowed']
        inputData.loc[index, 'AvgAst/TORatioAllowedLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'AvgAst/TORatioAllowed']
        inputData.loc[index, 'AvgAst/TORatioAllowed2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'AvgAst/TORatioAllowed']
        inputData.loc[index, 'AvgAst/TORatioAllowed3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'AvgAst/TORatioAllowed']

        inputData.loc[index, 'AvgAst/TORatioMarginThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'AvgAst/TORatio'] - startOfDaySeasonTotals.loc[teamA, 'AvgAst/TORatioAllowed']
        inputData.loc[index, 'AvgAst/TORatioMarginLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'AvgAst/TORatioMargin']
        inputData.loc[index, 'AvgAst/TORatioMargin2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'AvgAst/TORatioMargin']
        inputData.loc[index, 'AvgAst/TORatioMargin3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'AvgAst/TORatioMargin']

        inputData.loc[index, 'AvgAst/TORatio(alt)ThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'AvgAst/TORatio(alt)']
        inputData.loc[index, 'AvgAst/TORatio(alt)LastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'AvgAst/TORatio(alt)']
        inputData.loc[index, 'AvgAst/TORatio(alt)2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'AvgAst/TORatio(alt)']
        inputData.loc[index, 'AvgAst/TORatio(alt)3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'AvgAst/TORatio(alt)']

        inputData.loc[index, 'AvgAst/TORatio(alt)AllowedThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'AvgAst/TORatio(alt)Allowed']
        inputData.loc[index, 'AvgAst/TORatio(alt)AllowedLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'AvgAst/TORatio(alt)Allowed']
        inputData.loc[index, 'AvgAst/TORatio(alt)Allowed2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'AvgAst/TORatio(alt)Allowed']
        inputData.loc[index, 'AvgAst/TORatio(alt)Allowed3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'AvgAst/TORatio(alt)Allowed']

        inputData.loc[index, 'AvgAst/TORatio(alt)MarginThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'AvgAst/TORatio(alt)'] - startOfDaySeasonTotals.loc[teamA, 'AvgAst/TORatio(alt)Allowed']
        inputData.loc[index, 'AvgAst/TORatio(alt)MarginLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'AvgAst/TORatio(alt)Margin']
        inputData.loc[index, 'AvgAst/TORatio(alt)Margin2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'AvgAst/TORatio(alt)Margin']
        inputData.loc[index, 'AvgAst/TORatio(alt)Margin3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'AvgAst/TORatio(alt)Margin']

        inputData.loc[index, 'StlPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'Stl'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'StlPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'StlPerGame']
        inputData.loc[index, 'StlPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'StlPerGame']
        inputData.loc[index, 'StlPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'StlPerGame']

        inputData.loc[index, 'StlAllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'StlAllowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'StlAllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'StlAllowedPerGame']
        inputData.loc[index, 'StlAllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'StlAllowedPerGame']
        inputData.loc[index, 'StlAllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'StlAllowedPerGame']

        inputData.loc[index, 'StlMarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'Stl'] - startOfDaySeasonTotals.loc[teamA, 'StlAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'StlMarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'StlMarginPerGame']
        inputData.loc[index, 'StlMarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'StlMarginPerGame']
        inputData.loc[index, 'StlMarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'StlMarginPerGame']

        inputData.loc[index, 'BlkPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'Blk'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'BlkPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'BlkPerGame']
        inputData.loc[index, 'BlkPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'BlkPerGame']
        inputData.loc[index, 'BlkPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'BlkPerGame']

        inputData.loc[index, 'BlkAllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'BlkAllowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'BlkAllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'BlkAllowedPerGame']
        inputData.loc[index, 'BlkAllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'BlkAllowedPerGame']
        inputData.loc[index, 'BlkAllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'BlkAllowedPerGame']

        inputData.loc[index, 'BlkMarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'Blk'] - startOfDaySeasonTotals.loc[teamA, 'BlkAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'BlkMarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'BlkMarginPerGame']
        inputData.loc[index, 'BlkMarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'BlkMarginPerGame']
        inputData.loc[index, 'BlkMarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'BlkMarginPerGame']

        inputData.loc[index, 'PFPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'PF'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'PFPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'PFPerGame']
        inputData.loc[index, 'PFPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'PFPerGame']
        inputData.loc[index, 'PFPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'PFPerGame']

        inputData.loc[index, 'PFAllowedPerGameThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'PFAllowed'] / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'PFAllowedPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'PFAllowedPerGame']
        inputData.loc[index, 'PFAllowedPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'PFAllowedPerGame']
        inputData.loc[index, 'PFAllowedPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'PFAllowedPerGame']

        inputData.loc[index, 'PFMarginPerGameThisSeason A'] = (startOfDaySeasonTotals.loc[teamA, 'PF'] - startOfDaySeasonTotals.loc[teamA, 'PFAllowed']) / startOfDaySeasonTotals.loc[teamA, 'GamesPlayed']
        inputData.loc[index, 'PFMarginPerGameLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'PFMarginPerGame']
        inputData.loc[index, 'PFMarginPerGame2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'PFMarginPerGame']
        inputData.loc[index, 'PFMarginPerGame3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'PFMarginPerGame']

        # strength of schedule

        inputData.loc[index, 'CurrentSoSWeightedAvgOppWinPctThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppWinPctThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppWinPctThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppWinPctThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsWinPct']
        inputData.loc[index, 'CurrentSoSAvgOppWinPctNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Wins'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppWinPctNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Wins'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppWinPctNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Wins'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppWinPctNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Wins'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppWinPctNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppWinPctNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppWinPctNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppWinPctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFlipCloseWinPctThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFlipCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFlipCloseWinPctThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFlipCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFlipCloseWinPctThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFlipCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFlipCloseWinPctThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFlipCloseWinPct']
        inputData.loc[index, 'CurrentSoSAvgOppFlipCloseWinPctNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FlipCloseWins'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFlipCloseWinPctNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FlipCloseWins'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFlipCloseWinPctNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FlipCloseWins'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFlipCloseWinPctNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FlipCloseWins'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFlipCloseWinPctNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFlipCloseWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppFlipCloseWinPctNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFlipCloseWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppFlipCloseWinPctNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFlipCloseWinPctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppWinCloseWinPctThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsWinCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppWinCloseWinPctThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsWinCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppWinCloseWinPctThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsWinCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppWinCloseWinPctThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsWinCloseWinPct']
        inputData.loc[index, 'CurrentSoSAvgOppWinCloseWinPctNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'WinCloseWins'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppWinCloseWinPctNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'WinCloseWins'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppWinCloseWinPctNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'WinCloseWins'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppWinCloseWinPctNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'WinCloseWins'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppWinCloseWinPctNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppWinCloseWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppWinCloseWinPctNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppWinCloseWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppWinCloseWinPctNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppWinCloseWinPctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppLoseCloseWinPctThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsLoseCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppLoseCloseWinPctThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsLoseCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppLoseCloseWinPctThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsLoseCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppLoseCloseWinPctThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsLoseCloseWinPct']
        inputData.loc[index, 'CurrentSoSAvgOppLoseCloseWinPctNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'LoseCloseWins'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppLoseCloseWinPctNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'LoseCloseWins'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppLoseCloseWinPctNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'LoseCloseWins'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppLoseCloseWinPctNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'LoseCloseWins'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppLoseCloseWinPctNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppLoseCloseWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppLoseCloseWinPctNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppLoseCloseWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppLoseCloseWinPctNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppLoseCloseWinPctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppPointsPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsPointsPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsPointsPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsPointsPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsPointsPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppPointsPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Points'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Points'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Points'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Points'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppPointsPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppPointsPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPointsPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppPointsPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPointsPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppPointsPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppPointsAllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsAllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsAllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsAllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppPointsAllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PointsAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsAllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PointsAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsAllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PointsAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsAllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PointsAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppPointsAllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppPointsAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPointsAllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppPointsAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPointsAllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppPointsAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppPointsMarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsPointsPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsMarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsPointsPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsMarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsPointsPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsMarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsPointsPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppPointsMarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Points'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PointsAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsMarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Points'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PointsAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsMarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Points'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PointsAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsMarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Points'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PointsAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppPointsMarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppPointsMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPointsMarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppPointsMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPointsMarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppPointsMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGMPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGMPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGMPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGMPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGMPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGMPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGMPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGMPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGMPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGMPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGMPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGMPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGMAllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMAllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMAllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMAllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGMAllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGMAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMAllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGMAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMAllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGMAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMAllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGMAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGMAllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGMAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGMAllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGMAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGMAllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGMAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGMMarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGMPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMMarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGMPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMMarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGMPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMMarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGMPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGMMarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGMAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMMarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGMAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMMarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGMAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMMarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGMAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGMMarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGMMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGMMarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGMMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGMMarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGMMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGAPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGAPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGAPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGAPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGAPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGAPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGAPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGAPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGAPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGAPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGAPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGAPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGAAllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAAllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAAllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAAllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGAAllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGAAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAAllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGAAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAAllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGAAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAAllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGAAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGAAllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGAAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGAAllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGAAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGAAllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGAAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGAMarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGAPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAMarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGAPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAMarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGAPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAMarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGAPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGAMarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGAAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAMarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGAAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAMarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGAAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAMarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGAAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGAMarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGAMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGAMarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGAMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGAMarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGAMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGPctThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGPct']
        inputData.loc[index, 'CurrentSoSAvgOppFGPctNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGPctNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGPctNow']
        inputData.loc[index, 'PastSoSAvgOppFGPctNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGPctNow']
        inputData.loc[index, 'PastSoSAvgOppFGPctNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGPctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGPctAllowedThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctAllowedThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctAllowedThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctAllowedThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppFGPctAllowedNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGMAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGAAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctAllowedNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGMAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGAAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctAllowedNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGMAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGAAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctAllowedNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGMAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGAAllowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGPctAllowedNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGPctAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppFGPctAllowedNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGPctAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppFGPctAllowedNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGPctAllowedNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGPctMarginThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGPct'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctMarginThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGPct'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctMarginThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGPct'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctMarginThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGPct'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppFGPctMarginNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGPct'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGPctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctMarginNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGPct'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGPctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctMarginNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGPct'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGPctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctMarginNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGPct'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGPctAllowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGPctMarginNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGPctMarginNow']
        inputData.loc[index, 'PastSoSAvgOppFGPctMarginNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGPctMarginNow']
        inputData.loc[index, 'PastSoSAvgOppFGPctMarginNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGPctMarginNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGM3PerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGM3PerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3PerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGM3PerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3PerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGM3PerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3PerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGM3PerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGM3PerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3PerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3PerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3PerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGM3PerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGM3PerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGM3PerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGM3PerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGM3PerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGM3PerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGM3AllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3AllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3AllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3AllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGM3AllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3Allowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3AllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3Allowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3AllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3Allowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3AllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3Allowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGM3AllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGM3AllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGM3AllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGM3AllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGM3AllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGM3AllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGM3MarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGM3PerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3MarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGM3PerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3MarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGM3PerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3MarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGM3PerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGM3MarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3Allowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3MarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3Allowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3MarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3Allowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3MarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3Allowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGM3MarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGM3MarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGM3MarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGM3MarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGM3MarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGM3MarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGA3PerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGA3PerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3PerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGA3PerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3PerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGA3PerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3PerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGA3PerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGA3PerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3PerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3PerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3PerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGA3PerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGA3PerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGA3PerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGA3PerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGA3PerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGA3PerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGA3AllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3AllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3AllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3AllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGA3AllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3Allowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3AllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3Allowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3AllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3Allowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3AllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3Allowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGA3AllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGA3AllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGA3AllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGA3AllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGA3AllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGA3AllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGA3MarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGA3PerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3MarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGA3PerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3MarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGA3PerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3MarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGA3PerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGA3MarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3Allowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3MarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3Allowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3MarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3Allowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3MarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3Allowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGA3MarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFGA3MarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGA3MarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFGA3MarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGA3MarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFGA3MarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFG3PctThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFG3Pct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFG3Pct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFG3Pct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFG3Pct']
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3']).mean()
        inputData.loc[index, 'PastSoSAvgOppFG3PctNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFG3PctNow']
        inputData.loc[index, 'PastSoSAvgOppFG3PctNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFG3PctNow']
        inputData.loc[index, 'PastSoSAvgOppFG3PctNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFG3PctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFG3PctAllowedThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctAllowedThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctAllowedThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctAllowedThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctAllowedNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3Allowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3Allowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctAllowedNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3Allowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3Allowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctAllowedNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3Allowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3Allowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctAllowedNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGM3Allowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FGA3Allowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFG3PctAllowedNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFG3PctAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppFG3PctAllowedNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFG3PctAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppFG3PctAllowedNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFG3PctAllowedNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFG3PctMarginThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFG3Pct'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctMarginThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFG3Pct'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctMarginThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFG3Pct'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctMarginThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFG3Pct'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctMarginNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FG3Pct'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FG3PctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctMarginNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FG3Pct'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FG3PctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctMarginNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FG3Pct'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FG3PctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctMarginNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FG3Pct'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FG3PctAllowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFG3PctMarginNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFG3PctMarginNow']
        inputData.loc[index, 'PastSoSAvgOppFG3PctMarginNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFG3PctMarginNow']
        inputData.loc[index, 'PastSoSAvgOppFG3PctMarginNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFG3PctMarginNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTMPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFTMPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFTMPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFTMPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFTMPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFTMPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTM'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTM'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTM'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTM'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTMPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFTMPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTMPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFTMPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTMPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFTMPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTMAllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMAllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMAllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMAllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFTMAllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTMAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMAllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTMAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMAllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTMAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMAllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTMAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTMAllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFTMAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTMAllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFTMAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTMAllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFTMAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTMMarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFTMPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMMarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFTMPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMMarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFTMPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMMarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFTMPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFTMMarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTM'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTMAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMMarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTM'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTMAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMMarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTM'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTMAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMMarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTM'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTMAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTMMarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFTMMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTMMarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFTMMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTMMarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFTMMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTAPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFTAPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFTAPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFTAPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFTAPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFTAPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTA'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTA'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTA'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTA'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTAPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFTAPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTAPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFTAPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTAPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFTAPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTAAllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAAllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAAllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAAllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFTAAllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTAAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAAllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTAAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAAllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTAAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAAllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTAAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTAAllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFTAAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTAAllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFTAAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTAAllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFTAAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTAMarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFTAPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAMarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFTAPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAMarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFTAPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAMarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFTAPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFTAMarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTA'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTAAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAMarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTA'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTAAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAMarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTA'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTAAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAMarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTA'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTAAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTAMarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFTAMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTAMarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFTAMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTAMarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFTAMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTPctThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFTPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFTPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFTPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFTPct']
        inputData.loc[index, 'CurrentSoSAvgOppFTPctNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTM'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTA']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTM'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTA']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTM'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTA']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTM'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTA']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTPctNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFTPctNow']
        inputData.loc[index, 'PastSoSAvgOppFTPctNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFTPctNow']
        inputData.loc[index, 'PastSoSAvgOppFTPctNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFTPctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTPctAllowedThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctAllowedThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctAllowedThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctAllowedThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppFTPctAllowedNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTMAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTAAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctAllowedNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTMAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTAAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctAllowedNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTMAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTAAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctAllowedNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTMAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTAAllowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTPctAllowedNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFTPctAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppFTPctAllowedNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFTPctAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppFTPctAllowedNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFTPctAllowedNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTPctMarginThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFTPct'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctMarginThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFTPct'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctMarginThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFTPct'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctMarginThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFTPct'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppFTPctMarginNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTPct'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTPctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctMarginNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTPct'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTPctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctMarginNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTPct'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTPctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctMarginNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTPct'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'FTPctAllowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTPctMarginNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppFTPctMarginNow']
        inputData.loc[index, 'PastSoSAvgOppFTPctMarginNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppFTPctMarginNow']
        inputData.loc[index, 'PastSoSAvgOppFTPctMarginNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppFTPctMarginNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppRebPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame'] + startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame'] + seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame'] + seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame'] + seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppRebPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] + startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] + seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] + seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] + seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppRebPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppRebPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppRebPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppRebPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppRebPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppRebPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppRebAllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] + startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebAllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] + seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebAllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] + seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebAllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] + seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppRebAllowedPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed'] + startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebAllowedPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed'] + seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebAllowedPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed'] + seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebAllowedPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed'] + seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppRebAllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppRebAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppRebAllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppRebAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppRebAllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppRebAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppRebMarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame'] + startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebMarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame'] + seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebMarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame'] + seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebMarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame'] + seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppRebMarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] + startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebMarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] + seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebMarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] + seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebMarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] + seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppRebMarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppRebMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppRebMarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppRebMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppRebMarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppRebMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppORebPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppORebPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppORebPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppORebPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppORebPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppORebPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppORebPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppORebPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppORebAllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebAllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebAllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebAllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppORebAllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebAllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebAllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebAllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppORebAllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppORebAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppORebAllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppORebAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppORebAllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppORebAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppORebMarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebMarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebMarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebMarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsORebPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppORebMarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebMarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebMarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebMarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'OReb'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'ORebAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppORebMarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppORebMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppORebMarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppORebMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppORebMarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppORebMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppDRebPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppDRebPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppDRebPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppDRebPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppDRebPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppDRebPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppDRebPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppDRebPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppDRebAllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebAllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebAllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebAllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppDRebAllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebAllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebAllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebAllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppDRebAllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppDRebAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppDRebAllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppDRebAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppDRebAllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppDRebAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppDRebMarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebMarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebMarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebMarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsDRebPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppDRebMarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebMarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebMarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebMarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DReb'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppDRebMarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppDRebMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppDRebMarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppDRebMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppDRebMarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppDRebMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAstPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsAstPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsAstPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsAstPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsAstPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppAstPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Ast'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Ast'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Ast'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Ast'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppAstPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppAstPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppAstPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppAstPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppAstPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppAstPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAstAllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstAllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstAllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstAllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppAstAllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AstAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstAllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AstAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstAllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AstAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstAllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AstAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppAstAllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppAstAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppAstAllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppAstAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppAstAllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppAstAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAstMarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsAstPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstMarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsAstPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstMarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsAstPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstMarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsAstPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppAstMarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Ast'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AstAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstMarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Ast'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AstAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstMarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Ast'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AstAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstMarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Ast'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AstAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppAstMarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppAstMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppAstMarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppAstMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppAstMarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppAstMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppTOPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsTOPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsTOPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsTOPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsTOPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppTOPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TO'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TO'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TO'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TO'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppTOPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppTOPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppTOPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppTOPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppTOPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppTOPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppTOAllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOAllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOAllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOAllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppTOAllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TOAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOAllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TOAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOAllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TOAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOAllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TOAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppTOAllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppTOAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppTOAllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppTOAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppTOAllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppTOAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppTOMarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsTOPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOMarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsTOPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOMarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsTOPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOMarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsTOPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppTOMarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TO'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TOAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOMarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TO'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TOAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOMarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TO'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TOAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOMarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TO'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'TOAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppTOMarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppTOMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppTOMarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppTOMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppTOMarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppTOMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAvgAst/TORatioThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio']
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioNowThisSeason A'] = startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioNowLastSeason A'] = seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio'].mean()
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppAvgAst/TORatioNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppAvgAst/TORatioNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppAvgAst/TORatioNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAvgAst/TORatioAllowedThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioAllowedThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioAllowedThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioAllowedThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioAllowedNowThisSeason A'] = startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioAllowedNowLastSeason A'] = seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioAllowedNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioAllowedNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed'].mean()
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioAllowedNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppAvgAst/TORatioAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioAllowedNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppAvgAst/TORatioAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioAllowedNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppAvgAst/TORatioAllowedNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAvgAst/TORatioMarginThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioMarginThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioMarginThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioMarginThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioMarginNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioMarginNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioMarginNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioMarginNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioMarginNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppAvgAst/TORatioMarginNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioMarginNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppAvgAst/TORatioMarginNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioMarginNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppAvgAst/TORatioMarginNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAvgAst/TORatio(alt)ThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)ThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)Then2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)Then3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)']
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)NowThisSeason A'] = startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)NowLastSeason A'] = seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)Now2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)Now3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'].mean()
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)NowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppAvgAst/TORatio(alt)Now']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)Now2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppAvgAst/TORatio(alt)Now']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)Now3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppAvgAst/TORatio(alt)Now']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNowThisSeason A'] = startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNowLastSeason A'] = seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed'].mean()
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)AllowedNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppAvgAst/TORatio(alt)AllowedNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)AllowedNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppAvgAst/TORatio(alt)AllowedNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)AllowedNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppAvgAst/TORatio(alt)AllowedNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)MarginNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppAvgAst/TORatio(alt)MarginNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)MarginNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppAvgAst/TORatio(alt)MarginNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)MarginNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppAvgAst/TORatio(alt)MarginNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppStlPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsStlPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsStlPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsStlPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsStlPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppStlPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Stl'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Stl'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Stl'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Stl'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppStlPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppStlPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppStlPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppStlPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppStlPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppStlPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppStlAllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlAllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlAllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlAllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppStlAllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'StlAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlAllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'StlAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlAllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'StlAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlAllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'StlAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppStlAllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppStlAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppStlAllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppStlAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppStlAllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppStlAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppStlMarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsStlPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlMarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsStlPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlMarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsStlPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlMarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsStlPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppStlMarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Stl'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'StlAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlMarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Stl'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'StlAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlMarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Stl'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'StlAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlMarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Stl'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'StlAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppStlMarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppStlMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppStlMarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppStlMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppStlMarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppStlMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppBlkPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsBlkPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsBlkPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsBlkPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsBlkPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppBlkPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Blk'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Blk'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Blk'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Blk'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppBlkPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppBlkPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppBlkPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppBlkPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppBlkPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppBlkPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppBlkAllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkAllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkAllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkAllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppBlkAllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'BlkAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkAllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'BlkAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkAllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'BlkAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkAllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'BlkAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppBlkAllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppBlkAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppBlkAllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppBlkAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppBlkAllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppBlkAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppBlkMarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsBlkPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkMarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsBlkPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkMarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsBlkPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkMarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsBlkPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppBlkMarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Blk'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'BlkAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkMarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Blk'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'BlkAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkMarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Blk'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'BlkAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkMarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'Blk'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'BlkAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppBlkMarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppBlkMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppBlkMarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppBlkMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppBlkMarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppBlkMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppPFPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsPFPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsPFPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsPFPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsPFPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppPFPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PF'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PF'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PF'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PF'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppPFPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppPFPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPFPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppPFPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPFPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppPFPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppPFAllowedPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFAllowedPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFAllowedPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFAllowedPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppPFAllowedPerGameNowThisSeason A'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PFAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFAllowedPerGameNowLastSeason A'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PFAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFAllowedPerGameNow2SeasonsAgo A'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PFAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFAllowedPerGameNow3SeasonsAgo A'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PFAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppPFAllowedPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppPFAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPFAllowedPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppPFAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPFAllowedPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppPFAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppPFMarginPerGameThenThisSeason A'] = startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsPFPerGame'] - startOfDaySeasonTotals.loc[teamA, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFMarginPerGameThenLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsPFPerGame'] - seasonTotalsDict[season - 1].loc[teamA, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFMarginPerGameThen2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsPFPerGame'] - seasonTotalsDict[season - 2].loc[teamA, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFMarginPerGameThen3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsPFPerGame'] - seasonTotalsDict[season - 3].loc[teamA, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppPFMarginPerGameNowThisSeason A'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PF'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PFAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFMarginPerGameNowLastSeason A'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PF'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PFAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFMarginPerGameNow2SeasonsAgo A'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PF'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PFAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFMarginPerGameNow3SeasonsAgo A'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PF'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'PFAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamA, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppPFMarginPerGameNowLastSeason A'] = seasonTotalsDict[season - 1].loc[teamA, 'SoSAvgOppPFMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPFMarginPerGameNow2SeasonsAgo A'] = seasonTotalsDict[season - 2].loc[teamA, 'SoSAvgOppPFMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPFMarginPerGameNow3SeasonsAgo A'] = seasonTotalsDict[season - 3].loc[teamA, 'SoSAvgOppPFMarginPerGameNow']

        # Team B's features

        inputData.loc[index, 'NumGamesPlayedThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']

        inputData.loc[index, 'WinPctThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'Wins'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'WinPctLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'WinPct']
        inputData.loc[index, 'WinPct2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'WinPct']
        inputData.loc[index, 'WinPct3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'WinPct']

        inputData.loc[index, 'FlipCloseWinPctThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FlipCloseWins'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FlipCloseWinPctLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FlipCloseWinPct']
        inputData.loc[index, 'FlipCloseWinPct2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FlipCloseWinPct']
        inputData.loc[index, 'FlipCloseWinPct3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FlipCloseWinPct']

        inputData.loc[index, 'WinCloseWinPctThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'WinCloseWins'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'WinCloseWinPctLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'WinCloseWinPct']
        inputData.loc[index, 'WinCloseWinPct2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'WinCloseWinPct']
        inputData.loc[index, 'WinCloseWinPct3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'WinCloseWinPct']

        inputData.loc[index, 'LoseCloseWinPctThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'LoseCloseWins'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'LoseCloseWinPctLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'LoseCloseWinPct']
        inputData.loc[index, 'LoseCloseWinPct2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'LoseCloseWinPct']
        inputData.loc[index, 'LoseCloseWinPct3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'LoseCloseWinPct']

        inputData.loc[index, 'PointsPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'Points'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'PointsPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'PointsPerGame']
        inputData.loc[index, 'PointsPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'PointsPerGame']
        inputData.loc[index, 'PointsPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'PointsPerGame']

        inputData.loc[index, 'PointsAllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'PointsAllowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'PointsAllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'PointsAllowedPerGame']
        inputData.loc[index, 'PointsAllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'PointsAllowedPerGame']
        inputData.loc[index, 'PointsAllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'PointsAllowedPerGame']

        inputData.loc[index, 'PointsMarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'Points'] - startOfDaySeasonTotals.loc[teamB, 'PointsAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'PointsMarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'PointsMarginPerGame']
        inputData.loc[index, 'PointsMarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'PointsMarginPerGame']
        inputData.loc[index, 'PointsMarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'PointsMarginPerGame']

        inputData.loc[index, 'FGMPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGM'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FGMPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGMPerGame']
        inputData.loc[index, 'FGMPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGMPerGame']
        inputData.loc[index, 'FGMPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGMPerGame']

        inputData.loc[index, 'FGMAllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGMAllowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FGMAllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGMAllowedPerGame']
        inputData.loc[index, 'FGMAllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGMAllowedPerGame']
        inputData.loc[index, 'FGMAllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGMAllowedPerGame']

        inputData.loc[index, 'FGMMarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'FGM'] - startOfDaySeasonTotals.loc[teamB, 'FGMAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FGMMarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGMMarginPerGame']
        inputData.loc[index, 'FGMMarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGMMarginPerGame']
        inputData.loc[index, 'FGMMarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGMMarginPerGame']

        inputData.loc[index, 'FGAPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGA'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FGAPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGAPerGame']
        inputData.loc[index, 'FGAPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGAPerGame']
        inputData.loc[index, 'FGAPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGAPerGame']

        inputData.loc[index, 'FGAAllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGAAllowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FGAAllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGAAllowedPerGame']
        inputData.loc[index, 'FGAAllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGAAllowedPerGame']
        inputData.loc[index, 'FGAAllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGAAllowedPerGame']

        inputData.loc[index, 'FGAMarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'FGA'] - startOfDaySeasonTotals.loc[teamB, 'FGAAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FGAMarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGAMarginPerGame']
        inputData.loc[index, 'FGAMarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGAMarginPerGame']
        inputData.loc[index, 'FGAMarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGAMarginPerGame']

        inputData.loc[index, 'FGPctThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGM'] / startOfDaySeasonTotals.loc[teamB, 'FGA']
        inputData.loc[index, 'FGPctLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGPct']
        inputData.loc[index, 'FGPct2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGPct']
        inputData.loc[index, 'FGPct3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGPct']

        inputData.loc[index, 'FGPctAllowedThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGMAllowed'] / startOfDaySeasonTotals.loc[teamB, 'FGAAllowed']
        inputData.loc[index, 'FGPctAllowedLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGPctAllowed']
        inputData.loc[index, 'FGPctAllowed2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGPctAllowed']
        inputData.loc[index, 'FGPctAllowed3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGPctAllowed']

        inputData.loc[index, 'FGPctMarginThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGM'] / startOfDaySeasonTotals.loc[teamB, 'FGA'] - startOfDaySeasonTotals.loc[teamB, 'FGMAllowed'] / startOfDaySeasonTotals.loc[teamB, 'FGAAllowed']
        inputData.loc[index, 'FGPctMarginLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGPctMargin']
        inputData.loc[index, 'FGPctMargin2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGPctMargin']
        inputData.loc[index, 'FGPctMargin3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGPctMargin']

        inputData.loc[index, 'FGM3PerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGM3'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FGM3PerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGM3PerGame']
        inputData.loc[index, 'FGM3PerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGM3PerGame']
        inputData.loc[index, 'FGM3PerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGM3PerGame']

        inputData.loc[index, 'FGM3AllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGM3Allowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FGM3AllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGM3AllowedPerGame']
        inputData.loc[index, 'FGM3AllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGM3AllowedPerGame']
        inputData.loc[index, 'FGM3AllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGM3AllowedPerGame']

        inputData.loc[index, 'FGM3MarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'FGM3'] - startOfDaySeasonTotals.loc[teamB, 'FGM3Allowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FGM3MarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGM3MarginPerGame']
        inputData.loc[index, 'FGM3MarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGM3MarginPerGame']
        inputData.loc[index, 'FGM3MarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGM3MarginPerGame']

        inputData.loc[index, 'FGA3PerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGA3'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FGA3PerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGA3PerGame']
        inputData.loc[index, 'FGA3PerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGA3PerGame']
        inputData.loc[index, 'FGA3PerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGA3PerGame']

        inputData.loc[index, 'FGA3AllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGA3Allowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FGA3AllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGA3AllowedPerGame']
        inputData.loc[index, 'FGA3AllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGA3AllowedPerGame']
        inputData.loc[index, 'FGA3AllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGA3AllowedPerGame']

        inputData.loc[index, 'FGA3MarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'FGA3'] - startOfDaySeasonTotals.loc[teamB, 'FGA3Allowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FGA3MarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FGA3MarginPerGame']
        inputData.loc[index, 'FGA3MarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FGA3MarginPerGame']
        inputData.loc[index, 'FGA3MarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FGA3MarginPerGame']

        inputData.loc[index, 'FG3PctThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGM3'] / startOfDaySeasonTotals.loc[teamB, 'FGA3']
        inputData.loc[index, 'FG3PctLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FG3Pct']
        inputData.loc[index, 'FG3Pct2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FG3Pct']
        inputData.loc[index, 'FG3Pct3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FG3Pct']

        inputData.loc[index, 'FG3PctAllowedThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGM3Allowed'] / startOfDaySeasonTotals.loc[teamB, 'FGA3Allowed']
        inputData.loc[index, 'FG3PctAllowedLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FG3PctAllowed']
        inputData.loc[index, 'FG3PctAllowed2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FG3PctAllowed']
        inputData.loc[index, 'FG3PctAllowed3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FG3PctAllowed']

        inputData.loc[index, 'FG3PctMarginThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FGM3'] / startOfDaySeasonTotals.loc[teamB, 'FGA3'] - startOfDaySeasonTotals.loc[teamB, 'FGM3Allowed'] / startOfDaySeasonTotals.loc[teamB, 'FGA3Allowed']
        inputData.loc[index, 'FG3PctMarginLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FG3PctMargin']
        inputData.loc[index, 'FG3PctMargin2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FG3PctMargin']
        inputData.loc[index, 'FG3PctMargin3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FG3PctMargin']

        inputData.loc[index, 'FTMPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FTM'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FTMPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FTMPerGame']
        inputData.loc[index, 'FTMPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FTMPerGame']
        inputData.loc[index, 'FTMPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FTMPerGame']

        inputData.loc[index, 'FTMAllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FTMAllowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FTMAllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FTMAllowedPerGame']
        inputData.loc[index, 'FTMAllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FTMAllowedPerGame']
        inputData.loc[index, 'FTMAllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FTMAllowedPerGame']

        inputData.loc[index, 'FTMMarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'FTM'] - startOfDaySeasonTotals.loc[teamB, 'FTMAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FTMMarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FTMMarginPerGame']
        inputData.loc[index, 'FTMMarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FTMMarginPerGame']
        inputData.loc[index, 'FTMMarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FTMMarginPerGame']

        inputData.loc[index, 'FTAPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FTA'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FTAPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FTAPerGame']
        inputData.loc[index, 'FTAPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FTAPerGame']
        inputData.loc[index, 'FTAPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FTAPerGame']

        inputData.loc[index, 'FTAAllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FTAAllowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FTAAllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FTAAllowedPerGame']
        inputData.loc[index, 'FTAAllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FTAAllowedPerGame']
        inputData.loc[index, 'FTAAllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FTAAllowedPerGame']

        inputData.loc[index, 'FTAMarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'FTA'] - startOfDaySeasonTotals.loc[teamB, 'FTAAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'FTAMarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FTAMarginPerGame']
        inputData.loc[index, 'FTAMarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FTAMarginPerGame']
        inputData.loc[index, 'FTAMarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FTAMarginPerGame']

        inputData.loc[index, 'FTPctThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FTM'] / startOfDaySeasonTotals.loc[teamB, 'FTA']
        inputData.loc[index, 'FTPctLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FTPct']
        inputData.loc[index, 'FTPct2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FTPct']
        inputData.loc[index, 'FTPct3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FTPct']

        inputData.loc[index, 'FTPctAllowedThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FTMAllowed'] / startOfDaySeasonTotals.loc[teamB, 'FTAAllowed']
        inputData.loc[index, 'FTPctAllowedLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FTPctAllowed']
        inputData.loc[index, 'FTPctAllowed2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FTPctAllowed']
        inputData.loc[index, 'FTPctAllowed3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FTPctAllowed']

        inputData.loc[index, 'FTPctMarginThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'FTM'] / startOfDaySeasonTotals.loc[teamB, 'FTA'] - startOfDaySeasonTotals.loc[teamB, 'FTMAllowed'] / startOfDaySeasonTotals.loc[teamB, 'FTAAllowed']
        inputData.loc[index, 'FTPctMarginLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'FTPctMargin']
        inputData.loc[index, 'FTPctMargin2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'FTPctMargin']
        inputData.loc[index, 'FTPctMargin3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'FTPctMargin']

        inputData.loc[index, 'RebPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'OReb'] + startOfDaySeasonTotals.loc[teamB, 'DReb']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'RebPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'RebPerGame']
        inputData.loc[index, 'RebPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'RebPerGame']
        inputData.loc[index, 'RebPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'RebPerGame']

        inputData.loc[index, 'RebAllowedPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'ORebAllowed'] + startOfDaySeasonTotals.loc[teamB, 'DRebAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'RebAllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'RebAllowedPerGame']
        inputData.loc[index, 'RebAllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'RebAllowedPerGame']
        inputData.loc[index, 'RebAllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'RebAllowedPerGame']

        inputData.loc[index, 'RebMarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'OReb'] + startOfDaySeasonTotals.loc[teamB, 'DReb'] - startOfDaySeasonTotals.loc[teamB, 'ORebAllowed'] - startOfDaySeasonTotals.loc[teamB, 'DRebAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'RebMarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'RebMarginPerGame']
        inputData.loc[index, 'RebMarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'RebMarginPerGame']
        inputData.loc[index, 'RebMarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'RebMarginPerGame']

        inputData.loc[index, 'ORebPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'OReb'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'ORebPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'ORebPerGame']
        inputData.loc[index, 'ORebPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'ORebPerGame']
        inputData.loc[index, 'ORebPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'ORebPerGame']

        inputData.loc[index, 'ORebAllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'ORebAllowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'ORebAllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'ORebAllowedPerGame']
        inputData.loc[index, 'ORebAllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'ORebAllowedPerGame']
        inputData.loc[index, 'ORebAllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'ORebAllowedPerGame']

        inputData.loc[index, 'ORebMarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'OReb'] - startOfDaySeasonTotals.loc[teamB, 'ORebAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'ORebMarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'ORebMarginPerGame']
        inputData.loc[index, 'ORebMarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'ORebMarginPerGame']
        inputData.loc[index, 'ORebMarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'ORebMarginPerGame']

        inputData.loc[index, 'DRebPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'DReb'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'DRebPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'DRebPerGame']
        inputData.loc[index, 'DRebPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'DRebPerGame']
        inputData.loc[index, 'DRebPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'DRebPerGame']

        inputData.loc[index, 'DRebAllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'DRebAllowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'DRebAllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'DRebAllowedPerGame']
        inputData.loc[index, 'DRebAllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'DRebAllowedPerGame']
        inputData.loc[index, 'DRebAllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'DRebAllowedPerGame']

        inputData.loc[index, 'DRebMarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'DReb'] - startOfDaySeasonTotals.loc[teamB, 'DRebAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'DRebMarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'DRebMarginPerGame']
        inputData.loc[index, 'DRebMarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'DRebMarginPerGame']
        inputData.loc[index, 'DRebMarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'DRebMarginPerGame']

        inputData.loc[index, 'AstPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'Ast'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'AstPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'AstPerGame']
        inputData.loc[index, 'AstPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'AstPerGame']
        inputData.loc[index, 'AstPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'AstPerGame']

        inputData.loc[index, 'AstAllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'AstAllowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'AstAllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'AstAllowedPerGame']
        inputData.loc[index, 'AstAllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'AstAllowedPerGame']
        inputData.loc[index, 'AstAllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'AstAllowedPerGame']

        inputData.loc[index, 'AstMarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'Ast'] - startOfDaySeasonTotals.loc[teamB, 'AstAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'AstMarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'AstMarginPerGame']
        inputData.loc[index, 'AstMarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'AstMarginPerGame']
        inputData.loc[index, 'AstMarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'AstMarginPerGame']

        inputData.loc[index, 'TOPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'TO'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'TOPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'TOPerGame']
        inputData.loc[index, 'TOPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'TOPerGame']
        inputData.loc[index, 'TOPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'TOPerGame']

        inputData.loc[index, 'TOAllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'TOAllowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'TOAllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'TOAllowedPerGame']
        inputData.loc[index, 'TOAllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'TOAllowedPerGame']
        inputData.loc[index, 'TOAllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'TOAllowedPerGame']

        inputData.loc[index, 'TOMarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'TO'] - startOfDaySeasonTotals.loc[teamB, 'TOAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'TOMarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'TOMarginPerGame']
        inputData.loc[index, 'TOMarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'TOMarginPerGame']
        inputData.loc[index, 'TOMarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'TOMarginPerGame']

        inputData.loc[index, 'AvgAst/TORatioThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'AvgAst/TORatio']
        inputData.loc[index, 'AvgAst/TORatioLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'AvgAst/TORatio']
        inputData.loc[index, 'AvgAst/TORatio2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'AvgAst/TORatio']
        inputData.loc[index, 'AvgAst/TORatio3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'AvgAst/TORatio']

        inputData.loc[index, 'AvgAst/TORatioAllowedThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'AvgAst/TORatioAllowed']
        inputData.loc[index, 'AvgAst/TORatioAllowedLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'AvgAst/TORatioAllowed']
        inputData.loc[index, 'AvgAst/TORatioAllowed2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'AvgAst/TORatioAllowed']
        inputData.loc[index, 'AvgAst/TORatioAllowed3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'AvgAst/TORatioAllowed']

        inputData.loc[index, 'AvgAst/TORatioMarginThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'AvgAst/TORatio'] - startOfDaySeasonTotals.loc[teamB, 'AvgAst/TORatioAllowed']
        inputData.loc[index, 'AvgAst/TORatioMarginLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'AvgAst/TORatioMargin']
        inputData.loc[index, 'AvgAst/TORatioMargin2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'AvgAst/TORatioMargin']
        inputData.loc[index, 'AvgAst/TORatioMargin3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'AvgAst/TORatioMargin']

        inputData.loc[index, 'AvgAst/TORatio(alt)ThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'AvgAst/TORatio(alt)']
        inputData.loc[index, 'AvgAst/TORatio(alt)LastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'AvgAst/TORatio(alt)']
        inputData.loc[index, 'AvgAst/TORatio(alt)2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'AvgAst/TORatio(alt)']
        inputData.loc[index, 'AvgAst/TORatio(alt)3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'AvgAst/TORatio(alt)']

        inputData.loc[index, 'AvgAst/TORatio(alt)AllowedThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'AvgAst/TORatio(alt)Allowed']
        inputData.loc[index, 'AvgAst/TORatio(alt)AllowedLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'AvgAst/TORatio(alt)Allowed']
        inputData.loc[index, 'AvgAst/TORatio(alt)Allowed2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'AvgAst/TORatio(alt)Allowed']
        inputData.loc[index, 'AvgAst/TORatio(alt)Allowed3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'AvgAst/TORatio(alt)Allowed']

        inputData.loc[index, 'AvgAst/TORatio(alt)MarginThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'AvgAst/TORatio(alt)'] - startOfDaySeasonTotals.loc[teamB, 'AvgAst/TORatio(alt)Allowed']
        inputData.loc[index, 'AvgAst/TORatio(alt)MarginLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'AvgAst/TORatio(alt)Margin']
        inputData.loc[index, 'AvgAst/TORatio(alt)Margin2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'AvgAst/TORatio(alt)Margin']
        inputData.loc[index, 'AvgAst/TORatio(alt)Margin3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'AvgAst/TORatio(alt)Margin']

        inputData.loc[index, 'StlPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'Stl'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'StlPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'StlPerGame']
        inputData.loc[index, 'StlPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'StlPerGame']
        inputData.loc[index, 'StlPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'StlPerGame']

        inputData.loc[index, 'StlAllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'StlAllowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'StlAllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'StlAllowedPerGame']
        inputData.loc[index, 'StlAllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'StlAllowedPerGame']
        inputData.loc[index, 'StlAllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'StlAllowedPerGame']

        inputData.loc[index, 'StlMarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'Stl'] - startOfDaySeasonTotals.loc[teamB, 'StlAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'StlMarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'StlMarginPerGame']
        inputData.loc[index, 'StlMarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'StlMarginPerGame']
        inputData.loc[index, 'StlMarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'StlMarginPerGame']

        inputData.loc[index, 'BlkPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'Blk'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'BlkPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'BlkPerGame']
        inputData.loc[index, 'BlkPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'BlkPerGame']
        inputData.loc[index, 'BlkPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'BlkPerGame']

        inputData.loc[index, 'BlkAllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'BlkAllowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'BlkAllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'BlkAllowedPerGame']
        inputData.loc[index, 'BlkAllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'BlkAllowedPerGame']
        inputData.loc[index, 'BlkAllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'BlkAllowedPerGame']

        inputData.loc[index, 'BlkMarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'Blk'] - startOfDaySeasonTotals.loc[teamB, 'BlkAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'BlkMarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'BlkMarginPerGame']
        inputData.loc[index, 'BlkMarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'BlkMarginPerGame']
        inputData.loc[index, 'BlkMarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'BlkMarginPerGame']

        inputData.loc[index, 'PFPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'PF'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'PFPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'PFPerGame']
        inputData.loc[index, 'PFPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'PFPerGame']
        inputData.loc[index, 'PFPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'PFPerGame']

        inputData.loc[index, 'PFAllowedPerGameThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'PFAllowed'] / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'PFAllowedPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'PFAllowedPerGame']
        inputData.loc[index, 'PFAllowedPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'PFAllowedPerGame']
        inputData.loc[index, 'PFAllowedPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'PFAllowedPerGame']

        inputData.loc[index, 'PFMarginPerGameThisSeason B'] = (startOfDaySeasonTotals.loc[teamB, 'PF'] - startOfDaySeasonTotals.loc[teamB, 'PFAllowed']) / startOfDaySeasonTotals.loc[teamB, 'GamesPlayed']
        inputData.loc[index, 'PFMarginPerGameLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'PFMarginPerGame']
        inputData.loc[index, 'PFMarginPerGame2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'PFMarginPerGame']
        inputData.loc[index, 'PFMarginPerGame3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'PFMarginPerGame']

        # strength of schedule

        inputData.loc[index, 'CurrentSoSWeightedAvgOppWinPctThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppWinPctThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppWinPctThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppWinPctThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsWinPct']
        inputData.loc[index, 'CurrentSoSAvgOppWinPctNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Wins'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppWinPctNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Wins'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppWinPctNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Wins'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppWinPctNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Wins'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppWinPctNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppWinPctNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppWinPctNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppWinPctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFlipCloseWinPctThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFlipCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFlipCloseWinPctThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFlipCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFlipCloseWinPctThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFlipCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFlipCloseWinPctThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFlipCloseWinPct']
        inputData.loc[index, 'CurrentSoSAvgOppFlipCloseWinPctNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FlipCloseWins'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFlipCloseWinPctNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FlipCloseWins'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFlipCloseWinPctNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FlipCloseWins'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFlipCloseWinPctNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FlipCloseWins'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFlipCloseWinPctNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFlipCloseWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppFlipCloseWinPctNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFlipCloseWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppFlipCloseWinPctNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFlipCloseWinPctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppWinCloseWinPctThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsWinCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppWinCloseWinPctThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsWinCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppWinCloseWinPctThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsWinCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppWinCloseWinPctThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsWinCloseWinPct']
        inputData.loc[index, 'CurrentSoSAvgOppWinCloseWinPctNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'WinCloseWins'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppWinCloseWinPctNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'WinCloseWins'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppWinCloseWinPctNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'WinCloseWins'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppWinCloseWinPctNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'WinCloseWins'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppWinCloseWinPctNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppWinCloseWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppWinCloseWinPctNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppWinCloseWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppWinCloseWinPctNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppWinCloseWinPctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppLoseCloseWinPctThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsLoseCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppLoseCloseWinPctThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsLoseCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppLoseCloseWinPctThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsLoseCloseWinPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppLoseCloseWinPctThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsLoseCloseWinPct']
        inputData.loc[index, 'CurrentSoSAvgOppLoseCloseWinPctNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'LoseCloseWins'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppLoseCloseWinPctNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'LoseCloseWins'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppLoseCloseWinPctNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'LoseCloseWins'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppLoseCloseWinPctNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'LoseCloseWins'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppLoseCloseWinPctNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppLoseCloseWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppLoseCloseWinPctNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppLoseCloseWinPctNow']
        inputData.loc[index, 'PastSoSAvgOppLoseCloseWinPctNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppLoseCloseWinPctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppPointsPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsPointsPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsPointsPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsPointsPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsPointsPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppPointsPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Points'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Points'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Points'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Points'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppPointsPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppPointsPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPointsPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppPointsPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPointsPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppPointsPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppPointsAllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsAllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsAllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsAllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppPointsAllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PointsAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsAllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PointsAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsAllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PointsAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsAllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PointsAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppPointsAllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppPointsAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPointsAllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppPointsAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPointsAllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppPointsAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppPointsMarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsPointsPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsMarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsPointsPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsMarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsPointsPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPointsMarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsPointsPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsPointsAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppPointsMarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Points'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PointsAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsMarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Points'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PointsAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsMarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Points'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PointsAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPointsMarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Points'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PointsAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppPointsMarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppPointsMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPointsMarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppPointsMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPointsMarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppPointsMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGMPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGMPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGMPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGMPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGMPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGMPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGMPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGMPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGMPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGMPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGMPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGMPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGMAllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMAllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMAllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMAllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGMAllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGMAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMAllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGMAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMAllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGMAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMAllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGMAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGMAllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGMAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGMAllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGMAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGMAllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGMAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGMMarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGMPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMMarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGMPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMMarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGMPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGMMarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGMPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGMAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGMMarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGMAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMMarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGMAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMMarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGMAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGMMarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGMAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGMMarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGMMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGMMarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGMMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGMMarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGMMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGAPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGAPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGAPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGAPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGAPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGAPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGAPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGAPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGAPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGAPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGAPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGAPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGAAllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAAllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAAllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAAllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGAAllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGAAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAAllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGAAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAAllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGAAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAAllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGAAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGAAllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGAAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGAAllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGAAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGAAllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGAAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGAMarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGAPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAMarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGAPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAMarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGAPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGAMarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGAPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGAAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGAMarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGAAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAMarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGAAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAMarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGAAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGAMarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGAAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGAMarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGAMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGAMarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGAMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGAMarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGAMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGPctThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGPct']
        inputData.loc[index, 'CurrentSoSAvgOppFGPctNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGPctNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGPctNow']
        inputData.loc[index, 'PastSoSAvgOppFGPctNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGPctNow']
        inputData.loc[index, 'PastSoSAvgOppFGPctNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGPctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGPctAllowedThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctAllowedThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctAllowedThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctAllowedThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppFGPctAllowedNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGMAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGAAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctAllowedNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGMAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGAAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctAllowedNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGMAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGAAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctAllowedNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGMAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGAAllowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGPctAllowedNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGPctAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppFGPctAllowedNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGPctAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppFGPctAllowedNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGPctAllowedNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGPctMarginThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGPct'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctMarginThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGPct'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctMarginThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGPct'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGPctMarginThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGPct'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGPctAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppFGPctMarginNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGPct'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGPctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctMarginNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGPct'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGPctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctMarginNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGPct'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGPctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGPctMarginNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGPct'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGPctAllowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGPctMarginNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGPctMarginNow']
        inputData.loc[index, 'PastSoSAvgOppFGPctMarginNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGPctMarginNow']
        inputData.loc[index, 'PastSoSAvgOppFGPctMarginNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGPctMarginNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGM3PerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGM3PerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3PerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGM3PerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3PerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGM3PerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3PerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGM3PerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGM3PerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3PerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3PerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3PerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGM3PerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGM3PerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGM3PerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGM3PerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGM3PerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGM3PerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGM3AllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3AllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3AllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3AllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGM3AllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3Allowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3AllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3Allowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3AllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3Allowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3AllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3Allowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGM3AllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGM3AllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGM3AllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGM3AllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGM3AllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGM3AllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGM3MarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGM3PerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3MarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGM3PerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3MarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGM3PerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGM3MarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGM3PerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGM3AllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGM3MarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3Allowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3MarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3Allowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3MarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3Allowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGM3MarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3Allowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGM3MarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGM3MarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGM3MarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGM3MarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGM3MarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGM3MarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGA3PerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGA3PerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3PerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGA3PerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3PerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGA3PerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3PerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGA3PerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGA3PerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3PerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3PerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3PerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGA3PerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGA3PerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGA3PerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGA3PerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGA3PerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGA3PerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGA3AllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3AllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3AllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3AllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGA3AllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3Allowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3AllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3Allowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3AllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3Allowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3AllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3Allowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGA3AllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGA3AllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGA3AllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGA3AllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGA3AllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGA3AllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFGA3MarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGA3PerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3MarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGA3PerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3MarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGA3PerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFGA3MarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGA3PerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFGA3AllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFGA3MarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3Allowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3MarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3Allowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3MarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3Allowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFGA3MarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3Allowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFGA3MarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFGA3MarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGA3MarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFGA3MarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFGA3MarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFGA3MarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFG3PctThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFG3Pct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFG3Pct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFG3Pct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFG3Pct']
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3']).mean()
        inputData.loc[index, 'PastSoSAvgOppFG3PctNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFG3PctNow']
        inputData.loc[index, 'PastSoSAvgOppFG3PctNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFG3PctNow']
        inputData.loc[index, 'PastSoSAvgOppFG3PctNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFG3PctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFG3PctAllowedThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctAllowedThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctAllowedThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctAllowedThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctAllowedNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3Allowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3Allowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctAllowedNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3Allowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3Allowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctAllowedNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3Allowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3Allowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctAllowedNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGM3Allowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FGA3Allowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFG3PctAllowedNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFG3PctAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppFG3PctAllowedNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFG3PctAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppFG3PctAllowedNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFG3PctAllowedNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFG3PctMarginThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFG3Pct'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctMarginThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFG3Pct'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctMarginThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFG3Pct'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFG3PctMarginThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFG3Pct'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFG3PctAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctMarginNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FG3Pct'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FG3PctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctMarginNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FG3Pct'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FG3PctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctMarginNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FG3Pct'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FG3PctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFG3PctMarginNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FG3Pct'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FG3PctAllowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFG3PctMarginNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFG3PctMarginNow']
        inputData.loc[index, 'PastSoSAvgOppFG3PctMarginNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFG3PctMarginNow']
        inputData.loc[index, 'PastSoSAvgOppFG3PctMarginNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFG3PctMarginNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTMPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFTMPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFTMPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFTMPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFTMPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFTMPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTM'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTM'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTM'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTM'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTMPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFTMPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTMPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFTMPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTMPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFTMPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTMAllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMAllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMAllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMAllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFTMAllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTMAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMAllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTMAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMAllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTMAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMAllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTMAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTMAllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFTMAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTMAllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFTMAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTMAllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFTMAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTMMarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFTMPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMMarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFTMPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMMarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFTMPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTMMarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFTMPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFTMAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFTMMarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTM'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTMAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMMarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTM'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTMAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMMarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTM'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTMAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTMMarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTM'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTMAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTMMarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFTMMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTMMarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFTMMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTMMarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFTMMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTAPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFTAPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFTAPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFTAPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFTAPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFTAPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTA'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTA'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTA'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTA'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTAPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFTAPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTAPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFTAPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTAPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFTAPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTAAllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAAllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAAllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAAllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFTAAllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTAAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAAllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTAAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAAllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTAAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAAllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTAAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTAAllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFTAAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTAAllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFTAAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTAAllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFTAAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTAMarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFTAPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAMarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFTAPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAMarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFTAPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTAMarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFTAPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFTAAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppFTAMarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTA'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTAAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAMarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTA'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTAAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAMarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTA'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTAAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTAMarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTA'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTAAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTAMarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFTAMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTAMarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFTAMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppFTAMarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFTAMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTPctThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFTPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFTPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFTPct']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFTPct']
        inputData.loc[index, 'CurrentSoSAvgOppFTPctNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTM'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTA']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTM'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTA']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTM'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTA']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTM'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTA']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTPctNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFTPctNow']
        inputData.loc[index, 'PastSoSAvgOppFTPctNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFTPctNow']
        inputData.loc[index, 'PastSoSAvgOppFTPctNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFTPctNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTPctAllowedThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctAllowedThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctAllowedThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctAllowedThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppFTPctAllowedNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTMAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTAAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctAllowedNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTMAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTAAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctAllowedNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTMAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTAAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctAllowedNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTMAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTAAllowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTPctAllowedNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFTPctAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppFTPctAllowedNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFTPctAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppFTPctAllowedNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFTPctAllowedNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppFTPctMarginThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFTPct'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctMarginThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFTPct'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctMarginThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFTPct'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppFTPctMarginThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFTPct'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsFTPctAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppFTPctMarginNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTPct'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTPctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctMarginNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTPct'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTPctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctMarginNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTPct'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTPctAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppFTPctMarginNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTPct'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'FTPctAllowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppFTPctMarginNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppFTPctMarginNow']
        inputData.loc[index, 'PastSoSAvgOppFTPctMarginNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppFTPctMarginNow']
        inputData.loc[index, 'PastSoSAvgOppFTPctMarginNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppFTPctMarginNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppRebPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame'] + startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame'] + seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame'] + seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame'] + seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppRebPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] + startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] + seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] + seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] + seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppRebPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppRebPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppRebPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppRebPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppRebPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppRebPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppRebAllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] + startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebAllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] + seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebAllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] + seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebAllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] + seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppRebAllowedPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed'] + startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebAllowedPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed'] + seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebAllowedPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed'] + seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebAllowedPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed'] + seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppRebAllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppRebAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppRebAllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppRebAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppRebAllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppRebAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppRebMarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame'] + startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebMarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame'] + seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebMarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame'] + seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppRebMarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame'] + seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppRebMarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] + startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebMarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] + seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebMarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] + seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppRebMarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] + seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppRebMarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppRebMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppRebMarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppRebMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppRebMarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppRebMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppORebPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppORebPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppORebPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppORebPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppORebPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppORebPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppORebPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppORebPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppORebAllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebAllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebAllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebAllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppORebAllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebAllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebAllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebAllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppORebAllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppORebAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppORebAllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppORebAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppORebAllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppORebAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppORebMarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebMarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebMarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppORebMarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsORebPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsORebAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppORebMarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebMarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebMarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppORebMarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'OReb'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'ORebAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppORebMarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppORebMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppORebMarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppORebMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppORebMarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppORebMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppDRebPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppDRebPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppDRebPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppDRebPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppDRebPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppDRebPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppDRebPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppDRebPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppDRebAllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebAllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebAllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebAllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppDRebAllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebAllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebAllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebAllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppDRebAllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppDRebAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppDRebAllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppDRebAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppDRebAllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppDRebAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppDRebMarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebMarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebMarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppDRebMarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsDRebPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsDRebAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppDRebMarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebMarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebMarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppDRebMarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DReb'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'DRebAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppDRebMarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppDRebMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppDRebMarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppDRebMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppDRebMarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppDRebMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAstPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsAstPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsAstPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsAstPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsAstPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppAstPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Ast'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Ast'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Ast'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Ast'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppAstPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppAstPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppAstPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppAstPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppAstPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppAstPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAstAllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstAllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstAllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstAllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppAstAllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AstAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstAllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AstAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstAllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AstAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstAllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AstAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppAstAllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppAstAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppAstAllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppAstAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppAstAllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppAstAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAstMarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsAstPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstMarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsAstPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstMarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsAstPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppAstMarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsAstPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsAstAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppAstMarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Ast'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AstAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstMarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Ast'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AstAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstMarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Ast'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AstAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAstMarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Ast'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AstAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppAstMarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppAstMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppAstMarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppAstMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppAstMarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppAstMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppTOPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsTOPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsTOPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsTOPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsTOPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppTOPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TO'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TO'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TO'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TO'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppTOPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppTOPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppTOPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppTOPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppTOPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppTOPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppTOAllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOAllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOAllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOAllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppTOAllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TOAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOAllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TOAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOAllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TOAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOAllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TOAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppTOAllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppTOAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppTOAllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppTOAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppTOAllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppTOAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppTOMarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsTOPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOMarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsTOPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOMarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsTOPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppTOMarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsTOPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsTOAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppTOMarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TO'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TOAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOMarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TO'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TOAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOMarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TO'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TOAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppTOMarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TO'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'TOAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppTOMarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppTOMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppTOMarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppTOMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppTOMarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppTOMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAvgAst/TORatioThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio']
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioNowThisSeason B'] = startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioNowLastSeason B'] = seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio'].mean()
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppAvgAst/TORatioNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppAvgAst/TORatioNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppAvgAst/TORatioNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAvgAst/TORatioAllowedThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioAllowedThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioAllowedThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioAllowedThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioAllowedNowThisSeason B'] = startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioAllowedNowLastSeason B'] = seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioAllowedNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioAllowedNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed'].mean()
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioAllowedNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppAvgAst/TORatioAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioAllowedNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppAvgAst/TORatioAllowedNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioAllowedNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppAvgAst/TORatioAllowedNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAvgAst/TORatioMarginThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioMarginThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioMarginThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatioMarginThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatioAllowed']
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioMarginNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioMarginNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioMarginNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatioMarginNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatioAllowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioMarginNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppAvgAst/TORatioMarginNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioMarginNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppAvgAst/TORatioMarginNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatioMarginNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppAvgAst/TORatioMarginNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAvgAst/TORatio(alt)ThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)ThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)Then2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)Then3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)']
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)NowThisSeason B'] = startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)NowLastSeason B'] = seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)Now2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)Now3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'].mean()
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)NowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppAvgAst/TORatio(alt)Now']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)Now2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppAvgAst/TORatio(alt)Now']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)Now3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppAvgAst/TORatio(alt)Now']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)AllowedThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNowThisSeason B'] = startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNowLastSeason B'] = seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed'].mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)AllowedNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed'].mean()
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)AllowedNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppAvgAst/TORatio(alt)AllowedNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)AllowedNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppAvgAst/TORatio(alt)AllowedNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)AllowedNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppAvgAst/TORatio(alt)AllowedNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'PastSoSWeightedAvgOppAvgAst/TORatio(alt)MarginThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsAst/TORatio(alt)Allowed']
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppAvgAst/TORatio(alt)MarginNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'AvgAst/TORatio(alt)Allowed']).mean()
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)MarginNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppAvgAst/TORatio(alt)MarginNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)MarginNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppAvgAst/TORatio(alt)MarginNow']
        inputData.loc[index, 'PastSoSAvgOppAvgAst/TORatio(alt)MarginNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppAvgAst/TORatio(alt)MarginNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppStlPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsStlPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsStlPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsStlPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsStlPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppStlPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Stl'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Stl'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Stl'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Stl'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppStlPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppStlPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppStlPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppStlPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppStlPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppStlPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppStlAllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlAllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlAllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlAllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppStlAllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'StlAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlAllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'StlAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlAllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'StlAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlAllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'StlAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppStlAllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppStlAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppStlAllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppStlAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppStlAllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppStlAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppStlMarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsStlPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlMarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsStlPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlMarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsStlPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppStlMarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsStlPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsStlAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppStlMarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Stl'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'StlAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlMarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Stl'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'StlAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlMarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Stl'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'StlAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppStlMarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Stl'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'StlAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppStlMarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppStlMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppStlMarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppStlMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppStlMarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppStlMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppBlkPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsBlkPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsBlkPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsBlkPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsBlkPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppBlkPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Blk'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Blk'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Blk'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Blk'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppBlkPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppBlkPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppBlkPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppBlkPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppBlkPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppBlkPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppBlkAllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkAllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkAllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkAllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppBlkAllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'BlkAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkAllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'BlkAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkAllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'BlkAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkAllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'BlkAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppBlkAllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppBlkAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppBlkAllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppBlkAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppBlkAllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppBlkAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppBlkMarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsBlkPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkMarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsBlkPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkMarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsBlkPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppBlkMarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsBlkPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsBlkAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppBlkMarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Blk'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'BlkAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkMarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Blk'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'BlkAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkMarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Blk'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'BlkAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppBlkMarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'Blk'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'BlkAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppBlkMarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppBlkMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppBlkMarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppBlkMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppBlkMarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppBlkMarginPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppPFPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsPFPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsPFPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsPFPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsPFPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppPFPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PF'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PF'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PF'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PF'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppPFPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppPFPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPFPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppPFPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPFPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppPFPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppPFAllowedPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFAllowedPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFAllowedPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFAllowedPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppPFAllowedPerGameNowThisSeason B'] = (startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PFAllowed'] / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFAllowedPerGameNowLastSeason B'] = (seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PFAllowed'] / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFAllowedPerGameNow2SeasonsAgo B'] = (seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PFAllowed'] / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFAllowedPerGameNow3SeasonsAgo B'] = (seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PFAllowed'] / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppPFAllowedPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppPFAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPFAllowedPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppPFAllowedPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPFAllowedPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppPFAllowedPerGameNow']

        inputData.loc[index, 'CurrentSoSWeightedAvgOppPFMarginPerGameThenThisSeason B'] = startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsPFPerGame'] - startOfDaySeasonTotals.loc[teamB, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFMarginPerGameThenLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsPFPerGame'] - seasonTotalsDict[season - 1].loc[teamB, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFMarginPerGameThen2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsPFPerGame'] - seasonTotalsDict[season - 2].loc[teamB, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'PastSoSWeightedAvgOppPFMarginPerGameThen3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsPFPerGame'] - seasonTotalsDict[season - 3].loc[teamB, 'SoSWeightedAvgOpponentsPFAllowedPerGame']
        inputData.loc[index, 'CurrentSoSAvgOppPFMarginPerGameNowThisSeason B'] = ((startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PF'] - startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PFAllowed']) / startOfDaySeasonTotals.loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFMarginPerGameNowLastSeason B'] = ((seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PF'] - seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PFAllowed']) / seasonTotalsDict[season - 1].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFMarginPerGameNow2SeasonsAgo B'] = ((seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PF'] - seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PFAllowed']) / seasonTotalsDict[season - 2].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'CurrentSoSAvgOppPFMarginPerGameNow3SeasonsAgo B'] = ((seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PF'] - seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'PFAllowed']) / seasonTotalsDict[season - 3].loc[startOfDaySeasonTotals.loc[teamB, 'ListOpponentsTeamID'], 'GamesPlayed']).mean()
        inputData.loc[index, 'PastSoSAvgOppPFMarginPerGameNowLastSeason B'] = seasonTotalsDict[season - 1].loc[teamB, 'SoSAvgOppPFMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPFMarginPerGameNow2SeasonsAgo B'] = seasonTotalsDict[season - 2].loc[teamB, 'SoSAvgOppPFMarginPerGameNow']
        inputData.loc[index, 'PastSoSAvgOppPFMarginPerGameNow3SeasonsAgo B'] = seasonTotalsDict[season - 3].loc[teamB, 'SoSAvgOppPFMarginPerGameNow']


# calculate total runtime
delta = datetime.now() - startTime
print('\nTotal runtime: ' + str(delta.seconds // 3600) + ' hours, ' + str(delta.seconds // 60) + ' minutes, ' + str(delta.seconds % 60) + ' seconds')


print('Generate_Input_Data completed.')


