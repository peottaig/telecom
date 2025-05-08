'''This Class will create a file with the data to be used in the program.
The file will have the following format: 1132150001------1132501111---------------O2025031110175010-------00000003
Masc: POTA001_(YYYYMMDD+HHMMSS_NNNN).txt
'''

import random as r
from dados import MakeNumber
from dados import MakeData


class Files:

    def __init__(self, cont=0, mask='POTA001_', type='windowns'):
        self.md = MakeData()
        self.mn = MakeNumber()
        self.cont = cont
        self.mask = mask
        self.type = type
        self.dataDictSpec = {
            "numberDestiny": (16, "left"),
            "numberOrigin": (25, "left"),
            "debtor": (1, "left"),
            "dataStart": (14, "left"),
            "duration": (6, "left"),
            "entry_Route": (4, "left"),
            "exit_Route": (4, "left")
        }

    def createDataDict(self):
        # Gera os números de origem e destino
        number_origin = self.mn.numberRandom()
        number_destiny = self.mn.numberRandom()

        prefix = number_origin[2:6]  # Obtém os 4 dígitos do prefixo

        # Define as rotas de saída possíveis
        possible_routes = ['0001', '0002', '0003']

        # Escolhe uma rota aleatória
        exit_route = r.choice(possible_routes)

        # Cria o dicionário de dados
        dataDict = {
            "numberDestiny": number_destiny,
            "numberOrigin": number_origin,
            "debtor": self.md.debtorRandom(),
            "dataStart": self.md.dataStart(),
            "duration": self.md.durationRandom(),
            "entry_Route": self.md.entry_Route(),
            "exit_Route": exit_route  # Usa a rota de saída aleatória
        }

        return dataDict

    def dataFormat(self):
        """
        Define o alinhamento ('left' ou 'right'). Se None, usa o padrão da classe.
        """
        dict_ = self.createDataDict()
        data = ''
        for key, value in dict_.items():
            # Verifica se a chave existe e está bem formatada
            if key in self.dataDictSpec and len(self.dataDictSpec[key]) > 0:
                if self.dataDictSpec[key][1] == 'left':
                    data += f"{value:<{self.dataDictSpec[key][0]}}"
                elif self.dataDictSpec[key][1] == 'right':
                    data += f"{value:>{self.dataDictSpec[key][0]}}"
                else:
                    raise ValueError(
                        "O parâmetro 'alignment' deve ser 'left' ou 'right'")
            else:
                raise KeyError(
                    f"Chave '{key}' não encontrada ou mal formatada em dataDictSpec")
        return data.replace(' ', '-')

    def returnDataStartFromDict(self):
        dataStart = self.createDataDict()['dataStart']
        return dataStart

    '''This code will make records by quantity of records informed in the parameter cont'''

    def createFile(self):
        file = f"/home/cgi/luiggi/input/pota/{self.mask}{self.returnDataStartFromDict()}.txt"
        with open(file, 'w') as f:
            for i in range(self.cont):
                f.write(f"{self.dataFormat()}\n")
        print(f"File {file} created successfully!")

        if self.type == 'unix':
            with open(file, 'r') as f:
                data = f.read()
            # Verifica se data é uma string antes de substituir
            if isinstance(data, str):
                data = data.replace('\r\n', '\n')
            else:
                raise TypeError("O conteúdo do arquivo não é uma string")
            with open(file, 'w') as f:
                f.write(data)
            print("File generated in Unix format")
