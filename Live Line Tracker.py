import bs4
import requests
import csv
import time
import datetime

Times =['Stop Line', '1st Q', '2nd Q', '3rd Q', '4th Q', '1st P', '2nd P', '3rd P', 'Set 1', 'Set 2', 'Set 3','HALF', '1st H', '2nd H', 'OT1', 'OT3', 'OT4', 'OT2', 'Starts In', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th']
line = 0
total = []

def database(file_name):
    with open(file_name, 'a', newline='') as file:
        wr = csv.writer(file, dialect='excel')
        wr.writerow(total)

while True:
    sause = requests.get('https://www.sportsbook.ag/sbk/sportsbook4/tab/live.sbk')
    soup = bs4.BeautifulSoup(sause.text, 'html.parser')
    for game in soup.find_all('div', {'id': 'live-betting-table'}):
        gdata = (game.text)
        gdata = gdata.split('\n')
        gdata.append('Stop Line')
        today = str((datetime.datetime.today()))
        today = today.split('.')
        today = today[0]
        for item in gdata:
            if item != '':
                for thing in Times:
                    if item == thing:
                        if len(total) >= 4:
                            file = [total[3], ' Live Line.csv']
                            file = ''.join(file)
                            if total[1] == 'HALF':
                                pass
                            elif total[1] != 'Starts In':
                                database(file)
                            print(total)
                        line = 1
                        total = [today]
                if item == 'More' or item == 'TIME' or item == 'time':
                    line = 0
                if line == 1:
                    total.append(item)
    print('')

    time.sleep(20)
