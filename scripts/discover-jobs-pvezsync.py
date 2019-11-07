def discover_pve_zsync_jobsV4_0():
    import subprocess
    import json

    # Execute commands in bash and store output
    command = str("pve-zsync list | tr -s ' ' ',' | tr '\\n' ';' ")
    data = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    stdout, stderr = data.communicate()
    stdout = stdout.decode('utf-8')

    # Organize data in an array
    stdoutArrayAll = stdout.split(";")

    # Construct a Array of Dictionaries from it
    stdoutArrayDic = []

    count = len(stdoutArrayAll)
    for x in range(0, count):
        # Extracting values, putting in single arrays and cleaning values
        stdoutArraySingle = stdoutArrayAll[x].split(",")
        del stdoutArraySingle[-1]
        if stdoutArraySingle:
            # Mount Dictionary and Add Dictionary in list
            stdoutArrayDic.append({"{#SOURCE}": stdoutArraySingle[0], "{#NAME}": stdoutArraySingle[1], "{#STATE}": stdoutArraySingle[2], "{#LASTSYNC}": stdoutArraySingle[3], "{#TYPE}": stdoutArraySingle[4], "{#CON}": stdoutArraySingle[5]})
    del stdoutArrayDic[0]

    # Return Dic with Arrays of Dicts values
    dictArray = {"data": stdoutArrayDic}
    stringDict = json.dumps(dictArray)
    return stringDict


def discover_pve_zsync_jobsV4_2():
    import subprocess
    import json

    # Execute commands in bash and store output
    command = str("pve-zsync list | tr -s ' ' ',' | tr '\\n' ';' ")
    data = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    stdout, stderr = data.communicate()
    stdout = stdout.decode('utf-8')

    # Organize data in an array
    stdoutArrayAll = stdout.split(";")

    # Construct a Array of Dictionaries from it
    stdoutArrayDic = []

    count = len(stdoutArrayAll)
    for x in range(0, count):
        # Extracting values, putting in single arrays and cleaning values
        stdoutArraySingle = stdoutArrayAll[x].split(",")
        del stdoutArraySingle[-1]
        if stdoutArraySingle:
            # Mount Dictionary and Add Dictionary in list
            stdoutArrayDic.append({"{#SOURCE}": stdoutArraySingle[0], "{#NAME}": stdoutArraySingle[1], "{#STATE}": stdoutArraySingle[2], "{#LASTSYNC}": stdoutArraySingle[3], "{#TYPE}": stdoutArraySingle[4], "{#CON}": stdoutArraySingle[5]})
    del stdoutArrayDic[0]

    # Return Dic with Arrays of Dicts values
    arrayJSON = json.dumps(stdoutArrayDic)
    return arrayJSON
    # return '{' + json.dumps(stdoutArrayDic) + '}'

# Execute if standalone program
if __name__ == '__main__':
    import sys
    argsLen = len(sys.argv)
    if argsLen < 2:
        print("Missing parameter")
    elif argsLen > 2:
        print("Too many parameters")
    else:
        args = sys.argv[1]
        if sys.argv[1] == "4.2":
            print(discover_pve_zsync_jobsV4_2())
        elif sys.argv[1] == "4.0":
            print(discover_pve_zsync_jobsV4_0())
        else:
            print("Invalid parameter")







