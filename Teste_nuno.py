# import pandas as pd

# #Global Variables

# # File names
# ## Import
# csvFile = 'vgsales-12-4-2019.csv'

# ## Export
# excelFileName = 'ficheiro.xlsx'
# tab1Name = 'Raw Data'
# tab2Name = 'Platform Rank'

# # Pandas CSV configuration
# encodingName = 'utf8'
# separator = ','

# # Pandas XLS configuration
# engineName = 'xlsxwriter'

# # Essa função é reponsável pelo load de um ficheiro CSV 
# def extract_base(inCSVName):
#     load_file = pd.read_csv(inCSVName,sep=separator,encoding=encodingName)
#     return load_file

# file = extract_base(csvFile)
# df_teste = file.iloc[:11,12:17]

# def fillNull(df, *column_name ,fill_value=0):
#     for column in column_name:
#         if column in df.columns:
#             df[column] = df[column].fillna(fill_value)
#             df[column].replace('',fill_value, inplace=True)
#     return df



# print (fillNull(df_teste, 'Global_Sales', 'NA_Sales', 'PAL_Sales', 'JP_Sales', 'Other_Sales'))

x = max(1,2,3,4,5,6)

print(x)