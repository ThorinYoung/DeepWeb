from exts import db
from datetime import datetime
from sqlalchemy.dialects import mysql
from alembic import op
import sqlalchemy as sa

class UserModel(db.Model):
    __tablename__="user_data"
    id=db.Column(mysql.INTEGER(),primary_key=True,autoincrement=True, nullable=False, comment='用户id，唯一标识')
    name=db.Column( mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=30), nullable=False, unique=True,comment='用户名')
    nickname = db.Column(mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=30), nullable=True, comment='用户昵称，可重名')
    passwd = db.Column(mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=20), nullable=False, comment='用户登录密码')
    phonenumber = db.Column(mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=11), nullable=True, comment='用户手机号码')
    create_time=db.Column(mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True, comment='用户创建时间')
    gender=db.Column(mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=6), nullable=True, comment='用户性别')
    balance=db.Column(mysql.INTEGER(unsigned=True), server_default=sa.text("'0'"), autoincrement=False, nullable=True, comment='账户余额，单位为人民币')
    viplevel=db.Column(mysql.INTEGER(), server_default=sa.text("'0'"), autoincrement=False, nullable=True, comment='vip等级')
    avatar=db.Column(mysql.MEDIUMBLOB(), nullable=True, comment='用户头像')



class QuestionModel(db.Model):
    __tablename__ = "question_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id=db.Column(mysql.INTEGER(),db.ForeignKey("user_data.id"))
    create_time=db.Column(mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True)
    author=db.relationship("UserModel",backref="questions")


class AnswerModel(db.Model):
    __tablename__ = "answer_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True)
    question_id=db.Column(db.INTEGER,db.ForeignKey("question_data.id"))
    author_id = db.Column(mysql.INTEGER(), db.ForeignKey("user_data.id"))
    author = db.relationship("UserModel", backref="answers")
    question= db.relationship("QuestionModel",backref=db.backref("answers",order_by=create_time.desc()))