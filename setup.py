# -*- coding: utf-8 -*-
"""
Dual-Loop OS: JEPA Safety-Critical Latent Decision Architecture
========================================================
Setup script for pip-installable pcos-latent package.
"""

from setuptools import setup, find_packages

setup(
    name="pcos-latent",
    version="30.0.0",
    description="JEPA Safety-Critical Latent Decision Architecture: A Formal Neuro-Symbolic Framework with Deterministic Barrier Constraints",
    long_description="JEPA Safety-Critical Latent Decision Architecture: A Formal Neuro-Symbolic Framework with Deterministic Barrier Constraints",
    long_description_content_type="text/markdown",
    author="Sovereign Decision Intelligence Team",
    author_email="research@pcos-intelligence.org",
    url="https://github.com/SDRmsung/Dual-Loop OS",
    packages=find_packages(where="35-Areas/A42_Dual-Loop OS_Personal_Decision_Intelligence/03_Agentic_Implementation"),
    package_dir={"": "35-Areas/A42_Dual-Loop OS_Personal_Decision_Intelligence/03_Agentic_Implementation"},
    py_modules=["dual_loop_os_core_engine"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[],
)
