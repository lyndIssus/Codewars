def format_duration(seconds):
    if(seconds == 0):
        return 'now'
    times = ['years','days','hours','minutes','seconds']
    divisions = [31536000, 86400, 3600 , 60, 1]
    results = []
    reduce = seconds
    for i in divisions:
        results.append(reduce//i)
        reduce-=reduce//i*i
    readable =''
    for i in range(len(times)):
        if(results[i] == 0):
            pass
        elif results[i] == 1:
            readable+= '1 ' + times[i][0:len(times[i])-1] +', '
        else:
            readable+= str(results[i]) + ' ' + times[i] +', '
    return ' and'.join(readable[:-2].rsplit(',',1))

