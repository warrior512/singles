#v0.0.1

import requests
from bs4 import BeautifulSoup as bS, SoupStrainer
from colorama import Fore, init
from datetime import datetime, timedelta

init(autoreset=True)

date_format = '%d.%m.%Y'


def today_date():
    return datetime.now().strftime(date_format)


def yesterday_date():
    return (datetime.now() - timedelta(days=1)).strftime(date_format)


today_rate_url = 'https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To=' + today_date()

yesterday_rate_url = 'https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To=' + yesterday_date()

req_today = requests.get(today_rate_url)
req_yesterday = requests.get(yesterday_rate_url)

print(Fore.CYAN + '''       Курс валют установленный ЦБР на ''' + today_date() + ''' 
==========================================================''')


def get_rate(req):
    soup = bS(req.text, 'html.parser', parse_only=SoupStrainer('table', class_='data'))
    return soup.find_all('td')


rate_today = get_rate(req_today)
rate_yesterday = get_rate(req_yesterday)


def soup_to_list(soup):
    list_soup = []
    list_row = []
    cnt = 0
    for i in soup:
        if cnt < 5:
            list_row.append(str(i.next_element)[:28])
            cnt += 1
            if soup[-1] == i:
                list_soup.append(list_row)
            continue
        list_soup.append(list_row)
        list_row = [str(i.next_element)[:28]]
        cnt = 1
    return list_soup


today_list = soup_to_list(rate_today)
yesterday_list = soup_to_list(rate_yesterday)


def add_dif(first_list, second_list):
    for line in today_list:
        for row in second_list:
            if row[0] == line[0]:
                dif = round((((float(str(line[4]).replace(',', '.')) / int(line[2])) - (
                        float(str(row[4]).replace(',', '.')) / int(row[2]))) * int(line[2])), 4)
                if dif < 0:
                    line.append(str(dif))
                else:
                    line.append(str(dif))
    return first_list


today_list = add_dif(today_list, yesterday_list)


def get_lens_item(some_list):
    lens = [0 for _ in range(0, len(some_list[0]))]
    x = 0
    for j in some_list:
        for i in j:
            if len(i) > lens[x]:
                lens[x] = len(i)
            x += 1
        x = 0
    return lens


def print_table(print_list):
    cyan = Fore.CYAN
    white = Fore.WHITE
    red = Fore.RED
    green = Fore.GREEN
    yellow = Fore.YELLOW
    lens = get_lens_item(print_list)
    x = 0
    y = 2
    for i in print_list:
        if y % 2 == 0:
            col = white
        else:
            col = cyan
        for j in range(6):
            if j == 5:
                x = 0
                y += 1
                if float(i[5]) < 0:
                    print(red + '↓' + str(abs(float(i[5]))))
                elif float(i[5]) > 0:
                    print(green + '↑' + i[5])
                else:
                    print(yellow + i[5])
                continue
            print(col + i[x].ljust(lens[x]), end=' ')
            x += 1


print_table(today_list)

print(Fore.CYAN + '''==========================================================
          © 2022   nikolaysmirnov86@gmail.com''')
