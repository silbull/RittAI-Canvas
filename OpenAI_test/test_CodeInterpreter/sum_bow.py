bows = {'Machine': 5,
 'learning': 5,
 'is': 5,
 'a': 4,
 'form': 4,
 'of': 4,
 'artificial': 4,
 'intelligence': 3,
 'based': 3,
 'on': 7,
 'algorithms': 2,
 'that': 1,
 'are': 4,
 'trained': 4,
 'data.': 4,
 'intelligence.': 2,
 'Artificial': 1,
 'algorithms.': 2,
 'Algorithms': 2}

total = 0
for num in bows.values():
    total += num

print(total)

from nltk.corpus import stopwords
import nltk, pprint

nltk.download('stopwords')
stop_words = stopwords.words('english')
print(stop_words)

with open("test_CodeInterpreter/stopwords_eng.txt", "w") as f:
    for word in stop_words:
        f.write(f"{word}\n")