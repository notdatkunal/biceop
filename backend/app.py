from fastapi import FastAPI, Depends, HTTPException
 

app = FastAPI(title="FastAPI + PostgreSQL")


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with PostgreSQL"}

 
@app.get("/health")
def health_check():
    return {"status": "ok"}
