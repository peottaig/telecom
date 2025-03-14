from dados import MakeNumber
from dados import MakeData

md = MakeData()
mn = MakeNumber()

class Files:
    
    def __init__(self):
        super().__init__()
        self.md = MakeData()
        self.mn = MakeNumber()
        self.numberDestiny = mn.numberRandom()
        self.numberOrigin = mn.numberRandom()
        self.debtor = md.debtorRandom()
        self.dataStart = md.dataStart()
        self.duration = md.durationRandom()
        self.entry_Route = md.entry_Route()
        self.exit_Route = md.exit_Route()
        self.dataDict = {
            self.numberDestiny: 16,
            self.numberOrigin: 25,
            self.debtor: 1,
            self.dataStart: 14,
            self.duration: 6,
            self.entry_Route: 4,
            self.exit_Route: 4
        }

    
    def dataFormat(self):
        data = ''
        for key, value in self.dataDict.items():
            data += f"{key:<{value}}"     
        return data.replace(' ', '-')

