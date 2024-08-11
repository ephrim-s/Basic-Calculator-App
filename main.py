#Import Moduls
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont

class CalcApp(QWidget):
    #App Settings
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator App")
        self.resize(350,500)

        #Create all App Objects
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 32))


        self.grid = QGridLayout()

        self.buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+"
            ]
        
        row = 0
        col = 0

        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            button.setStyleSheet("QPushButton {font: 25pt Comic Sans Ms; padding: 10px}")
            self.grid.addWidget(button, row, col)
            col +=1

            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton("Clear")
        self.delete = QPushButton("<")
        self.clear.setStyleSheet("QPushButton {font: 25pt Comic Sans Ms; padding: 10px}")
        self.delete.setStyleSheet("QPushButton {font: 25pt Comic Sans Ms; padding: 10px}")

        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25,25,25,25)

        self.setLayout(master_layout)

        #Events
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)
        self.text_box.returnPressed.connect(self.button_click)

    def button_click(self):
        button = self.sender()
        # text = button.text()
        if isinstance(button, QPushButton):
            text = button.text()  # Corrected from tex() to text()
        else:
            text = "="  # Treat Enter key as pressing "="

        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))

            except Exception as e:
                print("Error:", e)
        
        elif text == "Clear":
            self.text_box.clear()

        elif text == "<":
            current_text = self.text_box.text()
            self.text_box.setText(current_text[:-1])
        
        else:
            current_text = self.text_box.text()
            self.text_box.setText(current_text + text)

    

    #All Design Here


#Show/Run our App
if __name__ in "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget {background-color: #f0f0")
    main_window.show()
    app.exec_()