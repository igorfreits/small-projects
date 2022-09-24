from typing import List
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
        for id in range(1, 150):
            self.contratos = input(f'{id} - Digite o número de contratos: ')
            self.lista_contratos.append(self.contratos)

            if self.contratos == 'n':
                self.lista_contratos.pop()
                break

        for id in range(1, 150):
            self.handleACC = input(f'{id} - Digite o handleACC: ')
            self.lista_handleACC.append(self.handleACC)

            if self.handleACC == 'n':
                self.lista_handleACC.pop()
                break
        self.file()

    def file(self):
        with open('HOTEL_ACC.txt', 'w') as file:
            for i in range(len(self.lista_contratos)):
                file.write(
                    f'UPDATE VM_PNRACCOUNTINGS SET FORNECEDOR='
                    f'{self.lista_contratos[i]} '
                    f'WHERE HANDLE IN ('
                    f'{self.lista_contratos[i]})\n')
        print('\033[34mArquivo HOTEL_ACC foi gerado com sucesso!\033[m\n')


class ComandosPNR(Comandos):
    def insert(self):
        self.lista_pnr: List[int] = []
        for id in range(1, 150):
            self.pnr = input(f'{id} - Digite o número dos PNRs: ')
            self.lista_pnr.append(self.pnr)

            if self.pnr == 'n':
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

