import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap
# 필요한 묘듈들 불러옵니다
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap('DK.png'))) # 창 화면에 이미지 출력
        self.setPalette(palette)

    def initUI(self):
        self.btn0 = QPushButton.clicked.connect(self.NumClicked)
        self.btn0.setIcon(QIcon("0.png"))
        self.btn0.setIconSize(QSize(50,50))
        self.btn0.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.btn1 = QPushButton(self)
        self.btn1.setIcon(QIcon("1.png"))
        self.btn1.setIconSize(QSize(50,50))
        self.btn1.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.btn2 = QPushButton(self)
        self.btn2.setIcon(QIcon("2.png"))
        self.btn2.setIconSize(QSize(50,50))
        self.btn2.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.btn3 = QPushButton(self)
        self.btn3.setIcon(QIcon("3.png"))
        self.btn3.setIconSize(QSize(50,50))
        self.btn3.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.btn4 = QPushButton(self)
        self.btn4.setIcon(QIcon("4.png"))
        self.btn4.setIconSize(QSize(50,50))
        self.btn4.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.btn5 = QPushButton(self)
        self.btn5.setIcon(QIcon("5.png"))
        self.btn5.setIconSize(QSize(50,50))
        self.btn5.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.btn6 = QPushButton(self)
        self.btn6.setIcon(QIcon("6.png"))
        self.btn6.setIconSize(QSize(50,50))
        self.btn6.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.btn7 = QPushButton(self)
        self.btn7.setIcon(QIcon("7.png"))
        self.btn7.setIconSize(QSize(50,50))
        self.btn7.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.btn8 = QPushButton(self)
        self.btn8.setIcon(QIcon("8.png"))
        self.btn8.setIconSize(QSize(50,50))
        self.btn8.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.btn9 = QPushButton(self)
        self.btn9.setIcon(QIcon("9.png"))
        self.btn9.setIconSize(QSize(50,50))
        self.btn9.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.bPlus = QPushButton(self)
        self.bPlus.setIcon(QIcon("ej.png"))
        self.bPlus.setIconSize(QSize(50,50))
        self.bPlus.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.bMinus = QPushButton(self)
        self.bMinus.setIcon(QIcon("Qo.png"))
        self.bMinus.setIconSize(QSize(50,50))
        self.bMinus.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.bgogo = QPushButton(self)
        self.bgogo.setIcon(QIcon("rhq.png"))
        self.bgogo.setIconSize(QSize(50,50))
        self.bgogo.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.bnana = QPushButton(self)
        self.bnana.setIcon(QIcon("sk.png"))
        self.bnana.setIconSize(QSize(50,50))
        self.bnana.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.clearAll = QPushButton(self)
        self.clearAll.setIcon(QIcon("C.png"))
        self.clearAll.setIconSize(QSize(50,50))
        self.clearAll.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")
        self.nen = QPushButton(self)
        self.nen.setIcon(QIcon("sms.png"))
        self.nen.setIconSize(QSize(50,50))
        self.nen.setStyleSheet("font-size: 40pt;"
                           "background-color: none;"
                           "border: none")


        self.play = QLineEdit("0" , self)
        self.play.setReadOnly(True)
        self.play.setAlignment(Qt.AlignRight)
        self.play.setStyleSheet("border:0px; font-size:20pt; font-family:Nanum Gothic; font-weight:bold; padding:10px")
        self.play.move(10, 10)  # 창위치 설정

        grid = QGridLayout()
        self.setLayout(grid)

        layout = QVBoxLayout()
        layout.addWidget(self.play)
        layout.addLayout(grid)
        self.setLayout(layout)

        grid.addWidget(self.play, 0, 0, 1, 4)
        grid.addWidget(self.btn1, 1, 0, 1, 1)
        grid.addWidget(self.btn2, 1, 1, 1, 1)
        grid.addWidget(self.btn3, 1, 2, 1, 1)
        grid.addWidget(self.btn4, 2, 0, 1, 1)
        grid.addWidget(self.btn5, 2, 1, 1, 1)
        grid.addWidget(self.btn6, 2, 2, 1, 1)
        grid.addWidget(self.btn7, 3, 0, 1, 1)
        grid.addWidget(self.btn8, 3, 1, 1, 1)
        grid.addWidget(self.btn9, 3, 2, 1, 1)
        grid.addWidget(self.btn0, 4, 1, 1, 1)
        grid.addWidget(self.bPlus, 1, 3, 1, 1)
        grid.addWidget(self.bMinus, 2, 3, 1, 1)
        grid.addWidget(self.bgogo, 3, 3, 1, 1)
        grid.addWidget(self.bnana, 4, 3, 1, 1)
        grid.addWidget(self.clearAll, 4, 0, 1, 1)
        grid.addWidget(self.nen, 4, 2, 1, 1)

        self.setWindowTitle('계산기') # 창 제목
        self.setWindowIcon(QIcon('icon.png')) # 창 아이콘 넣기
        self.left = 300
        self.top = 400
        self.width = 256
        self.height = 359
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def clearAll(self): # AllClear 함수 만듬
        self.play.setText("0")
        self.input_temporary = ""
        self.input_history = ""
        self.waitingForOperand = True


    def NumClicked(self):
        list = self.paly.text()
        now_text = self.btn0.text()

        self.play.setText(list + now_text)

if __name__ == '__main__': # 내장 변수수
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())