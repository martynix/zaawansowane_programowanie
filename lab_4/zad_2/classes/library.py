class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Biblioteka w mieście {self.city}, "
            f"na ulicy {self.street} {self.zip_code}."
            f"Otwarta {self.open_hours}. Kontakt: {self.phone}"
        )
