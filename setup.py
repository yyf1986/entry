from setuptools import setup, find_packages

ENTRY_POINTS = """
[console_scripts]
acc = entryclient.entry:main
"""

requirements = [
    'websocket-client==0.32.0',
    'protobuf==3.0.0b3',
    'six==1.9.0',
]

setup(
    name="entryclient",
    author='EricPai <ericpai94@hotmail.com>',
    version='2.2.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points=ENTRY_POINTS,
    install_requires=requirements,
)
