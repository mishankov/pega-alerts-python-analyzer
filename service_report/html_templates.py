import common_html

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pega Alerts Service Report</title>
</head>
<body>''' + common_html.HTML_STYLE + '''
<a name='top'>
<h1>Pega Alerts Service Report</h1>
<h2>Content</h2>
<ul>
    <li><a href='#top-10-executions'>Top 10 executions</a></li>
    <li><a href='#top-10-total-time'>Top 10 total time</a></li>
    <li><a href='#top-10-average-time'>Top 10 average time</a></li>
    <li><a href='#top-10-median-time'>Top 10 median time</a></li>
    <li><a href='#top-10-max-time'>Top 10 max time</a></li>
    <li><a href='#top-10-min-time'>Top 10 min time</a></li>
    <li><a href='#full-list'>Full list</a></li>
    <li><a href='#full-detailed-list'>Full detailed list</a></li>
</ul>
<a name='top-10-executions'>
<h2>Top 10 executions</h2>
<table>
    <thead>
        <tr>
            <th>Id</th>
            <th>Executions</th>
            <th>Total time</th>
            <th>Average time</th>
            <th>Median time</th>
            <th>Max time</th>
            <th>Min time</th>
        </tr>
    </thead>
    <tbody>
        {top_10_executions}
    </tbody>
</table>
<a href='#top'>Top</a>
<a name='top-10-total-time'>
<h2>Top 10 total time</h2>
<table>
    <thead>
        <tr>
            <th>Id</th>
            <th>Executions</th>
            <th>Total time</th>
            <th>Average time</th>
            <th>Median time</th>
            <th>Max time</th>
            <th>Min time</th>
        </tr>
    </thead>
    <tbody>
        {top_10_total_time}
    </tbody>
</table>
<a href='#top'>Top</a>
<a name='top-10-average-time'>
<h2>Top 10 average time</h2>
<table>
    <thead>
        <tr>
            <th>Id</th>
            <th>Executions</th>
            <th>Total time</th>
            <th>Average time</th>
            <th>Median time</th>
            <th>Max time</th>
            <th>Min time</th>
        </tr>
    </thead>
    <tbody>
        {top_10_average_time}
    </tbody>
</table>
<a href='#top'>Top</a>
<a name='top-10-median-time'>
<h2>Top 10 median time</h2>
<table>
    <thead>
        <tr>
            <th>Id</th>
            <th>Executions</th>
            <th>Total time</th>
            <th>Average time</th>
            <th>Median time</th>
            <th>Max time</th>
            <th>Min time</th>
        </tr>
    </thead>
    <tbody>
        {top_10_median_time}
    </tbody>
</table>
<a href='#top'>Top</a>
<a name='top-10-max-time'>
<h2>Top 10 max time</h2>
<table>
    <thead>
        <tr>
            <th>Id</th>
            <th>Executions</th>
            <th>Total time</th>
            <th>Average time</th>
            <th>Median time</th>
            <th>Max time</th>
            <th>Min time</th>
        </tr>
    </thead>
    <tbody>
        {top_10_max_time}
    </tbody>
</table>
<a href='#top'>Top</a>
<a name='top-10-min-time'>
<h2>Top 10 min time</h2>
<table>
    <thead>
        <tr>
            <th>Id</th>
            <th>Executions</th>
            <th>Total time</th>
            <th>Average time</th>
            <th>Median time</th>
            <th>Max time</th>
            <th>Min time</th>
        </tr>
    </thead>
    <tbody>
        {top_10_min_time}
    </tbody>
</table>
<a href='#top'>Top</a>
<a name='full-list'>
<h2>Full list</h2>
<table>
    <thead>
        <tr>
            <th>Id</th>
            <th>Executions</th>
            <th>Total time</th>
            <th>Average time</th>
            <th>Median time</th>
            <th>Max time</th>
            <th>Min time</th>
        </tr>
    </thead>
    <tbody>
        {main_info}
    </tbody>
</table>
<a href='#top'>Top</a>
<a name='full-detailed-list'>
<h2>Full detailed list</h2>
{detail_list}
<a href='#top'>Top</a>
</body>
</html>
'''

MAIN_INFO_TEMPLATE = '''
<tr>
    <td><a href='#{}'>{}</a></td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
</tr>
'''

DETAIL_LIST_TEMPLATE = '''
<tr>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
</tr>
'''

STATS_TEMPLATE = '''
<h3><a name='{}'>{}</a></h3>
<h4>Service</h4>
<p class='sql'>{}</p>
<h4>Stats</h4>
<table>
    <thead>
        <tr>
            <th>Executions</th>
            <th>Total time</th>
            <th>Average time</th>
            <th>Median time</th>
            <th>Max time</th>
            <th>Min time</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
    </tbody>
</table>
{}
<a href='#top'>Top</a>
'''

