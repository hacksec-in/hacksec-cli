from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="hacksec",
    version="1.0",
    description="access hacksec.in from command-line",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ScRiPt1337/hacksec-cli",
    author="script1337",
    author_email="script1337x@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["hacksec"],
    include_package_data=True,
    install_requires=["prompt-toolkit", "aiohttp", "asyncio",
                      "rich", "pyinquirer", "async-timeout"],
    entry_points={
        "console_scripts": [
            "hacksec=hacksec_cli.app:main",
        ]
    },
)
