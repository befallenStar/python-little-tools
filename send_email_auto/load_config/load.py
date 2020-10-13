# -*- encoding: utf-8 -*-
import configparser


def read_config(path):
    cf=configparser.ConfigParser()
    cf.read(path)
    # print(cf.sections())
    # for section in cf.sections():
    #     print(cf.options(section))
    #     print(cf.items(section))
    #     for option in cf.options(section):
    #         print(cf.get(section,option))
    email={}
    for item in cf.items('email'):
        email[item[0]]=item[1]
    return email
