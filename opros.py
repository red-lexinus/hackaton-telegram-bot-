# вопросы, 2 варианты ответов, 3 результаты ,они соотносятся по индыксам со 2
arr_question = [['в кино вы ходите только ради фильма', ['да', 'когда как', 'нет'], [0, 0.5, 1]],
                ['любитите ли вы заниматься шопингом', ['да', 'не особо', 'нет'], [1, 0.5, 0]],
                ['приятно ли вам посещать музеи', ['да', 'не особо', 'нет'], [1, 0.5, 0]],
                ['любите ли вы достопримечательности в посещаемых вами городах ', ['да', 'не особо', 'нет'],
                 [1, 0.5, 0]], ['какая погода может стать критичной для вас по отношеню к простой прогулке',
                                ['0', '-5', '-10', '-15', '-20', '-25', '30'],
                                [0, -5, -10, -15, -20, -25, -30]]]

arr_questions = {'фильмы': 0, 'магазины': 1, 'музеи': 2, 'достопримечательности': 3}
arr_answer = [1, 1, 1, 1, -20]


def completing_test(arr):
    global arr_answer
    arr_answer = arr


def change_answer(num, resulat=1):
    global arr_answer
    if num == 4 and resulat > 0:
        resulat = -20
    arr_answer[num] = resulat
