# -*- coding:utf-8 -*-

# read train label
standards = []

in_f = open("../../data/train_label.csv")
in_f.readline()
for line in in_f:
    term = line[:line.rindex("\t")]
    standards.append(term)
in_f.close()

# read result
in_f = open("result/result.csv")
result_terms = []
for line in in_f:
    result_terms.append(line.strip())

both = set(result_terms) & set(standards)
print len(both)
print len(result_terms)-len(both)
print len(standards)-len(both)

more_set = set(result_terms)-both
# for term in more_set:
#     print term