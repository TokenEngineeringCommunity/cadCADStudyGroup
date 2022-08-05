### Simple Cadcad template project using cadcad
### Summary
Project just serves as a framework for layout cadcad projects in a way compatible with 0.4.28 of cadcad.
It partitions the data in a way to allow for more portability of your data, and to back up your simulation runs.
Extending this with pytest isn't a far leap. 

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

