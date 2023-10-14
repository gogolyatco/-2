from PyQt5.QtWidgets import QApplication
#------------------------
#урок 3
from random import choice, shuffle
from time import sleep
#------------------------
app = QApplication([])
from m2 import *
from m3 import *
#------------------
#урок3
class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2,
                 wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1
#
#
q1 = Question('Що сказав Гендельф на містку?', 'Ти не пройдеш!', 'Ти не пожреш!', 'Ти помреш!', 'Ти в школу підеш')
q2 = Question('Хто йшов під крутий фонк?', 'Джим, д. Лівсі, Сквайр Трелоні', 'д. Лівсі', 'Чорний пес, сліпий П"ю, Джим', 'mr. Beast')
q3 = Question('Хто кричав фразу "Що ви забули на моєму болоті"?', 'Шрек', 'путін', 'осел', 'якийсь кіт')
q4 = Question('Хто ухилився від граду куль', 'Нео', 'Оен', 'Не нео', 'отой пацан')
q5 = Question('Скільки mr. Beast хотів скинути тротилу', '250 тисяч тонн', '250 тонн', '6 особин', '250 тисяч міліметрів')
q6 = Question('Яка мелодія була при програшу в fnaf', 'Марш Тореадора', 'Пісня Скотта', 'Симфонія Баха', 'Бетховен "Хорал"')
q7 = Question('Хто сказав фразум "Сім"я це головне"', 'Домінік Торетто', 'мама', 'Домінік Торенто', 'отой пацан')
q8 = Question('Хто ухилився від граду куль', 'Нео', 'Оен', 'Не нео', 'отой пацан')
q9 = Question('Хто ухилився від граду куль', 'Нео', 'Оен', 'Не нео', 'отой пацан')
q10 = Question('Хто ухилився від граду куль', 'Нео', 'Оен', 'Не нео', 'отой пацан')
q11 = Question('Хто ухилився від граду куль', 'Нео', 'Оен', 'Не нео', 'отой пацан')
q12 = Question('Хто ухилився від граду куль', 'Нео', 'Оен', 'Не нео', 'отой пацан')
#----------------------------------



def menu_generation():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)
window.show()
app.exec_()