import spacy
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score

nlp = spacy.load("en_core_web_sm")

# le TP de la dernier fois
def text_cleaning(text):
    doc = nlp(text)
    cleaned_tokens = []
    for token in doc:
        if not token.is_stop and not token.is_punct:
            cleaned_tokens.append(token.lemma_.lower())

    cleaned_text = " ".join(cleaned_tokens)
    les_nombres = {
        "zero":"0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9",
        "ten":"10"
    }
    mots = cleaned_text.split()
    for i in range(len(mots)):
        if mots[i] in les_nombres:
            mots[i] = les_nombres[mots[i]]
    phrase = " ".join(mots)
    return phrase.split()


# Load dataset
fake = pd.read_csv("Fake.csv").head(50)
true = pd.read_csv("True.csv").head(50)

fake["label"] = 0
true["label"] = 1

data = pd.concat([fake, true])

texts = (data["title"] + " " + data["text"]).astype(str)
labels = data["label"]


#text cleaning
cleaned_texts = []
for text in texts:
    cleaned_texts.append(text_cleaning(text))


# vocabulary
vocabulary = []
for text in cleaned_texts:
    for word in text:
        # prendre juste les mots unique
        if word not in vocabulary:
            vocabulary.append(word)


#Vectorization
vectors = []
for text in cleaned_texts:
    vector = []
    for word in vocabulary:
        #si le mot existe 1 sinon 0
        if word in text:
            vector.append(1)
        else:
            vector.append(0)
    vectors.append(vector)


#train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    vectors, labels, test_size=0.2, random_state=42
)

# Naive Bayes
model = BernoulliNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)