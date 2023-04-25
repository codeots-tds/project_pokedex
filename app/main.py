import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from fastapi.middleware.cors import CORSMiddleware
from email.mime import application
import uvicorn
from app.transform_data import process_pokedex
from typing import List
from app.schemas import schema

app=FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix='/graphql')
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    pass
