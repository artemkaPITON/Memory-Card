from PyQt5.QtWidgets import QWidget, QHBoxLayout, QRadioButton, \
    QPushButton, QLabel, QSpinBox, QButtonGroup, QApplication, QVBoxLayout, QGroupBox,QLineEdit
from PyQt5.QtCore import Qt


menu_w =QWidget()


lb_question = QLabel("Введіть запитання:")
lb_right_ans = QLabel("Введіть вірну віповідь:")
lb_wrong_ans1 = QLabel("введіть першу хибну відповідь:")
lb_wrong_ans2 = QLabel("введіть другу хибну відповідь:")
lb_wrong_ans3 = QLabel("введіть третю хибну відповідь:")





le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 =QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()