import re                                                              #imported regular expression


class project:                                                         #created a class that contains parameters(main class)
    def __init__(self):                                                #defined a function 
        self.file = open("text.txt","r")                               #initialized the file and opened it   
        
         
class write(project):                                                  #created another class which inherting the characters of mainclass
    def readfile(self):                                                #defined function to read the file 
        count=0                                                        #initialized the count=0
        TEXT_FILE = self.file.read()                                     #to read the file
        no_words = int(input("no of words to be searched"))              #to take inputword that to be searched
        while no_words > count:                                        #to check the condition to take multiple words
            input_word = input("enter the word to be searched:")         #it takes the mutiple words that to be searched
            file2 = open(input_word+".txt",'a')                        #it opens the output file that the words get stored
            pattern = re.findall(input_word, TEXT_FILE,re.M|re.I)      #it checks the entire text for the words that searched by the user
            if pattern:
                file2.write("count:"+str(len(pattern)))                #it gives the number of occurences of the word that searched
                w=TEXT_FILE.split()
                TEXT_WORDS = re.split('\W',str(w))
                TEXT_WORDS = list(filter(None, TEXT_WORDS))            #finally we get the clean text with out any signs etc
                TEXT_WORD_LENGTH = len(TEXT_WORDS)
                for i in range(0,TEXT_WORD_LENGTH):                    #it will traverse entire text and if any match occurs at that index
                    output = re.fullmatch(input_word,TEXT_WORDS[i],re.M|re.I) #if matched the word that user given
                    if(output):
                        file2.write("\n"+TEXT_WORDS[i-1]+" "+TEXT_WORDS[i]+" "+TEXT_WORDS[i+1]) #it prints the required output
                count+=1                                                   #it increment the count to terminate the loop
        
    def close(self):                                                #defined a function to close the files
        file.close()                                                #closed file
        file2.close()                                               #closed file
object1 = project()                                                   #created the object to call the class
object2 = write()                                                     #object for writing the output file
object2.readfile()                                                  #object for reading the input file