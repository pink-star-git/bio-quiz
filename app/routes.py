import os
import json
from flask import render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from app import app
from app.forms import QuizAddForm
from app.models import DB
# from app.models import DB

db = DB()

#  quizs-{
#   "<id>":<quiz>,
#   ...
#  }

#  quiz-{
#      "title":"<title>",
#      "description":"<description>",
#      "img_url":"<img_url>",
#      "type":"<type>",
#      "questions":[
#          <question>,
#          ...
#      ]
#  }

'''
{
    "title":"asdsdad",
    "description":"asdsaf",
    "theory":"test is the test quiz description",
    "img_url":"/static/img/600x800",
    "questions":[
        {
            "type":"a2a",
            "answers":{
                "asd":"asd"
            }
        },
        {
            "type":"card",
            "answers":{
                "asda":"dfgd"
            }
        }
    ]
}
'''

# quizs = {
#     "1": {
#         "title":"quiz #1",
#         "description":"test quiz description",
#         "theory":"test is the test quiz description",
#         "img_url":"/static/img/test.png",
#         "questions":[
#             {
#                 "type":"a2a",
#                 "answers":{
#                         "test 1":"aboba 1",
#                         "test 2":"aboba 2",
#                         "test 3":"aboba 3",
#                         "test 4":"aboba 4"
#                 }
#             },
#             {
#                 "type":"card",
#                 "answers":{
#                         "test 1\\n?":"aboba 1"
#                 }
#             }
#         ]
#     },
#     "2": {
#         "title":"quiz #2",
#         "description":"test more quiz",
#         "teory":"test is the test quiz description",
#         "img_url":"/static/img/zebra.png",
#         "type":"multiple_choice",
#         "questions":[
#             {
#                 "title":"question2",
#                 "answers":{
#                         "test 1":"aboba 1",
#                         "test 2":"aboba 2",
#                         "test 3":"aboba 3",
#                         "test 4":"aboba 4"
#                 }
#             }
#         ]
#     }
# }


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    quizs = {i[0]:json.loads(i[1]) for i in db.getAll()}
    return render_template('index.html', quizs=quizs)

@app.route('/add-quiz', methods=['GET', 'POST'])
@app.route('/add-quiz.html', methods=['GET', 'POST'])
def add_quiz():
    quiz_add_form = QuizAddForm()
    if quiz_add_form.is_submitted():
        filename = secure_filename(quiz_add_form.quiz_img.data.filename)
        quiz_add_form.quiz_img.data.save(f'{app.config["UPLOAD_FOLDER"]}/{filename}')

        # quizs[str(int(list(quizs.keys())[-1])+1)] = {
        #     'title':quiz_add_form.quiz_title.data,
        #     'description':quiz_add_form.quiz_discription.data,
        #     'theory':quiz_add_form.quiz_theory.data.replace('\r\n', '\\n',  -1),
        #     'img_url':f'/static/img/{filename}',
        #     'questions':[
        #         {
        #             'type':item['type'],
        #             'answers':{
        #                 qa['question']:qa['answer']
        #             for qa in item['question']}
        #         }
        #     for item in quiz_add_form.questions.data if item['type'] != 'none']
        # }
        # print(json.dumps(quizs[list(quizs.keys())[-1]]))
        db.add(json.dumps({
            'title':quiz_add_form.quiz_title.data,
            'description':quiz_add_form.quiz_discription.data,
            'theory':quiz_add_form.quiz_theory.data,
            'img_url':f'/static/img/{filename}',
            'questions':[
                {
                    'type':item['type'],
                    'answers':{
                        qa['question']:qa['answer']
                    for qa in item['question']}
                }
            for item in quiz_add_form.questions.data if item['type'] != 'none']
        }).replace('\r\n', '\\n',  -1))

        print('add quiz: successfully')
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('add-quiz.html', add_form=quiz_add_form)
    return redirect(url_for('error500'))

@app.route('/quiz/<quiz_id>')
def quiz(quiz_id):
    quizs = {f"{i}":q for i, q in db.getAll()}
    if quiz_id in list(quizs.keys()):
        return render_template('quiz.html', quiz=quizs[quiz_id])# quiz=json.dumps(quizs[quiz_id]))
    # else:
    #     print(quiz_id)
    #     print(list(quizs.keys()))
    return redirect(url_for('error404'))


@app.route('/error-404')
def error404():
    return render_template('errors/404.html')

@app.route('/error-500')
def error500():
    return render_template('errors/500.html')

@app.route('/error-502')
def error502():
    return render_template('errors/502.html')

# @app.route('/index', methods=['GET', 'POST'])
# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # проверим, передается ли в запросе файл 
#         if 'file' not in request.files:
#             # После перенаправления на страницу загрузки
#             # покажем сообщение пользователю 
#             flash('Не могу прочитать файл')
#             return redirect(request.url)
#         file = request.files['file']
#         # Если файл не выбран, то браузер может
#         # отправить пустой файл без имени.
#         if file.filename == '':
#             flash('Нет выбранного файла')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             # безопасно извлекаем оригинальное имя файла
#             filename = secure_filename(file.filename)
#             # сохраняем файл
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             # если все прошло успешно, то перенаправляем  
#             # на функцию-представление `download_file` 
#             # для скачивания файла
#             return redirect(url_for('download_file', name=filename))
#     return '''
#     <!doctype html>
#     <title>Загрузить новый файл</title>
#     <h1>Загрузить новый файл</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     </html>
#     '''