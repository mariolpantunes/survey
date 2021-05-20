# coding: utf-8

__author__ = 'Mário Antunes'
__version__ = '0.1'
__email__ = 'mariolpantunes@gmail.com'
__status__ = 'Development'


import logging
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
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
    #logger.info(df.shape)

    #filter data base on Situation
    if args.s is Situation.bachelor:
        df = df.loc[df['Qual a sua situação atual?'].isin(['Aluno 1º ano', 'Aluno 2º ano', 'Aluno 3º ano'])]
    elif args.s is Situation.masters:
        df = df.loc[df['Qual a sua situação atual?'].isin(['Aluno 4º ano (1º de Mestrado)', 'Aluno 5º ano (2º de Mestrado)'])]
    elif args.s is Situation.phd:
        df = df.loc[df['Qual a sua situação atual?'].isin(['Aluno de Doutoramento'])]
    #logger.info(df.shape)

    with PdfPages(args.o) as pdf:

        df[['A oferta formativa da Universidade é adequada?']].hist(grid=False, range=[1,4])
        pdf.savefig()
        plt.close()
    
        df[['Pretende continuar estudos (Mestrado/Doutoramento)?']].value_counts().plot(kind='pie', subplots=True, autopct='%.2f%%')
        plt.suptitle('Pretende continuar estudos (Mestrado/Doutoramento)?')
        pdf.savefig()
        plt.close()
        
        df[['Os mestrados atuais cobrem os meus interesses?']].hist(grid=False, range=[1,4])
        pdf.savefig()
        plt.close()

        df[['Considera que um mestrado/doutoramento permite acesso a melhores oportunidades no futuro?']].hist(grid=False, range=[1,4])
        pdf.savefig()
        plt.close()

        df[['Pondera concorrer a uma bolsa de investigação?']].value_counts().plot(kind='pie', subplots=True, autopct='%.2f%%')
        plt.suptitle('Pondera concorrer a uma bolsa de investigação?')
        pdf.savefig()
        plt.close()

        df[['Já teve alguma bolsa de investigação no passado?']].value_counts().plot(kind='pie', subplots=True, autopct='%.2f%%')
        plt.suptitle('Já teve alguma bolsa de investigação no passado?')
        pdf.savefig()
        plt.close()

        df[['Considera a remuneração das bolsas justa para o esforço?']].hist(grid=False, range=[1,4])
        pdf.savefig()
        plt.close()

        df[['Considera que uma bolsa de investigação melhora positivamente o seu CV?']].hist(grid=False, range=[1,4])
        pdf.savefig()
        plt.close()

        df[['Considera terminar a licenciatura e procurar emprego?']].value_counts().plot(kind='pie', subplots=True, autopct='%.2f%%')
        plt.suptitle('Considera terminar a licenciatura e procurar emprego?')
        pdf.savefig()
        plt.close()

        df[['Considera a remuneração de um emprego justo para o esforço?']].hist(grid=False, range=[1,4])
        pdf.savefig()
        plt.close()

        df[['Considera que um emprego na industria tem um peso positivo no CV?']].hist(grid=False, range=[1,4])
        pdf.savefig()
        plt.close()
        
        tmp = pd.to_numeric(df['Que salário líquido mensal considera adequado para si durante os próximos 12 meses?'], errors='coerce')
        tmp = tmp.dropna()
        tmp.hist(grid=False)
        plt.suptitle('Que salário líquido mensal considera adequado para si durante os próximos 12 meses?')
        pdf.savefig()
        plt.close()

        questions = ['Emprego empresa de TI em Aveiro', 'Emprego empresa de TI no Porto', 'Emprego empresa de TI em Lisboa', 'Emprego em Consultora',
        'Emprego em Software House de maior dimensão', 'Emprego em Academia ou Entidade de investigação', 'Bolsa de Investigação',
        'Emprego em empresa estrangeira (Remote)', 'Emprego em empresa estrangeira (no estrangeiro)', 'Emprego fora da área de TI',
        'Emprego numa Startup', 'Começar a minha Startup', 'Nenhum emprego']
        keys = ['Certamente', 'Provavelmente', 'Talvez', 'Não!']
        for q in questions:
            tmp = df[[f'Classifique os seguintes cenários em relação ao que considera ser o mais adequado face ao seu interesse e competências [{q}]']].value_counts()
            #logger.info(tmp)
            for k in keys:
                if k not in tmp:
                    tmp[k] = 0
            tmp = tmp[keys]
            tmp.plot(kind='bar', rot=0, color=['g', 'b', 'y', 'r'])
            plt.suptitle(q)
            pdf.savefig()
            plt.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Survey analysis tool')
    parser.add_argument('-i', type=str, help='input file', default='Empregabilidade.csv')
    parser.add_argument('-s', type=Situation, choices=list(Situation), default='bachelor')
    parser.add_argument('-o', type=str, help='output file', default='report.pdf')
    args = parser.parse_args()
    
    main(args)