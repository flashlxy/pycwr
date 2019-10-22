# -*- coding: utf-8 -*-
"""
suggested by bugsuse(https://github.com/bugsuse)
"""

from setuptools import find_packages, setup
import sys, os

parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

DISTNAME = "NuistRadar"
AUTHOR = "Yu Zheng"
AUTHOR_EMAIL = "zhengyunuist@gmail.com"
URL = "https://github.com/YvZheng"
PYTHON_REQUIRES = ">=3.6"
INSTALL_REQUIRES = ["matplotlib>=2.2.3", "pyproj>=1.9.6", "Cartopy>=0.17.0", "xarray>=0.12.1",\
"numpy>=1.17.2", "scipy>=1.1.0", "pandas>=0.23.4", "PyQt5>=5.13.1", "netCDF4>=1.5.2"]
DESCRIPTION = "China Weather Radar tools"
LONG_DESCRIPTION = """The Weather Radar Toolkit, support most of China's radar formats
(WSR98D, CINRAD/SA/SB/CB, CINRAD/CC/CCJ, CINRAD/SC/CD)"""

setup(
    name=DISTNAME,
    version="0.1",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    url=URL,
    include_package_data = True,
    packages=find_packages(parent_dir),
    package_data={"NuistRadar": ["data/*.*","__init_.py", "GraphicalInterface/*.py", "draw/colormap/balance-rgb.txt"]},
)
