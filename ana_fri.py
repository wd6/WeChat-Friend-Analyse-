# encoding=utf-8
# bian ma wen ti 
import sys
sys.path.append("/Users/wonder/anaconda/lib/python2.7/site-packages")
import itchat
itchat.login()
friends = itchat.get_friends(update=True)[0:]
male = female = other = 0
for i in friends[1:]:
    sex=i['Sex']
    if sex == 1:
        male = male+1
    elif sex == 2 :
        female = female+1
    else:
        other = other+1
total=len(friends[1:])
print 'Male friends:%.2f%%' % (float(male)/total*100)
print 'Female friends:%.2f%%' % (float(female)/total*100)
print total


def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable
NickName = get_var('NickName')
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Sinature = get_var('Signature')
from pandas import DataFrame
data = {'NickName':NickName, 'Sex':Sex, 'Province':Province, 'City':City,'Signature':Sinature}
frame = DataFrame(data)
frame.to_csv('data.csv',index=True)


import re
siglist = []
for i in friends:
    signature = i['Signature'].strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile ("lf\d+\w*|[<>/=]")
    signature = rep.sub("",signature)
    siglist.append(signature)
text = "".join(siglist)

import jieba
wordlist = jieba.cut(text,cut_all=True)
word_space_split = "".join(wordlist)

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
coloring = np.array(Image.open("Users/apple/Desktop/wechat.jep"))
my_wordcloud = WordCloud(backgroud_color="white",max_words=2000,mask=coloring,max_font_size=60,random_state=42,scale=2).generate(word_space_split)
image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
