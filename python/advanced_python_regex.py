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
    #Find degree frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

    titles_dictionary = {}
    for i in titles_in_list_func():
        if i not in titles_dictionary:
            titles_dictionary[i] = 1
        else:
            titles_dictionary[i] += 1

    titles_tuples=sorted(titles_dictionary.items())

    return titles_tuples

print titles_faculty_frequency()