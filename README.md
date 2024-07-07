# PuTTY SSH Client
This is a simple SSH client application built using PyQt5 and Paramiko for establishing SSH connections and executing commands on remote hosts.

## Features
Connection Setup: Enter hostname, port, username, and password to connect to a remote SSH server.
Command Execution: Execute commands on the remote server and display the output.
Error Handling: Handles connection errors and displays appropriate messages.
User Interface: Built with PyQt5 widgets for a user-friendly interface.

## Requirements
Python 3.x
PyQt5
Paramiko

### Installation
Clone the repository:
```bash
git clone https://github.com/Raulisr00t/PuTTYy.git
cd PuTTY
```
Install Dependencies
```bash
pip install -r requirements.txt
```
## Usage
Run the application:
```bash
python ssh_client.py
```
Enter SSH connection details:

Hostname: Enter the hostname or IP address of the SSH server.
Port: (Default is 22) Enter the SSH port number.
Username: Enter the SSH username.
Password: Enter the SSH password (hidden for security).
Execute Commands:

Enter a command in the "Command" field and click "Connect".
The output of the command will be displayed in the "Output" field.
Handling Errors:

If there are any connection or command execution errors, they will be displayed in the "Output" field.

## Contributing
Contributions are welcome! Please feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
