quizs = {
    "1": {
        "title": "quiz #1",
        "description": "test quiz description",
        "theory": "test is the test quiz description",
        "img_url": "/static/img/test.png",
        "questions": [
            {
                "type": "a2a",
                "answers": {
                        "test 1": "aboba 1",
                        "test 2": "aboba 2",
                        "test 3": "aboba 3",
                        "test 4": "aboba 4"
                }
            },
            {
                "type": "card",
                "answers": {
                        "test 1": "aboba 1"
                }
            }
        ]
    },
    "2": {
        "title": "quiz #2",
        "description": "test more quiz",
        "teory": "test is the test quiz description",
        "img_url": "/static/img/zebra.png",
        "type": "multiple_choice",
        "questions": [
            {
                "title": "question2",
                "answers": {
                    "test 1": "aboba 1",
                    "test 2": "aboba 2",
                    "test 3": "aboba 3",
                    "test 4": "aboba 4"
                }
            }
        ]
    }
}


for a in quizs['1']['questions'][0]['answers']:
    print(a)
    print(quizs['1']['questions'][0]['answers'][a])
