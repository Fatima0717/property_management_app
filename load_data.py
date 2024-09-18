import csv
from myapp.models import Headline

def load_data():
    with open('bbc_headlines.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Headline.objects.create(title=row['title'], link=row['link'])

if __name__ == '__main__':
    load_data()
