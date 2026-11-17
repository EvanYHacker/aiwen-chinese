import jieba

words = jieba.lcut("研究生命起源")
print(words)
print(type(words))
print(len(words))


from pypinyin import pinyin

print(pinyin("研究"))