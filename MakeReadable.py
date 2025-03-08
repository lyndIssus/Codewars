def make_readable(seconds):

    return f"{seconds//3600:02}:{(seconds - (seconds//3600*3600))//60:02}:{seconds - seconds//3600*3600 - (seconds - seconds//3600*3600)//60*60:02}"

print(make_readable(3599))