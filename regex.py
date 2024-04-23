import re

def log():
    log = "July 31 07:51 mycomputer bad_process[12345]: ERROR"
    regex = r"\[(\d+)\]"
    result = re.search(regex, log)
    return (result[1])

print (log())
