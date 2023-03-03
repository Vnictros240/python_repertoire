import re
import csv

# Define the regular expression pattern to match hostnames
pattern = r"^[a-zA-Z0-9\-]{12,13}"

# Open the source CSV file and create a dictionary of hostnames and IP addresses
with open('source.csv', 'r') as source_file:
    source_reader = csv.DictReader(source_file)
    source_data = {}
    for row in source_reader:
        hostname = row['hostname']
        ip_address = row['IP Address']
        source_data[hostname] = ip_address

# Open the mess CSV file and create a list of dictionaries
with open('mess.csv', 'r') as mess_file:
    mess_reader = csv.DictReader(mess_file)
    mess_data = list(mess_reader)

# Loop through the mess data and try to find a match in the source data
for row in mess_data:
    hostname = row['hostname']
    ip_address = row['IP Address']
    if not ip_address:  # Only update if IP address is missing
        try:
            # Use regular expression to match the hostname in source data
            match = None
            for source_hostname in source_data.keys():
                if re.match(pattern, source_hostname) and re.match(pattern, hostname) and \
                        source_hostname.lower() == hostname.lower():
                    match = source_hostname
                    break
            if match:
                # Update the IP address in the mess data
                row['IP Address'] = source_data[match]
        except Exception as e:
            # Append error message to a separate file
            with open('errors.txt', 'a') as error_file:
                error_file.write(f"Error: {e}\n")

# Write the updated mess data to a new CSV file
with open('output.csv', 'w', newline='') as output_file:
    fieldnames = ['hostname', 'IP Address']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in mess_data:
        writer.writerow(row)
