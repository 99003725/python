import re 
file = open("C:\\Users\\99003725\\Documents\\GitHub\\python\\text.txt","r")
input_word=input("enter the word to be searched:")
count=0
s=" " 
while s:
    s=file.read()
    pattern = re.findall(input_word, s,re.M|re.I)
    if pattern:
        print(len(pattern))
        file2 = open("C:\\Users\\99003725\\Documents\\GitHub\\python\\outputfile.txt",'a')
        file2.write(str(len(pattern)))
        file3 = open("C:\\Users\\99003725\\Documents\\GitHub\\python\\outputstring.txt",'a')
        #m=s.readline()
        #k=s.strip(" ")
        #m=k.strip("")
        x=re.split("-",s)
        print(x)
        y=len(x)
        for i in range(0,y):
            if(x[i]==input_word):
                file3.write("\n"+x[i-1]+" "+x[i]+" "+x[i+1])
            
        
       
        
    


    
