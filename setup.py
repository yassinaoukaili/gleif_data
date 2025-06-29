from setuptools import find_packages, setup

setup(
    name="gleif_data",
    version="1.0.0",
    include_package_data=True,
    packages=find_packages(),
    package_data={'gleif_data': ['data/*.csv']},
    author="Yassine A.",
    install_requires=['pandas==2.3.0',
                      'pycountry==24.6.1',
                      'pydantic==2.11.7',
                      'pydantic-extra-types==2.10.5',
                      'requests==2.32.4'],
    python_requires=">=3.10",
)
