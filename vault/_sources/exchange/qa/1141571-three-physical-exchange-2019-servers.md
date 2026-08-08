---
title: "Three physical Exchange 2019 servers."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1141571/three-physical-exchange-2019-servers
question_id: 1141571
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Three physical Exchange 2019 servers.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1141571/three-physical-exchange-2019-servers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everybody!    

There are three physical DELL PowerEdge R740xd servers, with the following configuration:    

2x Intel Xeon Silver 4215R (8C 11M X 3.20 GHz).    

128GB (4x32GB) DDR4 ECC REG.    

2x SSD Micron 5300PRO 480GB SATA for Windows Server 2022.    

22x HDD SEAGATE 1.2TB SAS 10k.    

DELL PERC H730p RAID controller (2GB+BBU) SAS/SATA.    

iDRAC9 Enterprise.    

4 1Gb/s Ethernet ports.    

2 10Gb/s Ethernet ports.    

2xBP 750W.    

2U Rack.    

These servers are physical, without virtualization, to which MS Exchange 2019 Enterprise CU12 is planned to migrate. All three servers will be combined into a DAG with three copies of databases (one active and two passive).    

The scaling conditions provide for up to 3000 mailboxes from the following calculation: A mailbox quota of up to 4 gigabytes, 100 mailboxes per base.    

Colleagues, please tell me which configuration would be preferable to choose based on reliability, performance and recovery time (RTO), in case of database or server failure?    

The Veeam B&R backup system used.    

I see three possible options so far:    

-  Use each disk in its own RAID0 group and the same 22 groups, without an additional RAID array. Based on the calculation, one physical disk is one database.    

-  Combine all 22 disks for the database into RAID6 and create as many logical disks on its basis as necessary for the database in the DAG to accommodate a maximum of 3000 mailboxes.    

-  Put a hypervisor on each of the servers (without HA), make one local datastor based on RAID6 and provide the VM with as many virtual disks as necessary for databases in the DAG.    

I assume the pros, cons and risks when choosing one of the three options (can you add something):    

Option 1:    

Cons:    

In case of failure of a physical disk in its RAID0 group, it will cause the database to fail in the DAG. Although a copy of the database will be activated on another server, it will still take time to restore the database from backup, or using the ESEUtil utility.    

It is possible that in the event of a disk departure from an active database, some emails may be “lost" in the process of moving the database to another server.    

There is no way to increase the number of databases to reduce their volume and the capacity of mailboxes in each database, since (One disk is one database).    

Positive:    

High performance of the disk subsystem depending on the cache of the Raid controller.    

Option 2:    

Pros:    

Protects up to two physical disks from failure, but the database remains in operation and does not depend on the failure of the physical disk. It is enough to replace the disk with a cold backup.    

The ability to manage the number of databases, reduce their volume and the capacity of mailboxes in each database.    

Availability of free disk space, in case of logical database recovery.    

Minuses:    

The performance of the disk subsystem is slightly lower, but taking into account the controller cache, the speed of rotation of the spindles and recommendations from the vendor (based on an average of 5 to 10 thousand mailboxes), a possible performance reduction does not affect end customers.    

Option 3:    

Pros:    

Server virtualization is independent of the hardware configuration, which allows, in case of an emergency, to migrate the VM to any virtualization host, or to the existing SAN architecture.    

Backup allows you to restore the entire VM with the mail system and database if the guest system awareness mode is supported using an agent.    

Protects up to two physical disks from failure, but the database remains in operation and does not depend on the failure of the physical disk. It is enough to replace the disk with a cold backup.    

The ability to manage the number of databases, reduce their volume and the capacity of mailboxes in each database.    

Availability of free disk space, in case of logical database recovery.    

Minuses:    

Additional virtualization layer and additional software configuration.    

Availability of a hypervisor license in case of backup by a Veeam agent in the VM.    

Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-26*

I would use the Exchange calculator to determine disk sizes, but if 600 GB is needed then make sure you have more than that for an extra space if necessary - if you can expand later, even better    

https://www.microsoft.com/en-us/download/details.aspx?id=102123

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-26*

Okay, then the last clarifying question, if I may:    

Tell me, if the volume of disks on a physical server is 1.2 Tb, and only 600 GB needs to be allocated for the Exchange database, then the partition itself can be formatted equal to the volume of the disk, but the size of the database will be according to its actual content?    

Or is it necessary to format a partition on a disk equal to 600 GB?    

It's easier in the VM, I've allocated as much as I need for the virtual disk there.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-25*

Nope! its the same with 2016 and 2019 as well    

https://learn.microsoft.com/en-us/powershell/module/exchange/update-mailboxdatabasecopy?view=exchange-ps

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-25*

Has this procedure not changed for the Exchange 2019 version? how-to-reseed-a-failed-database-copy-in-exchange-server-2013

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-25*

I would go with option 1:    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deployment-ref/storage-configuration?view=exchserver-2019    

" Although a copy of the database will be activated on another server, it will still take time to restore the database from backup, or using the ESEUtil utility."    

Not sure what you mean by this. You should never need to restore a database from backup with 3 copies ( you would simply reseed from an active database) nor is there any reason to use eseutil.
