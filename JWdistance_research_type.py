import csv

from pyjarowinkler import distance


def jw_distance_all_forward(a, b):
    record = [[0]*len(a) for i in range(len(b))]

    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] == b[i]:
                record[i][j] = 1
    m = 0
    t = 0
    mw = int(max(len(a), len(b)) / 2) - 1

    for i in range(len(b)):

        for front in range(mw+1):
            if i+front < len(a):
                if record[i][i+front] == 1 and front != 0:
                    m = m + 1
                    t = t + 1
                elif record[i][i+front] == 1 and front == 0:
                    m = m + 1
            else:
                break

        for back in range(1, mw+1):
            if i-back >= 0:
                if record[i][i-back] == 1:
                    m = m + 1
                    t = t + 1
            else:
                break

    t = t / 2
    if m == 0:
        simj = 0
    else:
        simj = (1/3) * (m/len(a) + m/len(b) + (m-t)/m)

    L = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i] and L < 4:
            L = L + 1

    P = 0.1

    simw = simj + L * P * (1 - simj)
    return simw


def jw_distance_all_backward(a, b):
    record = [[0]*len(a) for i in range(len(b))]

    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] == b[i]:
                record[i][j] = 1
    m = 0
    t = 0
    mw = int(max(len(a), len(b)) / 2) - 1

    for i in range(len(b)):
        for back in range(mw+1):
            if i-back >= 0:
                if record[i][i-back] == 1:
                    m = m + 1
                    t = t + 1
            else:
                break

        for front in range(1, mw+1):
            if i+front < len(a):
                if record[i][i+front] == 1 and front != 0:
                    m = m + 1
                    t = t + 1
                elif record[i][i+front] == 1 and front == 0:
                    m = m + 1
            else:
                break

    t = t / 2
    if m == 0:
        simj = 0
    else:
        simj = (1/3) * (m/len(a) + m/len(b) + (m-t)/m)

    L = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i] and L < 4:
            L = L + 1

    P = 0.1

    simw = simj + L * P * (1 - simj)
    return simw


def jw_distance_one_forward(a, b):
    record = [[0]*len(a) for i in range(len(b))]

    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] == b[i]:
                record[i][j] = 1
    m = 0
    t = 0
    mw = int(max(len(a), len(b)) / 2) - 1

    for i in range(len(b)):
        if record[i][i] == 1:
            m = m + 1
            continue

        for check in range(1, mw+1):
            if i+check < len(a):
                if record[i][i+check] == 1:
                    m = m + 1
                    t = t + 1
                    break

            if i-check >= 0:
                if record[i][i-check] == 1:
                    m = m + 1
                    t = t + 1
                    break

    t = t / 2
    if m == 0:
        simj = 0
    else:
        simj = (1/3) * (m/len(a) + m/len(b) + (m-t)/m)

    L = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i] and L < 4:
            L = L + 1

    P = 0.1

    simw = simj + L * P * (1 - simj)
    return simw


def jw_distance_one_backward(a, b):
    record = [[0]*len(a) for i in range(len(b))]

    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] == b[i]:
                record[i][j] = 1
    m = 0
    t = 0
    mw = int(max(len(a), len(b)) / 2) - 1

    for i in range(len(b)):
        if record[i][i] == 1:
            m = m + 1
            continue

        for check in range(1, mw+1):
            if i-check >= 0:
                if record[i][i-check] == 1:
                    m = m + 1
                    t = t + 1
                    break

            if i+check < len(a):
                if record[i][i+check] == 1:
                    m = m + 1
                    t = t + 1
                    break

    t = t / 2
    if m == 0:
        simj = 0
    else:
        simj = (1/3) * (m/len(a) + m/len(b) + (m-t)/m)

    L = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i] and L < 4:
            L = L + 1

    P = 0.1

    simw = simj + L * P * (1 - simj)
    return simw


def outputResult():
    with open("database.csv", 'r', newline='') as csvfile:
        rows = csv.reader(csvfile)

        with open("output.csv", 'w', newline='') as out:
            writer = csv.writer(out)

            for row in rows:
                row.append(distance.get_jaro_distance(row[0], row[1], winkler=True, scaling=0.1))
                row.append(jw_distance_all_forward(row[0], row[1]))
                row.append(jw_distance_all_backward(row[0], row[1]))
                row.append(jw_distance_one_forward(row[0], row[1]))
                row.append(jw_distance_one_backward(row[0], row[1]))
                writer.writerow(row)
