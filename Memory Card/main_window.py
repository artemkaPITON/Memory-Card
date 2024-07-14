from PyQt5.QtWidgets import QWidget, QHBoxLayout, QRadioButton, \
    QPushButton, QLabel, QSpinBox, QButtonGroup, QApplication
from PyQt5.QtCore import Qt


window = QWidget()



btn_menu = QPushButton()
btn_rest = QPushButton()
btn_next = QPushButton()


rb_an1 = QRadioButton("1")
rb_an2 = QRadioButton("2")
rb_an3 = QRadioButton("3")
rb_an4 = QRadioButton("4")

rbGroup = QButtonGroup
rbGroup.abbButton(rb_an1)
rbGroup.abbButton(rb_an2)
rbGroup.abbButton(rb_an3)
rbGroup.abbButton(rb_an4)
                 
                 
lb_question = QLabel("Запитання")
lb_rest = QLabel("хвилин")                 
                 

lb_rightAns = QLabel("відповідь")           
lb_result = QLabel("Вірно!")

sp_rest = QSpinBox()
gbAns = QButtonGroup("Варіанти вілповідей")

rb_v1 = QButtonGroup
rb_v2 = QButtonGroup
rb_v3 = QHBoxLayout

rb_v1.addWidget(rb_ans1)
rb_v2.addWidget(rb_ans2)
rb_v3.addWidget(rb_ans4)
rb_v4.addWidget(rb_ans4)

rb_h.addLayout(rb_v1)
rb_h.addLayout(rb_v2)

gbAns.setLayout(rb_h)



















                 
                 