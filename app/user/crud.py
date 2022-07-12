from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app= Flask(__name__, template_folder="templates")
app.config=['SQLALCHEMY_DATABASE_URI'] == 'sqllite:///users.sqlite3'

db= SQLAlchemy(app)


from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)
    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
        )
def __repr__(self):
    return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

from sqlalchemy import create_engine
engine = create_engine("sqlite://", echo=True, future=True)

@app.route('/sim')
def crud():
    return render_template('estu.html')
