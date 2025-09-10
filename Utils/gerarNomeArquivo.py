import random
import string

def gerarNomeArquivo():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
