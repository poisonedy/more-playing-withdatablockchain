from pickleshare import *
from web3 import Web3
import json
import logging
import concurrent.futures

from components import *
from configurator import configuratorClass

AbiDict ={'default':'[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"minTokensBeforeSwap","type":"uint256"}],"name":"MinTokensBeforeSwapUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tokensSwapped","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"ethReceived","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tokensIntoLiqudity","type":"uint256"}],"name":"SwapAndLiquify","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"enabled","type":"bool"}],"name":"SwapAndLiquifyEnabledUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"_liquidityFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_maxTxAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_taxFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"}],"name":"deliver","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"excludeFromFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"excludeFromReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"geUnlockTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"includeInFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"includeInReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isExcludedFromFee","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isExcludedFromReward","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"time","type":"uint256"}],"name":"lock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"},{"internalType":"bool","name":"deductTransferFee","type":"bool"}],"name":"reflectionFromToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"liquidityFee","type":"uint256"}],"name":"setLiquidityFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"maxTxPercent","type":"uint256"}],"name":"setMaxTxPercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_enabled","type":"bool"}],"name":"setSwapAndLiquifyEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"taxFee","type":"uint256"}],"name":"setTaxFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"swapAndLiquifyEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rAmount","type":"uint256"}],"name":"tokenFromReflection","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalFees","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"uniswapV2Pair","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"uniswapV2Router","outputs":[{"internalType":"contract IUniswapV2Router02","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"unlock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'
}

configurator = configuratorClass()

class blockchainConnector:

    def __init__(self, urlWeb3):

        self.urlWeb3 = urlWeb3
        self.web3 = Web3(Web3.HTTPProvider(urlWeb3))
        from web3.middleware import geth_poa_middleware
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    def isValidConnection (self):

        return self.web3.isConnected()

class blockchain(blockchainConnector):

    def __init__(self, blockchainName, urlWeb3):

        self.blockchainName = blockchainName
        self.urlWeb3 = urlWeb3

        logging.basicConfig(level=logging.INFO,format='(%(threadName)-10s) %(message)s',)
        blockchainConnector.__init__(self, self.urlWeb3)
        
        self.blockchainDb = dataBase(self.blockchainName, "blockchain")

    def _getBlockData (self, blockNum):

        self.blockNum = blockNum
        self.data = self.web3.eth.get_block(self.blockNum)
        return self.data

    def _getTransactionData (self, transactionID):

        self.transactionID = transactionID
        return self.web3.eth.get_transaction(self.transactionID)

    def _get_Transactions_FromBlock (self, blockdata ):

        self.data = blockdata
        self.transactions = self.data['transactions']
        return self.transactions

    def _getTokenName_FromAddress(self, address):

        self.address = address
        self.tokenAddress = str(self.web3.toChecksumAddress(self.address))
        self.tokenRouter = self.web3.eth.contract(self.tokenAddress, abi=json.loads(AbiDict['default']))
        return self.tokenRouter.functions.name().call()
    
    def _getTokenSymbol_FromContractAddress(self, address):

        self.address = address
        self.tokenAddress = str(self.web3.toChecksumAddress(self.address))
        self.tokenRouter = self.web3.eth.contract(self.tokenAddress, abi=json.loads(AbiDict['default']))
        return self.tokenRouter.functions.symbol().call()

    def _getTokenDecimals_FromContractAddress(self, address):

        self.address = address
        self.tokenAddress = str(self.web3.toChecksumAddress(self.address))
        self.tokenRouter = self.web3.eth.contract(self.tokenAddress, abi=json.loads(AbiDict['default']))
        return self.tokenRouter.functions.decimals().call()
    
    def _getTokenTotalSupply_FromContractAddress(self, address):

        self.address = address
        self.tokenAddress = str(self.web3.toChecksumAddress(self.address))
        self.tokenRouter = self.web3.eth.contract(self.tokenAddress, abi=json.loads(AbiDict['default']))
        return self.tokenRouter.functions.totalsupply().call()
    ##dynamic value
    def _getTokenTaxFee_FromContractAddress(self, address):

        self.address = address
        self.tokenAddress = str(self.web3.toChecksumAddress(self.address))
        self.tokenRouter = self.web3.eth.contract(self.tokenAddress, abi=json.loads(AbiDict['default']))
        return self.tokenRouter.functions.taxFee().call()

    def _insertContract_ToDb (self, contractAddress, tokenName):

        self.contractAddress = contractAddress
        self.tokenName = tokenName
        self.contractDb = dataBase(self.blockchainName, "contracts")
        self.contractDb._insertKeyValue(self.contractAddress, self.tokenName)
        del self.contractDb

    def _saveLastParsedBlock_ToDb (self, lastParsedBlock):

        self.lastParsedBlock = lastParsedBlock
        self.lastParsedBlockDb = dataBase(self.blockchainName, "blockchain")
        self.lastParsedBlockDb._insertKeyValue("lastParsedBlock.dat", self.lastParsedBlock)
        del self.lastParsedBlockDb

    def _getLastParsedBlock_FromDb (self):

        self.lastParsedBlockDb = dataBase(self.blockchainName, "blockchain")
        self.lastParsedBlock = self.lastParsedBlockDb._getValueByKey("lastParsedBlock.dat")
        del self.lastParsedBlockDb
        return self.lastParsedBlock
    
    def _getLastBlockFromBlockchain (self):

         return int(self.web3.eth.block_number)

    def processBlock (self, blocknum):
        
        logging.info (f"processing block {blocknum} from {self._getLastBlockFromBlockchain()}")
        actualBlockData = self._getBlockData(blocknum)
        transactionsFromActualBlockData = self._get_Transactions_FromBlock(actualBlockData)
        
        if transactionsFromActualBlockData != []:
            
            logging.debug (f"found transactions in block {blocknum}")
            
            for transaction in transactionsFromActualBlockData:

                logging.debug (transaction.hex())
                transactionData = self._getTransactionData(transaction)
                fromAddress = transactionData['from']
                toAddress = transactionData['to']
                logging.debug (fromAddress)
                logging.debug (toAddress)

                try:

                    isFromATokenAddress = self._getTokenName_FromAddress(fromAddress)
                    self._insertContract_ToDb(fromAddress,isFromATokenAddress)
                    logging.info (f"Found Token {isFromATokenAddress} in {fromAddress} address.")

                except:

                    logging.debug(f"From token address {fromAddress} not found contract")

                try:

                    isToATokenAddress = self._getTokenName_FromAddress(toAddress)
                    self._insertContract_ToDb(toAddress,isToATokenAddress)
                    logging.info (f"Found Token {isToATokenAddress} in {toAddress} address.")

                except:

                    logging.debug(f"From token address {fromAddress} not found contract")
        else:

            logging.info ("no transactions")

    def _parseRangeBlocks (self, range_blocks):
  
       for block in range_blocks:

           self.processBlock(block)

    def parseBlockchain (self):

        self._saveLastParsedBlock_ToDb(0)
        self.lastParsedBlock = self._getLastParsedBlock_FromDb()
        self.chunk = 400
        self.max_workers = 2

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:

            for blocktram in range(self.lastParsedBlock,self._getLastBlockFromBlockchain()):
                
                future_to_cc = {executor.submit(self._parseRangeBlocks, range(self.lastParsedBlock,self.lastParsedBlock + self.chunk))}
                self._saveLastParsedBlock_ToDb(self.lastParsedBlock+self.chunk)

        for future in concurrent.futures.as_completed(future_to_cc):
     
            try:

                blocktram = future_to_cc[future]

            except:

                logging.info ("Job Finished")

            try:

                data = future.result()
                

            except Exception as exc:

                logging.info('%r generated an exception: %s' % (blocktram, exc))

            else:

                logging.info('%r page is %d bytes' % (blocktram, len(data)))

#bc = blockchain("Polygon", "https://rpc-mainnet.matic.network/")#
bc = blockchain("Polygon", "http://10.42.0.56:8545/")
print (bc._getLastBlockFromBlockchain())

#bc = blockchain("Polygon", "https://polygon-mainnet.infura.io/v3/e209d7d77e934b32a98ab3fb700513e3")
bc.parseBlockchain()
#bc._parseRangeBlocks(8000070,8000075)
'''
data=bc._getTransactionData("0x7f4b056f8d189669bad621bead10e4aedffbe430b890cb68e5b5ba306a61cc4f")
addressFrom = data['from']
print (addressFrom)

addressTo = data ['to']
print (addressTo)
#bc._getTokenName_FromAddress(addressFrom)
name = bc._getTokenName_FromAddress(addressTo)
print (name)
bc._insertContract_ToDb(addressTo, name)
'''



    