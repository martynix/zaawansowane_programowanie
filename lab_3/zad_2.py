# zad_2
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


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Pracownik: {self.first_name} {self.last_name} "
            f"(Zatrudniony: {self.hire_date})"
        )


class Book:
    def __init__(
        self,
        library: Library,
        publication_date,
        author_name,
        author_surname,
        number_of_pages,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka w {self.library}, opublikowana {self.publication_date}, "
            f"autorstwa {self.author_name} {self.author_surname} "
            f"o liczbie stron {self.number_of_pages}"
        )


class Order:
    def __init__(self, employee: Employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = ", ".join(str(book) for book in self.books)
        return (
            f"Zamówienie złożone przez {self.employee} "
            f"dla {self.student} na książki {books_str} dnia {self.order_date}"
        )


lib1 = Library("Warszawa", "Koszykowa 26", "00-999", "08:00-20:00", "111-222-333")
lib2 = Library("Kraków", "Rajska 1", "31-124", "09:00-19:00", "444-555-666")

book1 = Book(lib1, "2020-01-15", "Adam", "Mickiewicz", 350)
book2 = Book(lib1, "2018-05-20", "Henryk", "Sienkiewicz", 520)
book3 = Book(lib2, "1997-06-26", "J.K.", "Rowling", 320)
book4 = Book(lib2, "1954-07-29", "J.R.R.", "Tolkien", 423)
book5 = Book(lib1, "2011-08-16", "George R.R.", "Martin", 1040)

emp1 = Employee(
    "Jan",
    "Kowalski",
    "2015-05-01",
    "1990-01-01",
    "Warszawa",
    "Polna",
    "00-001",
    "123-123-123",
)
emp2 = Employee(
    "Anna",
    "Nowak",
    "2018-09-15",
    "1992-05-22",
    "Kraków",
    "Główna",
    "31-000",
    "321-321-321",
)
emp3 = Employee(
    "Piotr",
    "Zieliński",
    "2021-11-01",
    "1988-11-11",
    "Warszawa",
    "Krótka",
    "00-002",
    "999-888-777",
)

order1 = Order(emp1, "Karolina Pisarczyk", [book1, book2, book5], "2023-10-25")
order2 = Order(emp2, "Marek Moś", [book3, book4], "2023-10-26")

print("ZAMÓWIENIE 1")
print(order1)
print("\nZAMÓWIENIE 2")
print(order2)
