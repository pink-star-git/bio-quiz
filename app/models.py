import sqlite3


class DB:
    def __init__(self):
        self.connect = sqlite3.connect("base.db", check_same_thread=False)
        self.cursor = self.connect.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS a (
                            id    INTEGER    PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT,
                            body  TEXT
        );""")

        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS quizz (
        #                         id    INTEGER    PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT,
        #                         name  TEXT (100),
        #                         des   TEXT,
        #                         th    TEXT,
        #                         image TEXT
        #                     );
        #                     """)

        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS quest (
        #                     id    INTEGER PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT,
        #                     type  INTEGER,
        #                     num   INTEGER,
        #                     quest TEXT,
        #                     answ  TEXT
        #                 );
        #                 """)

        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS qq (
        #                         id    INTEGER PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT,
        #                         quizz         REFERENCES quizz (id) ON DELETE CASCADE
        #                                                             ON UPDATE CASCADE,
        #                         quest         REFERENCES quest (id) ON DELETE CASCADE
        #                                                             ON UPDATE CASCADE
        #                     );
        #                     """)

    # def getLastId(self):
    #     self.cursor.execute('SELECT last_insert_rowid()')
    #     last_id = self.cursor.fetchone()
    #     return last_id

    # def addQ(self, title, desc, th, img):
    #     self.cursor.execute(
    #         'INSERT INTO quizz (name, des, th, image) VALUES (?, ?, ?, ?)', (title, desc, th, img))
    #     self.connect.commit()
    #     return self.getLastId()

    # def addQA(self, type, num, quest, answ):
    #     self.cursor.execute('INSERT INTO quest (type, num, quest, answ) VALUES (?,?,?,?)' (
    #         type, num, quest, answ))
    #     self.connect.commit()
    #     return self.getLastId()

    # def addQQ(self, quizz, quest):
    #     self.cursor.execute(
    #         'INSERT INTO qq (quizz, quest) VALUES (?, ?)', (quizz, quest))
    #     self.connect.commit()

    # def addQuizz(self, quizz):
    #     quizzId = self.addQ(
    #         quizz['title'], quizz['description'], quizz['theory'], quizz['img_url'])

    #     num = 0
    #     connectList = []
    #     for questions in quizz['questions']:
    #         if questions['type'] == "none":
    #             continue
    #         if questions['type'] == "a2a":
    #             num += 1
    #             for q in questions['answers']:
    #                 connectList.append(self.addQA(
    #                     questions['type'], num, q, questions['answers'][q]))
    #         else:
    #             connectList.append(self.addQA(
    #                 questions['type'], -1, questions['answers'], questions['answers'][q]))

    #     for cl in connectList:
    #         self.addQQ(quizzId, cl)

    # def getAllQuizz(self):
    #     self.cursor.execute("SELECT * FROM quizz")
    #     return self.cursor.fetchall()

    # def getQuizz(self, id):
    #     self.cursor.execute(f"""SELECT
    #                             quizz.id as id, quizz.name as title, quizz.des as des, quizz.th as theory, quizz.image as img,
    #                             quest.type as type, quest.num as num, quest.quest as quest, quest.answ as answer
    #                             FROM qq
    #                             LEFT JOIN quest ON quest.id == qq.quest
    #                             LEFT JOIN quizz ON quizz.id == qq.quizz
    #                             WHERE quizz.id == {id}""")

    #     answ = self.cursor.fetchall()
    #     num =
    #     for i in answ:
    #     return [answ[0][0],answ[0][1], answ[0][2], answ[0][3], answ[0][4], ]

    def add(self, q: str):
        self.cursor.execute("INSERT INTO a (body) VALUES (?)", (q,))
        self.connect.commit()

    def getAll(self) -> list[tuple[int, str]]:
        self.cursor.execute("SELECT * FROM a")
        return self.cursor.fetchall()

    def __del__(self):
        self.connect.close()
