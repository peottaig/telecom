
from dados import MakeNumber
from dados import MakeData

class Files:
    
    def __init__(self):
        self.md = MakeData()
        self.mn = MakeNumber()
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

