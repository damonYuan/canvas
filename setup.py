import codecs
from setuptools import setup, find_packages

with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="canvas",
    version="1.0.0",
    license='http://www.apache.org/licenses/LICENSE-2.0',
    description="a simple console canvas",
    author='Damon Yuan',
    author_email='damon.yuan.dev@gmail.com',
    url='https://www.damonyuan.com',
    packages=find_packages(include=['canvas', 'canvas.*']),

    package_data={
        'canvas': ['README.rst']
    },
    install_requires=[],
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest'],
    entry_points="""
    [console_scripts]
    canvas = canvas.app:main
    """,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    long_description=long_description,
)