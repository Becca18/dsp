def email_addresses_find_with_regex():
    import csv

    with open("faculty.csv") as f:
        t=list(csv.reader(f))
    y = [val for sublist in t for val in sublist]
    z=" ".join(y)

    import re
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', z)

    return emails


def write_emails_to_csv_file():
    import csv
    f=open("emails.csv", "w")
    t="\n".join(email_addresses_find_with_regex())
    f.write(t)
    f.close()
write_emails_to_csv_file()