import hashlib

class HashCalc():
    def __init__(self, path) -> None:
        self.path = path
        self.md5 = "-"
        self.sha256 = "-"
        self.__calculateFileHash()
            
    def __calculateFileHash(self):

        sha256 = hashlib.sha256()
        md5 = hashlib.md5()

        with open(self.path, "rb") as f:
            while True:
                data = f.read(65536) 
                if not data:
                    break
                sha256.update(data)
                md5.update(data)

        self.sha256 = sha256.hexdigest()
        self.md5 = md5.hexdigest()