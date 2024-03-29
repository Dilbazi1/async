from PyQt5.QtWidgets import QMainWindow, qApp, QMessageBox, QApplication, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PyQt5.QtCore import pyqtSlot, QEvent, Qt
import sys
import json
import logging

sys.path.append('../')
from client.main_window_conv import Ui_MainClientWindow
from client.add_contact import AddContactDialog
from client.del_contact import DelContactDialog
from client.client_database  import ClientDatabase
from client.transport import ClientTransport
from client.start_dialog import UserNameDialog
from common.errors import ServerError

logger=logging.getLogger('client')
# class main window
class ClientMainWindow(QMainWindow):
    def __init__(self,database,transport):
        super().__init__()
        # main variables
        self.database=database
        self.transport=transport
        # Load the window configuration from the designer
        self.ui=Ui_MainClientWindow()
        self.ui.setupUi(self)
        # "Exit" button
        self.ui.menu_exit.triggered.connect(qApp.exit)
        # Send message button
        self.ui.btn_send.clicked.connect(self.send_message)
        # add contact
        self.ui.btn_add_contact.clicked.connect(self.add_contact_window)
        self.ui.menu_add_contact.triggered.connect(self.add_contact_window)

        # remove contact
        self.ui.btn_remove_contact.clicked.connect(self.delete_contact_window)
        self.ui.menu_del_contact.triggered.connect(self.delete_contact_window)
        # Additional required attributes
        self.contacts_model = None
        self.history_model = None
        self.messages = QMessageBox()
        self.current_chat = None
        self.ui.list_messages.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.list_messages.setWordWrap(True)

        #Doubleclick on the contact list is sent to the handler
        self.ui.list_contacts.doubleClicked.connect(self.select_active_user)
        self.clients_list_update()
        self.set_disabled_input()
        self.show()
    # Deactivate input fields
    def set_disabled_input(self):
        #  inscription - recipient.
        self.ui.label_new_message.setText('Для выбора получателя дважды кликните на нем в окне контактов.')
        self.ui.text_message.clear()
        if self.history_model:
            self.history_model.clear()

        # The input field and send buttons are inactive until a recipient is selected.
        self.ui.btn_clear.setDisabled(True)
        self.ui.btn_send.setDisabled(True)
        self.ui.text_message.setDisabled(True)

        # Filling in the message history.
    def history_list_update(self):
            # Get history sorted by date
            list = sorted(self.database.get_history(self.current_chat), key=lambda item: item[3])
            # If the model is not created, create it.
            if not self.history_model:
                self.history_model = QStandardItemModel()
                self.ui.list_messages.setModel(self.history_model)
            # Clean up old posts
            self.history_model.clear()
            # We take no more than 20 recent entries.
            length = len(list)
            start_index = 0
            if length > 20:
                start_index = length - 20
            # Filling the model with records, it is also worth separating incoming and outgoing ones with alignment and different backgrounds.
            # Records are in reverse order, so we select them from the end and no more than 20
            for i in range(start_index, length):
                item = list[i]
                if item[1] == 'in':
                    mess = QStandardItem(f'Входящее от {item[3].replace(microsecond=0)}:\n {item[2]}')
                    mess.setEditable(False)
                    mess.setBackground(QBrush(QColor(255, 213, 213)))
                    mess.setTextAlignment(Qt.AlignLeft)
                    self.history_model.appendRow(mess)
                else:
                    mess = QStandardItem(f'Исходящее от {item[3].replace(microsecond=0)}:\n {item[2]}')
                    mess.setEditable(False)
                    mess.setTextAlignment(Qt.AlignRight)
                    mess.setBackground(QBrush(QColor(204, 255, 204)))
                    self.history_model.appendRow(mess)
            self.ui.list_messages.scrollToBottom()

        # Contact double click handler function
    def select_active_user(self):
            # The user-selected (doubleclick) is on the selected item in the QListView
            self.current_chat = self.ui.list_contacts.currentIndex().data()
            # calling the main function
            self.set_active_user()

        # Function that sets the active interlocutor
    def set_active_user(self):
            # Put an inscription and activate the buttons
            self.ui.label_new_message.setText(f'Введите сообщенние для {self.current_chat}:')
            self.ui.btn_clear.setDisabled(False)
            self.ui.btn_send.setDisabled(False)
            self.ui.text_message.setDisabled(False)

            # Fill in the message history window for the required user.
            self.history_list_update()

        # Function to update the contact list
    def clients_list_update(self):
            contacts_list = self.database.get_contacts()
            self.contacts_model = QStandardItemModel()
            for i in sorted(contacts_list):
                item = QStandardItem(i)
                item.setEditable(False)
                self.contacts_model.appendRow(item)
            self.ui.list_contacts.setModel(self.contacts_model)

        # Add contact function
    def add_contact_window(self):
            global select_dialog
            select_dialog = AddContactDialog(self.transport, self.database)
            select_dialog.btn_ok.clicked.connect(lambda: self.add_contact_action(select_dialog))
            select_dialog.show()

        # Function - add handler, tells the server to update the table and contact list
    def add_contact_action(self, item):
            new_contact = item.selector.currentText()
            self.add_contact(new_contact)
            item.close()

    # A function that adds a contact to the database
    def add_contact(self, new_contact):
        try:
            self.transport.add_contact(new_contact)
        except ServerError as err:
            self.messages.critical(self, 'Ошибка сервера', err.text)
        except OSError as err:
            if err.errno:
                self.messages.critical(self, 'Ошибка', 'Потеряно соединение с сервером!')
                self.close()
            self.messages.critical(self, 'Ошибка', 'Таймаут соединения!')
        else:
            self.database.add_contact(new_contact)
            new_contact = QStandardItem(new_contact)
            new_contact.setEditable(False)
            self.contacts_model.appendRow(new_contact)
            logger.info(f'Успешно добавлен контакт {new_contact}')
            self.messages.information(self, 'Успех', 'Контакт успешно добавлен.')
    # Delete contact function

    def delete_contact_window(self):
        global remove_dialog
        remove_dialog = DelContactDialog(self.database)
        remove_dialog.btn_ok.clicked.connect(lambda: self.delete_contact(remove_dialog))
        remove_dialog.show()

        # Contact deletion handler function, reports to the server, updates the contact table
    def delete_contact(self, item):
            selected = item.selector.currentText()
            try:
                self.transport.remove_contact(selected)
            except ServerError as err:
                self.messages.critical(self, 'Ошибка сервера', err.text)
            except OSError as err:
                if err.errno:
                    self.messages.critical(self, 'Ошибка', 'Потеряно соединение с сервером!')
                    self.close()
                self.messages.critical(self, 'Ошибка', 'Таймаут соединения!')
            else:
                self.database.del_contact(selected)
                self.clients_list_update()
                logger.info(f'Успешно удалён контакт {selected}')
                self.messages.information(self, 'Успех', 'Контакт успешно удалён.')
                item.close()
                # If the active user is deleted, then we deactivate the input fields.
                if selected == self.current_chat:
                    self.current_chat = None
                    self.set_disabled_input()

    # Function to send a message to the user.

    def send_message(self):
        # Текст в поле, проверяем что поле не пустое затем забирается сообщение и поле очищается
        message_text = self.ui.text_message.toPlainText()
        self.ui.text_message.clear()
        if not message_text:
            return
        try:
            self.transport.send_message(self.current_chat, message_text)
            pass
        except ServerError as err:
            self.messages.critical(self, 'Ошибка', err.text)
        except OSError as err:
            if err.errno:
                self.messages.critical(self, 'Ошибка', 'Потеряно соединение с сервером!')
                self.close()
            self.messages.critical(self, 'Ошибка', 'Таймаут соединения!')
        except (ConnectionResetError, ConnectionAbortedError):
            self.messages.critical(self, 'Ошибка', 'Потеряно соединение с сервером!')
            self.close()
        else:
            self.database.save_message(self.current_chat, 'out', message_text)
            logger.debug(f'Отправлено сообщение для {self.current_chat}: {message_text}')
            self.history_list_update()
    # Slot for receiving new messages

    @pyqtSlot(str)
    def message(self, sender):
        if sender == self.current_chat:
            self.history_list_update()
        else:
            # Check if there is such a user in our contacts:
            if self.database.check_contact(sender):
                # If there is, ask and wish to open a chat with him and open if desired
                if self.messages.question(self, 'Новое сообщение', \
                                          f'Получено новое сообщение от {sender}, открыть чат с ним?', QMessageBox.Yes,
                                          QMessageBox.No) == QMessageBox.Yes:
                    self.current_chat = sender
                    self.set_active_user()
            else:
                print('NO')
                #If not, we ask if we want to add the user to contacts.
                if self.messages.question(self, 'Новое сообщение', \
                                          f'Получено новое сообщение от {sender}.\n Данного пользователя нет в вашем контакт-листе.\n Добавить в контакты и открыть чат с ним?',
                                          QMessageBox.Yes,
                                          QMessageBox.No) == QMessageBox.Yes:
                    self.add_contact(sender)
                    self.current_chat = sender
                    self.set_active_user()

        # Loss of connection slot
        # Gives an error message and terminates the application
    @pyqtSlot()
    def connection_lost(self):
            self.messages.warning(self, 'Сбой соединения', 'Потеряно соединение с сервером. ')
            self.close()

    def make_connection(self, trans_obj):
        trans_obj.new_message.connect(self.message)
        trans_obj.connection_lost.connect(self.connection_lost)
