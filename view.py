from model import Floor, Wall, Ceiling
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget

class Window(QWidget):
        def __init__(self):
            super().__init__()

            self.user_1 = None # Вибір виду ремонту кімнати
            self.user_2 = None # Вибір матеріалів які будуть виеористані
            self.height = None # Висота кімнати
            self.wight = None # Ширина кімнати
            self.length = None # Довжина кімнати
            self.dor_window = None # Довжина дверей і вікон
            self.wallpapers = None # Ширина шпалер
            self.finance = None # Бюджет користувача
            self.value = None # Віджет, який використовується
            self.area = None # Площа кімнати

            self.ui_main_window = uic.loadUi('main_window.ui')
            self.ui_choice_widget = uic.loadUi('choice_widget.ui')
            self.ui_wall_widget = uic.loadUi('wall_widget.ui')
            self.ui_ceiling_widget = uic.loadUi('ceiling_widget.ui')
            self.ui_floor_widget = uic.loadUi('floor_widget.ui')
            self.ui_finish_widget = uic.loadUi('finish_widget.ui')

            self.ui_main_window.setMaximumSize(651, 531)
            self.ui_main_window.setMinimumSize(651, 531)
            self.ui_choice_widget.setMaximumSize(547, 454)
            self.ui_choice_widget.setMinimumSize(547, 454)
            self.ui_wall_widget.setMaximumSize(715, 608)
            self.ui_wall_widget.setMinimumSize(715, 608)
            self.ui_ceiling_widget.setMaximumSize(651, 531)
            self.ui_ceiling_widget.setMinimumSize(651, 531)
            self.ui_floor_widget.setMaximumSize(651, 531)
            self.ui_floor_widget.setMinimumSize(651, 531)
            self.ui_finish_widget.setMaximumSize(651, 531)
            self.ui_finish_widget.setMinimumSize(651, 531)

            self.ui_main_window.setWindowTitle('Ремонт кімнати')
            self.ui_choice_widget.setWindowTitle('Вид ремонту')
            self.ui_wall_widget.setWindowTitle('Ремонт стіни')
            self.ui_ceiling_widget.setWindowTitle('Ремонт потолка')
            self.ui_floor_widget.setWindowTitle('Ремонт підлоги')
            self.ui_finish_widget.setWindowTitle('Результат')

            self.ui_main_window.main_pushButton.clicked.connect(self.click_main_window)
            self.ui_main_window.main_pushButton_2.clicked.connect(self.click_main_window)
            self.ui_main_window.show()

        def click_main_window(self):
            sander = self.sender()
            if sander.text() == 'Розпочати':
                self.click_main_icon_1()
            else:
                sys.exit()

        def click_main_icon_1(self):
            self.ui_choice_widget.show()
            self.ui_main_window.close()

            self.ui_choice_widget.pushButton.setEnabled(False)
            self.ui_choice_widget.radioButton.clicked.connect(lambda: self.block(2))
            self.ui_choice_widget.radioButton_2.clicked.connect(lambda: self.block(2))
            self.ui_choice_widget.radioButton_3.clicked.connect(lambda: self.block(2))
            self.ui_choice_widget.pushButton_2.clicked.connect(self.click_icon_1)
            self.ui_choice_widget.pushButton.clicked.connect(self.click_icon_1)

        def click_icon_1(self):

            sander = self.sender()
            if sander.text() == 'Назад':
                self.ui_main_window.show()
                self.ui_choice_widget.close()
            elif sander.text() == 'Підтвердити':

                if self.ui_choice_widget.comboBox.currentText() == 'Малий':
                    self.finance = 1
                elif self.ui_choice_widget.comboBox.currentText() == 'Середній':
                    self.finance = 2
                elif self.ui_choice_widget.comboBox.currentText() == 'Великий':
                    self.finance = 3

                if self.ui_choice_widget.radioButton.isChecked():
                    self.user_1 = 1
                    self.wall()
                elif self.ui_choice_widget.radioButton_2.isChecked():
                    self.user_1 = 2
                    self.floor()
                elif self.ui_choice_widget.radioButton_3.isChecked():
                    self.user_1 = 3
                    self.ceiling()

        def click_icon_wall(self):
            sander = self.sender()
            if sander.text() == 'Назад':
                self.ui_choice_widget.show()
                self.ui_wall_widget.close()
            elif sander.text() == 'Підтвердити':
                self.height = self.ui_wall_widget.doubleSpinBox.value()
                self.wight = self.ui_wall_widget.doubleSpinBox_2.value()
                self.length = self.ui_wall_widget.doubleSpinBox.value()
                self.dor_window = self.ui_wall_widget.doubleSpinBox.value()

                if self.ui_wall_widget.radioButton.isChecked():
                    self.user_2 = 1
                elif self.ui_wall_widget.radioButton_2.isChecked():
                    self.user_2 = 2
                elif self.ui_wall_widget.radioButton_3.isChecked():
                    self.user_2 = 3

                if self.ui_wall_widget.comboBox.currentText() == '0.53':
                    self.wallpapers = 1
                elif self.ui_wall_widget.comboBox.currentText() == '0.7':
                    self.wallpapers = 2
                elif self.ui_wall_widget.comboBox.currentText() == '1.06':
                    self.wallpapers = 3

                self.finish()
                self.ui_wall_widget.close()

        def click_icon_ceiling(self):
            sander = self.sender()
            if sander.text() == 'Назад':
                self.ui_choice_widget.show()
                self.ui_ceiling_widget.close()

            elif sander.text() == 'Підтвердити':
                self.area = self.ui_ceiling_widget.doubleSpinBox_16.value()

                if self.ui_ceiling_widget.radioButton.isChecked():
                    self.user_2 = 1
                elif self.ui_ceiling_widget.radioButton_2.isChecked():
                    self.user_2 = 2

                self.finish()
                self.ui_ceiling_widget.close()

        def click_icon_floor(self):

            sander = self.sender()
            if sander.text() == 'Назад':
                self.ui_choice_widget.show()
                self.ui_floor_widget.close()
            elif sander.text() == 'Підтвердити':

                self.area = self.ui_floor_widget.doubleSpinBox_16.value()

                if self.ui_floor_widget.radioButton.isChecked():
                    self.user_2 = 1
                elif self.ui_floor_widget.radioButton_2.isChecked():
                    self.user_2 = 2
                elif self.ui_floor_widget.radioButton_3.isChecked():
                    self.user_2 = 3

                self.finish()
                self.ui_floor_widget.close()

        def click_icon_finish(self):

            sander = self.sender()
            if sander.text() == 'Назад':
                if self.value == 3:
                    self.ui_wall_widget.show()
                elif self.value == 4:
                    self.ui_ceiling_widget.show()
                elif self.value == 5:
                    self.ui_floor_widget.show()
                self.ui_finish_widget.close()
            elif sander.text() == 'Розпочати с початку':
                self.ui_finish_widget.close()
                self.ui_main_window.show()
            elif sander.text() == 'Завершити':
                self.ui_finish_widget.close()

        def wall(self):

            self.ui_wall_widget.show()
            self.ui_choice_widget.close()
            self.value = 3

            self.ui_wall_widget.pushButton_2.setEnabled(False)
            self.ui_wall_widget.comboBox.setEnabled(False)
            self.ui_wall_widget.radioButton.clicked.connect(lambda: self.block(3))
            self.ui_wall_widget.radioButton_2.clicked.connect(lambda: self.block(3))
            self.ui_wall_widget.radioButton_3.clicked.connect(lambda: self.block(3))

            self.ui_wall_widget.pushButton_2.clicked.connect(self.click_icon_wall)
            self.ui_wall_widget.pushButton.clicked.connect(self.click_icon_wall)

        def ceiling(self):

            self.ui_ceiling_widget.show()
            self.ui_choice_widget.close()
            self.value = 4

            self.ui_ceiling_widget.pushButton_2.setEnabled(False)
            self.ui_ceiling_widget.radioButton.clicked.connect(lambda: self.block(4))
            self.ui_ceiling_widget.radioButton_2.clicked.connect(lambda: self.block(4))

            self.ui_ceiling_widget.pushButton_2.clicked.connect(self.click_icon_ceiling)
            self.ui_ceiling_widget.pushButton.clicked.connect(self.click_icon_ceiling)

        def floor(self):

            self.ui_floor_widget.show()
            self.ui_choice_widget.close()
            self.value = 5

            self.ui_floor_widget.pushButton_2.setEnabled(False)
            self.ui_floor_widget.radioButton.clicked.connect(lambda: self.block(5))
            self.ui_floor_widget.radioButton_2.clicked.connect(lambda: self.block(5))
            self.ui_floor_widget.radioButton_3.clicked.connect(lambda: self.block(5))

            self.ui_floor_widget.pushButton_2.clicked.connect(self.click_icon_floor)
            self.ui_floor_widget.pushButton.clicked.connect(self.click_icon_floor)

        def block(self, number_block):

            if number_block == 2:

                if self.ui_choice_widget.radioButton.isChecked() == True or self.ui_choice_widget.radioButton_2.isChecked() == True or self.ui_choice_widget.radioButton_3.isChecked() == True:
                    self.ui_choice_widget.pushButton.setEnabled(True)

            elif number_block == 3:

                if self.ui_wall_widget.radioButton.isChecked() == True or self.ui_wall_widget.radioButton_2.isChecked() == True or self.ui_wall_widget.radioButton_3.isChecked() == True:
                    self.ui_wall_widget.pushButton_2.setEnabled(True)
                if self.ui_wall_widget.radioButton.isChecked():
                    self.ui_wall_widget.comboBox.setEnabled(True)
                else:
                    self.ui_wall_widget.comboBox.setEnabled(False)

            elif number_block == 4:

                if self.ui_ceiling_widget.radioButton.isChecked() == True or self.ui_ceiling_widget.radioButton_2.isChecked() == True:
                    self.ui_ceiling_widget.pushButton_2.setEnabled(True)
            elif number_block == 5:

                if self.ui_floor_widget.radioButton.isChecked() == True or self.ui_floor_widget.radioButton_2.isChecked() == True or self.ui_floor_widget.radioButton_3.isChecked() == True:
                    self.ui_floor_widget.pushButton_2.setEnabled(True)

        def finish(self):
            self.ui_finish_widget.show()
            if self.value == 3:
                if self.height == 0 or self.wight == 0 or self.length == 0:
                    self.msgInf = QtWidgets.QMessageBox()
                    self.msgInf.setIcon(QtWidgets.QMessageBox.Information)
                    self.msgInf.setInformativeText("Заповніть коректно поля")
                    self.msgInf.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    self.msgInf.exec_()
            elif self.value == 4 or self.value == 5:
                if self.area == 0:
                    self.msgInf = QtWidgets.QMessageBox()
                    self.msgInf.setIcon(QtWidgets.QMessageBox.Information)
                    self.msgInf.setInformativeText("Заповніть коректно поля")
                    self.msgInf.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    self.msgInf.exec_()
            if self.value == 3:
                W = Wall(self.user_1, self.user_2, self.height, self.wight, self.length, self.dor_window, self.wallpapers, self.finance)
                finnish = W.calculation()
                self.out_materials(finnish)
            elif self.value == 4:
                C = Ceiling(self.user_1, self.user_2, self.area, self.finance)
                finnish = C.calculation()
                self.out_materials(finnish)
            elif self.value == 5:
                F = Floor(self.user_1, self.user_2, self.area, self.finance)
                finnish = F.calculation()
                self.out_materials(finnish)

            self.ui_finish_widget.pushButton_2.clicked.connect(self.click_icon_finish)
            self.ui_finish_widget.pushButton.clicked.connect(self.click_icon_finish)
            self.ui_finish_widget.pushButton_3.clicked.connect(self.click_icon_finish)


        def out_materials(self, finnish):

            finnish_list = str()
            for j, k in finnish.items():
                finnish_list += j + '\n'
                for i, l in k.items():
                    finnish_list += i + ': ' + l + '\n'
            self.ui_finish_widget.textBrowser.setText(finnish_list)

def start_program():
    app = QtWidgets.QApplication(sys.argv)
    a = Window()
    sys.exit(app.exec_())