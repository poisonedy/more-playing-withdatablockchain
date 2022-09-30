from pickleshare import *
import os

class dataBase:

    def __init__(self, ownDirectory, pathTofileDB):

        self.rootDataDirectory = os.getcwd() + "/dataDB"
        self.ownDirectory = ownDirectory
        self.pathToFileDB = pathTofileDB
        if not os.path.isdir(self.rootDataDirectory):
            os.mkdir(self.rootDataDirectory)
        if not os.path.isdir(self.rootDataDirectory + "/" + self.ownDirectory):
            os.mkdir(self.rootDataDirectory + "/" + self.ownDirectory)


        self.completePath = self.rootDataDirectory + "/" +  self.ownDirectory + "/" + self.pathToFileDB

        try:

            self.objDB = PickleShareDB(self.completePath)

        except:

            return False

    def _emptyDB(self):
        
        try:

            self.objDB.clear()

        except:

            return False

    def _insertKeyValue(self, key, value):

        self.key = key
        self. value = value

        try:
            self.objDB[self.key] = self.value

        except:

            return False
    
    def _getValueByKey(self, key):

        self.key = key

        try:
            return self.objDB[self.key]

        except:

            return False

    def _DBItems (self):

        return self.objDB.items()