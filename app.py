from fastapi import FastAPI
import json
app = FastAPI()

def load_data():
    with open("patients.json" ,"r") as f:
        data = json.load(f)
    return data    

@app.get("/")
def about():
    return {"message":"about website"}

@app.get("/fastapi")
def fast():
    return {"message":"about fastapi practice"}
    
@app.get("/view")
def view():
    data = load_data()

    return data
