from setuptools import setup


setup(
    name='bojack',
    version='0.1.1',
    url='https://github.com/mauricioabreu/bojack-py',
    license='MIT',
    description='BoJack client written in Python',
    author='Mauricio de Abreu Antunes',
    author_email='mauricio.abreua@gmail.com',
    packages=['bojack'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
    ],
)
