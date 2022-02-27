class credentials:
    def __init__(self, username, password, hostname, port):
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port


My_Credentials = credentials('postgres', 'xxx***xxx', 'localhost', '5432')