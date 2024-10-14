from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# 设置chromedriver路径
PATH = '/Users/lqcmacmini/PycharmProjects/chromedriver-mac-arm64/chromedriver'
service = Service(PATH)
driver = webdriver.Chrome(service=service)

# 打开YouTube网站
driver.get('https://www.youtube.com/')

# 等待页面加载
time.sleep(2)

# 找到搜索框并输入关键词
search_box = driver.find_element(By.NAME, 'search_query')
search_box.send_keys('health literacy')  # 这里输入你想要搜索的关键词
search_box.send_keys(Keys.RETURN)  # 模拟按下回车键

# 等待搜索结果页面加载
time.sleep(3)

# 获取所有视频元素
videos = driver.find_elements(By.XPATH, '//a[@id="video-title"]')

# 初始化列表用于存储视频数据
video_data = []

# 爬取视频标题和链接
for video in videos:
    title = video.get_attribute('title')  # 获取视频标题
    link = video.get_attribute('href')    # 获取视频链接
    if title and link:  # 确保数据不为空
        video_data.append({'Title': title, 'Link': link})

# 关闭浏览器
driver.quit()

# 将数据转换为DataFrame
df = pd.DataFrame(video_data)

# 将数据写入Excel文件
df.to_excel('youtube_videos.xlsx', index=False)

print("视频信息已成功保存到Excel文件！")
