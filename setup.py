from setuptools import setup
setup(
    name="gql-next",
    version="0.1",
    py_modules="gql",
    python_requires = '>=3.7,<3.8.',
    install_requires=["click>=7.0,<8.0",
                      "graphql-core-next ~=1.0.1",
                      "requests >= 2.21, <3.0",
                      "jinja2 >= 2.10, <3.0",
                      "inflection >= 0.3.1, < .4",
                      "dataclasses-json >= 0.2.0, < .3",
                      "aiohttp >= 3.5, < 4.0",
                      "watchdog >= 0.9.0, <1.0.0" ],
     entry_points={
         'console_scripts': ['gql=gql.cli:cli'],
     }
)
