#I need you to make a function named word_count. It should accept a single argument which will be a string. The function needs to return a dictionary. The keys in the dictionary will be each of the words in the string, lowercased. The values will be how many times that particular word appears in the string.
#Check the comments below for an example.

def word_count(string):
	    return {word : string.lower().split().count(word) for word in string.lower().split()}
	    
print(word_count("I do not like it Sam I Am"))