# 단어 공부 - String

import sys

word = list(sys.stdin.readline().rstrip().upper())

word_dict={}
for w in word:
    if w not in word_dict:
        word_dict[w]=1
    else:
        word_dict[w]+=1
words=sorted(word_dict.items(), key=lambda x:x[1])
if len(words)>1 and words[-1][1]==words[-2][1]:
    print('?')
else:
    print(words[-1][0])