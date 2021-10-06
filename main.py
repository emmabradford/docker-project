#List name of all the text file at location: /home/data
#Read the two text files and count total number of words in each text files
#Add all the number of words to find the grand total (total number of words in both files)
#list the top 3 words with maximum number of counts in IF.txt.  Include the word counts for the top 3 words.
# Find the IP address of your machine
#Write all the output to a text file at location: /home/output/result.txt (inside the container)
#Upon running your container, it should do all the above stated steps and print the information on console from result.txt file and exit.

#Source: https://realpython.com/working-with-files-in-python/#listing-all-files-in-a-directory

import os
#list of names of files in /home/data
#change the value of basepath to be /home/data (where if. and limereick areZZ)
filenames = []
basepath = './'
print("file names in /home/data")
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)
        filenames.append(entry)
print(filenames)

#source:https://pythonexamples.org/python-count-number-of-words-in-text-file/

#read 2 text files and wordcount
#read and count number of words in if.txt
#change to \home\data\if.txt
filei = open("IF.txt", "rt")
datai = filei.read()
wordsInIF = datai.split()
print("number of words in if.txt")
print(wordsInIF)

#read and count number of words in limeric.txt
#change to \home\data\limeric.txt
filel = open("limeric.txt", "rt")
datal = filel.read()
wordsInLim = datal.split()
print("number of words in limeric.txt")
print(wordsInLim)
