# Solve problems using algorithms in Python

## Installation

Clone repository using:
```bash
git clone https://github.com/nasr-edine/P7_drai_nasr-edine.git
```
Move to the P7_drai_nasr-edine root folder with:
```bash
cd P7_drai_nasr-edine
```
Create a virtual environment in root folder of project 
```bash
python -m venv env
```
Activate virtual environment
```bash
source ./env/bin/activate
```
Install dependencies
```bash
pip install -r requirements.txt
```
## Usage

execute the python script below with a filename and a solver method in argument, by default brute force is taken:
```bash
python main.py [-h] -f FILENAME [-m {brute,dynamic}]
```

### Folder Structure

    .
    ├── main.py        # the main script to run 
    ├── bruteforce.py  # contains bruteforce solver 
    ├── optimized.py   # contains dynamic programming solver
    ├── requirements   # contains dependencies
    ├── flake-report/  # generating HTML reports of flake8 violations  
    └── README.md

### How to check style code ?

##### Consulting HTML reports of flake8 violations

To generate flake8 report, type command below
> :warning: **If you use this command**: exclude virtual environment from flake8

```bash
flake8 --format=html --htmldir=flake-report --exclude=env
```


* open flake-report/index.html file with your browser
```bash
open -a "Google Chrome" index.html
open -a "firefox" index.html
open -a "safari" index.html
```
##### In command line
```bash 
flake8 main.py bruteforce.py optimized.py