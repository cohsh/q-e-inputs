# Quantum ESPRESSO Workspace
A workspace for Quantum ESPRESSO

## Install
```Shell
git clone --recursive https://github.com/cohsh/q-e-workspace.git
cd q-e-workspace
./install.py
```

## Environment
local ↔️ remote

## Usage
### At local 
1. Install
2. Edit parameters in `./generate_project.py`
3. Execute `./generate_project.py`
4. Send input and job files to the remote computer.

### At remote
1. Install
2. Receive input and job files from the local computer.
3. Execute Quantum ESPRESSO by submitting `job.sh`.