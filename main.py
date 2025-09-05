from fastapi import FastAPI

import uvicorn

from routers.book_router import router as book_router
from routers.index_routers import router as index_routers
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/images", StaticFiles(directory="images", packages=None, html=False, check_dir=True), name="images" )
app.include_router(index_routers)
app.include_router(book_router)

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
