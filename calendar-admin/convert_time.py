from datetime import datetime


def convert_to_utc(params_time):
    """конвертирует время из таймзоны пользователя в UTC0"""
    params_time = datetime.strptime(params_time, "%Y-%m-%d:%H:%M")
    timezone = datetime.now()-datetime.utcnow()
    params_time -= timezone
    return params_time


def convert_to_utc_day(params_time):
    """конвертирует дату из таймзоны пользователя в UTC0"""
    params_time = datetime.strptime(params_time, "%Y-%m-%d")
    timezone = datetime.now()-datetime.utcnow()
    params_time -= timezone
    return params_time


def convert_from_utc(params_time):
    """конвертирует время из UTC0 в соответствии с таймзоной пользователя"""
    timezone = datetime.now()-datetime.utcnow()
    params_time += timezone
    return params_time

