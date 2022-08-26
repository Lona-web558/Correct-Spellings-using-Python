from spellchecker import SpellChecker
corrector = SpellChecker()
#correct spellings using Python
word = input("Enter a word : ")
if word in corrector:
    print("Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct Spelling is ", correct_word)
