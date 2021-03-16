from setuptools import setup

setup(
    name='NLP',
    author='Michael Kelley',
    packages=['NLP'],
    install_requires=['requests', 'sklearn', 'pandas',],
    entry_points={
        'console_scripts': [
        'challenge-1 = NLP.__challenge1__:challenge1',
        'challenge-2 = NLP.__challenge2__:challenge2',
        'challenge-5 = NLP.__challenge5__:challenge5',
        ],
    }
)
