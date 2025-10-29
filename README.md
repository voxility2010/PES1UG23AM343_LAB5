# PES1UG23AM343_LAB5 

## Files
1. `inventory_system.py` – original file  
2. `clean_inventory_system.py` – cleaned file  
3. `pylint_report.txt`  
4. `bandit_report.txt`  
5. `flake8_report.txt`  
6. `README.md`

## Run commands
```bash
pip install pylint bandit flake8
pylint clean_inventory_system.py > pylint_report.txt
bandit -r clean_inventory_system.py -f text -o bandit_report.txt
flake8 clean_inventory_system.py > flake8_report.txt
