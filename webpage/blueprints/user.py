from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from models import UserModel
from .forms import RegisterForm,LoginForm
from exts import db
import string
import random

bp=Blueprint("user",__name__,url_prefix="/user")

@bp.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form=LoginForm(request.form)
        if form.validate():
            name=form.name.data
            password=form.password.data
            user=UserModel.query.filter_by(name=name).first()
            if user and user.passwd == password:
                session["user_id"]=user.id
                return redirect("/")
            else:
                flash("用户名或密码错误！")
                return redirect(url_for("user.login"))
        else:
            flash("用户名或邮箱格式错误！")
            return redirect(url_for("user.login"))



@bp.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form=RegisterForm(request.form)
        if form.validate():
            username=form.name.data
            password=form.password.data
            user=UserModel(name=username,passwd=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            return redirect(url_for("user.register"))



@bp.route("/logout")
def logout():
    #清除所有数据
    session.clear()
    return redirect(url_for('user.login'))


@bp.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")
