from sql_report import generate_sql_report
from service_report import generate_service_report

if __name__ == '__main__':
    import sys

    file_names = sys.argv[1:]
    if len(file_names) > 0:
        pass
    else:
        import glob

        file_names = glob.glob('alerts/*.log')

    generate_sql_report(file_names)
    generate_service_report(file_names)
