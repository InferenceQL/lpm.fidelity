from setuptools import setup

setup(
    name="lpm_fidelity",
    description="Assessing fidelity of synthetic data",
    author="Ulli Schaechtle",
    author_email="ulli@mit.edu",
    packages=["lpm_fidelity", "fidelity_cli"],
    package_dir={"lpm_fidelity": "src", "fidelity_cli": "bin"},
    install_requires=[
        # XXX:This is solved via flake.nix.
        # Not filling anything in here to avoid duplication.
    ],
    entry_points={
        "console_scripts": [
            "assess-distance=fidelity_cli.dist:main",
            "assess-statistics=fidelity_cli.two_sample_testing:main",
        ],
    },
)
