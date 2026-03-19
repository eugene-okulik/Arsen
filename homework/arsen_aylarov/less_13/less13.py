import os
import re
import datetime


fail_path = os.path.dirname(os.path.abspath(__file__))
up_path = os.path.join(fail_path, '..', '..')
file_path = os.path.normpath(os.path.join(up_path, 'eugene_okulik', 'hw_13', 'data.txt'))
nwe_file_path = os.path.normpath(os.path.join(up_path, 'eugene_okulik', 'hw_13', 'data2.txt'))


def riad_file():
    with open(file_path, 'r') as data_file:
        for line in data_file:
            mach = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}', line)
            if mach:
                data_str = mach.group(0)
                date_object = datetime.datetime.strptime(data_str.strip(),"%Y-%m-%d %H:%M:%S.%f")
                yield date_object, line

with open('data2.txt', 'a') as nwe_file:
    for i, (data_line, original_text) in enumerate(riad_file(), start=1):
        if i == 1:
            result = data_line + datetime.timedelta(days=7)
            nwe_file.write(f"{data_line}: {result}\n")
        elif i == 2:
            result = data_line.strftime('%A')  # День недели
            nwe_file.write(f"{data_line}: {result}\n")
        elif i == 3:
            result = (datetime.datetime.now() - data_line).days
            nwe_file.write(f"{data_line}: {result}\n")
    clean_line = data_line.strftime("%Y-%m-%d %H:%M:%S.%f")
    nwe_file.write(clean_line + "\n")