import csv

def merge_csv(csv_list, output_path):
    # build list with all fieldnames
    fieldnames = []
    for file in csv_list:
        with open(file, "r", encoding="utf-8") as input_csv:
            field = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(f for f in field if f not in fieldnames)
            
    # write data to output file based on field fieldnames
    with open(output_path, "w", encoding="utf-8", newLine="") as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file, "r", encoding="utf-8") as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)