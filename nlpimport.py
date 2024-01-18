import joblib
from nlpTrain import preprocess

# Loading the pre-trained model and vectorizer
clf = joblib.load('disrespect_model.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

# Example usage
def Prediction(new_sentence):
    new_sentence = preprocess(new_sentence)
    new_sentence_vectorized = vectorizer.transform([new_sentence])
    prediction = clf.predict(new_sentence_vectorized)[0]
    return prediction

if __name__=="__main__":
    sentence="Stop living"
    print(f"Prediction: {Prediction(sentence)}")
