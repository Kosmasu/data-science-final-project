import hashlib
import csv



with open("Daily Received.csv", newline="") as infile, open("Daily Received_1.csv", "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        row["Customer"] = hashlib.sha256(row["Customer"].encode()).hexdigest()[:8]
        row["Sale Employee"] = hashlib.sha256(row["Sale Employee"].encode()).hexdigest()[:8]
        writer.writerow(row)