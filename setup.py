from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    
    """
    This function returns the list of requirements for the project.
    """
    
    requirements_lst = []
    
    return requirements_lst



setup(
    
    name='sensor',
    version='0.0.0',
    author='Bapan Bairagya',
    author_email='bapanmldl7892@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    
)