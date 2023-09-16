from selenium import webdriver
import time
 
driver = webdriver.Chrome("C:/Users/HJ/jupyter_code/scrapy_and_selenium/chromedriver_win32/chromedriver.exe")
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%ED%83%80%EC%B9%B4%ED%95%98%EC%8B%9C%20%EC%A5%AC%EB%A6%AC" )
time.sleep(3)
 
images = driver.find_elements_by_css_selector("#imgList > div > a > img")
img_url = []
 
for image in images :
    url = image.get_attribute('src')
    img_url.append(url)
 
# print(img_url)
 
driver.quit()



# Base URL
# https://wfwf288.com/cv?toon=13251&num=1
# https://wfwf288.com/cv?toon=13251&num=229



#<img src="https://i0.imgcloud16.com/13251/6c047eeb_2_0.jpg" alt="쌍망정은 부숴야 한다 2화_0">

# Full Xpath
#/html/body/section[1]/div[5]/img[1]
#/html/body/section[1]/div[5]/img[1]
#/html/body/section[1]/div[5]/img[1]
#/html/body/section[1]/div[5]/img[2]

