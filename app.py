# 1. Import Libraries
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# 3. Index route, opens automatically
@app.get('/')
def index():
    return{'message': 'Hello, world'}

# 4. Route with a single parameter returns the parameter within a message

@app.get('/name')
def get_name(name: str):
    return{'message': f'Hello, {name}'}

# 5. Expose the prediction unctionality, make a prediction from the passed
# JSON data and return the predicted Bank Note with the confidence

@app.post('/predict')  #/predict is the API name
def predict_banknote(data:BankNote):  #to capture the input we are giving
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    # print(classifier.predict([[variance, skewness, curtosis, entropy]]))
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if(prediction[0] > 0.5):
        prediction = "Fake note"
    else:
        prediction = "Its a Bank Note"
    return{
        'prediction': prediction
    }

#6 Run API with uvicon
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

#uvicorn app:app --reload