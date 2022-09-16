from .analyzer import InsidersecswiftAnalyzer
from .issues_data import issues_data

analyzers = {
    'insidersecswift':
        {
            'name': 'insidersecswift',
            'title': 'insidersecswift',
            'class': InsidersecswiftAnalyzer,
            'language': 'all',
            'issues_data': issues_data,
        },
}
