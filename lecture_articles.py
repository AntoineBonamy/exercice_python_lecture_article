import sys
from PySide6.QtWidgets import QApplication, QDialog
from ui_mainwindow import Ui_Dialog

class ArticleReader:
    def __init__(self) -> None:
        self.articles = []
        self.clean_articles = []
        with open("declaration1789.txt", "r") as file:
            for line in file:
                self.articles.append(line.strip("\n"))
        self.articles.pop(0)
        self.articles.pop(0)
        for article in self.articles:
            self.clean_articles.append(article)

    def get_article(self, index):
        if 0 <= index < len(self.clean_articles):
            return self.clean_articles[index]
        else:
            return "Article non trouvé"
            
    def valider_clic(self):
            pass

class ArticleReaderApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.article_reader = ArticleReader()
        self.dialog = QDialog()
        self.interface = Ui_Dialog()
        self.interface.setupUi(self.dialog)
        self.interface.buttonBox.accepted.connect(self.article_reader.valider_clic)
        self.interface.buttonBox.rejected.connect(self.dialog.reject)
        self.interface.spinBox.valueChanged.connect(self.update_article_display)
        self.update_article_display()

    def update_article_display(self):
        article_index = self.interface.spinBox.value() - 1
        article_text = self.article_reader.get_article(article_index)
        self.interface.plainTextEdit.setPlainText(article_text)

    def run(self):
        self.dialog.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    app_instance = ArticleReaderApp()
    app_instance.run()