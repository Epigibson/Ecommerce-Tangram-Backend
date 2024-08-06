import sys
import os
from pathlib import Path

# Obtén la ruta al directorio raíz del proyecto (asumiendo que tests está en la raíz)
root_dir = Path(__file__).parent.parent

# Añade la ruta del proyecto al sys.path
sys.path.insert(0, str(root_dir))

# Imprime el sys.path para depuración
print("sys.path:", sys.path)