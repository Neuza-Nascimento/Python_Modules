#!/usr/bin/env python3

import sys
import os
import site


#procura saber se estamos diante do ambiente virtual ou nao
#.prefix: Contém o caminho da pasta raiz do ambiente Python +
# que está a correr o script neste momento.
#.base_prefix: Contém o caminho da instalação original e global do Python na tua máquina
def is_virtual_ambient() -> bool:
    return sys.prefix != sys.base_prefix or 'VIRTUAL_ENV' in os.environ


def main() -> None:
    if not is_virtual_ambient():
        print("MATRIX STATUS: You're still plugged in\n")
        #Devolve o caminho absoluto do binário (o executável) do Python que iniciou o programa.
        #/usr/bin/python3
        print(f"Current Python: {sys.executable}") 
        print(f"Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\Scripts\\activate  # On Windows\n")
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        #/path/to/matrix_env/bin/python
        print(f"Current Python: {sys.executable}")
        # Pega num caminho completo e extrai apenas o nome do último elemento
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print(f"SUCCESS: You're in an isolated environment!")
        print(f"Safe to install packages without affecting the global system.\n")
        print("Package installation path:")
        #Retorna uma lista de caminhos onde o Python vai procurar e instalar bibliotecas.
        #permite mostrar ao utilizador a pasta site-packages
        print(site.getsitepackages()[0])


if __name__ == "__main__":
    main()
