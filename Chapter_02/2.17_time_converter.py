# get number of seconds from user
total_seconds = float(input('Enter number of seconds: '))

# get number of hours
hours = total_seconds // 3600

# get the number of minutes remaining
minutes = (total_seconds // 60) % 60

# get the number of seconds remaining
seconds = total_seconds % 60

# show results
print('Here is the time in hours, minutes and seconds:')
print('Hours:', hours)
print('Minutes', minutes)
print('Seconds', seconds)