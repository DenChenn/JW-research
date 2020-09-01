import csv


def wrongStr(a_string):
    replace_word = 'a'
    for i in range(25):
        flag = 0
        for j in range(len(a_string)):
            if a_string[j] == replace_word:
                flag = 1
                break
        if flag == 0:
            break
        else:
            replace_word = chr(ord(replace_word)+1)
            continue

    seperate_string = []
    for i in range(len(a_string)):
        seperate_string.append(a_string[i])

    wrong_string_list = []
    for i in range(len(a_string)):
        seperate_string[len(a_string)-1-i] = replace_word
        temp = ""
        for j in range(len(a_string)):
            temp = temp + str(seperate_string[j])
        wrong_string_list.append(temp)

    return wrong_string_list


def generateDatabase():
    with open("input.csv", 'r') as enter:

        rows = csv.reader(enter)

        database = []
        for row in rows:
            wrong_string_list = wrongStr(row[0])
            for s in wrong_string_list:
                example = []
                example.append(row[0])
                example.append(s)
                database.append(example)

    with open("database.csv", 'w', newline='') as out:
        writer = csv.writer(out)
        writer.writerows(database)
