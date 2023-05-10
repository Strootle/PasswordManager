from cryptography.fernet import Fernet

class PasswordManager:

    #Initialise the class
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    #Create new keys for files
    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    #Load keys to open different Files
    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    #Create new file to store passwords
    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    #Load file containing hashed passwords
    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    #Add new password to selected file
    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, "a+") as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    #Return decoded password on selected file and site
    def get_password(self, site):
        return self.password_dict[site]

pm = PasswordManager()


