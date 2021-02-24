
import re 
file = open("text.txt","r")
input_word=input("enter the word to be searched:")
file3 = open(input_word+".txt",'a')
#count=0
s=" " 
while s:
    s=file.read()
    pattern = re.findall(input_word, s,re.M|re.I)
    if pattern:
        file3.write("count:"+str(len(pattern)))
        w=s.split()
        x=re.split('\W',str(w))
        x = list(filter(None, x))
        print(x)
        y=len(x)
        for i in range(0,y):
            out=re.fullmatch(input_word,x[i],re.M|re.I)
            if(out):
                file3.write("\n"+x[i-1]+" "+x[i]+" "+x[i+1])
            
        
       
        
    


    
