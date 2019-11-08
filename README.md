# Template PVE Zsync

Template for monitoring replications jobs perfomaded by PVE Zsync tool in PVE. The project uses python 3 scripts and works starting with Zabbix Server 4.0. A modification
in discovery rule is needed to worker with versions newer than 4.2.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to run the scripts and how to install them using pip3. (Consulte the documentation of your system to install pip3 if you haven't)

```
pip3 install python-crontab
pip3 install croniter
pip3 install cron-descriptor
```
### Installing

Clone the repositorie to your machine, and enter in it. And after that, create a scripts folder in your zabbix-agent configuration folder. (Default: /etc/zabbix/)

```
mkdir /etc/zabbix/scripts
```

Then, copy the scripts to te folder.

```
cp ./Template-PVE-Zsync/scripts/* /etc/zabbix/scripts
```
Copy the userparameter file to the zabbix_agentd.d folder.

```
cp ./Template-PVE-Zsync/userparameter_pve_zsync.conf /etc/zabbix/zabbix_agentd.d/
```
Restart the zabbix-agent in your system. (The example below is made with Proxmox 6.x)

```
/etc/init.d/zabbix-agent restart
```

After that, import the template file "template_pve_zsync.xml" in your zabbix server frontend, and see your recent data coming.

## Details about Deployment

This project was developed and tested in Proxmox 6.0-4 and pve-zsync: 2.0-1.

The discovery item in the template receive a argument, that can be 4.0 or 4.2 (For >= 4.2. Default 4.2). Adjust accordly with your zabbix server version. 
The NextRun and PreviousRun item is disabled for default. Active if you want to. 

The Zabbix template has 5 items. Details about below:

* pvezsync.Jobstate[] - Return the state of replications tasks discovered. Receive a argument (4.0 or 4.2) to return the right data structure to Zabbix server. If you use => 4.2 use 4.2.
* pvezsync.NextRun[] - Return the date of the next run scheduled for the replication task.

* pvezsync.PreviousRun[] - Return the date of the previous run scheduled for the replication task.
* pvezsync.JobMaxSnap[] - Return the value of the maxsnap argument for the replication task.


## Built With

* [Pve-zsync: 2.0-1](https://pve.proxmox.com/wiki/PVE-zsync) - The ZFS replication tool from Proxmox
* [Zabbix 4.2](https://www.zabbix.com/documentation/4.2/manual) - The IT monitoring tool 
* [Python 3](https://www.python.org/) - A nice language to programming

## Authors

* **Caio Jorge** -  [Cacohh](https://github.com/Cacohh/)
