import csv
from db import get_all

def export_to_csv(file_path="export.csv"):
    data = get_all()
    with open(file_path, mode='w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Имя", "Возраст"])
        writer.writerows(data)
