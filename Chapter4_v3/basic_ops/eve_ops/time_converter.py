import datetime

def time_converter(yyyydoy,sod_time):
    '''
    Mainly for EVE level 2
    Parameters
    ----------
    yyyydoy : int
        Year and day of year in format YYYYDOY.
    sod_time : int
        Seconds of day.

    Returns
    -------
    date : datetime.datetime
        Datetime object.

    '''
    year = int(str(yyyydoy)[:4])
    day_of_year = int(str(yyyydoy)[4:])
    delta = datetime.timedelta(days=day_of_year - 1)
    date = datetime.datetime(year, 1, 1) + delta
    
    sod_time=int(sod_time)
    date += datetime.timedelta(seconds=sod_time)
    return date