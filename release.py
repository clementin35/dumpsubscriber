import re

class releaser:
    def __init__(self):
        print("MCP Release identifier Has Been Activated...")

    def identifier(self):
        with open("mcpRelease.txt", "r+") as releaseIdentifier:
            mcpData = releaseIdentifier.read()
            mcpLoad = re.findall(r'Release Level:   (\d\d\.\d)\.\d', str(mcpData))
            print(str(mcpLoad[0]))
            return(str(mcpLoad[0]))
