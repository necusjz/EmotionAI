import jieba
import xlrd
import math
from sklearn import svm
stop_word=[]
state=[]
pos=0
neg=0
word_pos={}
word_neg={}
words={}
clf = svm.SVC(probability=True)
#反义词
inverse=['不','没','无','非','莫','弗','毋','未','否','别','不够','不是','不曾','未必','不要','难以','未曾','还']
#分词后的句子表示
data_orginal=[]
data=[]
feature_word=[]
#训练集
trainning_feature=[]
trainning_state=[]
#测试集
test_feature=[]
test_state=[]
#选择多少特征词汇
feature_rate=0.6
trainning_rate=1

#特征表示
feature_express=[]
#加载文件
def load(file):
    global pos,neg
    table = xlrd.open_workbook(file).sheets()[0]
    data_xls = table.nrows
    for x in range(data_xls):
        category = table.cell(x, 7).value
        if category == 1:
            state.append(1)
            pos = pos + 1
            part_word2(table.cell(x, 9).value, data_orginal, category)
        elif category == 2:
            state.append(2)
            neg = neg + 1
            part_word2(table.cell(x, 9).value, data_orginal, category)


# 测试分词
def test(sentence, temp):
    seg_list = jieba.cut(sentence, cut_all=False)
    temp_sentence = list(seg_list)
    sum = 0
    pre = ''
    for i in temp_sentence:
        # 单词
        j = i.strip()
        if j in inverse:
            pre = j
            continue
        elif (j+'\n' in stop_word) == False and (pre in inverse) == False:
            sum = sum+1
            if j in temp:
                temp[j] = temp[j]+1
            else:
                temp[j] = 1
    # 双词
        later = j
        j = pre + j
        if (j + '\n' in stop_word) == False and pre != '':
            sum = sum + 1
            if j in temp:
                temp[j] = temp[j] + 1
            else:
                temp[j] = 1
                pre = later
        else:
            pre = ''
    #一句评论总词数
    temp['count'] = sum
    print(temp)


# 测试分词
def test1(sentence, temp):
    seg_list = jieba.cut(sentence, cut_all=False)
    temp_sentence = list(seg_list)
    sum = 0
    pre = ''
    leap1 = []
    stop_word1 = ['，', '。', '!', '！', '？', '?']
    for i in temp_sentence:
        # 单词
        j = i.strip()
        if j in stop_word1:
            continue
        pre = j
        # leap1.append(j)
        sum = sum + 1
        if j in temp:
            temp[j] = temp[j] + 1
        else:
            temp[j] = 1
            leap1.append(j)
    leap = leap1
    for m in range(len(leap)):
        # 双词
        if m < (len(leap1) - 1):
            n = leap1[m] + leap1[m + 1]
            # leap.append(n)
            sum = sum + 1
            if n in temp:
                temp[n] = temp[n] + 1
            else:
                temp[n] = 1
                leap.append(n)
    # 一句评论总词数
    temp['count'] = sum
    print(temp)


# 分词,统计每个词汇出现的文档次数
def part_word(sentence,express,category):
    seg_list=jieba.cut(sentence,cut_all=True)
    temp_sentence=list(seg_list)
    temp_set_sentence=set()
    temp={}
    leap=[]
    sum=0
    pre=''
    for i in temp_sentence:
        #单词
        j=i.strip()
        if j in inverse:
            pre=j
            continue
        elif (j+'\n' in stop_word)==False and (j in inverse)==False:
            leap.append(j)
            temp_set_sentence.add(j)
            sum=sum+1
            if j in temp:
                temp[j]=temp[j]+1
            else:
                temp[j]=1
        #双词
        later=j;
        j=pre+j
        if (j + '\n' in stop_word) == False and pre!='':
            leap.append(j)
            temp_set_sentence.add(j)
            sum = sum + 1
            if j in temp:
                temp[j] = temp[j] + 1
            else:
                temp[j] = 1
        pre=later
    else:
        pre=''
    #一句评论总词数
    temp['count']=sum
    express.append(temp)
    data.append(leap)
    for i in temp_set_sentence:
        j=i.strip()
        words[j]=0
        if j:
            if category==1:
                if (j in word_pos)==True:
                    word_pos[j]=word_pos[j]+1
                else:
                    word_pos[j]=1
            if category==2:
                if (j in word_neg)==True:
                    word_neg[j]=word_neg[j]+1
                else:
                    word_neg[j]=1


def part_word2(sentence,express,category):
    temp_set_sentence = set()
    temp = {}
    leap1 = []
    sum = 0
    _pre = ''
    stop_word1 = ['，', '。', '!', '！', '？', '?']
    seg_list = jieba.cut(sentence, cut_all=False)
    temp_sentence = list(seg_list)
    for i in temp_sentence:
        # 单词
        j = i.strip()
        if j in stop_word1:
            continue
        _pre = j
        # leap1.append(j)
        # temp_set_sentence.add(j)
        sum = sum + 1
        if j in temp:
            temp[j] = temp[j] + 1
        else:
            temp[j] = 1
            leap1.append(j)
            temp_set_sentence.add(j)
    leap = leap1
    for m in range(len(leap)):
        # 双词
        if m < (len(leap1) - 1):
            n = leap1[m] + leap1[m + 1]
            # leap.append(n)
            # temp_set_sentence.add(n)
            sum = sum + 1
            if n in temp:
                temp[n] = temp[n] + 1
            else:
                temp[n] = 1
                leap.append(n)
                temp_set_sentence.add(n)
    # 一句评论总词数
    temp['count'] = sum
    express.append(temp)
    data.append(leap)
    for i in temp_set_sentence:
        j = i.strip()
        words[j] = 0
        if j:
            if category == 1:
                if j in word_pos:
                    word_pos[j] = word_pos[j] + 1
                else:
                    word_pos[j] = 1
            if category == 2:
                if j in word_neg:
                    word_neg[j] = word_neg[j] + 1
                else:
                    word_neg[j] = 1
#信息增益(IG)
########################3
#def information():
#    ans = open('information_add.txt', 'w', encoding='utf-8')
#    for i in words:
#        #p(t)
#        postive=0
#        negative=0
#        if (i in word_pos)==True:
#            postive=word_pos[i]
#        if (i in word_neg)==True:
#            negative=word_neg[i]
#        k1=((postive+negative)/(pos+neg))
#        k2=0
#        if postive!=0:
#            k2=(postive/pos)*(math.log(postive/pos))
#        k3=0
#        if negative!=0:
#           k3=(negative / neg) * (math.log(negative / neg))
        #p(~t)
#        k4=1-k1
#        k5=0
#        if postive!=0:
#            k5=(1-(postive/pos))*(math.log((1-postive/pos)))
#        k6=0
#        if negative!=0:
#            k6=(1 - (negative / neg)) * (math.log((1 - negative / neg)))
        #计算信息熵
#        words[i]=k1*(k2+k3)+k4*(k5+k6)+1
#    ans.close()

#按照信息熵排序
def sort_words():
    '''
    tmp=sorted(words.items(),key=lambda item:item[1],reverse=True)
    sum=0
    lens=len(tmp)*feature_rate
    for i in tmp:
        if sum>lens:
            break
        feature_word.append(i[0])
        sum=sum+1
    print("特征词数量:"+str(lens))
    ans1=open('tezheng.txt', 'w', encoding='utf-8')
    for i in feature_word:
        ans1.write(i+':'+str(words[i])+'\n')
    ans1.close();
    '''
    ans2 = open('tongji.txt', 'w', encoding='utf-8')
    for i in words:
        s=0
        if i in word_neg:
            s=s+word_neg[i]
        if i in word_pos:
            s=s+word_pos[i]
        if s>5 :
            ans2.write(i+':'+str(s)+'\n')
            feature_word.append(i)
    ans2.close()


#文本表示
def text_express(senentence, feature_express):
    leap=[]
    flag=0
    for i in feature_word:
        tmp=1
        for j in senentence:
            if i==j:
                s1=senentence[j]/senentence['count']
                m1=0
                m2=0
                if i in word_pos:
                    m1=word_pos[i]
                if i in word_neg:
                    m2=word_neg[i]
                s2=math.log((pos+neg)/(m1+m2+1))
                s3=s1*s2
                leap.append(s3)
#                leap.append(1)
                tmp=0
        if tmp==1:
            leap.append(0)
    feature_express.append(leap)

#得到训练集和测试集
def trainning():
    s1=math.floor((len(feature_express)*trainning_rate))
    s2=math.floor((len(state)*trainning_rate))
    j=0
    for i in feature_express:
        if j>s1:
            test_feature.append(i)
        else:
            trainning_feature.append(i)
        j=j+1
    j=0
    for i in state:
        if j>s2:
            test_state.append(i)
        else:
            trainning_state.append(i)
        j=j+1

##########################################################################################################3
#读入评论数据
def start():
    load('MovieComments2016-09-13_13_29_47.704000.xls')
    load('du1.xls')
    load('guo.xls')
    # load('yang.xls')
#读入停用词
    data_stop_word=open('stop_word.txt','r',encoding='utf-8')
#把停用词读入list
    while True:
        i=data_stop_word.readline()
        if i:
            stop_word.append(i)
        else:
            break
    stop_word_test=open('test_stopword.txt', 'w', encoding='utf-8')
    for i in stop_word:
        stop_word_test.write(i+'\n')
    stop_word_test.close()

#特征选择
#information()
#排序
    sort_words()
#print(data_orginal)
#print(data)
#文本表示
#ans = open('text_express.txt', 'w', encoding='utf-8')
    for i in data_orginal:
    #print(i)
        text_express(i,feature_express)
#ans = open('text_express.txt', 'w', encoding='utf-8')
#l=0
#打印出特征表示阵列
#for i in feature_express:
#    ans.write(str(l)+':   ')
#    for j in i:
#        ans.write(str(j)+',')
#    ans.write(str(state[l])+'\n')
#    l=l+1
#ans.close()
#打印训练集和测试集
    trainning()
    clf.fit(trainning_feature, trainning_state)
#ok=open('trainning.txt','w',encoding='utf-8')
#for i in trainning_state:
#    ok.write(str(i)+',')
#    ok.write('\n')
#ok.close()
#ko=open('test.txt','w',encoding='utf-8')
#for i in test_state:
#    ko.write(str(i)+',')
#    ko.write('\n')
#ko.close()

def machine_learning(example):
#机器学习svm
    # clf.fit(trainning_feature,trainning_state)
    #results=clf.predict_proba(test_feature)
    #result=[]
    #for i in results:
    #    if i[0]>i[1]:
    #        result.append(1)
    #    else:
    #        result.append(2)

    #j=0
    #sum=0
    #for i in result:
    #    if test_state[j]==i:
    #        sum=sum+1
    #    j=j+1
    #print('准确率:'+str(sum/len(result)))

    print('文档数量'+str(pos+neg)+'  积极文档'+str(pos)+'   消极数量'+str(neg))
    ok = {}             # 词频字典
    test(example, ok)
    ck = []             # 权重列表
    text_express(ok, ck)
    res = clf.predict_proba(ck)     # 预测结果
    print(res)
    print(type(res))
    return res

# start()
# machine_learning('不是太好看')