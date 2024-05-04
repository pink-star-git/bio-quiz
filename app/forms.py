# from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField, SelectField, FieldList, FormField, Form
from wtforms.validators import DataRequired

file_choices = [('none', ''), ('a2a', 'Сопостовление'), ('card', 'Карточка')]

class QAForm(Form):
    question = TextAreaField('Вопрос', render_kw={"class": "question-field"})
    answer = StringField('Ответ', render_kw={"class": "question-field"})

class QuestionForm(Form):
    type = SelectField('Тип', choices=file_choices,render_kw={"class": "type-field"})
    question = FieldList(
        FormField(QAForm, ''),
        min_entries = 1, max_entries=16,
        render_kw={"class": "question"}
    )


class QuizAddForm(FlaskForm):
    quiz_title = StringField('Название')
    quiz_discription = StringField('Описание')
    quiz_theory = TextAreaField('Теория')
    quiz_img = FileField('Фон')
    quiz_submit = SubmitField('Создать')
    questions = FieldList(
        FormField(QuestionForm, 'Вопрос'),
        min_entries = 1, max_entries=16,
        render_kw={"class": "questions"}
    )
    # def validate_quiz_img(self, quiz_img):
    #     """ Функция проверки расширения файла """
    #     return ('.' in quiz_img.data.filename) and \
    #         quiz_img.data.filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']