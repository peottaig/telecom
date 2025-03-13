'''
This Class will change's the data to be used in the program.
Data required for the program:

Prefix (11) 3215 - (0000-9999)
            3250 (TIM)
            3260 (VIVO)
            3270 (CLARO)
                   (Range 0000-9999)
       (11) operator-XXXX (Range 0000-9999)

MCDU: (0000-9999)
Number of origin (11) 32XX-XXXX
Destination number (11) 32XX-XXXX
Debtor: O/D
Date start: YYYY/MM/DD/HH/MM/SS
Duration: SSSSSS in seconds
Entry Route: 0001
             0002
             0003
                
Exit route: 0001
            0002
            0003
'''
import random as r

class MakeNumber:

    def cdFix(self):
        return 11

    def prefixRandom(self):
        prefix =[3250, 3260, 3270]
        return r.choice(prefix)
    
    def mcduRandom(self):
        return f"{r.randint(0, 9999):04d}"
    
    def numberRandom(self):
        cd = self.cdFix()
        prefix = self.prefixRandom()
        mcdu = self.mcduRandom()
        return f"{cd}{prefix}{mcdu}"
    