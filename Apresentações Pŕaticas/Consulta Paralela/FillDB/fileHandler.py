#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class File:

    def read_nome(self):
        try:
            file = open("nome.txt", "r")
            nome = file.readlines()
            file.close()
        except Exception as error:
            print(error)
            return
        return nome

    def read_sobrenome(self):
        try:
            file = open("sobrenome.txt", "r")
            sobrenome = file.readlines()
            file.close()
        except Exception as error:
            print(error)
            return
        return sobrenome
