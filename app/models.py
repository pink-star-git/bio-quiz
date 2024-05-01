from app import db


class QuizzDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True)
    description = db.Column(db.Text, index=True)
    theory = db.Column(db.Text, index=True)
    image = db.Column(db.String(200), index=True)
    qqs = db.relationship('QQDatabase', backref='quests', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.name)


class QQDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idQuizz = db.Column(db.Integer, db.ForeignKey('quizzdatabase.id'))
    idQuest = db.Column(db.Integer, db.ForeignKey('questdatabase.id'))


class QuestDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, index=True)
    num = db.Column(db.Integer, index=True)
    quest = db.Column(db.Text, index=True)
    answer = db.Column(db.Text, index=True)
    qqs = db.relationship('QQDatabase', backref='quizzs', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.quest)
