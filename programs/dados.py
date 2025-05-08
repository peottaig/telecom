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
import calendar as c


class MakeNumber:

    def cdFix(self):
        return 11

    def prefixRandom(self):
        # Gera um prefixo aleatório entre 3200 e 3299
        prefix = f"{r.randint(3200, 3299)}"
        return prefix

    def mcduRandom(self):
        return f"{r.randint(0, 9999):04d}"

    def numberRandom(self):
        cd = self.cdFix()
        prefix = self.prefixRandom()
        mcdu = self.mcduRandom()
        return str(f"{cd}{prefix}{mcdu}")


class MakeData:

    def debtorRandom(self):
        debtor = ['O', 'D']
        return r.choice(debtor)

    def dataStart(self):
        YYYY = 2025
        MM = r.randint(1, 12)

        # Get the last day of the month
        _, lastdayforMonth = c.monthrange(YYYY, MM)
        DD = r.randint(1, lastdayforMonth)

        HH = r.randint(0, 23)
        MI = r.randint(0, 59)
        SS = r.randint(0, 59)
        dataStart = f"{YYYY}{MM:02d}{DD:02d}{HH:02d}{MI:02d}{SS:02d}"
        dataStart = str(dataStart)
        return dataStart

    def durationRandom(self):
        return str(f"{r.randint(0, 999999)}")

    def entry_Route(self):
        return '0000'
