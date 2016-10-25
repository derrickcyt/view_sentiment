# -*- coding:utf-8 -*-
import re


def check_if_num(to_check):
    return re.match(r"^\d+$",to_check)


def check_redundant_view(rv):
    new_res = []
    for v1 in rv:
        is_redundant = False
        for v2 in rv:
            if v1 != v2 and v1 in v2:
                is_redundant = True
                break
        if not is_redundant:
            new_res.append(v1)
    return new_res

# read view lexicon
view_list = []
in_f = open("../../data/View.csv")
for line in in_f:
    arr = line.strip().split("\t")
    if not check_if_num(arr[1]):
        view_list.append(arr[1])
in_f.close()

# read train data
in_f = open("../../data/Test.csv",'r')
out_f = open("result/result_test.csv","w")
for line in in_f:
    arr = line.strip().split("\t")
    sentence_id = arr[0]
    content = arr[1]
    res_view = []
    for view in view_list:
        if view in content:
            res_view.append(view)
    res_view = check_redundant_view(res_view)
    for view in res_view:
        out_f.write(sentence_id+"\t"+view+"\n")





