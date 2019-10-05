import io
import os
from setuptools import setup

__version__ = '0.0.1'
here = os.path.abspath(os.path.dirname(__file__))

# load requirements
with open("requirements.txt") as f:
    dependencies = f.read().splitlines()

# load README
with io.open(os.path.join(here, "README.md"), encoding="utf-8") as doc_file:
    documentation = '\n' + doc_file.read()



setup(
    name='Relation Classification via Convolutional Deep Neural Network',
    version=__version__,
    long_description=documentation,
    author_email='balavivek107@gmail.com',
    url='https://github.com/bsivanantham/Relation-Classification-via-Convolutional-Deep-Neural-Network',
    license="GPLv3",
    classifiers=["Development Status :: 5 - Production/Stable",
                 "Environment :: Console",
                 "Environment :: Win32 (MS Windows)",
                 "Environment :: MacOS X",
                 "Environment :: Web Environment",
                 "Environment :: Other Environment :: VPS",
                 "Intended Audience :: End Users/Desktop",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: GNU General Public License v3",
                 "Operating System :: Microsoft :: Windows",
                 "Operating System :: POSIX :: Linux",
                 "Operating System :: MacOS :: MacOS X",
                 "Operating System :: Unix",
                 "Programming Language :: Python",
                 "Programming Language :: JavaScript",
                 "Programming Language :: SQL",
                 "Topic :: Internet :: Browsers",
                 "Topic :: Other/Nonlisted Topic :: Automation :: Selenium",
                 "Topic :: Utilities",
                 "Natural Language :: English"],
    install_requires=dependencies,
    extras_require={"test":["pytest", "tox"]},
    include_package_data=True,
    python_requires=">=2.7",
    platforms=["win32", "linux", "linux2", "darwin"]
    )