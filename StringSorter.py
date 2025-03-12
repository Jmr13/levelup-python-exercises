# Own solution
def stringSorter(string):
  return " ".join(sorted(string.split(" "), key=lambda x: x.lower()))
    
print(stringSorter("camias Bannana Duhat Apple"))
print(stringSorter("String of words"))
print(stringSorter("banana ORANGE apple"))

def sort_words(words):
  return " ".join(sorted(words.split(" "), key=str.casefold))

print(sort_words("camias Bannana Duhat Apple"))
print(sort_words("String of words"))
print(sort_words("banana ORANGE apple"))