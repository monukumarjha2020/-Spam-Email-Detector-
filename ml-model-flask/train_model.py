import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
import nltk
nltk.download('stopwords')

# Sample dataset (SMS Spam Collection)
data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv", sep="\t", header=None, names=["label", "message"])

# Convert labels
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Create ML pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer(stop_words='english')),
    ('classifier', MultinomialNB())
])

# Train
X_train, X_test, y_train, y_test = train_test_split(data['message'], data['label'], test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model.pkl')

print("Model trained and saved to model.pkl")
