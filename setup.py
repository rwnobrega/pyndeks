from setuptools import setup, find_packages

_long_description = '''
**Pyndeks** is yet another HTML directory indexer.
'''

setup(
    name='pyndeks',
    version='0.0.0',
    description='Yet another HTML directory indexer.',
    long_description=_long_description,
    url='https://github.com/rwnobrega/pyndeks/',
    author='Roberto W. Nobrega',
    author_email='rwnobrega@gmail.com',
    license='MIT',
    project_urls={
        'Source': 'https://github.com/rwnobrega/pyndeks/',
    },
    packages=find_packages(),
    scripts=['pyndeks/pyndeks'],
    package_data={'pyndeks': ['template.html.jinja']},
    install_requires=['jinja2', 'natsort'],
    python_requires='>=3.7'
)
