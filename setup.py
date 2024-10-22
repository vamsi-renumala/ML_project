from typing import List
from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        this funtion will return the list of reqiurements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

#metadata
setup(
    name = 'ML_Project',
    version= '0.0.1',
    author='vamsirenumala',
    author_email='vamsirenumala000@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)