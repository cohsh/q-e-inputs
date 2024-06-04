# Quantum ESPRESSO Workspace
A workspace for Quantum ESPRESSO

## Install
```Shell
git clone --recursive https://github.com/cohsh/q-e-workspace.git
cd q-e-workspace
./install.py
```

## Usage
1. At local
    1. Edit parameters in `./generate_project.py`
    2. Execute `./generate_project.py`

2. At the computer that executes calculations
    1. Apply the changes (ex: by `scp` or `git pull`).