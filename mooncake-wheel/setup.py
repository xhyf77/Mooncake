import sys
from setuptools import setup, find_packages
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True

python_version = f">={sys.version_info.major}.{sys.version_info.minor}"

setup(
    name="mooncake",
    use_scm_version={"root": ".", "relative_to": __file__},
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
    package_data={"mooncake": [
        "*.so",
        "mooncake_master",
        "lib_so/libetcd-cpp-api.so",
    ]},
    include_package_data=True,
    zip_safe=False,
    distclass=BinaryDistribution,
    author="Mooncake",
    description="Prebuilt Python wheel for Mooncake, providing native bindings for distributed storage and transfer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C++",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=python_version,
)
