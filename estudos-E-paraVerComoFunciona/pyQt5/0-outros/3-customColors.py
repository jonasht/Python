
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QPushButton

app = QApplication([])

app.setStyle('Fusion')
palette = QPalette()
# palette.setColor(QPalette.buttonText, Qt.red)
palette.setColor(QPalette.buttonText, Qt.red)

app.setPalette(palette)
button = QPushButton('ola mundo/hello world')
button.show()
app.exec()
