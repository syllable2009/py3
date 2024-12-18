import pandas as pd

df = pd.read_csv('Demographic_Statistics_By_Zip_Code.csv', header=0,encoding='gbk')

# df.columns = ['JURISDICTION_NAME','COUNT_PARTICIPANTS','PERCENT_FEMALE']
# print(df.tail(5))
# print(len(df))

# pd.options.display.float_format = '{:,.3f}'.format # Limit output to 3 decimal places.

# print(df.describe())

# print(df['JURISDICTION NAME'])
# print(df.COUNT_PARTICIPANTS  > 20)
# print(df[df.COUNT_PARTICIPANTS > 50])
# print(df[(df.COUNT_PARTICIPANTS < 50) & (df.COUNT_PARTICIPANTS > 40)])
# print(df[df.COUNT_PARTICIPANTS.str.startswith('199')])
# print(df.iloc[0])
# df = df.set_index(['JURISDICTION_NAME'])
# print(df.head(5))
# print(df.ix[10016])