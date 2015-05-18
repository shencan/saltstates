#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import salt.utils
import ConfigParser

def files(name='/etc/ansible/ansible.cfg',
         inventory=None,
         forks=None,
         module_lang=None,
         host_key_checking=None,
         timeout=None
         ):
    ret = {
           'name': name,
           'changes': {},
           'result': True,
           'comment': ''
           }
    all={}
    file=__salt__['file.file_exists'](name)
    if __opts__['test']:
       ret['comment'] = 'some defaults has changed'
       ret['result'] = None
       return ret
    if file:
       cf = ConfigParser.ConfigParser()
       cf.read(name)
       if inventory:
          cf.set('defaults', 'inventory', inventory)
          mess= 'inventory change to {0} \n'.format(inventory)
       if forks:
          cf.set('defaults', 'forks', forks)
          mess+= 'forks chagng to {0} \n'.format(forks)
       if module_lang:
          cf.set('defaults','module_lang', module_lang)
          mess+= 'module_lang change to {0} \n'.format(module_lang)
       if host_key_checking:
          cf.set('defaults','host_key_checking',host_key_checking)
          mess+='host_key_checking change to {0} \n'.format(host_key_checking)
       if timeout:
          cf.set('defaults','timeout',timeout)
          mess+='timeout change to {0} \n'.format(timeout)
       cf.write(open(name, "w"))
       ret['result'] = True
       all['message'] = mess
       ret['comment'] = 'some defaults has changed'
       ret['changes'] = all
    else:
       ret['comment'] = '{0} files not exists'.format(name)
       ret['result'] = False
    return ret
