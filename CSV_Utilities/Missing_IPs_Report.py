# Missing_IPs_Report.py

import csv

# Open the source CSV file
with open('source.csv', 'r') as source_file:
    source_reader = csv.DictReader(source_file)
    source_data = list(source_reader)

# Count the total number of records and the number of missing IP addresses
total_records = len(source_data)
missing_records = 0
for row in source_data:
    if not row['IP Address']:
        missing_records += 1

# Print a summary of the total and missing records
print(f"Total records: {total_records}")
print(f"Missing IP addresses: {missing_records} ({missing_records / total_records:.2%})")

# Create a list of dictionaries for the missing IP addresses
missing_data = [row for row in source_data if not row['IP Address']]

# Write the missing data to a new CSV file sorted in alphabetical order
missing_data.sort(key=lambda row: row['hostname'])
with open('Missing_IP_Addresses.csv', 'w', newline='') as missing_file:
    fieldnames = ['hostname', 'IP Address']
    writer = csv.DictWriter(missing_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in missing_data:
        writer.writerow(row)
