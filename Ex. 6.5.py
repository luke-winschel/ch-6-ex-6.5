#Exercise 6.5
#(Counting Duplicate words) Write a script that uses a dictionary to determine and print the number of duplicate words in a sentence.

#Takes user input for a sentence
sentence = (input('Please enter a sentence, do not add puncuation: '))

#Create empty dictionary
duplicate_words = {}

#for loop that reads every word and adds to the dictionary.  Every time a word is read one is added to the counter
for word in sentence.split():
    if word in duplicate_words:
        duplicate_words[word] += 1
    else:
        duplicate_words[word] = 1

#Print headers       
print(f'{"Word"}\t Count')

#For each word in the dictionary, check the usage counter if the counter is greater than one print the word and the number of occurrences
for word, count in sorted(duplicate_words.items()):
    if count > 1:
        print(f'{word}\t {count}')

#Print the number of unique words in the sentence
print('\n Number of unique words: ', len(duplicate_words))