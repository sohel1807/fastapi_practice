from fastapi import FastAPI,Path,Q,HTTPException
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

@app.get("/view/{patient_id}")
def view(patient_id:str = Path (..., description="Id of patient for example P001")):
    data = load_data()

    return data[patient_id]




    
