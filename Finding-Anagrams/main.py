
# this is a function that compares two words to determine if they are anagram or not
def find_anagram(word, anagram):
    if sorted(word) != sorted(anagram):
        return False
    else:
        return True


# Taking string input from user for comparism
word = input("Enter your first word: ")
anagram = input("Enter your second word: ")

print(find_anagram(word, anagram))
