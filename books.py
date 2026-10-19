from fastapi import FastAPI, Body
from fastapi import HTTPException
app = FastAPI()

books = [
    {"title":"titleone", "author":"author1", "category":"Chemistry"},
    {"title":"titletwo", "author":"author2", "category":"Math"},
    {"title":"titlethree", "author":"author3", "category":"Philosophy"},
    {"title":"titlefour", "author":"author4", "category":"Sociology"},
    {"title":"titlefive", "author":"author1", "category":"Physics"},
    {"title":"titleone", "author":"author1", "category":"Physics"},
    {"title":"titletwo", "author":"author2", "category":"Numerical Methods"},
     {"title":"titlethree", "author":"author3", "category":"BigData"},
    {"title":"titlefour", "author":"author4", "category":"English"},
    {"title":"titletwo", "author":"author1", "category":"Geology"},
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
    raise HTTPException(status_code=404, detail="Book not found")


@app.get('/books/author/{author}')
def getbookby_author(author):
    for book in books:
        if book.get('author').casefold() == author.casefold():
            return book
    raise HTTPException(status_code=404, detail="Book not found")
        
        
# Try Endpoint http://127.0.0.1:8000/books/?category=Science
@app.get('/books/')
def getbookby_query(category: str):
    
    for book in books:
        if category.casefold() == book['category'].casefold():
            return book
    raise HTTPException(status_code=404, detail="Book not found")

#Try endpoint http://127.0.0.1:8000/books/author1/?title=titleone
@app.get('/books/{book_author}/')
def getbookby_querytitle(book_author, title: str):
    for book in books:
        if title.casefold() == book['title'].casefold() and \
        book.get('author').casefold() == book_author.casefold():
                return book
    raise HTTPException(status_code=404, detail="Book not found")        

@app.post('/books/create_book', status_code = 201)
def create_book(new_book = Body({
                                    "title": "titleeleven",
                                    "author": "author5",
                                    "category": "Computer Science"
                                })):
    return new_book
    
        
