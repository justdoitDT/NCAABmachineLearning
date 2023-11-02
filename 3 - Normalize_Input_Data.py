import pandas as pd
import numpy as np
from datetime import datetime


rootDirectory = '/Users/dthomas/Desktop/Coding/NCAAB'
startingYear = 2006
endingYear = 2023
#
# # normalize input data
# for year in range(startingYear, endingYear + 1):
#     inputDF = pd.read_csv(rootDirectory + '/InputData' + '/InputData' + str(year) + '.csv')
#     minDict = {}
#     maxMinusMinDict = {}
#     lenInputDF = len(inputDF)
#     widthInputDF = len(inputDF.columns[3:])
#     count = 0
#     for colHeading in inputDF.columns[4:]:
#         # inputDF.loc[:, colHeading] = (inputDF.loc[:, colHeading] - min(inputDF.loc[:, colHeading])) / (max(inputDF.loc[:, colHeading]) - min(inputDF.loc[:, colHeading]))
#         minDict[colHeading] = min(inputDF.loc[:, colHeading])
#         maxMinusMinDict[colHeading] = max(inputDF.loc[:, colHeading]) - minDict[colHeading]
#         for index in range(lenInputDF):
#             inputDF.loc[index, colHeading] = (inputDF.loc[index, colHeading] - minDict[colHeading]) / maxMinusMinDict[colHeading]
#         count += 1
#         print(str(year) + ': ' + str(count) + ' / ' + str(widthInputDF) + ' columns normalized.')
#     # write normalized input data
#     inputDF.to_csv(rootDirectory + '/NormalizedInputData' + '/NormalizedInputData' + str(year) + '.csv')
#     print(rootDirectory + '/NormalizedInputData' + '/NormalizedInputData' + str(year) + '.csv written.', str(datetime.now())[:-7])

# concatenate normalized input data
listNormalizedInputDF = []
for year in range(startingYear, endingYear + 1):
    print('Concatenating normalized data. Appending ' + str(year) + ' season. ', str(datetime.now())[:-7])
    normalizedInputDF = pd.read_csv(rootDirectory + '/NormalizedInputData/NormalizedInputData' + str(year) + '.csv')
    listNormalizedInputDF.append(normalizedInputDF)
concatenatedNormalizedInputDF = pd.concat(listNormalizedInputDF)
# write concatenated normalized input data
concatenatedNormalizedInputDF.to_csv(rootDirectory + '/NormalizedInputData/ConcatenatedNormalizedInputDF.csv')
print(rootDirectory + '/NormalizedInputData/ConcatenatedNormalizedInputDF.csv written.')


print('\nNormalize_Input_Data completed.')

