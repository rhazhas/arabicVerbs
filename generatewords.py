import random as rd
arabic_letters=['أ','ب','د','ه','و','ز','ح','ط','ي','ك','ل','م','ن','س','ع','ف','ص','ق','ر','ش','ت','ث','خ','ذ','و','ض','ظ','غ']
nbCount=3
max_words=20
meaningful_verbs = []
meaningless_verbs = []
i=0
while i<max_words:
    word="".join(rd.sample(arabic_letters,nbCount))
    if (word not in meaningless_verbs) and (word not in meaningful_verbs):
        print(str(i+1)+"->"+word)
        ok=False
        while not ok:
            resp=input ("meaningful :1\nmeaningless:2\nyour choice :")
            if resp in "12":
                if resp=='1':
                    meaningful_verbs.append(word)
                else:
                    meaningless_verbs.append(word)
                i+=1
                ok=True
print ("Liste of meaningless words :\n",meaningless_verbs)
print ("Liste of meaningfull words :\n",meaningful_verbs)
