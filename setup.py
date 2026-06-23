from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements from requirements.txt.
    It automatically filters out '-e .' if present.
    '''
    requirements = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file_obj:
            requirements = file_obj.readlines()
            # Remove newlines and strip whitespace
            requirements = [req.strip() for req in requirements]
            
            # Filter out comments and empty lines
            requirements = [req for req in requirements if req and not req.startswith('#')]
            
            # Remove '-e .' which is used for triggering editable installations locally
            if '-e .' in requirements:
                requirements.remove('-e .')
    except FileNotFoundError:
        pass
        
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Utkarsh',
    author_email='utkarshpareek04@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
