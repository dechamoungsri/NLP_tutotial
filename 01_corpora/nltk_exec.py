
from nltk.corpus import reuters

# Access the files in reuters corpus
files = reuters.fileids()
print(files)

# Access a word 
words16097 = reuters.words(['test/16097'])
print (words16097)

# Access word 0 to 20 
word20 = reuters.words(['test/16097'])[:20]
print(word20)

# Access topic categories in reuter corpus
reutersGenres = reuters.categories()
print(reutersGenres)
print(len(reutersGenres))

# Print a list of word for specific topics
print(reuters.words(categories=['bop','cocoa']))

# Print new line when find full-stop
for w in reuters.words(categories=['bop','cocoa']):
    print(w+' ', end='') # Print word
    if(w is '.'):
        print() # Print newline
