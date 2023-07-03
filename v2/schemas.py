from pydantic import BaseModel, model_validator


class Wine(BaseModel):
    id: int
    points: int
    title: str
    description: str | None
    price: float | None
    variety: str | None
    winery: str | None
    designation: str | None
    country: str | None
    province: str | None
    region_1: str | None
    region_2: str | None
    taster_name: str | None
    taster_twitter_handle: str | None

    @model_validator(mode="before")
    def _remove_unknowns(cls, values):
        "Set other fields that have the value 'null' as None so that we can throw it away"
        fields = ["designation", "province", "region_1", "region_2"]
        for field in fields:
            if not values.get(field) or values.get(field) == "null":
                values[field] = None
        return values

    @model_validator(mode="before")
    def _fill_country_unknowns(cls, values):
        "Fill in missing country values with 'Unknown', as we always want this field to be queryable"
        country = values.get("country")
        if not country or country == "null":
            values["country"] = "Unknown"
        return values

    @model_validator(mode="before")
    def _get_vineyard(cls, values):
        "Rename designation to vineyard"
        vineyard = values.pop("designation", None)
        if vineyard:
            values["vineyard"] = vineyard.strip()
        return values


if __name__ == "__main__":
    sample_data = {
        "id": 45100,
        "points": 85.0,  # Intentionally not an int to test coercion
        "title": "Balduzzi 2012 Reserva Merlot (Maule Valley)",
        "description": "Ripe in color and aromas, this chunky wine delivers heavy baked-berry and raisin aromas in front of a jammy, extracted palate. Raisin and cooked berry flavors finish plump, with earthy notes.",
        "price": 10,  # Intentionally not a float to test coercion
        "variety": "Merlot",
        "winery": "Balduzzi",
        "country": "null",  # Test null handling
        "province": "Maule Valley",
        "region_1": "null",  # Test null handling
        "region_2": "null",
        "taster_name": "Michael Schachner",
        "taster_twitter_handle": "@wineschach",
        "designation": "  The Vineyard  ",
    }
    wine = Wine(**sample_data)
    from pprint import pprint
    pprint(wine.model_dump(exclude_none=True))
