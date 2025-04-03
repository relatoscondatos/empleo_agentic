# generate_narative_ocupacion.md.py v20250403.0528
import os
import sys


# Preparar entorno y sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from graphs.run_narrativa import run_narrativa

if __name__ == "__main__":
    narrativa = run_narrativa("sexo")
    print(narrativa)