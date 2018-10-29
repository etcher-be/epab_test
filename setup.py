# coding=utf-8

import os

from setuptools import find_packages, setup

requirements = [
]
test_requirements = []

CLASSIFIERS = filter(None, map(str.strip,
                               """
Development Status :: 3 - Alpha
Topic :: Utilities
""".splitlines()))


def read_local_files(*file_paths: str) -> str:
    """
    Reads one or more text files and returns them joined together.
    A title is automatically created based on the file name.

    Args:
        *file_paths: list of files to aggregate

    Returns: content of files
    """

    def _read_single_file(file_path):
        with open(file_path) as f:
            filename = os.path.splitext(file_path)[0]
            title = f'{filename}\n{"=" * len(filename)}'
            return '\n\n'.join((title, f.read()))

    return '\n' + '\n\n'.join(map(_read_single_file, file_paths))


entry_points = ''

setup(
    name='epab_test',
    author='etcher-be',
    zip_safe=False,
    author_email='epab@daribouca.net',
    platforms=['win32'],
    url=r'https://github.com/etcher-be/epab_test',
    download_url=r'https://github.com/etcher-be/epab_test/releases',
    description="disregard this",
    license='GPLv3',
    long_description=read_local_files('README.md'),
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    python_requires='>=3.6',
    classifiers=CLASSIFIERS,
)
