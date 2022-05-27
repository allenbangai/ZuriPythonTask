# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here 
    def arrange(val):
        return val.replace(" ","").lower()
    return sorted(arrange(word)) == sorted(arrange(anagram))

print(find_anagram("allen", "Allen"))


