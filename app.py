from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

from routers import app_router

app = FastAPI()
app.mount("/images", StaticFiles(directory="images", packages=None, html=False, check_dir=True), name="images" )


app.include_router(app_router)



if __name__ == '__main__':
    uvicorn.run(app="app:app", host="127.0.0.1", port=8000, reload=True)
