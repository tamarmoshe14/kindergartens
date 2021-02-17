import json
import requests
from lxml import html
import xlsxwriter
from time import sleep

x = 1
page_count = 1
gan_count = 1
outyotam3 = xlsxwriter.Workbook("yotam3.xlsx")
outsheet = outyotam3.add_worksheet()

while x < 81:
        resp = requests.get(url = "https://api.infogan.co.il/api/garden-search-by-address?address=%D7%AA%D7%9C%20%D7%90%D7%91%D7%99%D7%91%20%D7%99%D7%A4%D7%95&page={}".format(x), headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"})
        tree = resp.json()
        x+=1
        page_count+=1
        print ("page {}".format(page_count))
        dict1 = tree["_embedded"]
        list_of_gans = dict1["garden_search_by_address"]
        for y in list_of_gans:
            gan_count+=1
            print (gan_count, len(list_of_gans))
            outsheet.write(gan_count, 0, y["name"])
            try:
                outsheet.write(gan_count, 1, y["goldNumber"])
            except:
                outsheet.write(gan_count, 1, "no phone")
            try:
                outsheet.write(gan_count, 2, y["street"])
            except:
                outsheet.write(gan_count, 2, "none")
            try:
                outsheet.write(gan_count, 3, y["houseNumber"])
            except:
                outsheet.write(gan_count, 3, "none")
            try:
                outsheet.write(gan_count, 4, y["city"])
            except:
                outsheet.write(gan_count, 4, "none")


outyotam3.close()

  

