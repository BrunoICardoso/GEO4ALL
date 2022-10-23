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
                def is_within_directory(directory, target):
                    
                    abs_directory = os.path.abspath(directory)
                    abs_target = os.path.abspath(target)
                
                    prefix = os.path.commonprefix([abs_directory, abs_target])
                    
                    return prefix == abs_directory
                
                def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
                
                    for member in tar.getmembers():
                        member_path = os.path.join(path, member.name)
                        if not is_within_directory(path, member_path):
                            raise Exception("Attempted Path Traversal in Tar File")
                
                    tar.extractall(path, members, numeric_owner=numeric_owner) 
                    
                
                safe_extract(tar, path=self.directory)

                for filetar in tar.getnames():
                    path = self.directory + '/' + filetar
                    listfile.append(path)

        return listfile
