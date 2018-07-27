import paramiko
import os
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('47.168.155.140', port=22, username='ntappadm',
    password='RAPtor1234')

channel = ssh.invoke_shell()

channel_data = str()
telnetName = str()
passwordName = str()


while True:
    if channel.recv_ready():
        channel_bytes = channel.recv(9999)
        channel_data = channel_bytes.decode("utf-8")
        os.system("cls")
        print("########### DEVICE OUPUT ###########")
        ssh.exec_command("telnet localhost 21000")
    else:
        continue
    if channel_data.endswith("Username:"):
        telnetName = raw_input('Enter username:')
        channel.send(telnetName)
    elif channel_data.endswith("Password:"):
        passwordName = raw_input('Enter pw:')
        channel.send(passwordName)
