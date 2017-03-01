# coding:UTF-8
import urllib
import urllib2
import bs4
from bs4 import BeautifulSoup
import re
import sys

import sys_config
import user_config

reload(sys)
sys.setdefaultencoding('UTF-8')

"""

获取http://bj.lianjia.com/ershoufang/页面的房价信息

Created on 2017-02-28

@author: starinbrook

"""
def setProxy(enable_proxy):
	if enable_proxy:
		print "set proxy : " + sys_config.PROXY_ADDRESS
		proxy_handler = urllib2.ProxyHandler({"http":sys_config.PROXY_ADDRESS})
		opener = urllib2.build_opener(proxy_handler)
	else:
		null_proxy_handler = urllib2.ProxyHandler({})
		opener = urllib2.build_opener(null_proxy_handler)
	urllib2.install_opener(opener)

def get_page_html(url):
	values = {}
	data = urllib.urlencode(values)
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}
	request = urllib2.Request(url,data,headers)
	try:
		response = urllib2.urlopen(request,timeout=20)
		return response.read()
	except urllib2.HTTPError,e:
		print e.code
	except urllib2.URLError,e:
		print e.reason
	else :
		print 'OK'

def find_href(str):
	return re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,str)

def page_process(html,output_fpath):

	# 输出文件路径
	fout = open(output_fpath, "a")

	soup = BeautifulSoup(html,'html.parser',from_encoding="UTF-8")
	for node in soup.find_all('li',class_='clear'):
		house_soup = BeautifulSoup(str(node),'html.parser',from_encoding='UTF-8')
		node_title = house_soup.select('div[class="title"]')
		node_address = house_soup.select('div[class="address"]')
		node_flood = house_soup.select('div[class="flood"]')
		node_taxfree = house_soup.select('div[class="taxfree"]')
		node_priceInfo = house_soup.select('div[class="totalPrice"]')
		print "简介：" + node_title[0].get_text() + "\n总价：" + node_priceInfo[0].get_text() + "\n链接：" + find_href(str(node))[0]
		print "==========================================================="
		fout.write("\n简介：" + node_title[0].get_text() + "\n总价：" + node_priceInfo[0].get_text() + "\n链接：" + find_href(str(node))[0] + "\n===========================================================")

	fout.flush()
	fout.close()

def get_url_params():
	params = ""
	params += user_config.setting['heating']
	params += user_config.setting['decoration']
	params += user_config.setting['elevator']
	params += user_config.setting['type']
	params += user_config.setting['years']
	params += user_config.setting['orientation']
	params += user_config.setting['floor']
	params += user_config.setting['purpose']
	params += user_config.setting['layout']
	params += user_config.setting['area']
	params += user_config.setting['price']
	return params

def main():
	setProxy(sys_config.ENABLE_PROXY) # 设置代理
	output_fpath = "./outputs/%s" % user_config.setting["output_fname"]
	page_number = int(user_config.setting['page_number'])
	url = sys_config.REQUEST_URL
	regions = user_config.setting['region']
	params = get_url_params()
	for region in regions:
		print region
		real_url = ""
		real_url = url + region + "/" + params

		for x in xrange(1,page_number+1):
			real_url_pg = ""
			real_url_pg = real_url + "pg" + str(x) + "/"
			html = get_page_html(real_url_pg) # 获取页面文档
			page_process(html,output_fpath) # 处理页面并将结果保存到指定文件
		print ""

if __name__ == '__main__':
	main()