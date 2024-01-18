import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib  # Import joblib directly

# dataset
from DATAtoTRAIN import train
data=train

def preprocess(sentence):
    words = word_tokenize(sentence)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.casefold() not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    return ' '.join(lemmatized_words)

#This condition is to not run when this file is imported or something
def train(data):
    # Applying preprocessing to the data
    X = [preprocess(sentence) for (sentence, label) in data]  # Exclude the last element in the data list
    y = [label for (sentence, label) in data]

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    X_vectorized = vectorizer.fit_transform(X)

    # Splitting the data
    X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

    # Training a RandomForestClassifier (you can experiment with other models)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Saving the trained model and vectorizer
    joblib.dump(clf, 'disrespect_model.joblib')
    joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')
    

if __name__=="__main__":
    train(data)
    print("Training done")
