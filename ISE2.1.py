
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')


with open("input.txt", "r") as file:
    text = file.read()


stop_words = set(stopwords.words("english"))


words = word_tokenize(text)


filtered_words = [
    word for word in words
    if word.lower() not in stop_words
]


print("Original text:")
print(text)

print("\nText after removing stopwords:")
print(" ".join(filtered_words))