import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://music.163.com/#/discover/toplist?id=3778678')
browser.switch_to.frame(browser.find_element(By.XPATH,'/html/body/iframe[1]'))
time.sleep(2)
for i in range(1,100):
    music_id = browser.find_element(By.XPATH,
                                    f'/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div[1]/table/tbody/tr[{i}]/td[2]/div/div/div/span/a').get_attribute(
        "href").split("=")[1]
    music_name = browser.find_element(By.XPATH,
                                      f'/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div[1]/table/tbody/tr[{i}]/td[2]/div/div/div/span/a/b').get_attribute(
        "title")
    url = 'http://music.163.com/song/media/outer/url?id=%s'%music_id
    response = requests.get(url).content
    with open('./网易云热歌榜下载/%s.mp3'%music_name,'wb')as f:
        f.write(response)
        print(i,"正在爬取音乐《%s》"%music_name)
        # time.sleep(1)
        print("爬取《%s》成功！"%music_name)
print("全部爬取成功!")
browser.quit()
