# -*- coding:utf-8 -*-
import jieba


if __name__ == "__main__":
    terms = jieba.cut(u"至于后来的“速腾断轴门”是属于车子质量问题，应该另当别论！。")
    if u"属于" in terms:
        print "fdsf"
    for term in terms :
        print term