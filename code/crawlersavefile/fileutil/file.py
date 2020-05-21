# encoding: utf-8
#!/usr/bin/python

import json

class File(object):

    def __init__(self,_fileUrl,_saveMethod,_indentNo,*args, **kwargs):
        self._fileUrl = _fileUrl
        self._saveMethod = _saveMethod
        self._indentNo = _indentNo

    def saveLine(self,dataline):
        with open(self._fileUrl,self._saveMethod, encoding='utf-8') as file:
            file.writelines(dataline+'\n')#indent 缩进字符个数