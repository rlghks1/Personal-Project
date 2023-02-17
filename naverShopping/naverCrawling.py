# Naver Shopping Search API  
import os
import sys
import urllib.request
import json
import csv

client_id = "WXRkOl6rH6gf4xRCQM_I"
client_secret = "ypJ1utK1SB"
start = 1
display = "100"
encText = urllib.parse.quote("닭가슴살 볶음밥")
for i in range(1,11):
    if i != 1:
        start += int(display)
    print(start)
    url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=" + display + "&start=" + str(start) # JSON result
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # result
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        #print(response_body.decode('utf-8'))
        with open('protein_meal_naver.csv', 'a', newline = '') as output_file :
            data = json.loads(response_body)
            #print(data['items'])
            f = csv.writer(output_file)
            isempty = os.stat('protein_meal_naver.csv').st_size
            print(isempty)
            if (isempty == 0) :
                f.writerow(["title","link","image","lprice","hprice","mallName",
                            "productId","productType","brand","maker","category1","category2","category3","category4"])
            
            # no save if the category of product is not 'meal' type
            
            matches = ['도시락','즉석밥','곤약','기타곤약가공품']
            
            for datum in data['items']:
                #print(datum["category1"],datum["category2"],datum["category3"],datum["category4"])
                categories = [datum["category1"],datum["category2"],datum["category3"],datum["category4"]]
                # exclude product which is not a meal
                if any(x in categories for x in matches):
                    f.writerow([datum["title"],datum["link"],datum["image"],datum["lprice"],datum["hprice"],datum["mallName"], 
                            datum["productId"],datum["productType"],datum["brand"],datum["maker"],datum["category1"],
                            datum["category2"], datum["category3"],datum["category4"]])
    else:
        print("Error Code:" + rescode)

