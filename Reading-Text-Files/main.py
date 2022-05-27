# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    return open(filename, 'r').read()

def count_words():
    text = read_file_content("story.txt")
    return {"as": text.count("as"), "would": text.count("would")}

print(count_words())