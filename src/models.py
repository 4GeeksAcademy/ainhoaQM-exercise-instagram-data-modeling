import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, func
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
 
Base = declarative_base()
 
 
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(256), unique=True, nullable=False)
    password = Column(String(18), nullable=False)
    description = Column(String(250), default="Hi, I'm using Instagram")
    created_date = Column(DateTime, default=func.now())
    admin_status = Column(Boolean, default=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url_image = Column(String(250), unique=False)
    post_id = Column(Integer, ForeignKey('post.id'))

 
# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')