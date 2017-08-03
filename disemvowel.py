def disemvowel(word):
	
	vowels = ["a","e","i","o","u"]
	count = 0

	for letter in vowels:
		word = word.replace(vowels[count].lower(), "")
		word =word.replace(vowels[count].upper(), "")
		count += 1
	
	print(word)
	return word

print("Please enter a word:")
while True:
   	word = input("> ")
   	if len(list(word)) == 0:
   		break
   	else:
   		disemvowel(word)
   		continue
