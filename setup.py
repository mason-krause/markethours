import setuptools

with open('README.rst', 'r') as f:
  long_description = f.read()

setuptools.setup(
  name = 'markethours',
  version = '1.0.0',
  author = 'Mason Krause',
  description = 'A python library for referencing and localizing US stock trading hours',
  long_description = long_description,
  long_description_content_type='text/x-rst',
  url='https://github.com/mason-krause/markethours',
  packages = setuptools.find_packages(),
  include_package_data = True,
  python_requires = '>=3.7',
  install_requires = [
    'requests',
    'pytz'],
    extras_require={
      'dev': [
        'pytest',
        'pytest-timeout']})