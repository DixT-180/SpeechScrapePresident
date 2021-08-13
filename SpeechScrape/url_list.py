import time
from selenium import webdriver
import io
# Web scrapper for infinite scrolling page


driver = webdriver.Chrome(
    executable_path=r"C:\Program Files (x86)\chromedriver.exe")
driver.get("https://millercenter.org/the-presidency/presidential-speeches")


time.sleep(2)  # Allow 2 seconds for the web page to open
# You can set your own pause time. My laptop is a bit slow so I use 1 sec
scroll_pause_time = 1
screen_height = driver.execute_script(
    "return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    driver.execute_script(
        "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break

with io.open('urls.txt', "a+", encoding="utf-8") as f:
    elems = driver.find_elements_by_xpath(
        "//article/div/div[2]/div/div/div/div/div/div[1]/span/a")
    for elem in elems:
        elem = elem.get_attribute("href")
        f.write(elem + "\n")
