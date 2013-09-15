from setuptools import setup, find_packages
import os

version = '0.8.0'

setup(name='wheelcms',
      version=version,
      description="Overall package for WheelCMS",
      long_description=open("README.md").read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Ivo van der Wijk',
      author_email='wheelcms@in.m3r.nl',
      url='http://github.com/wheelcms/wheelcms',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pytest',
          'wheelcms_axle',
          'wheelcms_spokes',
          'wheelcms_project'
      ],
      entry_points={
      },

      )

