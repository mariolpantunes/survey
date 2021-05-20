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
    phd = 'phd'

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
    elif args.s is Situation.phd:
        df = df.loc[df['Qual a sua situação atual?'].isin(['Aluno de Doutoramento'])]
    logger.info(df.shape)

    df[['A oferta formativa da Universidade é adequada?']].hist(grid=False, range=[1,4])
    #df = df[['A oferta formativa da Universidade é adequada?']].value_counts()
    #df = df.set_index([1,2,3,4])
    #df[['A oferta formativa da Universidade é adequada?']].value_counts().plot(kind='bar', subplots=True)

    #print(df[['A oferta formativa da Universidade é adequada?']])
    #df.plot(kind='bar', subplots=True)
    #plt.xlim(1,4)
    plt.show()

    df[['Pretende continuar estudos (Mestrado/Doutoramento)?']].value_counts().plot(kind='pie', subplots=True, autopct='%.2f%%')
    plt.suptitle('Pretende continuar estudos (Mestrado/Doutoramento)?')
    plt.show()
    
    df[['Os mestrados atuais cobrem os meus interesses?']].hist(grid=False, range=[1,4])
    plt.show()

    df[['Considera que um mestrado/doutoramento permite acesso a melhores oportunidades no futuro?']].hist(grid=False, range=[1,4])
    plt.show()

    df[['Pondera concorrer a uma bolsa de investigação?']].value_counts().plot(kind='pie', subplots=True, autopct='%.2f%%')
    plt.suptitle('Pondera concorrer a uma bolsa de investigação?')
    plt.show()

    df[['Já teve alguma bolsa de investigação no passado?']].value_counts().plot(kind='pie', subplots=True, autopct='%.2f%%')
    plt.suptitle('Já teve alguma bolsa de investigação no passado?')
    plt.show()

    df[['Considera a remuneração das bolsas justa para o esforço?']].hist(grid=False, range=[1,4])
    plt.show()

    df[['Considera que uma bolsa de investigação melhora positivamente o seu CV?']].hist(grid=False, range=[1,4])
    plt.show()

    df[['Considera terminar a licenciatura e procurar emprego?']].value_counts().plot(kind='pie', subplots=True, autopct='%.2f%%')
    plt.suptitle('Considera terminar a licenciatura e procurar emprego?')
    plt.show()

    df[['Considera a remuneração de um emprego justo para o esforço?']].hist(grid=False, range=[1,4])
    plt.show()

    df[['Considera que um emprego na industria tem um peso positivo no CV?']].hist(grid=False, range=[1,4])
    plt.show()

    tmp = pd.to_numeric(df['Que salário líquido mensal considera adequado para si durante os próximos 12 meses?'], errors='coerce')
    tmp = tmp.dropna()
    tmp.hist(grid=False)
    plt.suptitle('Que salário líquido mensal considera adequado para si durante os próximos 12 meses?')
    plt.show()

    #tmp = df[['Classifique os seguintes cenários em relação ao que considera ser o mais adequado face ao seu interesse e competências']]#.hist(grid=False)
    #logger.info(tmp)
    #plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Survey analysis tool')
    parser.add_argument('-i', type=str, help='input file', default='Empregabilidade.csv')
    parser.add_argument('-s', type=Situation, choices=list(Situation), default='bachelor')
    parser.add_argument('-o', type=str, help='output file')
    args = parser.parse_args()
    
    main(args)