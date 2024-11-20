# 1. library imports
import uvicorn #ASGI
from fastapi import FastAPI

# 2. create the app object
app = FastAPI()

# 3. index route, opens automatically on http://127.0.0.1:8000
@app.get("/")
def index():
    return {'message': 'Hello, world'}
 
# 4. Route with a single parameter, returns the parameter within a message 
# located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/welcome')
def get_name(name: str):
    return{'Welcome To my Youtube Channel': f'{name}'}

# 5. Run the API with uvicorn
# It eill run on https://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload


