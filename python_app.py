file=open("random_paragraphs.txt",mode="r")

#I read this ammount because it is the maximum amount to read
filewords=file.read(1000000)


from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stopwords if not downloaded
nltk.download('stopwords')
nltk.download('punkt')

# Load the stopwords
stop_words = set(stopwords.words('english'))

# Tokenize the text
words = word_tokenize(filewords)


# Filter out stop words
filtered_words = [word for word in words if word.isalpha() and word.lower() not in stop_words]

# Join the filtered words back into a single string
#filtered_words = ' '.join(filtered_words)

# Print the filtered text
#print(filtered_words)

uniquewords=set(filtered_words)
uniquewords=list(uniquewords)

#make function  to count word in list
def count(word,listx):
    counter=0
    for w in listx:
        if word==w:
            counter+=1
    return counter

#for loop to apply count function on the data and save it
listx=[]
for w in uniquewords:
    listx.append({w:count(w,filtered_words)})
    
#for loop for printing data
for item in listx:
    for key, value in item.items():
        print('word',key,'count is',value,'\n')