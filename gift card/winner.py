import csv, random

emails = []

with open("gift_card_names.csv","r") as file:
    for line in csv.reader(file):
        emails.append(line[0])

# remove duplicates from the list
emails = list(set(emails))

winners_file = open('winners.txt', 'w')

for winner in range(4): 
    winners_file.write(emails[random.randrange(153)])