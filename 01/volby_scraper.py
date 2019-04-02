'''
	this script is written solely to scrape data from this website https://volby.cz/pls/ep2014/ep2111
'''

from bs4 import BeautifulSoup
import requests
import csv


url = 'https://volby.cz/pls/ep2014/ep2111?xjazyk=CZ&xv=1&xt=2&xstrana=0'


# modified code from https://realpython.com/python-csv/
def main():
	with open('elections_2014.csv', mode='w') as elections_file:
		elections_writer = csv.writer(elections_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		# names of features
		elections_writer.writerow(['číslo','název','poř. číslo','příjmení, jméno, tituly',
									'věk','Navrhující strana','Politická příslušnost','hlasy abs.',
									'hlasy %','Mandát','Pořadí'])
		r = requests.get(url)
		r.raise_for_status()
		soup = BeautifulSoup(r.text, features="html.parser")
		rows = soup.find('table', attrs={'class':'table'}).find_all('tr')
		# skip two rows, they cotaint info about table structure
		for row in rows[2:]:
			row = [each.text for each in row.find_all('td')]
			elections_writer.writerow(row)


if __name__ == '__main__':
	main()