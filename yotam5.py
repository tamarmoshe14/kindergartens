import requests
from lxml import html
import xlsxwriter
from time import sleep

page_num = 1
list_main_url = []
for i in range(63):
    main_url = 'https://www.allschool.co.il/%D7%9E%D7%95%D7%A1%D7%93%D7%95%D7%AA/%D7%97%D7%99%D7%A4%D7%95%D7%A9?locality=%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91+-+%D7%99%D7%A4%D7%95&page={}'.format(page_num)
    page_num += 1
    list_main_url.append(main_url)
#now i have a list of all pages

page_count = 1
gan_count = 1
outyotam5 = xlsxwriter.Workbook("yotam5.xlsx")
outsheet = outyotam5.add_worksheet()

for page in list_main_url:
    print (page_count, len(list_main_url))
    resp = requests.get(page, headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"})
    tree = html.fromstring(html = resp.text) 
    short_links = tree.xpath('//tbody/tr/td/a/@href')
    page_count += 1
    for short_link in short_links:
        print (gan_count, len(short_links))
        full_link = "{}{}".format("https://www.allschool.co.il", short_link)
        resp2 = requests.get(full_link, headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"})
        tree2 = html.fromstring(html = resp2.text)
        try:
            name = tree2.xpath('//div[@class="page-header"]/h1/text()')[0]
        except:
            name = "name eror"
        try:
            city = tree2.xpath('//div[@class="col-sm-4"][position()=2]/div/div[position()=2]/dl/dd[position()=1]/text()')[0]
        except:
            city = "none"
        try:
            address = tree2.xpath('//div[@class="col-sm-4"][position()=2]/div/div[position()=2]/dl/dd[position()=2]/text()')[0]
        except:
            address = "no address"
        try:
            phone = tree2.xpath('//div[@class="col-sm-4"][position()=2]/div/div[position()=2]/dl/dd/a/text()')[0]
        except:
            phone = "no phone"

        outsheet.write(gan_count, 0, name)
        outsheet.write(gan_count, 1, address)
        outsheet.write(gan_count, 2, city)
        outsheet.write(gan_count, 3, phone)
        gan_count +=1

outyotam5.close()

