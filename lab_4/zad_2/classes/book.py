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
