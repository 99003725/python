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
        #m=file.readlines()
        #for k in s:
         #   pattern = re.findall(input_word, s,re.M|re.I)
        file3 = open("C:\\Users\\99003725\\Documents\\GitHub\\python\\outputstring.txt",'a')
        for i in pattern:
            file3.write(i+'\n')
            #for a in words:
             #   print(a,end="")
        
       
        
    


    
