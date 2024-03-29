import sys
import logging
sys.path.append('../')
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
LOGGER=logging.getLogger('client')

#Dialog for selecting a contact to add
class AddContactDialog(QDialog):
    def __init__(self,transport,database):
        super().__init__()
        self.transport=transport
        self.database=database

        self.setFixedSize(350,120)
        self.setWindowTitle('Выберите контакт для добавления:')
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setModal(True)

        self.selector_label=QLabel('Выберите контакт для добавления:', self)
        self.selector_label.setFixedSize(200,20)
        self.selector_label.move(10,0)

        self.selector=QComboBox(self)
        self.selector.setFixedSize(200,20)
        self.selector.move(10,30)

        self.btn_refresh=QPushButton('Обновить список', self)
        self.btn_refresh.setFixedSize(100,30)
        self.btn_refresh.move(60,60)

        self.btn_ok=QPushButton('Добавить', self)
        self.btn_ok.setFixedSize(100,30)
        self.btn_ok.move(230,20)

        self.btn_cancel=QPushButton('Отмена', self)
        self.btn_cancel.setFixedSize(100,30)
        self.btn_cancel.move(230,60)
        self.btn_cancel.clicked.connect(self.close)

        # Fill in the list of possible contacts
        self.possible_contacts_update()
        # Assign an action to the refresh button
        self.btn_refresh.clicked.connect(self.update_possible_contacts)
    # Populate the list of possible contacts with the difference between all users
    def possible_contacts_update(self):
        self.selector.clear()
        # sets of all contacts and customer contacts
        contact_list=set(self.database.get_contacts())
        users_list=set(self.database.get_users())
        # Remove ourselves from the list of users so we can't add ourselves
        users_list.remove(self.transport.username)
        # Add a list of possible contacts
        self.selector.addItems(users_list-contact_list)

    # Update possible contacts. Updates the table of known users,
    # then the contents of the intended contacts
    def update_possible_contacts(self):
        try:
            self.transport.user_list_update()
        except OSError:
            pass
        else:
            LOGGER.debug('Обновление списка пользователей с сервера выполнено')
            self.possible_contacts_update()

