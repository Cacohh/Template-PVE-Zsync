# Function to access crontab file
def accessCrontab(filePath):
    from crontab import CronTab
    fileCron = CronTab(tabfile=filePath)
    return fileCron


# Function to obtain replication state for specific job
def pvezsyncJobState(job):
    import subprocess
    command = str("l=$(pve-zsync list | grep " + str(
        job) + " | tr -s ' ' ',' | cut -d, -f 3 ); if [ $l == 'ok' ]; then echo 0; elif [ $l == 'syncing' ]; then echo 1; elif [ $l == 'stopped' ]; then echo 2; elif [ $l == 'error' ]; then echo 3; elif [ $l == 'waiting' ]; then echo 4;  else echo 5; fi;")
    data = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    stdout, stderr = data.communicate()
    return stdout.decode('utf-8')


# Function that return the date of the next run from a job in crontab file
def pvezsyncNextRun(crontabSystem, commandoJob):
    import re
    import datetime
    for job in crontabSystem:
        x = re.findall(commandoJob, str(job))
        if x:
            sch = job.schedule(date_from=datetime.datetime.now())
            return sch.get_next()


# Function that return the date of the previous run from a job in crontab file
def pvezsyncPreviousRun(crontabSystem, commandoJob):
    import re
    import datetime
    for job in crontabSystem:
        x = re.findall(commandoJob, str(job))
        if x:
            sch = job.schedule(date_from=datetime.datetime.now())
            return sch.get_prev()


def pvezsyncDescriptor(crontabSystem, commandoJob):
    import re
    for job in crontabSystem:
        x = re.findall(commandoJob, str(job))
        if x:
            return job.description(use_24hour_time_format=True)


def pvezsyncMaxSnap(crontabSystem, commandoJob):
    import re
    for job in crontabSystem:
        jobStr = str(job)
        x = re.findall(commandoJob, jobStr)
        if x:
            jobList = jobStr.split()
            index = jobList.index("--maxsnap")
            return jobList[index + 1]


if __name__ == '__main__':
    # Imports
    import sys
    # Define location of crontab file of PVE-Zsync (Default: '/etc/cron.d/pve-zsync')
    file = '/etc/cron.d/pve-zsync'
    # Decide which function to use and pass arguments from cli
    if sys.argv[1] == "pvezsyncJobState":
        print(pvezsyncJobState(sys.argv[2]))
    elif sys.argv[1] == "pvezsyncNextRun":
        print(pvezsyncNextRun(accessCrontab(file), sys.argv[2]))
    elif sys.argv[1] == "pvezsyncPreviousRun":
        print(pvezsyncPreviousRun(accessCrontab(file), sys.argv[2]))
    elif sys.argv[1] == "pvezsyncDescriptor":
        print(pvezsyncDescriptor(accessCrontab(file), sys.argv[2]))
    elif sys.argv[1] == "pvezsyncMaxSnap":
        print(pvezsyncMaxSnap(accessCrontab(file), sys.argv[2]))
    else:
        print("Wrong arguments!!! Check your configuration and documentation if necessary!!!")
