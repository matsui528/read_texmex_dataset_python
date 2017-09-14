from setuptools import setup


def requirements():
    with open('requirements.txt') as f:
        list_requirements = f.read().splitlines()
    return list_requirements


setup(
    name='texmex_python',
    version='1.0.0',
    author='',
    author_email='',
    description='',
    long_description='',
    install_requires=requirements(),
    packages=['texmex_python'],
    zip_safe=False,
)
