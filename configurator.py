from components import dataBase

class configuratorClass(dataBase):
    
    def __init__(self):

        self.rpcUrlsData = {}
        self.rpcUrls = "RPC_URLS.dat"
        dataBase.__init__(self, "config", "")

    def insertRPCURL(self, url, name):

        try:
            
            self.rpcUrlsData = self.objDB[self.rpcUrls]
            
        except:

            pass

        finally:

            try:

                self.rpcUrlsData[url] = name
                self._insertKeyValue(self.rpcUrls, self.rpcUrlsData)
                self.rpcUrlsData = {}

            except:

                return False

    def deleteRPCURL(self, url):

        try:

            self.rpcUrlsData = self.objDB[self.rpcUrls]
            del self.rpcUrlsData[url]
            self.rpcUrlsData = {}

        except:

            return False

    def getRPCURLFromNetworkName(self, name):

        rpcDict= []
        myitems = self.objDB[self.rpcUrls]
        
        for key, val in myitems.items():

            if name in val:

                rpcDict.append(key)

        return rpcDict


    def getRPCURLS(self):

        try:

            return self.objDB[self.rpcUrls]

        except:

            return False

    def deleteAllRPCURLS(self):

        self.objDB.clear()
        






