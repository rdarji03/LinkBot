from fastapi import FastAPI
from app.routes.scrap_route import router as get_website


app = FastAPI()
app.include_router(get_website)

@app.get('/')
def root():
    return {"message":"Hello Serving Yout API..."}
