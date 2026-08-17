from setuptools import setup, find_packages

setup(
    name="dlos",
    version="0.59.0",
    description="Deterministic Safety Shielding for JEPA-Based Embodied AI",
    author="Ming-Hung Sung (ORCID: 0009-0003-3305-0637), Shih-Yu Sung",
    packages=find_packages(),
    install_requires=["numpy>=1.20.0", "scipy>=1.7.0", "torch>=2.0.0"],
    python_requires=">=3.8",
)
