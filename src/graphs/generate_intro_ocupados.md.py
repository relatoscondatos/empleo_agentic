# generate_narative_ocupacion.md.py v20250404.1318
import os
import sys


# Preparar entorno y sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from graphs.run_intro import run_intro

if __name__ == "__main__":
    intro = run_intro("ocupados")
    print(intro)