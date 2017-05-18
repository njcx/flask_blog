from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Sitedesc(db.Model):
    __tablename__ = "sitedesc"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kw = db.Column(db.String(64))
    desc = db.Column(db.String(64))


class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    desc = db.Column(db.Text(), nullable=True)
    passwd_hash = db.Column(db.String(128))

    @property
    def password(self):
        return None

    @password.setter
    def password(self, password):
        self.passwd_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.passwd_hash,password)





class Comment(db.Model):
    __tablename__="comments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.String(db.String)
    content = db.Column(db.String(200))





class Article(db.Model):
    __tablename__="articles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64))
    datetime = db.Column(db.DateTime())
    content = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    #Tag_id =



class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))

