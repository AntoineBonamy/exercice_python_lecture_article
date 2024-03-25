import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QVBoxLayout, QWidget, QTextEdit
from PySide6.QtGui import QTextOption

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Déclaration des Droits de l'Homme et du Citoyen de 1789")

        self.articles = []
        with open("declaration1789.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("Art."):
                    self.articles.append(line.strip())

        welcome_label = QLabel("Bienvenue ! Veuillez choisir un numéro d'article dans la liste déroulante :")

        self.article_combobox = QComboBox()
        self.article_combobox.addItems([str(i+1) for i in range(len(self.articles))])

        show_article_button = QPushButton("Afficher l'article")
        show_article_button.clicked.connect(self.show_article)

        layout = QVBoxLayout()
        layout.addWidget(welcome_label)
        layout.addWidget(self.article_combobox)
        layout.addWidget(show_article_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.article_window = None

    def show_article(self):
        article_index = self.article_combobox.currentIndex()
        if 0 <= article_index < len(self.articles):
            article_text = self.articles[article_index]

            if not self.article_window or not self.article_window.isVisible():
                self.article_window = ArticleWindow(article_text)
            else:
                self.article_window.update_article(article_text)
            self.article_window.show()

    def closeEvent(self, event):
        if self.article_window:
            self.article_window.close()
            self.article_window = None
        event.accept()
class ArticleWindow(QMainWindow):
    def __init__(self, article_text):
        super().__init__()

        self.setWindowTitle("Article")
        self.resize(400, 100)

        self.article_text_edit = QTextEdit()
        self.article_text_edit.setPlainText(article_text)
        self.article_text_edit.setReadOnly(True)
        self.article_text_edit.setWordWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)

        self.setCentralWidget(self.article_text_edit)

    def update_article(self, article_text):
        self.article_text_edit.setPlainText(article_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())