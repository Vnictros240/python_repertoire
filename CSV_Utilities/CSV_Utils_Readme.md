# Python Tools used to acess and automate bulk data in CSV files

## Python Utilities
### - [fill_in_IPs.py](https://github.com/Vnictros240/python_repertoire/blob/master/CSV_Utilities/fill_in_IPs.py)
#### fill_in_IPs.py Breakdown: 
   1. We define the regular expression pattern to match hostnames.
   2. We open the source CSV file and create a dictionary of hostnames and IP addresses.
   3. We open the mess CSV file and create a list of dictionaries.
   4. We loop through the mess data and try to find a match in the source data.
   5. If we find a match, we update the IP address in the mess data.
   6. If there is an error, we append the error message to a separate file.
   7. We write the updated mess data to a new CSV file.

Note that the code handles cases where the IP address is already present in the mess data (i.e., the IP Address field is not empty), and also handles cases where there are multiple matches in the source data (i.e., it picks the first match found).

Also note that the try and except blocks are used to handle errors gracefully and append error messages to a separate file. This is useful for debugging and troubleshooting.

### - [Missing_IPs_Report.py](https://github.com/Vnictros240/python_repertoire/blob/master/CSV_Utilities/Missing_IPs_Report.py)
#### Missing_IPs_Report.py Breakdown:
  1.  It opens the CSV file "source.csv" using csv.DictReader() and reads its contents into a list of dictionaries called source_data.
  2.  It counts the total number of records and the number of missing IP addresses by looping over source_data and checking the IP Address field of each row.
  3.  It prints a summary of the total and missing records using f-strings.
  4.  It creates a new list of dictionaries called missing_data that contains only the rows with missing IP addresses.
  5.  It sorts missing_data alphabetically by hostname.
  6.  It writes missing_data to a new CSV file called "Missing_IP_Addresses.csv" using csv.DictWriter(). This function writes the header row using the fieldnames argument and then writes each row in missing_data using writer.writerow(). The newline='' argument is used to ensure that the file is written with the correct line endings for the platform you're running on.
