def disemvowel(word):
    
    vowels = ["a","e","i","o","u"]
    vowel_count = 0
    word_count = 0
    word_list = list(word)
    word_length = len(word)

    for i in vowels:
    	if vowel_count == len(vowels):
    		break

    	elif i != word_list[word_count]:
    		word_count += 1
    	elif i == word_list[word_count]:
    		
    		
    		del word_list[word_count]
    		break
    		#(need to check if we've gone through the whole word)
    	elif word_count == word_length:
    		word_count = 0
    		vowel_count +1

    word = ''.join(word_list)


    return word

print("Please enter a word:")
while True:
   	word = input("> ")
   	if len(list(word)) == 0:
   		break
   	else:
   		disemvowel(word)
   		continue

