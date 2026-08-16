from setuptools import setup, find_packages

setup(
    name="dlos",
    version="0.51.0",
    description="Neuro-Symbolic Safety Shield for JEPA Latent Decision Systems",
    author="Ming-Hung Sung (ORCID: 0009-0003-3305-0637), Shih-Yu Sung",
    packages=find_packages(),
    install_requires=["numpy>=1.20.0", "scipy>=1.7.0"],
    python_requires=">=3.8",
)
