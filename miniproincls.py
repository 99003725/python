import re
class project:
    def __init__(self):
        self.file = open("text.txt","r")                                  
        self.no_words=int(input("no of words to be searched"))
        self.count=0 
    def readfile(self):
        TEXT_FILE=self.file.read()
        while self.no_words > self.count:
            input_word=input("enter the word to be searched:")
            file2 = open(input_word+".txt",'a')
            pattern = re.findall(input_word, TEXT_FILE,re.M|re.I)
            if pattern:
                file2.write("count:"+str(len(pattern)))
                w=TEXT_FILE.split()
                TEXT_WORDS=re.split('\W',str(w))
                TEXT_WORDS = list(filter(None, TEXT_WORDS))
                TEXT_WORD_LENGTH=len(TEXT_WORDS)
                for i in range(0,TEXT_WORD_LENGTH):
                    output=re.fullmatch(input_word,TEXT_WORDS[i],re.M|re.I)
                    if(output):
                        file2.write("\n"+TEXT_WORDS[i-1]+" "+TEXT_WORDS[i]+" "+TEXT_WORDS[i+1])
                self.count+=1
        
    def close(self):
        file.close()
        file2.close()
object1=project()
object1.readfile()
