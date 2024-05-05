import sqlite3


class DB:
    _connection = {}
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._connection = sqlite3.connect("base.db", check_same_thread=False)
            cls._connection.execute("""
                                    CREATE TABLE IF NOT EXISTS a (
                                    id    INTEGER    PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT,
                                    body  TEXT);""")

        return cls._instance

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

    @classmethod
    def add(cls, q: str):
        cls._connection.execute("INSERT INTO a (body) VALUES (?)", (q,))
        cls._connection.commit()

    @classmethod
    def getAll(cls) -> list[tuple[int, str]]:
        cursor = cls._connection.cursor()
        cursor.execute("SELECT * FROM a")
        return cursor.fetchall()

    @classmethod
    def shutdown(cls):
        cls._connection.close()
