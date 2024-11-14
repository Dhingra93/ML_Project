from setuptools import find_packages,setup
from typing import List

HyponDoTE="-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements. 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()  ## reading file
        requirements=[req.replace('\n','') for req in requirements]     

        if HyponDoTE in requirements:
            requirements.remove() 


    return requirements




setup(
name="ML_Project",
version='0.0.1',
author="Rohit Dhingra",
author_email='rohitdhingra93@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)



