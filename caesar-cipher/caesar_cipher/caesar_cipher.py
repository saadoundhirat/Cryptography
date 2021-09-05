import nltk, re
from nltk.corpus import words , names

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)
word_list = words.words()
name_list = names.words()

english_letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(text,num):
    chars=text.split()
    new_chars=[]
    for word in chars:
        encrypted_text=''
        for i in word:
            if i.lower() != i and i.lower() in english_letters:
                number=(english_letters.index(i.lower())+num) %26
                encrypted_text+=(english_letters[number].upper())
            elif i.lower() == i and i.lower() in english_letters:
                number=(english_letters.index(i)+num) %26
                encrypted_text+=(english_letters[number])
            else :
                encrypted_text+=i
        new_chars.append(encrypted_text) 
    return " ".join(new_chars)

def decrypt(encrypted,key):
    return encrypt(encrypted,-key)

def count_words(text):
    candidate_words = text.split()
    count = 0
    for i in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', i)
        if word.lower() in word_list or word in name_list:
            count += 1
        else:
            pass
    return count

def crack(encrypted):
    for i in range (0,26):
        text = decrypt(encrypted,i)
        percentage = int(count_words(text) / len(encrypted.split()) * 100)
        if percentage > 50:
            return text 
          
