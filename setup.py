from setuptools import setup, find_packages

setup(
    name="cryptobot-shared",
    version="0.1.1",
    packages=find_packages(include=['shared', 'shared.*']),
    include_package_data=True,
    install_requires=[
        "pydantic>=2.0",
    ],
)