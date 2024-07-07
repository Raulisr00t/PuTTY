import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
import paramiko

class SSHClient(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PuTTY')

        self.ip_label = QLabel('Hostname:')
        self.ip_input = QLineEdit()

        self.port_label = QLabel('Port:')
        self.port_input = QLineEdit()
        self.port_input.setText('22') 

        self.user_label = QLabel('Username:')
        self.user_input = QLineEdit()

        self.pass_label = QLabel('Password:')
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)

        self.cmd_label = QLabel('Command:')
        self.cmd_input = QLineEdit()

        self.output_label = QLabel('Output:')
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)

        self.connect_btn = QPushButton('Connect')
        self.connect_btn.clicked.connect(self.connectSSH)

        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.ip_label)
        hbox1.addWidget(self.ip_input)
        hbox1.addWidget(self.port_label)
        hbox1.addWidget(self.port_input)
        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.user_label)
        hbox2.addWidget(self.user_input)
        hbox2.addWidget(self.pass_label)
        hbox2.addWidget(self.pass_input)
        vbox.addLayout(hbox2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.cmd_label)
        hbox3.addWidget(self.cmd_input)
        vbox.addLayout(hbox3)

        vbox.addWidget(self.output_label)
        vbox.addWidget(self.output_display)
        vbox.addWidget(self.connect_btn)

        self.setLayout(vbox)
        self.show()

    def connectSSH(self):
        ip = self.ip_input.text()
        port = int(self.port_input.text())
        username = self.user_input.text()
        password = self.pass_input.text()

        if not port or not username or not password or not ip:
            ok = QMessageBox.information(self,"Options Error","Please check Credentials again!",QMessageBox.Ok)
            if ok:
                return ""
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, port, username, password)
            command = self.cmd_input.text()

            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()

            if output:
                self.output_display.append(output)
            if error:
                self.output_display.append(error)

            ssh.close()

        except Exception as e:
            self.output_display.append(f"Error: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SSHClient()
    sys.exit(app.exec_())
