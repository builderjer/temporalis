from setuptools import setup

setup(
    name='temporalis',
    version='0.1',
    packages=['temporalis', 'temporalis.providers'],
    url='https://github.com/builderjer/temporalis',
    license='Apache2',
    author='builderjer',
    install_requires=["requests",
                      "timezonefinder",
                      "geopy",
                      "geocoder",
                      "pendulum",
                      "python-dateutil",
                      "pytz",
                      "requests-cache",
                      "astral"],
    author_email='builderjer@gmail.com',
    description='unified weather service apis'
)
