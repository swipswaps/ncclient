#!/usr/bin/env python
from ncclient import manager
import getpass


def connect(host, port, user, password, command):
    '''
    Set a new description to an interface
    '''
    with manager.connect(
        host=host,
        port=port,
        username=user,
        password=password,
        timeout=10,
        device_params={'name': 'junos'},
        hostkey_verify=False
    ) as m:
        with m.locked(target='candidate'):
            m.load_configuration(action='set', config=command)
            result = m.commit()
            print result.tostring


if __name__ == '__main__':
    host = 'router.example.com'
    username = raw_input('Give the username for %s: ' % host)
    password = getpass.getpass('Give the password: ')
    interface = 'ge-1/1/5'
    connect(host, 830, username, password, 'set interfaces %s description example' % (interface))
