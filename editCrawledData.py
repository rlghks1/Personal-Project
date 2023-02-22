import pandas as pd

# read google data only needed from the raw data
path_to_file = "googleShopping\dataset_google-shopping-scraper.csv"
gData = pd.read_csv(path_to_file, encoding='utf-8')
gData = gData.loc[:, ~gData.columns.isin(['merchantLink','positionOnSearchPage','reviewsCount','reviewsScore'])]

# change the order into  productId, productName, price, productDetails, description, merchantName(maker)
gData = gData.iloc[:,[6,5,2,3,0,1]]
print(gData)

# save the edited google data
gData.to_csv('data_google.csv')

# read naver data only needed from the raw data
path_to_file = "protein_meal_naver.csv"
nData = pd.read_csv(path_to_file, encoding='euc-kr')
nData = nData.loc[:, ~nData.columns.isin(['productType','category1','category2','category3','category4'])]

# change the order into title, price, maker, brand, productId
nData = nData.iloc[:,[6,0,1,8,7]]
#print(nData)

# save the edited naver data
nData.to_csv('data_naver.csv')