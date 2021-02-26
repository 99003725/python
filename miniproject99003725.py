import re  # imported regular expression


class project:  # created a class that contains parameters(main class)
    def __init__(self):   # defined a function
        self.file = open("text.txt", "r")  # initialized the file and open it


class write(project):  # created another class which inherting the parent class
    def readfile(self):  # defined function to read the file
        count = 0   # initialized the count=0
        TEXT_FILE = self.file.read()  # to read the file
        # totake inputword tobe searched
        no_words = int(input("no of words to be searched"))
        # to check the condition to take multiple words
        while no_words > count:
            # it takes the mutiple words that to be searched
            input_word = input("enter the word to be searched:")
        # it opens the output file that the words get stored
            file2 = open(input_word+".txt", 'a')
        # it checks the entire text for the words that searched by the user
            pattern = re.findall(input_word, TEXT_FILE, re.M | re.I)
            if pattern:
                # it gives the number of occurences of the word that searched
                file2.write("count:"+str(len(pattern)))
                w = TEXT_FILE.split()
                TEXT = re.split('\W', str(w))
                # finally we get the clean text with out any signs etc
                TEXT = list(filter(None, TEXT))
                TEXT_WORD_LENGTH = len(TEXT)
                # it will traverse entire text and if any match occurs
                for i in range(0, TEXT_WORD_LENGTH):
                    # if matched the word that user given
                    output = re.match(input_word, TEXT[i], re.M | re.I)
                    if(output):
                        # it prints the required output
                        file2.write("\n"+TEXT[i-1]+" "+TEXT[i]+" "+TEXT[i+1])
            count = count+1  # it increment the count to terminate the loop


def close(self):  # defined a function to close the files
        file.close()  # closed file
        file2.close()  # closed file
object1 = project()  # created the object to call the class
object2 = write()  # object for writing the output file
object2.readfile()  # object for reading the input file
