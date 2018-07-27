import paramiko_shell as pr
import time
import release

_release = release.releaser()
load = _release.identifier()

sshUsername = "ntappadm"
sshPassword = "RAPtor1234"
sshServer = "47.168.155.138"


connection = pr.ssh(sshServer, sshUsername, sshPassword)
connection.openShell()

connection.sendMcpRelease("mcpRelease.pl")

_release = release.releaser()
load = _release.identifier()

connection.sendShell("cd /var/mcp/run/MCP_" + load)
time.sleep(5)
connection.sendShell("cd SESM1_1 || cd SESM1_0")
time.sleep(5)
data = connection.sendShell("./bin/getInstanceState.pl")

with open("dummytext.txt", "w+") as dummy:
    dummy.write(str(data))

# Save >>dump subscriber command to a file
# Then we need to "Regular Expression" to evaluate data...

command = input('$ ')
