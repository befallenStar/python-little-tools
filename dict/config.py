# -*- encoding: utf-8 -*-
import configparser


def load(path, section, option):
    """
    load from conf and return the filename of the dict
    :param path: path of config file
    :param section: section we need
    :param option: option we need
    :return: value of the option
    """
    conf = configparser.ConfigParser()
    conf.read(path)
    # print(conf.get('file', 'filename'))
    return conf.get(section, option)


def save(path, section, option, value):
    """
    save config
    :param path: path of config file
    :param section: section to change
    :param option: option to change
    :param value: value
    :return:
    """
    conf = configparser.ConfigParser()
    conf.read(path)
    conf.set(section, option, value)
    conf.write(open(path, 'w'))


def main():
    # filename = load('dict.conf', 'file', 'filename')
    # print(filename)
    save('dict.conf', 'user', 'password', 'asdasd')


if __name__ == '__main__':
    main()
