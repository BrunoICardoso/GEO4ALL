import os

def PathDownload():
    #Essa função tem objetive de trazer seu caminho de pasta para Pode salvar todo qualquer tipo arquivo.
    return str(os.path.dirname(os.path.abspath(__file__))).replace('\\','/')