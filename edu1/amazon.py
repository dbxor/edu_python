#Import
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen

import urllib
import time
import sys
import re
import math
import numpy as np  
import pandas as pd 
import xlwt
import random
import os


#Step1
query_txt = "아마존 닷컴 베스트 상품"

query_url = 'http://amazon.com/bestsellers?id=NSGoogle'

sec = input('''
    1. Amazon Devices & Accessories     2. Amazon Launchpad                 3. Amazon Pantry
    4. Appliances                       5. Apps & Games                     6. Arts, Crafts & Sewing
    7. Audible Books & Originals        8. Automotive                       9. Baby
    10. Beauty & Personal Care          11. Books                           12. CDs & Vinyl
    13. Camera & Photo                  14. Cell Phones & Accessories       15. Clothing, Shoes & Jewelry
    16. Collectible Currencies          17. Computers & Accessories         18. Digital Music
    19. Electronics                     20. Entertainment Collectibles      21. Gift Cards
    22. Grocery & Gourmet Food          23. Handmade Products               24. Health & Household
    25. Home & Kitchen                  26. Industrial & Scientific         27. Kindle Store
    28. Kitchen & Dining                29. Magazine Subscriptions          30. Movies & TV
    31. Musical Instruments             32. Office Products                 33. Patio, Lawn & Garden
    34. Pet Supplies                    35. Software                        36. Sports & Outdoors
    37. Sports Collectibles             38. Tools & Home Improvement        39. Toys & Games
    40. Video Games
    => 위 목록에서 수집할 분야의 번호를 선택: ''')

if int(sec) <= 0 or int(sec) >= 41 :
    print("Error 선택범위를 벗어났습니다!.")
    sys.exit()

cnt = int(input("크롤링할 데이터 건수(1~100): "))

f_dir = input("저장할 폴더명: ")

print("\n")

if sec == '1':
    sec_name = 'Amazon Devices & Accessories'
elif sec == '2':
    sec_name = ''
elif sec == '3':
    sec_name = ''
elif sec == '4':
    sec_name = ''
elif sec == '5':
    sec_name = ''
elif sec == '6':
    sec_name = ''
elif sec == '7':
    sec_name = ''        
elif sec == '8':
    sec_name = ''
elif sec == '9':
    sec_name = ''
elif sec == '10':
    sec_name = ''
elif sec == '11':
    sec_name = ''
elif sec == '12':
    sec_name = ''
elif sec == '13':
    sec_name = ''       
elif sec == '14':
    sec_name = ''
elif sec == '15':
    sec_name = ''
elif sec == '16':
    sec_name = ''
elif sec == '17':
    sec_name = ''
elif sec == '18':
    sec_name = ''
elif sec == '19':
    sec_name = ''        
elif sec == '20':
    sec_name = ''
elif sec == '21':
    sec_name = ''
elif sec == '22':
    sec_name = ''
elif sec == '23':
    sec_name = ''
elif sec == '24':
    sec_name = ''
elif sec == '25':
    sec_name = ''  
elif sec == '26':
    sec_name = ''
elif sec == '27':
    sec_name = ''
elif sec == '28':
    sec_name = ''
elif sec == '29':
    sec_name = ''
elif sec == '30':
    sec_name = ''
elif sec == '31':
    sec_name = ''        
elif sec == '32':
    sec_name = ''
elif sec == '33':
    sec_name = ''
elif sec == '34':
    sec_name = ''
elif sec == '35':
    sec_name = ''
elif sec == '36':
    sec_name = ''
elif sec == '37':
    sec_name = ''  
elif sec == '38':
    sec_name = ''
elif sec == '39':
    sec_name = ''
elif sec == '40':
    sec_name = ''
else :
    pass

#
if cnt > 30:
    print("요청건수가 많아 시간이 소요")
else :
    print("데이터를 수집중")


#저장할 파일명
now = time.localtime()
s = '%04d-%02d-%02d-%02d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)


start_time = time.time()

os.makedirs(f_dir, exist_ok = True)
os.chdir(f_dir)

ff_dir = f_dir + s + '-' + query_txt + '-'+ sec_name

ff_name = s +'-' + query_txt + '-'+ sec_name + '.txt'
fc_name = s +'-' + query_txt + '-'+ sec_name + '.csv'
fx_name = s +'-' + query_txt + '-'+ sec_name + '.xls'

path = "/Users/yutaekkim/workspace/python_ws/chromedriver"
driver = webdriver.Chrome(path)

driver.get(query_url)
time.sleep(2)

#분야별 더보가
if int(sec)>= 1 and int(sec) <= 40:
    print("category select: ", sec)
    print("""//*[@id="zg_browseRoot"]/ul/li["""+sec+"""]/a""")
    x_path = """//*[@id="zg_browseRoot"]/ul/li["""+sec+"""]/a"""
    print("x_path: ", x_path)
    driver.find_element_by_xpath(x_path).click()
else :
    pass

time.sleep(1)

#검색첫화면에 20개, 넘어갈 경우 스크롤다운.

def scroll_down(driver) :
    driver.execute_script("window.scrollBy(0, 9300);")
    time.sleep(2)

scroll_down(driver)

#비트맵 이미지 아이콘을 대체하기 위한 딕셔너리
bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#페이지 불러오기
html= driver.page_source
soup1 = BeautifulSoup(html,'html.parser')

reple_result = soup1.select('#zg-center-div > #zg-ordered-list')

#print(reple_result)
#상품정보 하나씩 추출
slist = reple_result[0].find_all('li')
#print(slist)
#아이템 갯수가 50개보다 많으면 
if cnt < 51 :
    #엑셀형식으로 만들기 위한 리스트
    ranking2 = []
    title3 = []
    price2 = []
    score2 = []
    sat_count2 = []
    count = 0

    for li in slist:
        f = open(ff_name, 'a', encoding= 'UTF-8')
        f.write("\n")
        f.write("---------1---------2---------3"+"\n")

        print("=" *70)
        count += 1
        #판매순위
        try:
            ranking = li.find('span', class_='zg-badge-text').get_text().replace("#","")
        except AttributeError:
            ranking = ''
            print(ranking.replace("#",""))
        else:
            print("판매순위: ", ranking)
            f.write("판매순위: "+ ranking +"\n")
        
        #제품설명
        try:
            title1 = li.find('div', class_='p13n-sc-truncated').get_text().replace("\n","")
        except AttributeError:
            title1 = ''
            print("제품소개: ", title1.replace("\n",""))
            f.write("제품소개: "+ title1 +"\n")
        else:
            title2 = title1.translate(bmp_map).replace("\n","")
            print("제품소개: ", title2.replace("\n",""))
            f.write("제품소개: "+ title2 +"\n")

        #가격
        try:
            price = li.find('span', 'p13n-sc-price').get_text().replace("\n","")
        except AttributeError:
            price = ''

        print("가  격: ", price.replace("\n",""))
        f.write("가  격: "+ price +"\n")       

        #상품평 수
        try:
            sat_count = li.find('a', 'a-size-small a-link-normal').get_text().replace(".","")
        except (IndexError, AttributeError):
            sat_count = 0
            print("상품평수: ", sat_count)
            f.write("상품평수: "+ sat_count)
        else:
            print("상품평수: ", sat_count.replace("\n",""))
            f.write("상품평수: "+ sat_count +"\n")

        #상품평점
        try:
            score = li.find('span', 'a-icon-alt').get_text().replace(".","")
        except (AttributeError):
            score = ' '

        print("상품평점", score.replace("\n",""))
        f.write("상품평점: "+ score +"\n")

        print("-" * 70)

        f.close()
        time.sleep(2)

        ranking2.append(ranking)
        title3.append(title2.replace("\n",""))
        price2.append(price.replace("\n",""))
        try:
            sat_count2.append(sat_count)
        except (IndexError):
            sat_count2.append(0)
        score2.append(score.replace("\n",""))

        if count == cnt:
            break

elif cnt >= 51:
    driver.find_element_by_xpath("""//*[@id=zg-center-div"]/div/ul/li[2]/a""").click()
    print("2  페이지 목록 추출 작업 중")

else :
    print("")

#Table 형태로 저장
amazon_bestseller = pd.DataFrame()
amazon_bestseller['판매순위'] = ranking2
amazon_bestseller['제품소가'] = pd.Series(title2)
amazon_bestseller['판매가격'] = pd.Series(price2)
amazon_bestseller['상품평수'] = pd.Series(sat_count2)
amazon_bestseller['상품평점'] = pd.Series(score2)

#csv로 저장
amazon_bestseller.to_csv(fc_name, encoding='utf-8-sig', index=True)
#excel로 저장
amazon_bestseller.to_excel(fx_name, index=True)

end_time = time.time()
total_time = end_time - start_time

orig_stdout = sys.stdout
f = open(ff_name, 'a', encoding='UTF-8')
sys.stdout = f

print("\n")
print("=" *50)
print("총 소요시간은 %s 초이고 시작시간은 %s 종료시간은 %s ."%(round(total_time), start_time, end_time))
print("총 저장건수는 %s 건" %(count))
print("=" *50)

sys.stdout = orig_stdout
f.close()

#화면으로 결과 출력
print("\n")
print("=" *50)
print("요청된 총 %s 건의 리뷰중 실체 크롤링된 리뷰는 각 %s 건 ."%(cnt, count))
print("총 소요시간은 %s 초."%round(total_time))
print("총 저장건수는 %s 건" %(count))
print("Text File  %s " %ff_name)
print("CSV File   %s " %fc_name)
print("Excel File %s " %fx_name)
print("=" *50)

driver.close()
#END