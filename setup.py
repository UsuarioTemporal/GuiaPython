from setuptools import setup
#paquetes distribuibles
setup(
    name="Conexion",
    version="1.0.0",
    description="paquete de repasos",
    author="Thom",
    author_email="thomtwd@gmail.com",
    url="https://github.com/UsuarioTemporal/RepasoPython",
    packages=["conexionDB"]
)

"""
    python setup.py sdist

    cd dist

    pip3.7 install paquete...
"""