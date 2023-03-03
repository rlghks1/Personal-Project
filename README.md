# Personal-Project

----------------------------

## Objective
I am interested in protein meals in Australia but there doesn't seem to be a lot of information organized at once. So I collected the protein meals as data and organized them with mySQL.
As building a mySQL server, I can easily recognize them with the organised data and I'm planning make some queries for useful information from those.  

## Api/Language used in project

1. Apify Google Shopping Scraper - Done web crawling and saved the data in csv format (o)
2. Naver Developers API - Done web crawling from naver and saved the data in csv format (o)
3. Python - extract data needed from raw data and analyse the data to get useful information (x)
4. Mysql - Built a database server to manage the protein meal data easily (o)


## What information I need to use & What information I don't need from raw data  


**Google** - description, merchantLink, merchantName, positionOnSearchPage, price, productDetails, productLink, productName, reviewsCount, reviewsScore, shoppingId<br/><br/>  

information I need => description, merchantName, price, productDetails, productLink, productName, shoppingId  

information I don't need => merchantLink, positionOnSearchPage, reviewsCount, reviewsScore<br/><br/>  


=>changed the order into productName, price, productDetails, productLink, description, merchantName(maker), productId<br/><br/>


**Naver** - title, link, image, lprice, hprice, mallName, productId, productType, brand, maker, category1, category2, category3, category4  <br/><br/>


information I need</span> => title, link, image, lprice, hprice, mallName, productId, brand, maker  

information I don't need => image, productType, category1, category2, category3, category4<br/><br/>


=>changed the order into title, lprice, hprice, link, maker, brand, productId, image, mallName<br/><br/>  


==> basically I persue to change the order into **productName, price, productDetails, link, merchantName(maker), brand, productId**<br/><br/>

## ER Diagram<br/><br/>

## To Do<br/><br/>

1. completed to build MySQL Server but didn't convert and upload the csv file to sql format.  
  => uploaded all data using MySql Import Wizard<br/><br/>
2. Every product have own weight and price but I need to compare all products using unit price ($ per 100g) so I need to modify currency and weight to be same.
  => I'll do this as making SQL Query<br/><br/>

** As Australian 1$ = Korean 880.16 won (03/03/23), I express the won in Au dollars based on this exchange rate.<br/><br/>

3. need to compare and analyse the data from google and naver, then find common and different features or hopefully new features I couldn't discover yet.

### Edit History<br/><br/>
-> changed the currency Korean won to Australian dollar based on daily exchange rate on mySQL server.<br/><br/>
-> delete powder products from googleprotein <br/><br/>
-> change price data type to decimal for googleprotein <br/><br/>
-> 


