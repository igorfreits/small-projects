from typing import Dict, List
from abc import ABC, abstractmethod


class Comandos(ABC):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def file(self):
        pass


class ComandosACC(Comandos):
    def insert(self):
        self.lista_contratos: List[int] = []
        self.lista_handleACC: List[int] = []
        self.dados: Dict[int, int] = {}
        while True:
            self.contratos = int(input('Digite o número de contratos: '))
            self.lista_contratos.append(self.contratos)

            if self.contratos == 0:
                self.lista_contratos.pop()
                break
        while True:
            self.handleACC = int(input('Digite o handleACC: '))
            self.lista_handleACC.append(self.handleACC)

            if self.handleACC == 0:
                self.lista_handleACC.pop()
                break

        for i in range(len(self.lista_handleACC)):
            self.dados[self.lista_contratos[i]] = self.lista_handleACC[i]

        self.file()

    def file(self):
        with open('HOTEL_ACC.txt', 'w') as file:
            for i in range(len(self.dados)):
                file.write(
                    f'UPDATE VM_PNRACCOUNTINGS SET FORNECEDOR='
                    f'{self.lista_contratos[i]} '
                    f'WHERE HANDLE IN ('
                    f'{self.lista_handleACC[i]})\n')
        print('\033[34mArquivo HOTEL_ACC foi gerado com sucesso!\033[m\n')


class ComandosPNR(Comandos):
    def insert(self):
        self.lista_pnr: List[int] = []
        while True:
            self.pnr = int(input('Digite o número dos PNRs: '))
            self.lista_pnr.append(self.pnr)

            if self.pnr == 0:
                self.lista_pnr.pop()
                break
        self.file()

    def file(self):
        with open('HOTEL_PNR.txt', 'w') as file:

            file.write(
                "UPDATE VM_PNRS SET SITUACAO=1, CONCLUIDO='S', \n"
                "EXPORTADO='N', AGUARDANDOEMISSAO='N' WHERE HANDLE IN( \n")

            for i in range(len(self.lista_pnr)):
                if i == len(self.lista_pnr) - 1:
                    file.write(f'{self.lista_pnr[i]})')
                else:
                    file.write(f'{self.lista_pnr[i]},')
        print('\033[34mArquivo HOTEL_PNR foi gerado com sucesso!\033[m\n')
