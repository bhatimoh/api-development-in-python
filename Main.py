from fastapi import FastAPI
from fastapi.params import Body
app =FastAPI()

@app.get("/")
def root():
  return {"message":"Hello world"}

@app.get("/posts")
def posts():
  return {"content":"this is get request"}

@app.post("/home") 
def create_posts(payload:dict=Body(...)):
  return {"new post":f"title {payload['title']} cotent {payload['content']}"}  