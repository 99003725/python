
import re                                                    
file = open("text.txt","r")                                  
no_words=int(input("no of words to be searched"))
count=0                          
#TEXT_FILE=" "                                                
TEXT_FILE=file.read()
while no_words > count:
    input_word=input("enter the word to be searched:")
    file2 = open(input_word+".txt",'a')
    pattern = re.findall(input_word, TEXT_FILE,re.M|re.I)
    if pattern:
        file2.write("count:"+str(len(pattern)))
        w=TEXT_FILE.split()
        TEXT_WORDS=re.split('\W',str(w))
        TEXT_WORDS = list(filter(None, TEXT_WORDS))
        print(TEXT_WORDS)
        TEXT_WORD_LENGTH=len(TEXT_WORDS)
        for i in range(0,TEXT_WORD_LENGTH):
            output=re.fullmatch(input_word,TEXT_WORDS[i],re.M|re.I)
            if(output):
                file2.write("\n"+TEXT_WORDS[i-1]+" "+TEXT_WORDS[i]+" "+TEXT_WORDS[i+1])
        count=count+1
            
        
       
        
    


    
