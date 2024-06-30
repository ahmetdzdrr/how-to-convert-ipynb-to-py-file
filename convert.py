import nbformat
from nbconvert import PythonExporter

# Gerekli paketleri yükleyin
# pip install nbformat nbconvert

notebook_filename = "example.ipynb"  # Write your ipynb file name here
notebook = nbformat.read(notebook_filename, as_version=4)

# Convert the notebook to a Python script
python_exporter = PythonExporter()
python_script, _ = python_exporter.from_notebook_node(notebook)

# Save the Python script
python_filename = "example.py"  # Name of the python file to save
with open(python_filename, "w") as f:
    f.write(python_script)
