polyzymd_builder
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/joelaforet/polyzymd_builder/workflows/CI/badge.svg)](https://github.com/joelaforet/polyzymd_builder/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/joelaforet/polyzymd_builder/branch/main/graph/badge.svg)](https://codecov.io/gh/joelaforet/polyzymd_builder/branch/main)


Useful collection of scripts for the building of polymer-protein systems for MD simulations.

This repository is currently under development. To do a developmental install, download this repository and type

`pip install -e .`

in the repository directory.

## Important Notes

### Building Polymers from Monomers
* Monomers must be constructed in a way that is compliant with the reaction chemistry you wish to perform.
* For example, Atom-Transfer Radical Polymerization (ATRP) first requires activation of monomers via halogenating them.
![abstract](docs/_static/atrp_visual.png)
* To perform this reaction, you must provide a **halogenated** monomer structure, in the example case a **chlorinated** one. 
![abstract](docs/_static/SPMA_activation.png)

### Copyright

Copyright (c) 2025, Joe Laforet Jr.


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.11.
