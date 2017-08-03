def sillycase(word):
    word_half = len("word")//2
    word = word[:len(word)//2].lower()+word[len(word)//2:].upper()
    print(word)
    return word

sillycase("test")