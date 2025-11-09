def time_string(hours,minutes,time_format):
    hours=str(hours)
    minutes=str(minutes)
    if len(hours)<2:
        hours='0'+hours
    if len(minutes)<2:
        minutes='0'+minutes
    if time_format=='24':
        time=hours+':'+str(minutes)
    elif time_format=='12':
        if int(hours)>12:
            time=str(int(hours)-12)+':'+str(minutes)+'p.m.'
        else:
            time=str(hours)+':'+str(minutes)+'a.m.'
    return time