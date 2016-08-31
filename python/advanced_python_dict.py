def names_func():
    import csv
    f = open("faculty.csv")
    csv_f = csv.reader(f)
    names_in_list = []
    for row in csv_f:
        names_in_list.append(row[0])
    names_in_list.pop(0)
    names = []
    for i in names_in_list:
        names.append(i.split())
    return names

def last_names_func():
    last_names=[]
    for i in names_func():
        last_names.append(i[-1])
    return last_names

def first_names_func():
    first_names = []
    for i in names_func():
        first_names.append(i[0])
    return first_names

def degrees_func():
    import csv
    f = open("faculty.csv")
    csv_f = csv.reader(f)
    degrees = []
    for row in csv_f:
        degrees.append(row[1])
    degrees.pop(0)
    return degrees

def titles_func():
    import csv
    f = open("faculty.csv")
    csv_f = csv.reader(f)
    titles = []
    for row in csv_f:
        titles.append(row[2])
    titles.pop(0)
    z = " ".join(titles)
    import re
    titles = re.findall(r'Associate Professor|Assistant Professor|Professor', z)
    return titles

def emails_func():
    import csv
    f = open("faculty.csv")
    csv_f = csv.reader(f)
    emails = []
    for row in csv_f:
        emails.append(row[3])
    emails.pop(0)
    return emails

def faculty_dict():

    t=zip(last_names_func(), degrees_func(), titles_func(), emails_func())

    z=[]
    for i in t:
        z.append(list(i))

    d=dict()
    for i in last_names_func():
        d[i]=[]

    for i in z:
        d[i[0]].append(i[1:])

    first3pairs = {k: d[k] for k in d.keys()[:3]}

    print first3pairs

faculty_dict()

def professor_dict():

    first_then_last =zip(first_names_func(),last_names_func())

    t=zip(first_then_last, degrees_func(), titles_func(), emails_func())

    z=[]
    for i in t:
        z.append(list(i))

    d=dict()
    for i in z:
        if i[0] in d:
            d[i[0]].append(i[1:])
        else:
            d[i[0]]=i[1:]

    first3pairs = {k: d[k] for k in d.keys()[:3]}

    print first3pairs

professor_dict()

def professor_dict_last_name():

    first_then_last =zip(first_names_func(),last_names_func())

    t=zip(first_then_last, degrees_func(), titles_func(), emails_func())

    z=[]
    for i in t:
        z.append(list(i))

    d=dict()
    for i in z:
        if i[0] in d:
            d[i[0]].append(i[1:])
        else:
            d[i[0]]=i[1:]

    l = sorted(d, key=lambda x: x[1])
    for i in l:
        print i, d.get(i)

professor_dict_last_name()