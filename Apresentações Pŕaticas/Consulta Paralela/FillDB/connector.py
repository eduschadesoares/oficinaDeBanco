#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from randomer import Random
import sys
import postgresql

sys.path.append('..')

random = Random()

db = None


class Connector:

    def __init__(self, user, password, ip, db_name):
        self.user = user
        self.password = password
        self.ip = ip
        self.db_name = db_name
        self.db = None

    def open_db(self):
        try:
            self.db = postgresql.open("pq://{}:{}@{}/{}".format(self.user, self.password, self.ip, self.db_name))
        except Exception as error:
            print(error)
            return
        print('Successfully connected to {}!'.format(self.db_name))

    def create_alunos(self):
        try:
            alunos_number = int(input('How many alunos do you want to create? '))
        except Exception as error:
            print('Insert a number!')
            return
        created = 0
        not_created = 0
        print('Creating {} alunos...'.format(alunos_number))
        for i in range(alunos_number):
            content = random.randomizeAluno()

            sql = "insert into alunos( mat_alu, nom_alu, cod_curso, dat_nasc, tot_cred, mgp )" \
                  " values ( {}," \
                  " '{}'," \
                  " {}," \
                  " to_date( '{}', 'DD/MM/YYYY' ), " \
                  "{}," \
                  " {} )".format(content['mat_alu'], content['nom_alu'], content['cod_curso'], content['dat_nasc'], content['tot_cred'], content['mgp'],)

            try:
                self.db.execute(sql)
                created += 1
            except Exception as error:
                print('Error, PK {} already exists!'.format(content['mat_alu']))
                not_created += 1

        print('{} created, {} failed;'.format(created, not_created))

    def close_db(self):
        db.close()

