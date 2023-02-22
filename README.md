# Personal-Project

----------------------------

## Objective
I am interested in protein meals in Australia but there doesn't seem to be a lot of information organized at once. So I collected the protein meals as data and organized them with mySQL.
As building a mySQL server, I can easily recognize them with the organised data and I'm planning make some queries for useful information from those.  

## Api/Language used in project

1. Apify Google Shopping Scraper - Done web crawling and saved the data in csv format (o)
2. Naver Developers API - Done web crawling from naver and saved the data in csv format (x)
3. Python - extract data needed from raw data and analyse the data to get useful information (x)
4. Mysql - Built a database server to manage the protein meal data easily (x)
5.

## What information I need to use & What information I don't need from raw data

Google - description, merchantLink, merchantName, positionOnSearchPage, price, productDetails, productLink, productName, reviewsCount, reviewsScore, shoppingId

information I need => merchantName, price, productDetails, productLink, productName, shoppingId  

information I don't need => description, merchantLink, positionOnSearchPage, reviewsCount, reviewsScore  

Naver - title, link, image, lprice, hprice, mallName, productId, productType, brand, maker, category1, category2, category3, category4  

information I need => title, link, image, lprice, hprice, mallName, productId, brand, maker  

information I don't need => productType, category1, category2, category3, category4  

=>changed the order into productName, price, productDetails, productLink, merchantName(maker), brand, productId

## ER Diagram

## 
