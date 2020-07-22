# PAPA - Pega Alerts Python Analyzer
Pega Alert logs analyzer written in Python 

## How to
1. Create folder `alerts` on the same level as `papa.py`
2. Put Pega Alert files with `.log` extension in this folder
3. Run `papa.py`
4. See files
    1. `sql-report.html` - SQL queries statistics based on `PEGA0005` alerts
    2. `service-report.html` - services statistics based on `PEGA0011` alerts
    99. to be...
    
You can also use `index.html` to access reports

You can pass concrete file name as command line arguments
```bash
python papa.py folder/PegaRULES-ALERT_1.log PegaRULES-ALERT_2.log
``` 
Then report will be generated with passe files

## Reports contents
### SQL report
- Top 10 executions
- Top 10 total time
- Top 10 average time
- Top 10 median time
- Top 10 max time
- Top 10 min time
- Full list
- Full detailed list

### Service report
- Top 10 executions
- Top 10 total time
- Top 10 average time
- Top 10 median time
- Top 10 max time
- Top 10 min time
- Full list
- Full detailed list
