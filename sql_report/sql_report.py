from .html_templates import *


def generate_sql_report(file_names):
    from statistics import median

    result_file_name = 'sql-report.html'
    print('Generating sql report from files {}'.format(file_names))

    sql_report = []
    for file_name in file_names:
        f = open(file_name, 'r', encoding='utf-8')
        alerts = f.read().split('\n')
        f.close()

        for alert in alerts:
            parsed_alert = alert.split('*')
            if len(parsed_alert) > 1 and parsed_alert[2] == 'PEGA0005':
                alert_message = parsed_alert[-2]
                sql = alert_message.split('SQL: ')[1]

                sql_report.append(
                    {
                        'sql': sql,
                        'elapsed_seconds': int(parsed_alert[3]) / 1000,
                        'time': parsed_alert[0],
                        'user': parsed_alert[9],
                        'raw_alert': alert,
                        'file_name': file_name
                    }
                )

    sql_report = sorted(sql_report, key=lambda i: i['time'], reverse=False)

    sql_dict = {}
    sql_id = 0
    for sql in sql_report:
        if sql['sql'] in sql_dict.keys():
            sql_dict[sql['sql']]['executions'].append(sql['elapsed_seconds'])
            sql_dict[sql['sql']]['obj'].append(sql)
        else:
            sql_dict[sql['sql']] = {'id': sql_id, 'executions': [sql['elapsed_seconds']], 'obj': [sql]}
            sql_id += 1

    sql_main_values = []
    for key, value in sql_dict.items():
        e = value['executions']
        sql_main_values.append({
            'id': value['id'],
            'executions': len(e),
            'total_time': round(sum(e), 3),
            'average_time': round(sum(e) / len(e), 3),
            'median_time': round(median(e), 3),
            'max_time': max(e),
            'min_time': min(e)
        })

    main_info_str = ''
    detail_list_str = ''
    for key, value in sql_dict.items():
        e = value['executions']
        main_info_str += MAIN_INFO_TEMPLATE.format(value['id'], value['id'], len(e), round(sum(e), 3),
                                                   round(sum(e) / len(e), 3), round(median(e), 3),
                                                   max(e), min(e))

        detail_list = ''
        for sql in sorted(value['obj'], key=lambda i: i['time']):
            detail_list += DETAIL_LIST_TEMPLATE.format(sql['elapsed_seconds'], sql['time'], sql['user'],
                                                       sql['file_name'])
        detail_list = '''
            <h4>Executions</h4>
            <table>
                <thead>
                    <tr>
                        <th>Elapsed seconds</th>
                        <th>Time</th>
                        <th>User</th>
                        <th>File name</th>
                    </tr>
                </thead>
                <tbody>
        ''' + detail_list + '''
                </tbody>
            </table>
        '''

        detail_list_str += STATS_TEMPLATE.format(value['id'], value['id'], key, len(e), round(sum(e), 3),
                                                 round(sum(e) / len(e), 3),
                                                 round(median(e), 3), max(e), min(e), detail_list)

    top_10_executions_str = ''
    for sql in sorted(sql_main_values, key=lambda i: i['executions'], reverse=True)[:10]:
        top_10_executions_str += MAIN_INFO_TEMPLATE.format(sql['id'], sql['id'], sql['executions'],
                                                           sql['total_time'],
                                                           sql['average_time'], sql['median_time'],
                                                           sql['max_time'], sql['min_time'])

    top_10_total_time_str = ''
    for sql in sorted(sql_main_values, key=lambda i: i['total_time'], reverse=True)[:10]:
        top_10_total_time_str += MAIN_INFO_TEMPLATE.format(sql['id'], sql['id'], sql['executions'],
                                                           sql['total_time'],
                                                           sql['average_time'], sql['median_time'],
                                                           sql['max_time'], sql['min_time'])

    top_10_average_time_str = ''
    for sql in sorted(sql_main_values, key=lambda i: i['average_time'], reverse=True)[:10]:
        top_10_average_time_str += MAIN_INFO_TEMPLATE.format(sql['id'], sql['id'], sql['executions'],
                                                             sql['total_time'],
                                                             sql['average_time'], sql['median_time'],
                                                             sql['max_time'], sql['min_time'])

    top_10_median_time_str = ''
    for sql in sorted(sql_main_values, key=lambda i: i['median_time'], reverse=True)[:10]:
        top_10_median_time_str += MAIN_INFO_TEMPLATE.format(sql['id'], sql['id'], sql['executions'],
                                                            sql['total_time'],
                                                            sql['average_time'], sql['median_time'],
                                                            sql['max_time'], sql['min_time'])

    top_10_max_time_str = ''
    for sql in sorted(sql_main_values, key=lambda i: i['max_time'], reverse=True)[:10]:
        top_10_max_time_str += MAIN_INFO_TEMPLATE.format(sql['id'], sql['id'], sql['executions'],
                                                         sql['total_time'],
                                                         sql['average_time'], sql['median_time'],
                                                         sql['max_time'], sql['min_time'])

    top_10_min_time_str = ''
    for sql in sorted(sql_main_values, key=lambda i: i['min_time'], reverse=True)[:10]:
        top_10_min_time_str += MAIN_INFO_TEMPLATE.format(sql['id'], sql['id'], sql['executions'],
                                                         sql['total_time'],
                                                         sql['average_time'], sql['median_time'],
                                                         sql['max_time'], sql['min_time'])

    f = open(result_file_name, 'w')
    f.write(HTML_TEMPLATE.format(
        detail_list=detail_list_str,
        main_info=main_info_str,
        top_10_executions=top_10_executions_str,
        top_10_total_time=top_10_total_time_str,
        top_10_average_time=top_10_average_time_str,
        top_10_median_time=top_10_median_time_str,
        top_10_max_time=top_10_max_time_str,
        top_10_min_time=top_10_min_time_str
    ))
    f.close()
    print('Result: {}'.format(result_file_name))


if __name__ == '__main__':
    import sys

    file_names = sys.argv[1:]
    if len(file_names) > 0:
        pass
    else:
        import glob

        file_names = glob.glob('alerts/*.log')

    generate_sql_report(file_names)
