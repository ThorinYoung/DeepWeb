import wtforms
from wtforms.validators import length,EqualTo,InputRequired

class RegisterForm(wtforms.Form):
    name=wtforms.StringField(validators=[length(min=1,max=20)])
    password=wtforms.StringField(validators=[length(min=6,max=20)])
    password_confirm=wtforms.StringField(validators=[EqualTo("password")])

class LoginForm(wtforms.Form):
    name = wtforms.StringField(validators=[length(min=1, max=20)])
    password = wtforms.StringField(validators=[length(min=6, max=20)])


class QuestionForm(wtforms.Form):
    title=wtforms.StringField(validators=[length(min=3,max=200)])
    content= wtforms.StringField(validators=[length(min=5)])


class AnswerForm(wtforms.Form):
    content=wtforms.StringField(validators=[length(min=1)])
    question_id=wtforms.IntegerField(validators=[InputRequired()])