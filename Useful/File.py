import os, logging, time, re, wget, codecs, tarfile
from datetime import datetime

# Essa clase tem a função de exercer toda a manipulaão de arquivos
class Files():

    def __init__(self, directory):
        self.directory = directory

    def ReturnExtractTazGz(self, url: str) -> list:
        # Essa função faz download do arquivo e extrai arquivos para diretorio
        # Retorna a lista do que foi extraido
        # URL url do Download cujo o arquivo seja Taz.GZ

        listfile = []
        if url:
            filename = wget.download(url=url, out=self.directory)
            with tarfile.open(filename) as tar:
                tar.extractall(path=self.directory)

                for filetar in tar.getnames():
                    path = self.directory + '/' + filetar
                    listfile.append(path)

        return listfile
