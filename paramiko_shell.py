# -*- coding: utf-8 -*-
import threading, paramiko, time
import sys
from subprocess import Popen, PIPE


class ssh:
    shell = None
    client = None
    transport = None

    def __init__(self, address, username, password):
        print("Connecting to server on ip", str(address) + ".")
        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        self.client.connect(address, username=username, password=password, look_for_keys=False)
        self.transport = paramiko.Transport((address, 22))
        self.transport.connect(username=username, password=password)


        thread = threading.Thread(target=self.process)
        thread.daemon = True
        thread.start()

    def closeConnection(self):
        if(self.client != None):
            self.client.close()
            self.transport.close()

    def openShell(self):
        self.shell = self.client.invoke_shell()

    def sendShell(self, command):
        if(self.shell):
            self.shell.send(command + "\n")
        else:
            print("Shell not opened.")

    def sendMcpRelease(self, command):
        # Check if connectivity exists
        if(self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                # Print output if available
                if stdout.channel.recv_ready():
                    # First 1024 bytes
                    alldata = stdout.channel.recv(1024)
                    while stdout.channel.recv_ready():
                        # Retrieve next 1024 bytes
                        alldata += stdout.channel.recv(1024)
                    # Print with encoded
                    print(str(alldata, "utf8"))
                    with open("mcpRelease.txt", "w+") as mcpRelease:
                        mcpRelease.write(str(alldata, "utf8"))
        else:
            print("Connection not opened.")

    def sendInstancePalette(self, command):
        # Check if connectivity exists
        if(self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                # Print output if available
                if stdout.channel.recv_ready():
                    # First 1024 bytes
                    alldata = stdout.channel.recv(1024)
                    while stdout.channel.recv_ready():
                        # Retrieve next 1024 bytes
                        alldata += stdout.channel.recv(1024)
                    # Print with encoded
                    print(str(alldata, "utf8"))
                    print("ACTIVATED......")
                    with open("Active_Instance.txt", "w+") as mcpRelease:
                        mcpRelease.write(str(alldata, "utf8"))
        else:
            print("Connection not opened.")

    def process(self):
        global connection
        encodingMethod = sys.stdout.encoding
        dump_subscriber_data = open('dump_subscriber_data.txt', 'w+')
        while True:
            # Print data when available
            if self.shell != None and self.shell.recv_ready():
                alldata = self.shell.recv(99999999)
                while self.shell.recv_ready():
                    alldata += self.shell.recv(99999999)
                strdata = alldata.decode('utf-8').encode(encodingMethod,'replace').decode(encodingMethod)
                strdata.replace('\r', '')

                print(strdata, end = "")
                # Write a file here
                dump_subscriber_data.write(str(strdata))
                if "ACTIVE" in strdata:
                    print("THIS IS AN ACTIVE SESM")
                if(strdata.endswith("$ ")):
                    print("\n$ ", end = "")
