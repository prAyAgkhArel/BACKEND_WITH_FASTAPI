from fastapi import FastAPI
app = FastAPI()

books = [
    {"title":"titleone", "author":"author1", "category":"Science"},
    {"title":"titletwo", "author":"author2", "category":"Math"},
    {"title":"titlethree", "author":"author3", "category":"Philosophy"},
    {"title":"titlefour", "author":"author4", "category":"English"},
]

@app.get("/")
def home():
    return {
        "Hello Prayag"
    }
  
@app.get("/books")
def getbooks():
    return books


@app.get('/books/title/{book_title}')
def getbook(book_title:str):
    for book in books:
        if book["title"].casefold() == book_title.casefold():
            return book["title"]




@app.get('/books/author/{author}')
def getbookby_author(author):
    for book in books:
        if book.get('author').casefold() == author.casefold():
            return book
        
        
# Try Endpoint http://127.0.0.1:8000/books/?category=Science
@app.get('/books/')
def getbookby_query(category: str):
    
    for book in books:
        if category.casefold() == book['category'].casefold():
            books.append(category)
            return book

#Try endpoint http://127.0.0.1:8000/books/author1/?category=titletwo
@app.get('/books/{book_author}/')
def getbookby_querytitle(book_author, category: str):
    for book in books:
        if category.casefold() == book['title'].casefold():
            if book.get('author') == book_author:
                books.append(category)
                return book

        
    