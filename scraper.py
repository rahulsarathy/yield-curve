from urllib.request import urlopen, Request as req
from bs4 import BeautifulSoup
import json
from datetime import datetime

class DailyBond:
	def __init__(self, date, month1, month2, month3, month6, year1, year2, year3, year5, year7, year10, year20, year30):
		self.date = date
		self.month1 = month1
		self.month2 = month2
		self.month3 = month3
		self.month6 = month6
		self.year1 = year1
		self.year2 = year2
		self.year3 = year3
		self.year5 = year5
		self.year7 = year7
		self.year10 = year10
		self.year20 = year20
		self.year30 = year30

	def to_json(self):
		return json.dumps({
			'date': datetime.strftime(self.date, "%Y-%m-%d"),
			'month1': self.month1,
			'month2': self.month2,
			'month3': self.month3,
			'month6': self.month6,
			'year1': self.year1,
			'year2': self.year2,
			'year3': self.year3,
			'year5': self.year5,
			'year7': self.year7,
			'year10': self.year10,
			'year20': self.year20,
			'year30': self.year30
		})

def getXML():
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

	url = "https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData"

	toSend = req(url=url, headers=headers)

	xml = urlopen(toSend).read()

	rss_feed = BeautifulSoup(xml, 'xml')

	return rss_feed


# FOR TESTING PURPOSES UNCOMMENT
# retrieves data from text file instead of from treasury.gov

# f = open('./data_dump.txt', 'r')
# rss_feed = BeautifulSoup(f, 'xml')
# f.close()


# Retrieves data from treasury govt. Comment out if testing
rss_feed = getXML()
contents = rss_feed.find_all('content')

for content in contents:
	date = content.find('NEW_DATE').get_text()
	parsed_date = datetime.strptime(date, "%Y-%m-%dT00:00:00")

	#Some of these fields might be None or "" if it is an old date
	
	month1 = content.find('d:BC_1MONTH').get_text()
	month2 = content.find('d:BC_2MONTH').get_text()
	month3 = content.find('d:BC_3MONTH').get_text()
	month6 = content.find('d:BC_6MONTH').get_text()
	year1 = content.find('d:BC_1YEAR').get_text()
	year2 = content.find('d:BC_2YEAR').get_text()
	year3 = content.find('d:BC_3YEAR').get_text()
	year5 = content.find('d:BC_5YEAR').get_text()
	year7 = content.find('d:BC_7YEAR').get_text()
	year10 = content.find('d:BC_10YEAR').get_text()
	year20 = content.find('d:BC_20YEAR').get_text()
	year30 = content.find('d:BC_30YEAR').get_text()

	new_bond = DailyBond(parsed_date, month1, month2, month3, month6, year1, year2, year3, year5, year7, year10, year20, year30)

	print(new_bond.to_json())