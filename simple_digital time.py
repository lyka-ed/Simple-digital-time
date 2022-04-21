import time

while True:
    local_digital_time = time.localtime()
    output = time.strftime("%I:%M:%S", local_digital_time)
    #passed in directives to rep time format as hh:mm:ss

    print(output)
    time.sleep(1)