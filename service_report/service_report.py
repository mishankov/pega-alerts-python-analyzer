from .html_templates import *


def generate_service_report(file_names):
    from statistics import median

    result_file_name = 'service-report.html'
    print('Generating service report from files {}'.format(file_names))

    service_report = []
    for file_name in file_names:
        f = open(file_name, 'r', encoding='utf-8')
        alerts = f.read().split('\n')
        f.close()

        for alert in alerts:
            parsed_alert = alert.split('*')
            if len(parsed_alert) > 1 and parsed_alert[2] == 'PEGA0011':
                service_report.append(
                    {
                        'time': parsed_alert[0],
                        'elapsed_seconds': int(parsed_alert[3]) / 1000,
                        'service': parsed_alert[21],
                        'user': parsed_alert[9],
                        'raw_alert': alert,
                        'file_name': file_name
                    }
                )

    service_report = sorted(service_report, key=lambda i: i['time'], reverse=False)

    service_dict = {}
    service_id = 0
    for service in service_report:
        if service['service'] in service_dict.keys():
            service_dict[service['service']]['executions'].append(service['elapsed_seconds'])
            service_dict[service['service']]['obj'].append(service)
        else:
            service_dict[service['service']] = {'id': service_id, 'executions': [service['elapsed_seconds']],
                                                'obj': [service]}
            service_id += 1

    service_main_values = []
    for key, value in service_dict.items():
        e = value['executions']
        service_main_values.append({
            'id': value['id'],
            'name': key,
            'executions': len(e),
            'total_time': round(sum(e), 3),
            'average_time': round(sum(e) / len(e), 3),
            'median_time': round(median(e), 3),
            'max_time': max(e),
            'min_time': min(e)
        })

    main_info_str = ''
    detail_list_str = ''
    for key, value in service_dict.items():
        e = value['executions']
        main_info_str += MAIN_INFO_TEMPLATE.format(value['id'], key, len(e), round(sum(e), 3),
                                                   round(sum(e) / len(e), 3), round(median(e), 3),
                                                   max(e), min(e))

        detail_list = ''
        for service in sorted(value['obj'], key=lambda i: i['time']):
            detail_list += DETAIL_LIST_TEMPLATE.format(service['elapsed_seconds'], service['time'], service['user'],
                                                       service['file_name'])
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
    for service in sorted(service_main_values, key=lambda i: i['executions'], reverse=True)[:10]:
        top_10_executions_str += MAIN_INFO_TEMPLATE.format(service['id'], service['name'], service['executions'],
                                                           service['total_time'],
                                                           service['average_time'], service['median_time'],
                                                           service['max_time'], service['min_time'])

    top_10_total_time_str = ''
    for service in sorted(service_main_values, key=lambda i: i['total_time'], reverse=True)[:10]:
        top_10_total_time_str += MAIN_INFO_TEMPLATE.format(service['id'], service['name'], service['executions'],
                                                           service['total_time'],
                                                           service['average_time'], service['median_time'],
                                                           service['max_time'], service['min_time'])

    top_10_average_time_str = ''
    for service in sorted(service_main_values, key=lambda i: i['average_time'], reverse=True)[:10]:
        top_10_average_time_str += MAIN_INFO_TEMPLATE.format(service['id'], service['name'], service['executions'],
                                                             service['total_time'],
                                                             service['average_time'], service['median_time'],
                                                             service['max_time'], service['min_time'])

    top_10_median_time_str = ''
    for service in sorted(service_main_values, key=lambda i: i['median_time'], reverse=True)[:10]:
        top_10_median_time_str += MAIN_INFO_TEMPLATE.format(service['id'], service['name'], service['executions'],
                                                            service['total_time'],
                                                            service['average_time'], service['median_time'],
                                                            service['max_time'], service['min_time'])

    top_10_max_time_str = ''
    for service in sorted(service_main_values, key=lambda i: i['max_time'], reverse=True)[:10]:
        top_10_max_time_str += MAIN_INFO_TEMPLATE.format(service['id'], service['name'], service['executions'],
                                                         service['total_time'],
                                                         service['average_time'], service['median_time'],
                                                         service['max_time'], service['min_time'])

    top_10_min_time_str = ''
    for service in sorted(service_main_values, key=lambda i: i['min_time'], reverse=True)[:10]:
        top_10_min_time_str += MAIN_INFO_TEMPLATE.format(service['id'], service['name'], service['executions'],
                                                         service['total_time'],
                                                         service['average_time'], service['median_time'],
                                                         service['max_time'], service['min_time'])

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

    generate_service_report(file_names)
