# FastAPI Model Prediction

This project implements a FastAPI-based web service to serve a machine learning model and make predictions.

## Features
- **Prediction Endpoint**: A RESTful API endpoint (`/predict`) that accepts a POST request with a JSON payload and returns a prediction based on the trained model.


## Installation

### 1. Clone the repository:
`git clone https://github.com/mbithesss/FastAPI.git`


### 2. Set up a virtual environment:
`python -m venv env`
`source env/Script/activate`

### 3. Install dependencies
`pip install -r requirements.txt`

### 4. To start the FastAPI application, run:
`uvicorn app:app --reload`

The API will be available at http://127.0.0.1:8000.


