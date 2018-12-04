import csv

#Game Information
League = 'NFL'
Team1 = 'New Orleans'
Team2 = 'Minnesota'
Date = '2018-10-28'


if League == 'NCAAF':
    T2L = 9
elif League == 'NBA' or League == 'NHL' or League == 'NFL':
    T2L = 10
elif League == 'MLB':
    T2L = 11
last_row = 0
new_file = ['I:\\Coding Projects\\Sports Betting\\Games\\', League, ' Games\\', Date, ' ', League, ' ', Team1, ' V ', Team2, '.csv']
new_file = ''.join(new_file)
open_file = [League,' Live Line.csv']
open_file = ''.join(open_file)
csv_file = csv.reader(open(open_file, "r"), delimiter=",")
last_row = ['','','','']
for row in csv_file:
    if row[T2L] == Team2 and row[4] == Team1 and row[0].startswith(Date):
        if row[2] == last_row[2] and League != 'MLB':
            pass
        else:
            with open(new_file, 'a', newline='') as file:
                wr = csv.writer(file, dialect='excel')
                wr.writerow(row)
        last_row = row

