import datetime

data = {
    'Bitcoin': {
        '2013-12-27': {
            'class': 'SELL',
            'open': '763.28',
            'close': '735.07',
            'high': '777.51',
            'low': '713.6',
            'volume': '46862700',
            'market': '8955394564',
        },
        '2013-12-28': {
            'class': 'STAY',
            'open': '737.98',
            'close': '727.83',
            'high': '747.06',
            'low': '705.35',
            'volume': '32505800',
            'market': '8869918644',
        }
    }
}

for date in data:
    current_date = datetime.date(*map(int, date.split('-')))
    print(current_date)
    print(current_date-datetime.timedelta(1))

