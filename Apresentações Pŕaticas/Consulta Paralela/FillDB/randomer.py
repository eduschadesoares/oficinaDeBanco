#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
import datetime
from fileHandler import File

sys.path.append('..')


class Random:
    def randomizeAluno(self):
        nomes = []
        sobrenomes = []
        cursos = [3, 10, 26]

        def get_nomes():
            try:
                data = self.file.read_nome()
            except Exception as error:
                print(error)
                return
            if data:
                for line in data:
                    line = line.rstrip('\n')  # Remove \n
                    nomes.append(line)


        def get_sobrenomes():
            try:
                data = self.file.read_sobrenome()
            except Exception as error:
                print(error)
                return
            if data:
                for line in data:
                    line = line.rstrip('\n')  # Remove \n
                    sobrenomes.append(line)

        def create_aluno():

            nome_aluno = random.choice(nomes)
            sobrenome_aluno = random.choice(sobrenomes)

            nome_final = '{} {}'.format(nome_aluno, sobrenome_aluno)

            now = datetime.datetime.now()
            mat_alu = '{}{}{}'.format(now.minute, now.second, now.microsecond)
            cod_curso = random.choice(cursos)

            y = random.choice(range(1978, 2001))
            m = random.choice(range(1, 13))
            d = random.choice(range(1, 29))

            dat_nasc = '{:02d}/{:02d}/{}'.format(d, m, y)

            tot_cred = random.choice(range(1, 100))

            mgp = round(random.uniform(3, 10), 2)

            content = {
                'nom_alu': nome_final,
                'mat_alu': mat_alu,
                'cod_curso': cod_curso,
                'dat_nasc': dat_nasc,
                'tot_cred': tot_cred,
                'mgp': mgp,
            }

            return content

        get_nomes()
        get_sobrenomes()
        content = create_aluno()
        return content

    def __init__(self):
        self.file = File()
