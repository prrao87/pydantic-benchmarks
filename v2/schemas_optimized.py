from pydantic import BeforeValidator, TypeAdapter, constr, field_validator
from pydantic_core import PydanticOmit
from typing_extensions import Annotated, NotRequired, TypedDict


def exclude_none(s: str | None) -> str:
    if s is None:
        # since we want `exclude_none=True` in the end,
        # just omit it None during validation
        raise PydanticOmit
    else:
        return s

# Annotated types to allow exclusion of None values to occur during validation, not after
ExcludeNoneStr = Annotated[constr(strip_whitespace=True), BeforeValidator(exclude_none)]
ExcludeNoneFloat = Annotated[float, BeforeValidator(exclude_none)]


class Wine(TypedDict):
    id: int
    points: int
    title: str
    description: NotRequired[ExcludeNoneStr]
    price: NotRequired[ExcludeNoneFloat]
    variety: NotRequired[ExcludeNoneStr]
    winery: NotRequired[ExcludeNoneStr]
    designation: NotRequired[ExcludeNoneStr]
    country: NotRequired[str]
    province: NotRequired[str]
    region_1: NotRequired[str]
    region_2: NotRequired[str]
    taster_name: NotRequired[ExcludeNoneStr]
    taster_twitter_handle: NotRequired[ExcludeNoneStr]

    @field_validator("designation", "province", "region_1", "region_2", mode="before")
    def omit_null_none(cls, v):
        if v is None or v == "null":
            raise PydanticOmit
        else:
            return v

    @field_validator("country", mode="before")
    def country_unknown(cls, s: str | None) -> str:
        if s is None or s == "null":
            return "Unknown"
        else:
            return s


WinesTypeAdapter = TypeAdapter(list[Wine])


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
    wines = WinesTypeAdapter.validate_python([sample_data])
    from pprint import pprint

    pprint(wines, sort_dicts=False)
