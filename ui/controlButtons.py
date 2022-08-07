from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class ControlButtons(QWidget):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        layout = QHBoxLayout(self)
        
        self.pushButton = QPushButton(self)
        self.pushButton.setText(u"play/stop")

        self.pushButtonPrev = QPushButton(self)
        self.pushButtonPrev.setText(u"<")
        
        self.pushButtonNext = QPushButton(self)
        self.pushButtonNext.setText(u">")
        
        layout.addWidget(self.pushButtonPrev)      
        layout.addWidget(self.pushButton)
        layout.addWidget(self.pushButtonNext)

        self.setLayout(layout)