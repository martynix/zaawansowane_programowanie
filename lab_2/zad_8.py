# zad_8

import argparse
from typing import Optional
import requests


class Brewery:

    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        address_1: Optional[str],
        address_2: Optional[str],
        address_3: Optional[str],
        city: str,
        state_province: str,
        postal_code: str,
        country: str,
        longitude: Optional[str],
        latitude: Optional[str],
        phone: Optional[str],
        website_url: Optional[str],
        state: Optional[str],
        street: Optional[str],
    ) -> None:
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self) -> str:
        miejsce = f"{self.city}, {self.country}"
        strona = self.website_url if self.website_url else "brak strony"
        return (
            f"Browar: {self.name} | Typ: {self.brewery_type} "
            f"| Lokalizacja: {miejsce} | WWW: {strona}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pobiera listę browarów z Open Brewery DB."
    )
    parser.add_argument(
        "--city",
        type=str,
        help="Nazwa miasta do przefiltrowania wyników (np. Berlin, San Diego)",
    )
    args = parser.parse_args()

    url = "https://api.openbrewerydb.org/v1/breweries"
    parametry = {"per_page": 20}

    if args.city:
        parametry["by_city"] = args.city
        print(f"Filtrowanie po mieście: {args.city}\n")

    odpowiedz = requests.get(url, params=parametry)
    dane_browarow = odpowiedz.json()

    lista_obiektow_browarow: list[Brewery] = []

    for browar_dict in dane_browarow:
        nowy_browar = Brewery(
            id=browar_dict.get("id"),
            name=browar_dict.get("name"),
            brewery_type=browar_dict.get("brewery_type"),
            address_1=browar_dict.get("address_1"),
            address_2=browar_dict.get("address_2"),
            address_3=browar_dict.get("address_3"),
            city=browar_dict.get("city"),
            state_province=browar_dict.get("state_province"),
            postal_code=browar_dict.get("postal_code"),
            country=browar_dict.get("country"),
            longitude=browar_dict.get("longitude"),
            latitude=browar_dict.get("latitude"),
            phone=browar_dict.get("phone"),
            website_url=browar_dict.get("website_url"),
            state=browar_dict.get("state"),
            street=browar_dict.get("street"),
        )
        lista_obiektow_browarow.append(nowy_browar)

    if not lista_obiektow_browarow:
        print("Nie znaleziono żadnych browarów dla podanych kryteriów.")
        return

    print(f"Pobrano {len(lista_obiektow_browarow)} obiektów:\n")
    for browar in lista_obiektow_browarow:
        print(browar)


if __name__ == "__main__":
    main()

# jak uruchomić skrypt w terminalu (Bash):
# python main.py --city=Berlin
