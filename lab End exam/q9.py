# Student Name: Akshay Kumar Reddy
# Roll Number: 2420030604
# Lab End Semester Exam

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from wordcloud import WordCloud

data = {
    "Review": [
        "Great food and fast service",
        "Cold food terribly slow experience",
        "Average taste but friendly staff",
        "Bad management food was late",
        "Loved the desserts and quick serving"
    ],
    "Rating": [5, 1, 3, 2, 5]
}

df = pd.DataFrame(data)

# Q9(1)
cv = CountVectorizer(stop_words="english")

# Q9(2)
X = cv.fit_transform(df["Review"])
y = df["Rating"]

# Q9(3)
model = MultinomialNB()
model.fit(X, y)

print("Prediction:", model.predict(cv.transform(["fast food service"])))

# Q9(4)
df["Rating"].value_counts().plot(kind="bar")
plt.title("Service Rating Count")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# Q9(5)
text = " ".join(df["Review"])
wc = WordCloud().generate(text)

plt.imshow(wc)
plt.axis("off")
plt.show()

# Q9(6)
df["Rating"].value_counts().plot.bar()
plt.title("Value Count of Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()
