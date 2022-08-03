### Simple Cadcad template project using cadcadTools
### Summary
Project just serves as a framework for layout cadcad projects in a way compatible with 0.4.28 of cadcad.
this repo uses cadcadTools. We choose cadcadTools as a stop gap between 0.4.28 and the new reference implementation of 
cadcad. The motivation behind this is that the new reference implementation uses types and reduces complexity alot. This
can be seen as a stepping stone towards that end.


### Installation
```
# setup a local environment to build from
python3.10 -m venv venv
source activate venv/bin/activate
# should be within the python environment now
pip install -r requirements.txt
# depending on your setup you may need to install ipykernel
pip install ipykernel
```

