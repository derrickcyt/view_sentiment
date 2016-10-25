# -*- coding:utf-8 -*-


# read train ids
in_f = open("../data/Train.csv","r")
print in_f.readline()
train_ids = [line.strip().split("\t")[0] for line in in_f if len(line.strip()) > 0]

# read label ids
in_f = open("../data/Label.csv","r")
out_f = open("../data/train_label.csv","w")
out_f.write(in_f.readline())
for line in in_f:
    if line.strip().split("\t")[0] in train_ids:
        out_f.write(line)