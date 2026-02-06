# macro_data_reports
Script  for processing csv files and generating reports based on the results of processing

## Install
1) Clone repository
```
git clone git@github.com:KlimovArtem/macro_data_reports.git
```
2) Go into repo directory
3) Create virtuale env and activate it
```
# for macos and linux
python -m venv venv %% source venv/bin/activate

# for windows
python -m venv venv %% source venv/Scripts/activate
```
4) Instal requirement dependensies
```
pip istall -e .
```

5) Run script with the following parametrs:
- -f (--files) - list of paths to files for analys
- -r (--report) - type of report

Now avalible following repors:
- average-gdb - generate report on average GDP by country;
```
python src/macrodata_reports/main.py -f economic1.csv economic2.csv -r average-gdp
```
