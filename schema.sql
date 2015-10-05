CREATE TABLE train (
    train_no VARCHAR(10) PRIMARY KEY,
    station_train_code VARCHAR(10),
    start_station_telecode VARCHAR(10),
    start_station_name VARCHAR(10),
    end_station_telecode VARCHAR(10),
    end_station_name VARCHAR(10),
    from_station_telecode VARCHAR(10),
    from_station_name VARCHAR(10),
    to_station_telecode VARCHAR(10),
    to_station_name VARCHAR(10),
    start_time VARCHAR(10),
    arrive_time VARCHAR(10),
    day_difference VARCHAR(10),
    lishi VARCHAR(10),
    lishiValue VARCHAR(10),
    from_station_no VARCHAR(10),
    to_station_no VARCHAR(10),
    sale_time VARCHAR(10)
)