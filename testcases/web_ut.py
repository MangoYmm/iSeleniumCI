import configparser
import os

import allure
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options

from iSeleniumCI.base import base


@allure.feature("web的持续集成")
class TestISelenium:
	# def get_config(self):
	# 	config = configparser.ConfigParser()
	# 	config.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'iSelenium.ini'),encoding="utf-8")
	# 	print(config)
	# 	return  config
	# def  test_envirom(self):
	# 	print(os.environ)
	#
	def setup_class(self):
		self.base = base()
		# config=self.get_config()
		# #控制是否采用无界面形式运行自动化测试
		# try:
		# 	using_headless = os.environ["using_headless"]
		# except KeyError:
		# 	using_headless = None
		# 	print("没有配置环境变量using_headless，则按照有界面方式运行自动化测试")
		#
		# chrome_option = Options()
		# if using_headless is not None and using_headless.lower()=='true':
		# 	print("使用无界面方式运行")
		# 	chrome_option.add_argument("--headless")
		# self.driver = webdriver.Chrome(executable_path=config.get('driver','chrome_driver'),
		# 							   chrome_options=chrome_option)
	@allure.story("搜索今日头条")
	def test_search1(self):
		title = self.base.search("今日头条")
		print(title)
		assert "今日头条" in title

	@allure.story("搜索王者荣耀")
	def test_search2(self):
		title = self.base.search("王者荣耀")
		print(title)
		assert "王者荣耀" in title
