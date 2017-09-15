from setuptools import setup


def requirements():
    with open('requirements.txt') as f:
        list_requirements = f.read().splitlines()
    return list_requirements


setup(
    name='texmex_python',
    version='1.0.0',
    author='Hi-king',
    author_email='hikingko1@gmail.com',
    url='https://github.com/Hi-king/read_texmex_dataset_python',
    description='read texmex dataset',
    long_description='',
    install_requires=requirements(),
    packages=['texmex_python'],
    zip_safe=False,
)
