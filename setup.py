from setuptools import setup, find_packages
from pkg_resources import parse_requirements


def load_requirements(requirements_file_name: str) -> list:
    requirements = []
    with open(requirements_file_name, 'r') as f:
        for req in parse_requirements(f.read()):
            extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
            requirements.append(
                '{}{}{}'.format(req.name, extras, req.specifier)
            )
    return requirements


setup(
    name='marysya-skill-for-children',
    author='Kirill Neevin',
    author_email='neevin-kirill@mail.ru',
    description='My first simple service on Python',
    packages=find_packages(exclude=['tests']),
    version='0.0.1',
    install_requires=load_requirements('requirements.txt'),
    extras_require={'dev': load_requirements('requirements.dev.txt')},
)