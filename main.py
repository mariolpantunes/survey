# coding: utf-8

__author__ = 'Mário Antunes'
__version__ = '0.1'
__email__ = 'mariolpantunes@gmail.com'
__status__ = 'Development'


import logging
import argparse
import pandas as pd
import matplotlib.pyplot as plt


from enum import Enum


class Situation(Enum):
    masters = 'masters'
    bachelor = 'bachelor'

    def __str__(self):
        return self.value


logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def main(args):
    df = pd.read_csv(args.i, index_col=0)
    logger.info(df.shape)

    #filter data base on Situation
    if args.s is Situation.bachelor:
        df = df.loc[df['Qual a sua situação atual?'].isin(['Aluno 1º ano', 'Aluno 2º ano', 'Aluno 3º ano'])]
    elif args.s is Situation.masters:
        df = df.loc[df['Qual a sua situação atual?'].isin(['Aluno 4º ano (1º de Mestrado)', 'Aluno 5º ano (2º de Mestrado)'])]
    logger.info(df.shape)

    #df[['A oferta formativa da Universidade é adequada?']].hist()
    #plt.suptitle('A oferta formativa da Universidade é adequada?')
    #plt.show()

    df[['Pretende continuar estudos (Mestrado/Doutoramento)?']].value_counts().plot(kind='pie', subplots=True, autopct='%.2f%%')
    plt.suptitle('Pretende continuar estudos (Mestrado/Doutoramento)?')
    plt.show()




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Survey analysis tool')
    parser.add_argument('-i', type=str, help='input file', default='Empregabilidade.csv')
    parser.add_argument('-s', type=Situation, choices=list(Situation), default='bachelor')
    parser.add_argument('-o', type=str, help='output file')
    args = parser.parse_args()
    
    main(args)