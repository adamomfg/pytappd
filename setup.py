from setuptools import setup

setup(
    name='pytappd',
    version='0.1',
    packages=['untappd'],
    zip_safe = False,
    include_package_data=True,
    url='http://github.com/dstegelman/pytappd',
    license='MIT',
    author='Derek Stegelman',
    author_email='email@stegelman.com',
    description='Python Wrapper for Untappd API',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        "Framework :: Django",
        ],
    install_requires = ['requests']
)
