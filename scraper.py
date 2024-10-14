from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

PATH = '/Users/lqcmacmini/PycharmProjects/chromedriver-mac-arm64/chromedriver'
service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get('https://www.youtube.com/')

time.sleep(2)

search_box = driver.find_element(By.NAME, 'search_query')
search_box.send_keys('health literacy')
search_box.send_keys(Keys.RETURN)

time.sleep(3)

videos = driver.find_elements(By.XPATH, '//a[@id="video-title"]')

video_data = []

for video in videos:
    title = video.get_attribute('title')  # 标题
    link = video.get_attribute('href')    # 链接
    if title and link:  # 数据不为空
        video_data.append({'Title': title, 'Link': link})

driver.quit()

df = pd.DataFrame(video_data)

df.to_excel('youtube_videos.xlsx', index=False)

print("视频信息已成功保存到Excel文件！")
