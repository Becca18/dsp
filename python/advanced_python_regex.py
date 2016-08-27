def degrees_in_list_func():
    import csv
    f = open("faculty.csv")
    csv_f = csv.reader(f)

    degrees_in_list = []
    for row in csv_f:
        degrees_in_list.append(row[1].upper().replace(".", ""))
    degrees_in_list.pop(0)
    degrees_in_list.remove("0")

    degrees_in_string = " ".join(degrees_in_list)
    degrees_in_list = degrees_in_string.split()
    return degrees_in_list


def degrees_faculty_different_degrees():
    ####Find how many different degrees there are.

    degrees_in_short_list=sorted(list(set(degrees_in_list_func())))

    count=0
    for i in degrees_in_short_list:
        count+=1

    return "There are %d different degrees." % count


print degrees_faculty_different_degrees()

def degrees_faculty_frequency():
    #Find degree frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

    degrees_dictionary = {}
    for i in degrees_in_list_func():
        if i not in degrees_dictionary:
            degrees_dictionary[i] = 1
        else:
            degrees_dictionary[i] += 1

    degrees_tuples=sorted(degrees_dictionary.items())

    return degrees_tuples

print degrees_faculty_frequency()


def titles_in_list_func():
    import csv
    f = open("faculty.csv")
    csv_f = csv.reader(f)

    titles_in_list = []
    for row in csv_f:
        titles_in_list.append(row[2].upper().replace(".", ""))
    titles_in_list.pop(0)
    return titles_in_list


def different_titles():
    titles_in_short_list = sorted(list(set(titles_in_list_func())))

    count = 0
    for i in titles_in_short_list:
        count += 1

    return "There are %d different titles." % count

print different_titles()


def titles_faculty_frequency():
    #Find title frequencies

    titles_dictionary = {}
    for i in titles_in_list_func():
        if i not in titles_dictionary:
            titles_dictionary[i] = 1
        else:
            titles_dictionary[i] += 1

    titles_tuples=sorted(titles_dictionary.items())

    return titles_tuples

print titles_faculty_frequency()

#I found the email addresses in 2 different ways.

def email_addresses_find():
    import csv
    f = open("faculty.csv")
    csv_f = csv.reader(f)

    emails_in_list=[]
    for i in csv_f:
        emails_in_list.append(i[3])
    emails_in_list.pop(0)

    return emails_in_list

print email_addresses_find()

def email_addresses_find_with_regex():
    import csv

    with open("faculty.csv") as f:
        t=list(csv.reader(f))
    y = [val for sublist in t for val in sublist]
    z=" ".join(y)

    import re
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', z)

    return emails

print email_addresses_find_with_regex()

def unique_email_domains_with_regex():
    import csv

    with open("faculty.csv") as f:
        t=list(csv.reader(f))
    y = [val for sublist in t for val in sublist]
    z=" ".join(y)

    import re
    email_domains = re.findall(r'([\w\.-]+)@([\w\.-]+)', z)

    p=[]
    for i in email_domains:
        p.append(i[1])


    email_domains_list=sorted(p)
    i = 1
    n = len(email_domains_list)
    while i < n:
        if email_domains_list[i] == email_domains_list[i - 1]:
            del email_domains_list[i]
            n -= 1
        else:
            i += 1
    return email_domains_list

def number_email_domains():
    count=0
    for i in unique_email_domains_with_regex():
        count+=1
    return "There are %d different unique email domains." % count
print number_email_domains()

print unique_email_domains_with_regex()