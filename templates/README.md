## Simulation Example Templates
This is just meant to be a starting point for projects that you might want to build with cadcad or cadcadTools or any of the simulations.
There's a small range of options and this I think captures most of what you'll need.

### cadcad_og
The current 0.4.28 implementation of cadcad. It is simply laid out in a way that is codusive to running multiple test, and helps seperate concerns
This layout was inspired by this [repo](https://github.com/BlockScience/filecoin-baseline-incentives/tree/ac3874ba98c3fe9a5b11e5682072aa04f980c655)

```
├── cadcad_fromdisk.ipynb // top level notebook to read simulations from disk
├── cadcad_live.ipynb // top level notebook to read simulation after executing experimennt
├── data
│   └── simulations // folder for the cached simulation results
├── model
│   ├── __init__.py // init
│   ├── __main__.py // main for commandline execution
│   ├── execution.py // main for exposing a method to execute experiment
│   ├── experiment.py // the experiment object
│   ├── logic.py // logic for the state and policy updates
│   ├── params.py // params parameters used for setting model state
│   └── structure.py // The wiring together of the state update blocks
└── requirements.txt 
```

### cadcad_tools
This is slightly can't be used for blockscience labs simulation, but is a smaller stop gap between the new cadcad-ri implementation and 0.4.28

This is a single layout version of this that we'll be using for most things in the group until larger project,and we will mostly follow the format 
of the `cadcad_og`


###  python
This simulator is just what a simulator does at its core, even cadcad at it's base level. This is mostly to do something quick with 0 overhead.
It's also to get a feel for what it takes to simulate something.


### requirements.txt
For the group if you're missing a package, you can just refer to the requirements.txt and more than likely this should resolve it. It will include 
more than what you need but your dependency basis should be covered.


