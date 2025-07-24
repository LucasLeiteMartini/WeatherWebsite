import os
from re import search

import httpx
from dotenv import load_dotenv
from fastapi import APIRouter

from app.schemas import AddressSchema

load_dotenv()


map_router = APIRouter(
    # prefixo para as rotas
    prefix="/map",
    # tag para o swagger
    tags=["Maps"],
)

BASE_URL = os.getenv("BASE_URL", "https://maps.googleapis.com/maps/api/geocode/json?")
PARAMS = {"key": os.getenv("API_KEY")}


@map_router.post("/search/{location}", response_model=AddressSchema)
async def search_location(location):
    """TODO add comentarios"""
    PARAMS["address"] = location

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=PARAMS)

    response = response.json()

    print(response)

    formatted_address = response["results"][0]["formatted_address"]
    lng = response["results"][0]["geometry"]["location"]["lng"]
    lat = response["results"][0]["geometry"]["location"]["lat"]

    data = {"address": formatted_address, "lng": lng, "lat": lat}

    return data


@map_router.get("/{location}")
async def map_location(location):
    data = await search_location(location)

    return data
