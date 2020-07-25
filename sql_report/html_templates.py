import common_html

HTML_TEMPLATE = common_html.HTML_TEMPLATE.replace('{%title%}', 'Pega Alerts SQL Report')

MAIN_INFO_TEMPLATE = common_html.MAIN_INFO_TEMPLATE

DETAIL_LIST_TEMPLATE = common_html.DETAIL_LIST_TEMPLATE

STATS_TEMPLATE = common_html.STATS_TEMPLATE.replace('{%h4%}', 'SQL')
