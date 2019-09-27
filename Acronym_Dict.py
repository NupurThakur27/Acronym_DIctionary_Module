
# coding: utf-8

# In[49]:


import string,sys
tmp_path="/".join(sys.argv[2].split("/")[:-1])
#print(tmp_path)
fi=open(tmp_path+"/Acronym_Lookup.txt",'w')
def remove_punct_from_word(word):
    #print(word, word.strip(string.punctuation))
    return(word.strip(string.punctuation))

def extract_only_words_from_sent(sent):
        all_words = sent.split(" ")
        #print(all_words)
        plain_words=[]
        for word in all_words:
            plain_words.append(remove_punct_from_word(word))
        #print(plain_words)
        while "" in plain_words:    #If E_sentence/H_sentence contains 2 sentence remove an empty word
            plain_words.remove("")
        return(plain_words)
def corpus_to_sentence(corpus):
    cor=open(corpus,"r")
    lines=cor.read().split("\n")
    return lines
def acronym():
    acr=[]
    e_lines=corpus_to_sentence(e_corpus)
    #print(e_lines)
    for i in e_lines:
        #print(i)
        e_words=extract_only_words_from_sent(i)
        #print(e_words)
        for j in e_words:
            if j.isupper() :
                if j not in acr :
                    acr.append(j)
    print(acr)
    return acr
def find_acronym():
    final=[]
    a=acronym()
    print(a)
    h_word_list=[]
    e_alpha=[]
    h_alpha=[]
    f = open(Acro_Dict, 'r')
    line= f.read()
    lines= line.split('\n')
    for i in lines :
        str1=i.split("\t")
        e_alpha+=str1[::2]  #list slicing 
        h_alpha+=str1[1::2]
    h_lines=corpus_to_sentence(h_corpus)
    for line in h_lines:
        h_words=extract_only_words_from_sent(line)
        for i in a : #English acronyms from the corpus
            h_word=""
            temp=[]
            for j in i :
                [temp.append(h_alpha[k]) for k in range(len(e_alpha)) if j == e_alpha[k]]
            h_word="".join(temp)
            h_word_list.append(h_word)
            for h in h_words :
                if h == h_word :
                    temp_str=i+" <> "+h
                    final.append(temp_str)
    for i in final :
        print(i)
        fi.write(i+"\n")
Acro_Dict="/home/nupur/internship/Acronym_DIctioary_Module/Acronym_Dict"   #Path Should be changed acc. to the path of Acronym Dict
e_corpus=sys.argv[1]
h_corpus=sys.argv[2]
find_acronym()

