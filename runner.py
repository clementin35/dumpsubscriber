import main, release

connection = main.ssh("47.168.155.140", "ntappadm", "RAPtor1234")
connection.sendMcpRelease("mcpRelease.pl")

_release = release.releaser()
load = _release.identifier()

connection.sendCommand("cd /var/mcp/run/MCP_" + load)
print("cd /var/mcp/run/MCP_" + load)
connection.sendCommand("cd SESM1_1 || cd SESM1_0")
print("cd SESM1_1 || cd SESM1_0")
connection.sendInstancePalette("./bin/getInstanceState.pl")
print("./bin/getInstanceState.pl")
