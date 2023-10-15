"""Start module in app"""
import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from database import get_async_session
from person.router import router as router_person
from legion.router import router as router_legion


#create FastApi app
app = FastAPI(
    title='Warhammer 40K'
)


@app.get("/db")
async def get_db_version(session: AsyncSession = Depends(get_async_session)):
    res = await session.execute(text("SELECT version()"))
    return f"{res.first()}"


#include routers
app.include_router(router_person)
app.include_router(router_legion)


if __name__ == '__main__':
    #run app
    uvicorn.run(app, host="0.0.0.0", port=8000)
