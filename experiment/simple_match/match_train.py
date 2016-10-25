# -*- coding:utf-8 -*-
import re,codecs


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


def view_complete(rv,content):
    new_rv=[]
    for v in rv:
        complete = find_num_char_after(v,content)
        after_complete = v+complete
        if len(after_complete)<=10:
            if complete and re.match(ur"^[A-Za-z0-9_]+$",after_complete):
                continue
            new_rv.append(after_complete)
        else:
            new_rv.append(v)
    return new_rv


def find_num_char_after(view,content):
    regex1 = ur"[A-Za-z0-9_]+"
    # check if view end with num or char
    is_end_with_nc = False
    result = re.findall(regex1,view)
    for r in result:
        if view.rindex(r)+len(r) == len(view):
            is_end_with_nc = True
    if not is_end_with_nc:
        return ""

    regex = ur"[A-Za-z0-9_]+"
    after_str = content[content.index(view)+len(view):]
    result = re.findall(regex,after_str)
    if result:
        for r in result:
            if after_str.index(r) == 0:
                return r
    return ""




# read view lexicon
view_list = []
in_f = codecs.open("../../data/View.csv","r","utf-8")
must_not_strs = [u"汽车"]
for line in in_f:
    arr = line.strip().split("\t")
    is_view = True
    for must_not in must_not_strs:
        if must_not in arr[1]:
            is_view = False
    if not check_if_num(arr[1]) and is_view:
        view_list.append(arr[1].upper())
in_f.close()


def match_view(content):
    res_view = []
    temp_content = content.upper()
    for view in view_list:
        if view in temp_content:
            # find real str
            view_index = temp_content.index(view)
            real_view = content[view_index:view_index+len(view)]
            res_view.append(real_view)
    res_view = check_redundant_view(view_complete(res_view,content))
    return res_view


if __name__ == "__main__":
    print match_view(u"斯柯达速派，设计充满力量感，更年轻更动感，TSI DSG的黄金动力组合让人享受如赛场上的激情拼搏。")





