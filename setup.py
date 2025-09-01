from setuptools import setup, find_packages

setup(
    name="duino-coin",
    version="4.3.0",
    description="Official Duino-Coin PC & AVR Miner",
    author="Duino-Coin Team",
    url="https://github.com/revoxhere/duino-coin",
    license="MIT",
    packages=find_packages(include=["*", "Tools", "Resources"]),
    install_requires=[
        "requests",
        "colorama",
        "pyserial",
    ],
    entry_points={
        "console_scripts": [
            "pcminer=PC_Miner:main",
            "avrminer=AVR_Miner:main",
        ],
    },
    include_package_data=True,
    python_requires=">=3.6",
)
