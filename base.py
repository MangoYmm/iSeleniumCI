import configparser
import os
import time

from selenium.webdriver.chrome.options import Options
from selenium import  webdriver

class base:
	def get_config(self):
		config = configparser.ConfigParser()
		config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)),'iSelenium.ini'),encoding="utf-8")
		print(config)
		return  config
	def __init__(self):
		self.config=self.get_config()
		#控制是否采用无界面形式运行自动化测试
		try:
			print(os.environ)
			using_headless = os.environ["using_headless"]
		except KeyError:
			using_headless = None
			print("没有配置环境变量using_headless，则按照有界面方式运行自动化测试")

		chrome_option = Options()
		if using_headless is not None and using_headless.lower()=='true':
			print("使用无界面方式运行")
			chrome_option.add_argument("--headless")
		self.driver = webdriver.Chrome(executable_path=self.config.get('driver','chrome_driver'),
									   chrome_options=chrome_option)
	def search(self,keywords):
		self.driver.get(self.config.get('driver','url'))
		time.sleep(3)
		self.driver.maximize_window()
		self.driver.find_element_by_id('kw').send_keys(keywords)
		self.driver.find_element_by_id('su').click()
		time.sleep(5)
		title  = self.driver.title
		return  title
