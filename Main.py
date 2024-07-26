import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QWidget
from PyQt5.QtCore import QObject, pyqtSlot

from MainWindow import MainWindow
from untitled import Ui_MainWindow
from database import connect_to_db, get_medical_institutions, insert_medical_institution


class Main:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Инициализация базы данных
        self.conn = connect_to_db()
        # Загрузка данных при инициализации
        self.show_medical_institutions()

        self.ui.stackedWidget.setCurrentWidget(self.ui.HomePage)

        # Main Button Pages
        self.ui.main_button.clicked.connect(self.showMainPage)
        self.ui.equipment_button.clicked.connect(self.showEquipmentPage)
        self.ui.pacient_button.clicked.connect(self.showPacientPage)
        self.ui.documents_button.clicked.connect(self.showDocumentsPage)
        self.ui.chat_button.clicked.connect(self.showChatPage)
        self.ui.directory_button.clicked.connect(self.showDirectoryPage)
        self.ui.settings_button.clicked.connect(self.showSettingsPage)

        # Directory Button Pages
        self.ui.check_button_med.clicked.connect(self.showCheckPageMed)
        self.ui.add_button_med.clicked.connect(self.showAddPageMed)

        self.ui.send_button_med.clicked.connect(self.add_data_to_db)

    def show(self):
        self.main_win.showMaximized()

    def showMainPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.MainPage)

    def showEquipmentPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.EquipmentPage)

    def showPacientPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PacientPage)

    def showDocumentsPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.DocumentsPage)

    def showChatPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ChatPage)

    def showDirectoryPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.DirectoryPage)

    def showSettingsPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.SettingsPage)

    def showCheckPageMed(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.check_page_med)

    def showAddPageMed(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.add_page_med)

    def show_medical_institutions(self):
        data = get_medical_institutions()
        if data:
            self.load_data_into_table(data)

    def load_data_into_table(self, data):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(
            ["ID", "Name", "Address", "Phone", "Email", "Type", "Website", "Worktime", "Head"])

        for row in data:
            items = [QStandardItem(str(field)) for field in row]
            model.appendRow(items)

        self.ui.tableView.setModel(model)

    def add_data_to_db(self):
        # Получаем данные из LineEdit
        name = self.ui.lineEdit_2.text()
        address = self.ui.lineEdit_3.text()
        phone = self.ui.lineEdit_4.text()
        email = self.ui.lineEdit_5.text()
        med_type = self.ui.lineEdit_6.text()
        website = self.ui.lineEdit_7.text()
        worktime = self.ui.lineEdit_8.text()
        head = self.ui.lineEdit_9.text()

        # SQL запрос для вставки данных
        query = """
        INSERT INTO medical_institutions (
            medical_name, medical_address, medical_phone, medical_email, medical_type, medical_website, medical_worktime, medical_head
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (name, address, phone, email, med_type, website, worktime, head)

        # Выполняем запрос
        cursor = self.conn.cursor()
        cursor.execute(query, data)
        self.conn.commit()
        cursor.close()

        # Обновляем данные в TableView
        self.load_data_into_table(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = Main()
    main_win.show()

    sys.exit(app.exec_())






