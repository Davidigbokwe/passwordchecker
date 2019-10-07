from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')

    def closeBrowser():
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_photo(self, hashtag):
	    driver = self.driver
	    driver.get("https://www.instagram.com/explore/tags/"+ hashtag + "/")
	    time.sleep(3)
	    for i in range(1, 3):
	    	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	    	time.sleep(2)
	    hrefs = driver.find_elements_by_tag_name('a')
	    pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
	    print(pic_hrefs)
	    [hrefs for href in pic_hrefs if hashtag in href]
	    print(hashtag + 'photos: ' + str(len(pic_hrefs)))

	    for pic_href in pic_hrefs:
	    	driver.get(pic_href)
	    	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	    	try:
	    		driver.find_element_by_xpath("//span[contains(@class,\"glyphsSpriteHeart\") and @aria-label = \"Like\"]//parent::button").click()
	    		time.sleep(10)
	    	except Exception as e:
	    		time.sleep(2)




davidIG = InstagramBot()
davidIG.login()
davidIG.like_photo('basketball')

