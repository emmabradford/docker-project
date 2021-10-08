#tasks
#List name of all the text file at location: /home/data
#Read the two text files and count total number of words in each text files
#Add all the number of words to find the grand total (total number of words in both files)
#list the top 3 words with maximum number of counts in IF.txt.  Include the word counts for the top 3 words.
# Find the IP address of your machine
#Write all the output to a text file at location: /home/output/result.txt (inside the container)
#Upon running your container, it should do all the above stated steps and print the information on console from result.txt file and exit.

#Source: https://realpython.com/working-with-files-in-python/#listing-all-files-in-a-directory

import os
import socket   
from collections import Counter
#list of names of files in /home/data
#change the value of basepath to be /home/data (where if. and limereick areZZ)
filenames = []
basepath = './home/data'
print("file names in /home/data")
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)
        filenames.append(entry)

#source:https://pythonexamples.org/python-count-number-of-words-in-text-file/

#read 2 text files and wordcount
#read and count number of words in if.txt
#change to \home\data\if.txt
filei = open("./home/data/IF.txt", "rt")
datai = filei.read()
wordsInIF = datai.split()
numWordsInIF = len(wordsInIF)
print("number of words in if.txt")
print(numWordsInIF)

#read and count number of words in limeric.txt
#change to \home\data\limeric.txt
filel = open("Limerick-1-1.txt", "rt")
datal = filel.read()
wordsInLim = datal.split()
numWordsInLim = len(wordsInLim)
print("number of words in limeric.txt")
print(numWordsInLim)

#Add all the number of words to find the grand total (total number of words in both files)
print("total words in both files")
totalWords = numWordsInLim + numWordsInIF
print(totalWords)

#Source: https://computersciencehub.io/python/python-find-most-commonly-used-word-in-text-file/
#list the top 3 words with maximum number of counts in IF.txt.  Include the word counts for the top 3 words.
counting = Counter(wordsInIF)
wordAndFrequency = counting.most_common()
print("Most common word")
print(wordAndFrequency[0][0])
print("frequency of word")
print(wordAndFrequency[0][1])
f1 = wordAndFrequency[0][1]
w1 = wordAndFrequency[0][0]

print("Second most common word")
print(wordAndFrequency[1][0])
print("frequency of word")
print(wordAndFrequency[1][1])
f2 = wordAndFrequency[1][1]
w2 = wordAndFrequency[1][0]

print("Third most common word")
print(wordAndFrequency[2][0])
print("frequency of word")
print(wordAndFrequency[2][1])
f3 = wordAndFrequency[2][1]
w3 = wordAndFrequency[2][0]

#Source: https://www.geeksforgeeks.org/python-program-find-ip-address/
# Find the IP address of your machine
hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
print("Ip address of computer")   
print(IPAddr)
IP = IPAddr
