# The version file is generated automatically by setuptools_scm
from cookiecutter_test._version import version as __version__
from .just_to_check_documentation import print_smile


def add_one(x: int):
    """An example function that increases a number

    :param x: The input parameter to increase
    :return: The successor of the given number
    """
    return x + 1

def multiply_one(x:int, y:int):
    """An example function that multiplies a number by 2

    :param x: The first input parameter to multiply
    :param y: The second input parameter to multiply
    :return: The result of the multiplication
    """
    return x * y
