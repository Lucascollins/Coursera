
def txt (sentence,word):
    if word in sentence:
        sentence = sentence.replace(f"{word}",word.upper())
        print(sentence)

txt("Have a nice day", "nice")

def highlight_word(sentence, word):
	return(sentence.replace(f"{word}",word.upper()))
	
print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))