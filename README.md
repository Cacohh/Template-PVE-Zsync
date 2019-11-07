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

The discovery item in the template receive a argument, that can be 4.0 or 4.2 (For >= 4.2. Default 4.2). Adjust accordly with your zabbix server version. 
The NextRun and PreviousRun item is disabled for default. Active if you want to. 

## Built With

* [Zabbix 4.2](https://www.zabbix.com/documentation/4.2/manual) - The IT monitoring tool 
* [Python 3](https://www.python.org/) - A nice language to programming

## Authors

* **Caio Jorge** - *Initial work* - [Cacohh](https://github.com/Cacohh/)
