import jieba
from pypinyin import pinyin

def segment(text):
    segmented_words = jieba.lcut(text)
    word_list = []
    for word in segmented_words: #now lets take the hanzi and add its pinyin / # how to add a key+value to a current dict
        #{"word": word, "pinyin":pinyin(word)}
        word_dict={}
        word_dict["word"]=word

        pinyin_sounds = pinyin(word)

        final_pinyin = []

        for syllable in pinyin_sounds:
            final_pinyin.append(syllable[0]) 
        word_dict["pinyin"]= "".join(final_pinyin)
        word_list.append(word_dict)


    return word_list

print(segment("研究生命起源"))