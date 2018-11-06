#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from connector import Connector

import sys
sys.path.append('..')



def initialize():
    if len(sys.argv) <= 1:
        print('Usage: ')
        print('./start.py [OPTIONS]')
        print('Try \'./start.py --help\' for more information.')
        return False
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-h'\
                or sys.argv[1] == '-help' \
                or sys.argv[1] == '--help':
            print('Usage: ')
            print('./start.py [user] [password] [server ip] [database name]')
            print('Connect to a postgres database.')
            print('Make sure the database is running!')
            return False
        else:
            print('Invalid parameters!')

    elif len(sys.argv) == 5:
        return True

    else:
        print('Invalid number of parameters!')
        print('Try \'./start.py --help\' for more information.')
        return False


def create_connection_obj():
    user = sys.argv[1]
    password = sys.argv[2]
    ip = sys.argv[3]
    db = sys.argv[4]

    connection = Connector(user, password, ip, db)
    connection.open_db()
    try:
        connection.create_alunos()
    except Exception as error:
        print('Something went wrong! Verify the name list files!')

if __name__ == '__main__':
    if initialize():
        create_connection_obj()
else:
    print('It\'s necessary to execute this file in terminal!')

