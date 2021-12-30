from typing import TextIO


def pig_latin(text):
  say = "ay"
  # Separate the text into words
  words = text.split()
  a = []
  for word in words: 
      x = word[1:]+ word[0] + say
      a.append(x)
  return ' '.join(a)

	
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpa
