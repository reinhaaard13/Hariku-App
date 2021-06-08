from sqlalchemy import Column, Integer, String, create_engine, orm, exc, Date, Time, extract
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
import bcrypt
from sqlalchemy.sql.expression import select

Base = declarative_base()
engine = create_engine("sqlite:///hariku.db")
Session = orm.sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    password = Column(String)

class Diary(Base):
    __tablename__ = "diary"
    diary_id = Column(Integer, primary_key=True)
    date = Column(Date)
    time = Column(Time)
    content = Column(String)
    mood_score = Column(Integer)

def register_user(password):
    Base.metadata.create_all(engine)
    pwd_hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    user = User(password=pwd_hashed)
    session.add(user)
    session.commit()

def verify_user(password):
    if bcrypt.checkpw(password, session.query(User.password).first().password):
        return True
    else:
        return False

def addDiary(date, time, content, mood_score):
    diary = Diary(
        date=date,
        time=time,
        content=content,
        mood_score=mood_score
    )
    session.add(diary)
    session.commit()

def getAllDiaries():
    return session.query(Diary).order_by(Diary.date).all()

def getDiaryById(id):
    return session.query(Diary).filter(Diary.diary_id == id).first()

def getDiaryByMonth(year, month):
    return session.query(Diary).filter(extract('year', Diary.date) == year).filter(extract('month', Diary.date) == month).all()

def deleteDiaryById(id):
    session.query(Diary).filter(Diary.diary_id == id).delete()
    session.commit()
    return True

if __name__ == "__main__":
    pass