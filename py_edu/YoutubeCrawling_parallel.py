
#Import
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen

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
query_txt = input("유튜브에서 검색할 주제 키워드? ")
cnt = int(input("크롤링할 동영상 건수?"))

reple_cnt = int(input("추출할 댓글 수?"))

f_dir = input("저장할 폴더명?")

print("\n")
print("데이터를 수집중입니다!")

#Step2
now = time.localtime()
s = '%04d-%02d-%02d-%02d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

#print(File_Name)
os.makedirs(f_dir, exist_ok = True)
os.chdir(f_dir)
#print("os.chdir")
#print("os.getcwd() :" + os.getcwd())

#ff_name = f_dir + s + '-' + query_txt + '\\' + f_dir + s + '-' + query_txt + '.txt'
ff_name = s +'-' + query_txt + '.txt'
fc_name = s +'-' + query_txt + '.csv'
fx_name = s +'-' + query_txt + '.xls'
#print(ff_name)

Start_Time = time.time()
#print(Start_Time)
#Step3

path = "/Users/yutaekkim/workspace/python_ws/chromedriver"
driver = webdriver.Chrome(path)

driver.get('https://www.youtube.com')

time.sleep(2)

element = driver.find_element_by_name("search_query")
element.send_keys(query_txt)
element.submit()

#화면을 이동하여 영상목록을 출력
#검색첫화면에 20개, 넘어갈 경우 스크롤다운.

def scroll_down(driver) :
    driver.execute_script("window.scrollBy(0, 3000);")
    time.sleep(2)

if reple_cnt < 20 :
    Page_Count = 1
else :
    Page_Count = math.ceil(reple_cnt / 20)

#print("Page_Count" , Page_Count)
#print("cnt" , cnt)
if cnt > 20 :
    i = 1
    while (i <= Page_Count) :
        print("%s scroll" %i)
        scroll_down(driver)
        time.sleep(1)
        i += 1
    print("i: " , i)

# Step
time.sleep(2)

html = driver.page_source
soup1 = BeautifulSoup(html,'html.parser')

count = 0
item = []
print("\n")

for i in soup1.find_all('a', 'yt-simple-endpoint style-scope ytd-video-renderer') :
    #simul
    item.append(i['href'])
    count += 1

    if count == cnt :
        break

print("%s 개의 동영상 댓글 추출" %cnt)
print("*" *80)
print("\n")

bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#댓글 출력
full_url = []
url_cnt = 0

for x in range(0,len(item)) :
    url_cnt += 1
    #
    url = 'https://www.youtube.com'+item[x]
    #동영상 주소
    #print(url)
    full_url.append(url)
    if url_cnt == cnt :
        break

play_cnt = 1

for y in range(0, len(full_url)) :
    driver.get(full_url[y])
    time.sleep(2)
    print("\n")
    print("\n")
    print("%s번쨰 동영상 정보를 수집" %play_cnt)

    i = 1
    while (i <= Page_Count) :
        scroll_down(driver)
        time.sleep(1)
        i += 1

    html = driver.page_source
    soup2 = BeautifulSoup(html,'html.parser')

    #t_Count_0 = soup2.select('#count > #view-count')
    t_Count_0 = soup2.select('#count')
    t_Count_1 = t_Count_0[1].get_text()
    t_Count_2 = t_Count_1.replace(",","")
    #154 라인 참고
    t_Count_3 = re.search(r'\d+', t_Count_2)
    #print(t_Count_3)
    t_Count_4 = int(t_Count_3.group())

    t_Title_1 = soup2.select('#info-contents')
    t_Title_2 = t_Title_1[0].find('h1').get_text()
    t_Title_3 = t_Title_2.translate(bmp_map).replace('\n',"")

    t_View_1 = t_Count_0[1].get_text().replace("\n","")
    t_View_2 = t_View_1.replace(",","")
    #144 라인 참고
    t_View_3 = re.search("\\d+", t_View_2)
    t_View_4 = int(t_View_3.group())

    print("=" *80)
    print("%s 번쨰 동영상 조회수는  %s회이고 댓글은 총 %s개" %(play_cnt, t_Count_4, t_View_4))
    print("%s 번쨰 동영상 제목은 %s" %(play_cnt, t_Title_3))
    print("=" *80)
    print("%s 번쨰 동영상에서 댓글 수집중" %play_cnt)
    print("\n")

#화면을 스크롤 해서 요청댓글수
# Page_Count = math.ceil(t_View_4 / 19)    

    i = 1
    while ( i <= Page_Count + 1) :
        scroll_down(driver)
        time.sleep(0.5)
        i += 1

    url2 = []
    reple2 =[]
    reple3 =[]
    reple4 = []
    writer2 = []
    wdate = []

    time.sleep(2)

    html = driver.page_source
    soup3 = BeautifulSoup(html, 'html.parser')

    count = 0
    d2 = 0

    reple_result = soup3.select('#comments > #sections > #contents')
    
    for a in range(0, reple_cnt) :
        count += 1

        f = open(ff_name, 'a', encoding= 'UTF-8')
        f.write("\n")
        f.write("---------1---------2---------3"+"\n")


        #댓글작성자
        try :
            writer = reple_result[0].select("#header-author > #author-text")[a].get_text().replace("\n","").strip()
        except IndexError :
            break
        else : 
            print("\n")
            print("%s 번쨰 영상의 %s 번째 댓글" %(play_cnt, count))
            f.write("%s 번쨰 영상의 %s 번째 댓글" %(play_cnt, count) + "\n")
            print("-" *70)

        print("URL 주소: "+ full_url[y])
        f.write("URL 주소: "+ full_url[y] + "\n")
        url2.append(full_url[y])

        #댓글작성자
        print("댓글 작성자: "+ writer)
        f.write("댓글 작성자: "+ writer + "\n")
        writer2.append(writer)
        
        #댓글내용
        reple1 = reple_result[0].select('#content-text')[a].get_text().replace("\n","")
        reple2 = reple1.translate(bmp_map).replace("\n","")
        print("댓글내용", reple2)
        f.write("댓글내용"+ reple2 + "\n")     
        reple3.append(reple2)

        f.close()

        if count == reple_cnt:
            break

    time.sleep(2)
    play_cnt += 1


#Excel 형태로 저장
youtube_reple = pd.DataFrame()
youtube_reple['URL주소'] = url2
youtube_reple['댓글작성자'] = pd.Series(writer2)
youtube_reple['댓글내용'] = pd.Series(reple3)

#csv로 저장
youtube_reple.to_csv(fc_name, encoding='utf-8-sig', index=True)

#excel로 저장
youtube_reple.to_excel(fx_name, index=True)

End_Time = time.time()
Total_Time = End_Time - Start_Time

orig_stdout = sys.stdout
f = open(ff_name, 'a', encoding='UTF-8')
sys.stdout = f

print("\n")
print("=" *50)
print("총 소요시간은 %s 초이고 시작시간은 %s 종료시간은 %s ."%(round(Total_Time), Start_Time, End_Time))
print("총 저장건수는 %s 건" %(count*cnt))
print("=" *50)

sys.stdout = orig_stdout
f.close()

#화면으로 결과 출력
print("\n")
print("=" *50)
print("요청된 총 %s 건의 동영상 리뷰중 실체 크롤링된 리뷰는 각 %s 건 ."%(cnt, count))
print("총 소요시간은 %s 초 ."%round(Total_Time))
print("총 저장건수는 %s 건" %(count*cnt))
print("Text File %s" %ff_name)
print("CSV File %s 건" %fc_name)
print("Excel File %s 건" %fx_name)
print("=" *50)

driver.close()
#END


