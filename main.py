#List name of all the text file at location: /home/data
#Read the two text files and count total number of words in each text files
#Add all the number of words to find the grand total (total number of words in both files)
#list the top 3 words with maximum number of counts in IF.txt.  Include the word counts for the top 3 words.
# Find the IP address of your machine
#Write all the output to a text file at location: /home/output/result.txt (inside the container)
#Upon running your container, it should do all the above stated steps and print the information on console from result.txt file and exit.

#Source: https://realpython.com/working-with-files-in-python/#listing-all-files-in-a-directory
import os
#change the value of basepath to be /home/data (where if. and limereick areZZ)
filenames = []
basepath = './'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)
        filenames.append(entry)
print(filenames)