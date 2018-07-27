from paramiko import client

class ssh:
    client = None
    """docstring for ssh."""
    def __init__(self, address, username, password):
        # We are connecting to server
        print("Connecting to server...")
        # create new ssh client
        self.client = client.SSHClient()
        # Required line
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())

        # make the connection
        self.client.connect(address, username = username,
            password = password, look_for_keys=False)
    def sendCommand(self, command):
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

        else:
            print("Connection not opened.")

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
                    with open("instance.txt", "w+") as mcpRelease:
                        mcpRelease.write(str(alldata, "utf8"))
        else:
            print("Connection not opened.")

    def sendCredit(self):
        shell = self.client.invoke_shell()

        channel_data = str()
        telnetName = str()
        passwordName = str()

        while True:
            if shell.recv_ready():
                channel_bytes = shell.recv(9999)
                channel_data = channel_bytes.decode("utf-8")
                os.system("cls")
                print("########### DEVICE OUtPUT ###########")
            else:
                continue
            if channel_data.endswith("Username:"):
                telnetName = raw_input('Enter username:')
                shell.send(telnetName)
            elif channel_data.endswith("Password:"):
                passwordName = raw_input('Enter pw:')
                shell.send(passwordName)


        while True:
            command = input('$ ')
            if command.startswith(" "):
                command = command[1:]
            connection.sendShell(command)
