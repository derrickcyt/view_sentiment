# -*- coding:utf-8 -*-
import codecs,jieba


# read pos
pos_list = []
in_f = codecs.open(r"D:\PythonProjects\competition\view_sentiment\resource\hownet\HowNet_Sentiment_PlusSentiment_C.txt","r","gbk")
for line in in_f:
    word = line.strip().split()[0]
    pos_list.append(word)
in_f.close()
in_f = codecs.open(r"D:\PythonProjects\competition\view_sentiment\resource\hownet\HowNet_Sentiment_PlusFeeling_C.txt","r","gbk")
for line in in_f:
    word = line.strip().split()[0]
    pos_list.append(word)
in_f.close()

# read neg
neg_list = []
in_f = codecs.open(r"D:\PythonProjects\competition\view_sentiment\resource\hownet\HowNet_Sentiment_MinusFeeling_C.txt","r","gbk")
for line in in_f:
    word = line.strip().split()[0]
    neg_list.append(word)
in_f.close()
in_f = codecs.open(r"D:\PythonProjects\competition\view_sentiment\resource\hownet\HowNet_Sentiment_MinusSentiment_C.txt","r","gbk")
for line in in_f:
    word = line.strip().split()[0]
    neg_list.append(word)
in_f.close()


def cal_sentiment(content, view_list, dist_threshold=4):
    if isinstance(content, str):
        content = content.decode("utf-8")

    terms = jieba.lcut(content)
    pos_res = []
    for pos in pos_list:
        if pos in terms:
            pos_res.append((pos,content.index(pos)))
    neg_res = []
    for neg in neg_list:
        if neg in terms:
            neg_res.append((neg, content.index(neg)))
    view_res = []
    for view in view_list:
        view_res.append((view, content.index(view)))

    # find opinion word for each view
    pair_result = []
    for vr in view_res:
        min_dist = float("Inf")
        min_polarity = "neu"
        min_word = ""
        for pos in pos_res:
            dist = abs(pos[1]-vr[1])
            if dist < min_dist:
                min_dist = dist
                min_polarity = u"pos"
                min_word = pos[0]
        for neg in neg_res:
            dist = abs(neg[1] - vr[1])
            if dist < min_dist:
                min_dist = dist
                min_polarity = u"neg"
                min_word = neg[0]
        if min_dist < dist_threshold:
            pair_result.append((vr[0],min_polarity,min_word))
        else:
            pair_result.append((vr[0],u"neu",""))
    return pair_result





if __name__ =="__main__":

    import match_train
    # read train data
    in_f = codecs.open("../../data/Train.csv",'r',"utf-8")
    out_f = codecs.open("result/result.csv","w","utf-8")
    save_f = codecs.open("result/processing_result.csv","w","utf-8")
    out_f.write(u"SentenceId,View,Opinion\n")
    for line in in_f:
        arr = line.strip().split("\t")
        sentence_id = arr[0]
        content = arr[1]
        res_view = match_train.match_view(content)
        result = cal_sentiment(content,res_view,dist_threshold=4)
        print result
        # pairs_str = u"["
        pairs_str = ""
        for r in result:
            out_f.write(sentence_id+u","+r[0]+u","+r[1]+u"\n")
            # pairs_str += r[0]+u"-"+r[2]+u"-"+r[1]+u","
            pairs_str+=r[0]+","
        # pairs_str += u"]"
        save_f.write(sentence_id + u"\t" + content + u"\t" + pairs_str + u"\n")


