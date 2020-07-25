HTML_STYLE = '''
<style>
    table {{
        border-collapse: collapse;
        margin: 10px;
    }}
    table, th, td {{
        border-bottom: 1px solid #ddd;
    }}
    th, td {{
        padding: 5px;
    }}
    th {{
        background-color: #0f0047;
        color: white;
        position: -webkit-sticky;
        position: sticky;
        top: 0;
        z-index: 2;
    }}
    tr:nth-child(even) {{
        background-color: #f2f2f2;
    }}
    tr:hover {{
        background-color: #ddd;
    }}
</style>
'''