
'''This Class will create a file with the data to be used in the program.
The file will have the following format: 1132150001------1132501111---------------O2025031110175010-------00000003
Masc: POTA001_(YYYYMMDD+HHMMSS_NNNN).txt
'''


from dados import MakeNumber
from dados import MakeData

class Files:
    
    def __init__(self, cont):
        self.md = MakeData()
        self.mn = MakeNumber()
        self.cont = cont
        self.dataDictSpec = {
            "numberDestiny": 16,
            "numberOrigin": 25,
            "debtor": 1,
            "dataStart": 14,
            "duration": 6,
            "entry_Route": 4,
            "exit_Route": 4
        }

    def createDataDict(self):
        dataDict = {
            "numberDestiny": self.mn.numberRandom(),
            "numberOrigin": self.mn.numberRandom(),
            "debtor": self.md.debtorRandom(),
            "dataStart": self.md.dataStart(),
            "duration": self.md.durationRandom(),
            "entry_Route": self.md.entry_Route(),
            "exit_Route": self.md.exit_Route()
        }
        return dataDict

    def dataFormat(self):
        dict_ = self.createDataDict()
        data = ''
        for key, value in dict_.items():
            data += f"{value:<{self.dataDictSpec[key]}}"     
        return data.replace(' ', '-')

    def returnDataStartFromDict(self):
        dataStart = self.createDataDict()['dataStart']
        return dataStart


    '''This code will make records by quantity of records informed in the parameter cont'''
    def createFile(self,cont):
        file = rf"C:\POTA\POTA001_{self.returnDataStartFromDict()}.txt"
        with open(file, 'w') as f:
            for i in range(cont):
                f.write(f"{self.dataFormat()}\n")
        print(f"File {file} created successfully!")
        
