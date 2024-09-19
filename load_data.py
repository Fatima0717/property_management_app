import os
import csv
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')  # Ensure this matches your project name
django.setup()

from myapp.models import Headline  # Import the model after setting up Django

def load_data():
    with open('bbc_headlines.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Headline.objects.create(title=row['Headline'], link=row['URL'])  # Ensure these match your CSV columns

if __name__ == '__main__':
    load_data()
