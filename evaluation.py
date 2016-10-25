# -*- coding:utf-8 -*-
from __future__ import division


def evaluate(result_path, standard_path):
    standards = {}
    in_f = open(standard_path)
    in_f.readline()
    for line in in_f:
        arr = line.strip().split("\t")
        term = arr[0] + " " + arr[1]
        polarity = arr[2]
        standards[term] = polarity
    in_f.close()
    # read result
    in_f = open(result_path)
    result_terms = {}
    in_f.readline()
    for line in in_f:
        arr = line.strip().split(",")
        term = arr[0] + " " + arr[1]
        polarity = arr[2]
        result_terms[term] = polarity

    both = set(result_terms.keys()) & set(standards.keys())
    fn1 = len(set(standards.keys()) - both)
    more_set = set(result_terms.keys()) - both
    fn2 = len(more_set)

    for more in more_set:
        print more

    tp = 0
    fp = 0
    for term, polarity in result_terms.items():
        if term in standards:
            if polarity == standards[term]:
                tp += 1
            else:
                fp += 1

    print fn1, fn2, tp, fp

    P = tp / (tp + fp + fn2)
    R = tp / (tp + fn1)
    F1 = 2 * P * R / (P + R)
    print P, R, F1


if __name__ == "__main__":
    sp = "data/train_label.csv"
    rp = "experiment/simple_match/result/result.csv"
    evaluate(rp, sp)
