from pydantic import BaseModel


class AddressSchema(BaseModel):
    address: str
    lng: float
    lat: float
