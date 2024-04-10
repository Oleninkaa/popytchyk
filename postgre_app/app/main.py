from fastapi import FastAPI, Depends, status, Response, HTTPException, Body
from sqlalchemy.orm import Session
from schemas import Trips
import models
from database import engine, get_db
from models import Base
from fastapi.responses import JSONResponse, FileResponse

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def main():
    return FileResponse("public/start.html")

@app.get("/admin")
def main():
    return FileResponse("public/admin.html")

@app.get("/user")
def main():
    return FileResponse("public/user.html")





@app.get("/trips")
def get_all(db: Session = Depends(get_db)):
    all_trips = db.query(models.Trip).order_by(models.Trip.start.desc()).all()
    return all_trips

@app.get("/trips/{id}")
def get_trip(id:int, db: Session = Depends(get_db)):
    trip = db.query( models.Trip).filter( models.Trip.id == id).first()
    return trip





@app.post("/trips")
def create(trip: Trips, db: Session = Depends(get_db)):
    new_trip = models.Trip(**trip.dict())
    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)
    return new_trip




@app.delete("/trips/{id}")
def delete(id:int, db:Session = Depends(get_db), status_code = status.HTTP_204_NO_CONTENT):
    delete_trip = db.query( models.Trip).filter( models.Trip.id == id).first()
    if delete_trip:
        db.delete(delete_trip)
        db.commit()
        
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/trips")
def update(data = Body(), db:Session = Depends(get_db)):
    update_trip = db.query( models.Trip).filter(models.Trip.id == data["id"]).first()
    if update_trip:
        update_trip.name = data["name"]
        update_trip.surname = data["surname"]
        update_trip.phone = data["phone"]
        update_trip.email = data["email"]
        update_trip.start = data["start"]
        update_trip.finish = data["finish"]
        update_trip.date = data["date"]
        update_trip.comment = data["comment"]
        db.commit() # зберігаємо зміни
        db.refresh(update_trip)
        return update_trip
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found")
    







@app.get("/img/01.jpg", tags=["Files connection"])
def main():
    return FileResponse("public/img/01.jpg")

@app.get("/img/02.jpg", tags=["Files connection"])
def main():
    return FileResponse("public/img/02.jpg")

@app.get("/img/path.svg", tags=["Files connection"])
def main():
    return FileResponse("public/img/path.svg")

@app.get("/img/mountain.svg", tags=["Files connection"])
def main():
    return FileResponse("public/img/mountain.svg")


@app.get("/style.css", tags=["Files connection"])
def main():
    return FileResponse("public/style.css")

@app.get("/script.js", tags=["Files connection"])
def main():
    return FileResponse("public/script.js")