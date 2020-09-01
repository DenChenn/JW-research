import csv

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

from threshold_set import judgeThreshold


def statisticCal():
    threshold = 0.8
    x = []
    y_1_ac = []
    y_2_ac = []
    y_3_ac = []
    y_4_ac = []

    y_1_F1 = []
    y_2_F1 = []
    y_3_F1 = []
    y_4_F1 = []

    for i in range(11):
        actual = []
        predict_1 = []
        predict_2 = []
        predict_3 = []
        predict_4 = []
        rows = judgeThreshold(threshold)
        x.append(threshold)
        threshold = threshold + i*0.01

        for row in rows:
            actual.append(row[0])
            predict_1.append(row[1])
            predict_2.append(row[2])
            predict_3.append(row[3])
            predict_4.append(row[4])

        tn_1, fp_1, fn_1, tp_1 = confusion_matrix(actual, predict_1, labels=[0, 1]).ravel()
        tn_2, fp_2, fn_2, tp_2 = confusion_matrix(actual, predict_2, labels=[0, 1]).ravel()
        tn_3, fp_3, fn_3, tp_3 = confusion_matrix(actual, predict_3, labels=[0, 1]).ravel()
        tn_4, fp_4, fn_4, tp_4 = confusion_matrix(actual, predict_4, labels=[0, 1]).ravel()

        accuracy_1 = (tp_1+tn_1)/(tp_1+fp_1+fn_1+tn_1)
        accuracy_2 = (tp_2+tn_2)/(tp_2+fp_2+fn_2+tn_2)
        accuracy_3 = (tp_3+tn_3)/(tp_3+fp_3+fn_3+tn_3)
        accuracy_4 = (tp_4+tn_4)/(tp_4+fp_4+fn_4+tn_4)
        y_1_ac.append(accuracy_1)
        y_2_ac.append(accuracy_2)
        y_3_ac.append(accuracy_3)
        y_4_ac.append(accuracy_4)

        precision_1 = tp_1/(tp_1+fp_1)
        precision_2 = tp_2/(tp_2+fp_2)
        precision_3 = tp_3/(tp_3+fp_3)
        precision_4 = tp_4/(tp_4+fp_4)

        recall_1 = tp_1/(tp_1+fn_1)
        recall_2 = tp_2/(tp_2+fn_2)
        recall_3 = tp_3/(tp_3+fn_3)
        recall_4 = tp_4/(tp_4+fn_4)

        F1_1 = 2 / ((1 / precision_1) + (1 / recall_1))
        F1_2 = 2 / ((1 / precision_2) + (1 / recall_2))
        F1_3 = 2 / ((1 / precision_3) + (1 / recall_3))
        F1_4 = 2 / ((1 / precision_4) + (1 / recall_4))
        y_1_F1.append(F1_1)
        y_2_F1.append(F1_2)
        y_3_F1.append(F1_3)
        y_4_F1.append(F1_4)

    plt.title("JW analysis")
    plt.xlabel("threshold")
    plt.ylabel("ACC")
    plt.plot(x, y_1_ac, '--o')
    plt.plot(x, y_2_ac, '--o')
    plt.plot(x, y_3_ac, '--o')
    plt.plot(x, y_4_ac, '--o')

    plt.savefig("D:\data\Desktop\ACC.png")
    plt.figure()

    plt.title("JW analysis")
    plt.xlabel("threshold")
    plt.ylabel("F1")
    plt.plot(x, y_1_F1, '--o')
    plt.plot(x, y_2_F1, '--o')
    plt.plot(x, y_3_F1, '--o')
    plt.plot(x, y_4_F1, '--o')
    plt.savefig("D:\data\Desktop\F1.png")
