from fastapi import FastAPI
import json
from fastapi.responses import FileResponse

app = FastAPI() #fastapi object 


# returning html file
@app.get("/") #api endpoint
def get_audio():
    return FileResponse("trials\\index.html")

#returning pdf
@app.get("/cv")
def get_audio():
    return FileResponse("trials\\Srinivas_CV.pdf")




def get_data():
    with open("trials\\students.json","r") as file:
        return json.load(file)
    
# returning json data
@app.get("/s")                      
def students():
    return get_data()