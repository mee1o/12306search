import web

db = web.database(dbn='sqlite', db='train.sqlite3')

def save_info(train):
    try:
        db.insert('train', 
        train_no=train['train_no'],
        station_train_code=train['station_train_code'],
        start_station_telecode=train['start_station_telecode'],
        start_station_name=train['start_station_name'],
        end_station_telecode=train['end_station_telecode'],
        end_station_name=train['end_station_name'],
        from_station_telecode=train['from_station_telecode'],
        from_station_name=train['from_station_name'],
        to_station_telecode=train['to_station_telecode'],
        to_station_name=train['to_station_name'],
        start_time=train['start_time'],
        from_station_no=train['from_station_no'],
        to_station_no=train['to_station_no'],
        sale_time=train['sale_time']
        )
    except:
        print 'Already has this train: %s' % train['station_train_code']
            
def get_info(train_no):
    train = db.select('train', where='station_train_code="%s"' % train_no)
    return train