import os
import re

class Searcher:
    def __init__(self, path, query):
        self.path   = path

        if self.path[-1] != '/':
            self.path += '/'

        self.path = self.path.replace('/', '\\')
        self.query  = query
        self.searched = {}

    def find(self):
        for root, dirs, files in os.walk( self.path ):
            for file in files:
                if re.match(r'.*?\.txt$', file) is not None:
                    if root[-1] != '\\':
                        root += '\\'           
                    f = open(root + file, 'rt')
                    txt = f.read()
                    f.close()

                    count = len( re.findall( self.query, txt ) )
                    if count > 0:
                        self.searched[root + file] = count

    def getResults(self):
        return self.searched