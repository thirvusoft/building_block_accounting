from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in building_block_accounting/__init__.py
from building_block_accounting import __version__ as version

setup(
	name="building_block_accounting",
	version=version,
	description="Building Block Accounting",
	author="Thirvusoft",
	author_email="info@thirvusoft.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
