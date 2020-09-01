import csv


def judgeThreshold(threshold):
    with open("output.csv", 'r', newline='') as csvfile:
        rows = csv.reader(csvfile)
        result = []
        for row in rows:
            alist = []
            for index in range(2, len(row)):
                if float(row[index]) >= threshold:
                    alist.append(1)
                else:
                    alist.append(0)
            result.append(alist)

    return result
