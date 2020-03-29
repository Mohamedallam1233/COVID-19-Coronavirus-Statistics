from covid import Covid
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import csv
covid = Covid()
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
ui,_ = loadUiType('main.ui')
class MainApp(QMainWindow , ui):
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.label_5.setText(str(covid.get_total_active_cases()))
        self.label_6.setText(str(covid.get_total_confirmed_cases()))
        self.label_7.setText(str(covid.get_total_recovered()))
        self.label_8.setText(str(covid.get_total_deaths()))
        cov = covid.get_data()
        name=""
        for i in cov:
            name += list(i.values())[1]
            name += ","
        self.tableWidget.setRowCount(len(cov))
        self.tableWidget.setVerticalHeaderLabels((name).split(","))
        for i in range(len(cov)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(list(cov[i].values())[2])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(list(cov[i].values())[3])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(list(cov[i].values())[4])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(list(cov[i].values())[5])))
        self.handel_btn()
    def handel_btn(self):
        self.pushButton.clicked.connect(self.save_csv)
    def save_csv(self):
        try:
            url_output = QFileDialog.getSaveFileName(self, 'Save As', '', 'excel (*.csv)')[0]
            cov = covid.get_data()
            print(cov)
            # my data rows as dictionary objects
            # field names
            fields = ['id', 'country', 'confirmed', 'active', 'deaths', 'recovered', 'latitude', 'longitude','last_update']
            # name of csv file
            filename = url_output
            # writing to csv file
            with open(filename, 'w') as csvfile:
                # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                # writing headers (field names)
                writer.writeheader()
                # writing data rows
                writer.writerows(cov)
            QMessageBox.about(self, 'ok', 'it saved succesfully')
        except:
            QMessageBox.about(self, 'error', 'you have error try again')

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
if __name__ == '__main__':
    sys.excepthook = except_hook
    main()
