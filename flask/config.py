class Config:
    SECRET_KEY = "strong secret key"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///trips.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
