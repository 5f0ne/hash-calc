import os
import time

from datetime import datetime

class Controller():
    def __init__(self) -> None:
        self.startTime = time.time()

    def printHeader(self, path, md5, sha256):
        print("##############################################################################################")
        print("")
        print("Hash Calc by 5f0")
        print("Calculates MD5 and SHA256 hashes for a given file")
        print("")
        print("Current working directory: " + os.getcwd())
        print("        Investigated file: " + path)
        print("")
        print("                 MD5 Hash: " + md5)
        print("              SHA256 Hash: " + sha256)
        print("")
        print("                 Datetime: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("")
        print("##############################################################################################")
        print("")

    def printExecutionTime(self):
        end = time.time()
        print("")
        print("Execution Time: " + str(end-self.startTime)[0:8] + " sec")
        print("")