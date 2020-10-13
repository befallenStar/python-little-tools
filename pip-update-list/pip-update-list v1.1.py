# -*- encoding: utf-8 -*-
from subprocess import call

from pip._internal.utils.misc import get_installed_distributions


def main():
    # update pip first
    call('python -m pip install --upgrade pip')
    fails = []
    for dist in get_installed_distributions():
        code = call("pip install --upgrade " + dist.project_name, shell=True)
        if code != 0:
            fails.append(dist)
    for dist in fails:
        print("error in updating package:" + dist.project_name)
    print("packages not updated:{}".format(len(fails)))


if __name__ == '__main__':
    main()
