from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse

# створюємо таблиці
Base.metadata.create_all(bind=engine)
app = FastAPI()
# визначаємо залежність
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return FileResponse("public/start.html")

@app.get("/admin")
def main():
    return FileResponse("public/admin.html")

@app.get("/user")
def main():
    return FileResponse("public/user.html")



@app.get("/api/users")
def get_people(db: Session = Depends(get_db)):
    return db.query(Person).all()


@app.get("/api/users/{id}")
def get_person(id, db: Session = Depends(get_db)):
    # отримуємо користувача за id
    person = db.query(Person).filter(Person.id == id).first()
    # якщо не знайдений, відправляємо статусний код і повідомлення про помилку
    if person==None:
        return JSONResponse(status_code=404, content={ "message": "Користувач не знайдений"})
    #якщо користувача знайдено, відправляємо його
    return person



@app.post("/api/users")
def create_person(data = Body(), db: Session = Depends(get_db)):
    person = Person(name=data["name"], surname=data["surname"], phone=data["phone"], email=data["email"], start=data["start"], finish=data["finish"],date=data["date"], comment=data["comment"])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person



@app.put("/api/users")
def edit_person(data = Body(), db: Session = Depends(get_db)):
    # отримуємо користувача за id
    person = db.query(Person).filter(Person.id == data["id"]).first()
    # якщо не знайдений, відправляємо статусний код і повідомлення про помилку
    if person == None:
        return JSONResponse(status_code=404, content={ "message": "Користувач не знайдений"})
    # якщо користувач знайдений, змінюємо його дані і відправляємо назад клієнту
    person.name = data["name"]
    person.surname = data["surname"]
    person.phone = data["phone"]
    person.email = data["email"]
    person.start = data["start"]
    person.finish = data["finish"]
    person.date = data["date"]
    person.comment = data["comment"]
    db.commit() # зберігаємо зміни
    db.refresh(person)
    return person



@app.delete("/api/users/{id}")
def delete_person(id, db: Session = Depends(get_db)):
    # отримуємо користувача за id
    person = db.query(Person).filter(Person.id == id).first()
    # якщо не знайдений, відправляємо статусний код і повідомлення про помилку
    if person == None:
        return JSONResponse( status_code=404, content={ "message": "Користувач не знайдений"})
    # якщо користувача знайдено, видаляємо його
    db.delete(person) # видаляємо об'єкт
    db.commit() # зберігаємо зміни
    return person











@app.get("/img/01.jpg")
def main():
    return FileResponse("public/img/01.jpg")

@app.get("/img/02.jpg")
def main():
    return FileResponse("public/img/02.jpg")

@app.get("/img/path.svg")
def main():
    return FileResponse("public/img/path.svg")

@app.get("/img/mountain.svg")
def main():
    return FileResponse("public/img/mountain.svg")


@app.get("/style.css")
def main():
    return FileResponse("public/style.css")

@app.get("/script.js")
def main():
    return FileResponse("public/script.js")