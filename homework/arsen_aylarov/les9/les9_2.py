import datetime

data = 'Jan 15, 2023 - 12:05:33'
pithon_time = datetime.datetime.strptime(data, '%b %d, %Y - %H:%M:%S')
human_time = pithon_time.strftime('%B %d, %Y - %H:%M:%S')
data_data = pithon_time.strftime('%d.%m.%y, %H:%M')
print(data_data)
print(human_time)
