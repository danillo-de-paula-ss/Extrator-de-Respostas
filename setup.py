import os
import sys
from cx_Freeze import setup, Executable

# path = os.path.dirname(__file__) + os.sep
# O que deve ser incluído na pasta final
FILES = []
INCLUDES = ['os', 'glob', 'copy', 'string', 'itertools']
PACKAGES = ['PySimpleGUI', 'numpy', 'cv2']
EXCLUDES = []

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.

# Saída de arquivos
config = Executable(
    script='extrator_de_respostas.py',
    # icon=path + 'nxt.ico',
    base=base
)

# Configurar o cx-freeze (detalhes do programa)
setup(
    name='extrator_de_respostas',
    version='1.0.0',
    description='Este programa extrai respostas de gabaritos',
    author='DanilloDePaulaSS',
    options={'build_exe': {'include_msvcr': False,
                           'include_files': FILES,
                           'includes': INCLUDES,
                           'excludes': EXCLUDES,
                           'packages': PACKAGES,}},
    executables=[config]
)
