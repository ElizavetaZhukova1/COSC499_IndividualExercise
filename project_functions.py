import re
def calc_sym_words_ratio(text):
    words_arr=words_tokenize(text)
    sym_count=0
    for word in words_arr:
        sym_count+=len(word)
    words_num=len(words_arr)
    if words_num<1:
        return None
    return round(sym_count/words_num,3)
def calc_words_sent_ratio(text):
    sents_arr=re.split(r"[.!?\n]", text)
    sents_arr=[i for i in sents_arr if i]
    words=words_tokenize(text)
    sents_num=len(sents_arr)
    num_words=len(words)
    if sents_num<1 or num_words<1:
        return None
    return round(num_words/sents_num,3)
def words_tokenize(u_str):
    prep_text=re.sub(r"[^a-z0-9 ]"," ",u_str.lower()) #substitute all characters other than letters, numbers and whitespaces with whitespaces
    prep_text=re.sub(r" +", " ", prep_text)
    words_arr=prep_text.split(" ")
    words_arr=[i for i in words_arr if i]
    return words_arr


