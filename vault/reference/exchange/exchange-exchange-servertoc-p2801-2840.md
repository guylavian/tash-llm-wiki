---
title: "Exchange Server — pages 2801-2840"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2801-2840
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2801-2840
family: exchange
documentKind: "doc"
abstract: "requires at least three locations, as it requires deploying DAG members in two locations and the DAG's witness server in a third location. If you don't have three locations, or even if you do have three locations but you want to control datacenter-level recovery actions, you can"
---

# Exchange Server — pages 2801-2840

<!-- p.2801 -->

requires at least three locations, as it requires deploying DAG members in two locations and the
DAG's witness server in a third location.

If you don't have three locations, or even if you do have three locations but you want to control
datacenter-level recovery actions, you can configure a DAG for manual recovery if a site-level
failure occurs. In that event, you would perform a process called a datacenter switchover. As with
many disaster recovery scenarios, prior planning and preparation for a datacenter switchover can
simplify your recovery process and reduce the duration of your outage. For detailed steps to
performing a datacenter switchover, see Datacenter switchovers

Failovers
A failover is an automatic activation process that can occur at the database, server, or datacenter
level. Failovers occur in response to a failure that affects an individual database (for example, an
isolated storage loss) an entire server (for example, a motherboard failure or a loss of power), or an
entire site (for example, the loss of all DAG members in a site).

DAGs and mailbox database copies provide full redundancy and rapid recovery of both the data
and the services that provide access to the data. The following table lists the expected recovery
actions for various failures. Some failures require the administrator to initiate the recovery, and
other failures are automatically handled by the system.

                                                                                           ﾉ    Expand table

 Description        Automatic        Automatic         State          State     Repair actions     Comments
                    activation       repair action     during         during
                                                       repair:        repair:
                                                       Active         Passive

 Extensible         Possible short   Automatic         Manual         Failed    RAID rebuild,      There may be
 Storage Engine     outage.          patching of bad   switchover,              database and       other soft
 (ESE) soft         Possible         page.             automatic                database copy      database
 database           automatic                          failover, or             repair, restore    failure codes.
 failure: The       failover.                          online                   and run            Doesn't
 drives storing                                        repair.                  recovery then      include NTFS
 the database                                                                   page patching,     file system
 are returning                                                                  or page            block failures.
 errors on some                                                                 patching from      If failover or
 reads (for                                                                     copy.              switchover is
 example, a                                                                                        performed,
 -1018 error).                                                                                     host server is
                                                                                                   updated.

 ESE " semi-soft"   Short outage     Automatic         Dismounted     Failed    RAID rebuild       An ESE semi-
 database           during           volume/disk       if can't be              may solve the      soft write
 failure: The       automatic        rebuilt after     recovered.               problem.           error means
 drives storing     failover.                                                   Copy and           some writes

<!-- p.2802 -->

Description        Automatic      Automatic        State         State     Repair actions    Comments
                   activation     repair action    during        during
                                                   repair:       repair:
                                                   Active        Passive

the database                      possible drive                           repair, restore   are
are returning                     replacement.                             and run           successful.
errors on some                                                             recovery, or      Doesn't
writes.                                                                    volume/disk       include an
                                                                           rebuilt after     NTFS block
                                                                           possible          failure.
                                                                           replacement.

ESE "semi-soft"    Short outage   Automatic        Dismounted    Failed    RAID rebuild      An ESE semi-
log failure: The   during         volume/disk      if can't be             may solve the     soft
drives storing     automatic      rebuilt after    recovered.              problem.          read/write
the log data       failover.      possible drive                           Copy and          error means
are returning                     replacement.                             repair, restore   some
non-recovered                                                              and run           reads/writes
errors on some                                                             recovery, or      are
reads or writes.                                                           volume/disk       successful.
                                                                           rebuilt after     If the
                                                                           possible          database
                                                                           replacement.      fails,
                                                                                             automated
                                                                                             recovery will
                                                                                             occur before
                                                                                             log data
                                                                                             recovery
                                                                                             processing
                                                                                             starts.

ESE software       Short outage   None.            Dismounted    Failed    Fix underlying    This failure
error or           during                          if can't be             resource issue.   could be the
resource           automatic                       recovered.                                surfaced
exhaustion: An     failover.                                                                 error of other
error where                                                                                  cases.
ESE terminates
instance (for
example, Event
ID 1022,
checkpoint
depth too
deep).

NTFS block         Short outage   Volume rebuilt   Dismounted    Failed    RAID rebuild      This situation
failures: The      during         after possible   if can't be             may solve the     is more likely
drives storing     automatic      drive            recovered.              problem. NTFS     to occur
the database       failover.      replacement.                             utilities may     when RAID
or logs                                                                    solve the NTFS    isn't in use. If
experiences a                                                              problems.         this scenario
read or write                                                              Exchange          impacts the

<!-- p.2803 -->

Description        Automatic          Automatic         State         State     Repair actions     Comments
                   activation         repair action     during        during
                                                        repair:       repair:
                                                        Active        Passive

error to an                                                                     recovery may       active log
NTFS control                                                                    be required.       volume,
structure.                                                                                         some recent
                                                                                                   log files will
                                                                                                   be lost.
                                                                                                   Doesn't
                                                                                                   include
                                                                                                   errors
                                                                                                   automatically
                                                                                                   corrected by
                                                                                                   NTFS or its
                                                                                                   underlying
                                                                                                   software or
                                                                                                   hardware
                                                                                                   stack.

Database or        Short outage       Drive             Dismounted    Failed    Drive              Not
log drive          during             reformatted or    if can't be             replacement        applicable.
failure: A drive   automatic          replaced,         recovered.              followed by
storing the        failover.          followed by                               possible RAID
database or                           complete                                  rebuild.
logs has failed                       volume rebuild.                           Drive
and is                                                                          replacement
inaccessible.                                                                   followed by
                                                                                complete
                                                                                volume rebuild.
                                                                                Complete
                                                                                volume rebuild.

Database or        Short outage       Drive             Dismounted    Failed    Drive              Not
log volume         during             reformatted or    if can't be             replacement        applicable.
failure: The       automatic          replaced.         recovered.              followed by
volume fails       failover.                                                    possible RAID
due to NTFS or                                                                  rebuild.
lower level                                                                     Drive
volume issues.                                                                  replacement
                                                                                followed by
                                                                                complete
                                                                                volume rebuild.
                                                                                Complete
                                                                                volume rebuild.

Database or        Automatic          None.             Dismounted.   Failed    Run full or        Not
log volume out     failover if                                                  incremental        applicable.
of space: The      other copy                                                   backups,
NTFS file          isn't in similar                                             manually
system with        state.                                                       delete logs, let

<!-- p.2804 -->

Description       Automatic         Automatic       State         State        Repair actions     Comments
                  activation        repair action   during        during
                                                    repair:       repair:
                                                    Active        Passive

the database                                                                   time pass,
or log files is                                                                resume
out of space.                                                                  database copy,
                                                                               or repair failed
                                                                               database copy.

Administrator     If automatic      None.           Dismounted.   Not          Administrator      Not
dismounts the     failover isn't                                  applicable   corrects the       applicable.
wrong             blocked by                                                   error.
database.         the
                  administrator,
                  there will be a
                  short outage.
                  If automatic
                  failover is
                  prevented,
                  there will be
                  an outage
                  until the
                  database is
                  mounted.

Administrator     Depending on      None.           Not           Suspended    Administrator      Not
suspends the      configuration                     applicable.                corrects the       applicable.
wrong             and impacted                                                 error.
database copy.    copy, auto
                  recovery may
                  be prevented.

Administrator     If automatic      None.           Dismounted.   Not          Administrator      Not
dismounts a       failover isn't                                  applicable   completes the      applicable.
database for      blocked by                                                   task.
storage, NTFS,    the
or volume         administrator,
maintenance.      there will be a
                  short outage.
                  If automatic
                  failover is
                  blocked, there
                  will be an
                  outage until
                  the
                  administrator
                  completes the
                  task.

<!-- p.2805 -->

Description        Automatic         Automatic       State         State       Repair actions   Comments
                   activation        repair action   during        during
                                                     repair:       repair:
                                                     Active        Passive

Administrator      Depending on      None.           Not           Suspended   Administrator    Not
suspends a         configuration                     applicable.               completes the    applicable.
database copy      and impacted                                                actions.
for storage,       copy, auto
NTFS, or           recovery may
volume             be prevented.
maintenance.

Administrator      Outage until      None.           Dismounted.   Suspended   Administrator    Active and
dismounts a        repaired.                                                   completes the    passive
database for                                                                   actions.         database
offline                                                                                         copies are
database                                                                                        diverged.
maintenance.                                                                                    Administrator
                                                                                                must
                                                                                                suspend
                                                                                                copies.

Storage area       Short outage      None.           Dismounted.   Any         Repair           A passive
network (SAN),     during                                                      hardware.        database
disk, or storage   automatic                                                                    copy will be
controller         failover.                                                                    in the state
failure.                                                                                        that existed
                                                                                                at the time
                                                                                                when the
                                                                                                system failed.

Server             Short outage      None.           Dismounted.   Any         Complete         A passive
hardware           during                                                      actions.         database
maintenance.       automatic                                                                    copy will be
                   failover                                                                     in the state
                   (unless                                                                      that existed
                   blocked by an                                                                at the time
                   administrator).                                                              when the
                                                                                                system was
                                                                                                shut down.

Server software    Short outage      None.           Dismounted.   Any         Complete         A passive
maintenance.       during                                                      actions.         database
                   automatic                                                                    copy will be
                   failover                                                                     in the state
                   (unless                                                                      that existed
                   blocked by an                                                                at the time
                   administrator).                                                              when the
                                                                                                system was
                                                                                                shut down.

<!-- p.2806 -->

Description        Automatic        Automatic         State           State        Repair actions    Comments
                   activation       repair action     during          during
                                                      repair:         repair:
                                                      Active          Passive

Microsoft          Short outage     None.             Dismounted.     Any          Restart the       Not
Exchange           during                                                          Microsoft         applicable.
Information        automatic                                                       Exchange
Store service is   failover.                                                       Information
stopped or                                                                         Store service.
paused by an
administrator.

Microsoft          Short outage     Service Control   Dismounted.     Any          Manually or       A passive
Exchange           during           Manager                                        automatically     database
Information        automatic        restarts the                                   restart the       copy will be
Store service      failover.        Microsoft                                      Microsoft         in the state
fails; operating                    Exchange                                       Exchange          that existed
system is still                     Information                                    Information       when the
running.                            Store service.                                 Store service.    Microsoft
                                                                                                     Exchange
                                                                                                     Information
                                                                                                     Store service
                                                                                                     failed.

Partial            Possible short   None.             Mounted         Any, but     Restart server,   Not
Microsoft          outage during                      and partially   may be       operating         applicable.
Exchange           automatic                          functional.     only         system, or
Information        failover.                                          partially    Microsoft
Store service                                                         functional   Exchange
failure; some                                                                      Information
part of the                                                                        Store service.
Exchange store
stops
functioning,
but it's not
identified as
completely
failed.

Server failure:    Short outage     Restart           Dismounted.     Any          Restore power,    Not
The server fails   during           computer.                                      change            applicable.
for one of the     automatic                                                       operating
following          failover.                                                       system
reasons:                                                                           settings,
Complete                                                                           change
power failure                                                                      hardware
Unrecovered                                                                        settings,
failure of the                                                                     replace
processor chip,                                                                    hardware,
motherboard,                                                                       restart
or backplane                                                                       operating

<!-- p.2807 -->

Description       Automatic        Automatic         State         State     Repair actions    Comments
                  activation       repair action     during        during
                                                     repair:       repair:
                                                     Active        Passive

Operating                                                                    system, service
system stop                                                                  operating
error                                                                        system, service
Operating                                                                    hardware, or
system stops                                                                 repair
responding                                                                   communication
Complete                                                                     problems.
communication
failure

DAG               Outage until     None.             Dismounted.   Any       Repair failed     A passive
experiences a     repaired.                                                  quorum, assign    database
quorum failure.                                                              new quorum,       copy will be
                                                                             or restore the    in the state
                                                                             network that's    that existed
                                                                             causing           at the time
                                                                             quorum failure.   when the
                                                                                               system failed.

MAPI network      Short outage     None.             Dismounted.   Any       Fix               Not
communication     during           Communication                             communication     applicable.
failure: The      automatic        continues to be                           problem by
server is no      failover; must   attempted.                                correcting
longer            be lossless.                                               hardware or
available on                                                                 software
the MAPI                                                                     issues.
network.

Replication       Possible short   None.             None.         Any       Fix               Resiliency
network           copying or       Communication                             communication     impacted by
communication     seeding          continues to be                           problem by        failure.
failure: The      outage while     attempted.                                correcting
server can't      the workload                                               hardware or
receive           is switched to                                             software
heartbeats, log   other                                                      issues.
copies, or seed   network.
through the
failed
replication
network.

Multiple          Short outage     None.             Dismounted.   Any       Fix               At least one
network           during           Communication                             communication     network is
communication     automatic        continues to be                           problem by        still
failure: The      failover; must   attempted.                                correcting        functional.
server can't      be lossless.                                               hardware or
receive

<!-- p.2808 -->

Description       Automatic      Automatic       State          State     Repair actions   Comments
                  activation     repair action   during         during
                                                 repair:        repair:
                                                 Active         Passive

heartbeats, log                                                           software
copies, or seed                                                           issues.
through
multiple
networks.

Partial failure   Failure not    None.           Mounted,       Any       Fix              Network
of one or more    detected; no                   but possible             communication    experiences
networks:         action.                        performance              problem by       higher than
Networks                                         issues.                  correcting       normal error
experience                                                                hardware or      rates.
high error                                                                software
rates.                                                                    issues.

Undetected        None.          None.           Any.           Any       Restart or       Hang isn't
operating                                                                 terminate the    detected so
system hang:                                                              resources that   no action is
Operating                                                                 aren't           taken.
system stops                                                              responding.      Some
responding but                                                                             functionality
it's not                                                                                   may be
detected by                                                                                operational.
monitoring or
clustering.

Operating         Short outage   None.           Dismounted.    Any       Replace drive    Not
system drive      during                                                  and rebuild      applicable.
experiences a     automatic                                               server or
failure.          failover.                                               rebuild volume
                                                                          by using RAID.

Operating         Short outage   None.           Dismounted.    Any       Manually free    Not
system drive      during                                                  space on the     applicable.
out of space.     automatic                                               volume.
                  failover.

Drive             Short outage   None.           Dismounted.    Any       Replace drive    Not
containing        during                                                  and reinstall    applicable.
Exchange          automatic                                               application or
binaries          failover.                                               rebuild volume
experiences a                                                             by using RAID.
volume or
drive failure.

<!-- p.2809 -->

 Description         Automatic       Automatic       State         State     Repair actions    Comments
                     activation      repair action   during        during
                                                     repair:       repair:
                                                     Active        Passive

 Drive               Short outage    None.           Dismounted.   Any       Manually free     Not
 containing the      during                                                  space on the      applicable.
 Exchange            automatic                                               volume.
 binaries is out     failover.
 of space.

 Invalid new log     Short outage    None.           Dismounted.   Failed    Remove            The
 detected: The       during                                                  disruptive logs   disruptive
 log sequence is     automatic                                               after             logs
 disrupted by        failover;                                               determining       shouldn't
 an existing file.   assume other                                            source.           replicate.
                     copies don't
                     have the same
                     problem.

 Continuous          Not             Discard log.    Not           Failed    Discard invalid   Not
 replication         applicable.                     applicable.             log; move         applicable.
 detects invalid                                                             impacting log
 log: Replay                                                                 stream.
 detects an
 inappropriate
 log during
 copy or replay.

Database Failovers
A database failover occurs when a database copy that was active is no longer able to remain active.
The following occurrences are part of a database failover:

   1. The database failure is detected by the Microsoft Exchange Information Store service.

   2. The Microsoft Exchange Information Store service writes failure events to the crimson channel
      event log.

   3. The Active Manager on the server that contains the failed database detects the failure events.

   4. The Active Manager requests the database copy status from the other servers that hold a
      copy of the database.

   5. The other servers return the requested database copy status to the requesting Active
      Manager.

   6. The PAM initiates a move of the active database to another server in the DAG using a best
      copy selection algorithm.

<!-- p.2810 -->

   7. The PAM updates the database mount location in the cluster database to refer to the selected
     server.

   8. The PAM sends a request to the Active Manager on the selected server to become the
     database master.

   9. The Active Manager on the selected server requests that the Microsoft Exchange Replication
     service attempt to copy the last logs from the previous server and set the mountable flag for
     the database.

 10. The Microsoft Exchange Replication service copies the logs from the server that previously
     had the active copy of the database.

 11. The Active Manager reads the maximum log generation number from the cluster database.

 12. The Microsoft Exchange Information Store service mounts the new active database copy.

Server Failovers
A server failover occurs when the DAG member is no longer able to service the MAPI network, or
when the Cluster service on a DAG member is no longer able to contact the remaining DAG
members. The following occurrences are part of a server failover:

   1. The Cluster service on the PAM sends a notification to the PAM for one of two conditions:

   2. Node Down: The server is reachable but is unable to participate in DAG operations.

   3. MAPI Network Down: The server can't be contacted over the MAPI network and therefore
     can't participate in DAG operations.

   4. If the server is reachable, the PAM contacts the Active Manager on the affected server and
     requests that all databases be immediately dismounted.

   5. For each affected database copy:

   6. The PAM requests the database copy status from all servers in the DAG.

   7. The PAM receives a response from all reachable and active DAG members.

   8. The PAM tries to determine the best log source among all responding servers by querying the
     most recent log generation number from each of the responders.

   9. Each of the servers responds with the log generation number.

 10. The PAM retrieves the current search index catalog status from the cluster database.

 11. Based on the log generation number and catalog health of each database copy, the PAM
     selects the best copies to activate.

<!-- p.2811 -->

  12. The PAM updates the mounted location of the database in the cluster database.

  13. The PAM initiates database failover by communicating with the Active Manager on one or
      more other servers.

  14. The Active Manager on the selected servers requests that the Microsoft Exchange Replication
      service attempt to copy the last logs from the previous server and set the mountable flag.

  15. When the database is mountable, the Active Manager on the servers mounts the databases.

For more information about Active Manager's best copy selection process, see Active Manager.

Datacenter Failovers
Significant changes have been made since Exchange 2010 regarding site resilience configuration.
With namespace simplification, consolidation of server roles, separation of Client Access services
and DAG recovery (in Exchange Server, the namespace does not need to move with the DAG), and
changes around load balancing, Exchange Server provides site resilience options like the ability to
use a single global namespace. If you have more than two locations in which to deploy messaging
service components, Exchange Server also enables configuration of the messaging service for
automatic failover in response to failures that required manual intervention in previous versions.

Exchange uses fault tolerance built into the namespace through multiple IP addresses, load
balancing, and, if necessary, the ability to take servers in and out of service. Exchange Server makes
it possible to use the clients' ability to cache multiple IP addresses returned from a DNS server in
response to a name resolution request. Clients with the ability to cache multiple IP addresses
(which includes almost all HTTP-based clients in Exchange Server, such as Outlook, Outlook
Anywhere, EAS, EWS, Outlook on the web, EAC, RPS, etc.), all have the ability to use those multiple
IP addresses, and this provides failover on the client side. You can configure DNS to hand multiple
IP addresses to a client during name resolution. The client asks for mail.contoso.com and gets back
two IP addresses, or four IP addresses, for example. However many IP addresses the client gets
back will be used reliably by the client. This makes the client a lot better off because if one of the IP
addresses fails, the client has one or more others to try to connect to. If a client tries one and it
fails, it waits around 20 seconds and then tries the next one in the list. Thus, if you lose connectivity
to your primary Client Access services (CAS) array, and you have a second published IP address for
a second CAS array, recovery for the clients happens automatically (and in about 21 seconds).

Modern HTTP clients (operating systems and Web browsers that are ten years old or less) work with
this redundancy automatically. The HTTP stack can accept multiple IP addresses for an FQDN, and if
the first IP it tries fails hard (for example, cannot connect), it will try the next IP in the list. In a soft
failure (connect lost after session established, due to an intermittent failure in the service where, for
example, a device is dropping packets and needs to be taken out of service), the user might need
to refresh their browser.

<!-- p.2812 -->

With the proper configuration, failover can happen at the client level and clients will be
automatically redirected to a second datacenter where Client Access services is running, and the
servers that are running Client Access services will proxy the communication back to the user's
Mailbox server, which remains unaffected by the outage (because you don't do a switchover).
Instead of working to recover service, the service recovers itself and you can focus on fixing the
core issue (for example, replacing a failed load balancer).

Since you can failover the namespace between datacenters, all that is needed to achieve a
datacenter failover is a mechanism for failover of the Mailbox role across datacenters. To get
automatic failover for the DAG, you simply architect a solution where the DAG is evenly split
between two datacenters, and then place the witness server in a third location so that it can be
arbitrated by DAG members in either datacenter, regardless of the state of the network between
the datacenters that contain the DAG members. The key is that third location is isolated from
network failures that affect the locations containing the DAG members.

If you only have two datacenters and would like to be able to configure automatic failover, you can
utilize Microsoft Azure as your third location. You will need to create an Azure virtual network and
connect it to your two datacenters using a multi-point VPN. You will then be able to place your
witness server on a Microsoft Azure virtual machine. For more information, see Using a Microsoft
Azure VM as a DAG witness server.

<!-- p.2813 -->

Datacenter switchovers
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

In a site resilient configuration, automatic recovery in response to a site-level failure can occur
within a DAG, allowing the messaging system to remain in a functional state. This configuration
requires at least three locations, as it requires deploying DAG members in two locations and
the DAG's witness server in a third location.

If you don't have three locations, or even if you do have three locations but you want to
control datacenter-level recovery actions, you can configure a DAG for manual recovery in the
event of a site-level failure. In that event, you would perform a process called a datacenter
switchover. As with many disaster recovery scenarios, prior planning and preparation for a
datacenter switchover can simplify your recovery process and reduce the duration of your
outage.

There are four basic steps that you complete to perform a datacenter switchover, after making
the initial decision to activate the second datacenter:

   1. Terminate a partially running datacenter: This step involves terminating Exchange
      services in the primary datacenter, if any services are still running. This is particularly
      important for the Mailbox server role because it uses an active/passive high availability
      model. If services in a partially failed datacenter aren't stopped, it's possible for problems
      from the partially failed datacenter to negatively affect the services during a switchover
      back to the primary datacenter.

          ） Important

          If network or Active Directory infrastructure reliability has been compromised as a
          result of the primary datacenter failure, we recommend that all messaging services
          be off until these dependencies are restored to healthy service.

   2. Validate and confirm the prerequisites for the second datacenter: This step can be
      performed in parallel with step 1 because validation of the health of the infrastructure in
      the second datacenter is largely independent of the first datacenter. Each organization
      typically requires its own method for performing this step. For example, you may decide
      to complete this step by reviewing health information collected and filtered by an
      infrastructure monitoring application, or by using a tool that's unique to your
      organization's infrastructure. This is a critical step, because you don't want to activate the
      second datacenter when its infrastructure is unhealthy and unstable.

<!-- p.2814 -->

   3. Activate the Mailbox servers: This step begins the process of activating the second
     datacenter. This step can be performed in parallel with step 4 because the Microsoft
     Exchange services can handle database outages and recover. Activating the Mailbox
     servers involves a process of marking the failed servers from the primary datacenter as
     unavailable followed by activation of the servers in the second datacenter. The activation
     process for Mailbox servers depends on whether the DAG is in database activation
     coordination (DAC) mode. See Datacenter Activation Coordination mode for more
     information.

     If the DAG is in DAC mode, you can use the Exchange site resilience cmdlets to terminate
     a partially failed datacenter (if necessary) and activate the Mailbox servers. For example, in
     DAC mode, this step is performed by using the Stop-DatabaseAvailabilityGroup cmdlet. In
     some cases, the servers must be marked as unavailable twice (once in each datacenter).
     Next, the Restore-DatabaseAvailabilityGroup cmdlet is run to restore the remaining
     members of the database availability group (DAG) in the second datacenter by reducing
     the DAG members to those that are still operational, thereby reestablishing quorum. If the
     DAG isn't in DAC mode, you must use the Windows Failover Cluster tools to activate the
     Mailbox servers. After either process is complete, the database copies that were
     previously passive in the second datacenter can become active and be mounted. At this
     point, Mailbox server recovery is complete.

   4. Activate Client Access services: This involves using the URL mapping information and the
     Domain Name System (DNS) change methodology to perform all required DNS updates.
     The mapping information describes what DNS changes to perform. The amount of time
     required to complete the update depends on the methodology used and the Time to Live
     (TTL) settings on the DNS record (and whether the deployment's infrastructure honors the
     TTL).

Users should start to have access to messaging services sometime after steps 3 and 4 are
completed. Steps 3 and 4 are described in greater detail later in this topic.

Terminating a Partially Failed Datacenter
If any DAG members in the failed datacenter are still running, they should be terminated.

When the Exchange DAG is in DAC mode, you can disable the servers in a failed datacenter
with a single command. This will allow you to mount the databases in another datacenter even
if the DAG doesn't have quorum (more than half the members of the DAG available).

When the DAG is in DAC mode, the specific actions to terminate any surviving DAG members in
the primary datacenter are as follows:

<!-- p.2815 -->

  1. The DAG members in the primary datacenter must be marked as stopped in the primary
     datacenter. Stopped is a state of Active Manager that prevents databases from mounting,
     and Active Manager on each server in the failed datacenter is put into this state by using
     the Stop-DatabaseAvailabilityGroup cmdlet. The ActiveDirectorySite parameter of this
     cmdlet can be used to mark all of the servers in the primary datacenter as stopped with a
     single command. This step may not be possible depending on the failure. This step
     should be taken if the state of the datacenter permits it. The Stop-
     DatabaseAvailabilityGroup cmdlet should be run against all servers in the primary
     datacenter. If the Mailbox server is unavailable but Active Directory is operating in the
     primary datacenter, the Stop-DatabaseAvailabilityGroup command with the
     ConfigurationOnly parameter must be run against all servers in this state in the primary
     datacenter, or the Mailbox server must be turned off. Failure to either turn off the Mailbox
     servers in the failed datacenter or to successfully perform the Stop-
     DatabaseAvailabilityGroup command against the servers will create the potential for
     split-brain syndrome to occur across the two datacenters. You may need to individually
     turn off computers through power management devices to satisfy this requirement.

  2. The second datacenter must now be updated to represent which primary datacenter
     servers are stopped. This is done by running the same Stop-DatabaseAvailabilityGroup
     command with the ConfigurationOnly parameter using the same ActiveDirectorySite
     parameter and specifying the name of the Active Directory site in the failed primary
     datacenter. The purpose of this step is to inform the servers in the second datacenter
     about which mailbox servers are available to use when restoring service.

When the DAG isn't in DAC mode, the specific actions to terminate any surviving DAG
members in the primary datacenter are as follows:

  1. The DAG members in the primary datacenter must be forcibly evicted from the DAG's
     underlying cluster by running the following commands on each member:

       PowerShell

       net stop clussvc

       PowerShell

       cluster <DAGName> node <DAGMemberName> /forcecleanup

  2. The DAG members in the second datacenter must now be restarted and then used to
     complete the eviction process from the second datacenter. Stop the Cluster service on
     each DAG member in the second datacenter by running the following command on each
     member:

<!-- p.2816 -->

       PowerShell

        net stop clussvc

   3. On a DAG member in the second datacenter, force a quorum start of the Cluster service
     by running the following command:

       PowerShell

        net start clussvc /forcequorum

   4. Open the Failover Cluster Management tool and connect to the DAG's underlying cluster.
     Expand the cluster, and then expand Nodes. Right-click each node in the primary
     datacenter, select More Actions, and then select Evict. When you're done evicting the
     DAG members in the primary datacenter, close the Failover Cluster Management tool.

If any Unified Messaging services are in use in the failed datacenter, they must be disabled to
prevent call routing to the failed datacenter. You can disable Unified Messaging services by
using the Disable-UMService cmdlet (for example, Disable-UMService EX1 ). Alternatively, if
you're using a Voice over IP (VoIP) gateway, you can also remove the server entries from the
VoIP gateway, or change the DNS records for the failed servers to point to the IP address of the
servers in the second datacenter if your VoIP gateway is configured to route calls using DNS.

  ７ Note

  Unified Messaging is not available in Exchange 2019

Activating Mailbox Servers
The steps needed to activate Mailbox servers during a datacenter switchover also depend on
whether the DAG is in DAC mode. Before activating the DAG members in the second
datacenter, we recommend that you validate that the infrastructure services in the second
datacenter are ready for messaging service activation.

When the DAG is in DAC mode, the steps to complete activation of the mailbox servers in the
second datacenter are as follows:

   1. The Cluster service must be stopped on each DAG member in the second datacenter. You
     can use the Stop-Service cmdlet to stop the service (for example, Stop-Service ClusSvc ),
     or use net stop clussvc from an elevated command prompt.

<!-- p.2817 -->

   2. The Mailbox servers in the standby datacenter are then activated by using the Restore-
     DatabaseAvailabilityGroup cmdlet. The Active Directory site of the standby datacenter is
     passed to the Restore-DatabaseAvailabilityGroup cmdlet to identify which servers to use
     to restore service and to configure the DAG to use an alternate witness server. If the
     alternate witness server wasn't previously configured, you can configure it by using the
     AlternateWitnessServer and AlternateWitnessDirectory parameters of the Restore-
     DatabaseAvailabilityGroup cmdlet. If this command succeeds, the quorum criteria are
     shrunk to the servers in the standby datacenter. If the number of servers in that
     datacenter is an even number, the DAG will switch to using the alternate witness server as
     identified by the setting on the DAG object.

   3. The databases can now be activated. Depending on the specific configuration used by the
     organization, this may not be automatic. If the servers in the standby datacenter have an
     activation blocked setting, the system won't do an automatic failover from the primary
     datacenter to the standby datacenter of any database. If no failover restrictions are
     present for any of the database copies in the standby datacenter, the system will activate
     copies in the second datacenter assuming they are healthy. If databases are configured
     with an activation blocked setting that requires explicit manual action, there are two
     choices for action:

   4. Clear the setting that blocks activation. This will make the system return to its default
     behavior, which is to activate any available copy.

   5. Leave the setting unchanged and use the Move-ActiveMailboxDatabase cmdlet to
     complete the database activation in the second datacenter. To complete this step using
     the Move-ActiveMailboxDatabase cmdlet when activation blocked is set, you must
     explicitly identify the target of the move.

   6. The last step is to review all error and warning messages from the tasks. Any indicated
     warnings should be followed up and corrected. The task design model for these
     commands is to only fail if they can't achieve the fundamental goal of their design. For
     example, the Restore-DatabaseAvailabilityGroup cmdlet will fail if it can't shrink the
     quorum of the DAG to allow a server in the second datacenter to be restarted for
     servicing without causing a quorum outage. However, each task's output is also used to
     identify the issues that require administrator follow-up. You're strongly encouraged to
     save all task output and review it for follow-up actions.

When the DAG isn't in DAC mode, the steps to complete activation of the mailbox servers in
the second datacenter are as follows:

   1. The quorum must be modified based on the number of DAG members in the second
     datacenter.

<!-- p.2818 -->

   2. If there's an odd number of DAG members, change the DAG quorum model from a Node
     a File Share Majority to a Node Majority quorum by running the following command:

       PowerShell

        cluster <DAGName> /quorum /nodemajority

   3. If there's an even number of DAG members, reconfigure the witness server and directory
     by running the following command in the Exchange Management Shell:

       PowerShell

        Set-DatabaseAvailabilityGroup <DAGName> -WitnessServer <ServerName>

   4. Start the Cluster service on any remaining DAG members in the second datacenter by
     running the following command:

       PowerShell

        net start clussvc

   5. Perform server switchovers to activate the mailbox databases in the DAG by running the
     following command for each DAG member:

       PowerShell

        Move-ActiveMailboxDatabase -Server <DAGMemberinPrimarySite> -ActivateOnServer
        <DAGMemberinSecondSite>

   6. Mount the mailbox databases on each DAG member in the second site by running the
     following command:

       PowerShell

        Get-MailboxDatabase <DAGMemberinSecondSite> | Mount-Database

Activating Client Access services
Clients connect to service endpoints (for example Outlook on the web, Autodiscover, Exchange
ActiveSync, Outlook Anywhere, POP3, IMAP4, and the RPC Client Access services array) to
access Exchange services and data. Therefore, activating Client Access services involves
changing the mapping of the DNS records for these service endpoints from IP addresses in the

<!-- p.2819 -->

primary datacenter to the IP addresses in the second datacenter that are configured as the new
service endpoints. Depending on your DNS configuration, the DNS records that need to be
modified may or may not be in the same DNS zone.

Activating Client Access services
Clients will then automatically connect to the new service endpoints in one of two ways:

        Clients will continue to try to connect, and should automatically connect after the TTL has
        expired for the original DNS entry, and after the entry is expired from the client's DNS
        cache. Users can also run the ipconfig /flushdns command from a command prompt to
        manually clear their DNS cache.

        Clients starting or restarting will perform a DNS lookup on startup and will get the new IP
        address for the service endpoint, which will be an Exchange server running Client Access
        services, or a Client Access services array, in the second datacenter.

Assuming that all appropriate configuration changes have been completed to define and
configure the services in the second datacenter to function as they were in the primary
datacenter, and assuming that the established DNS configuration is correct, no further changes
should be needed to activate Client Access services.

Activating Transport services
Clients and other servers that submit messages typically identify those servers using DNS.
Activating transport services in the second datacenter involves changing DNS records to point
to the IP addresses of the Mailbox servers in the second datacenter. Clients and sending
servers will then automatically connect to the servers in the second datacenter in one of two
ways:

        Clients will continue to try to connect, and should automatically connect after the TTL has
        expired for the original DNS entry, and after the entry is expired from the client's DNS
        cache. Users can also run the ipconfig /flushdns command from a command prompt to
        manually clear their DNS cache.

        Clients starting or restarting will perform a DNS lookup on startup and will get the new IP
        address for the SMTP endpoint, which will be a Mailbox server in the second datacenter.

Assuming that all appropriate configuration changes have been completed to define and
configure the services in the second datacenter to function as they were in the primary
datacenter, and assuming that the established DNS configuration is correct, no further changes
should be needed to activate transport services.

<!-- p.2820 -->

Activating Unified Messaging services in Exchange 2016

  ７ Note

  Unified Messaging is not available in Exchange 2019.

Unified Messaging (UM) services in Exchange 2016 connect to an organization's PBX system
and phone lines. The logical connection between the PBX system and the Unified Messaging
service is provided by an IP gateway. IP gateways include high availability functionality and are
able to switch between multiple Unified Messaging services when a failure is detected.

If there are Unified Messaging services in the second datacenter that were in a disabled state
because they are dedicated to the site resilience solution, they can be enabled by using the
Enable-UMService cmdlet (for example, Enable-UMService EX4 ).

Assuming the IP gateways are associated with Unified Messaging services by using DNS
servers, activating Unified Messaging services therefore involves changing DNS records to
point to the new IP addresses that will be configured for the Unified Messaging service in the
second datacenter. Assuming that all appropriate configuration changes have been completed
to define and configure the services in the second datacenter to function as they were in the
primary datacenter, and assuming that the established DNS configuration is correct, no further
changes should be needed to activate Unified Messaging services.

If the IP gateway in use doesn't support the use of DNS names to resolve the Unified
Messaging services, additional configuration steps will be necessary to manually point the IP
gateway to the IP addresses of the Unified Messaging services in the second datacenter.

Activating Edge Transport Servers
The steps to activate the Edge Transport server role will vary, depending on the specific
configuration. Edge Transport servers in two datacenters can be configured in either an
active/passive or an active/active configuration. In an active/passive configuration, the Edge
Transport server in the second datacenter is idle until the second datacenter is activated. In an
active/active configuration, Edge Transport servers in both datacenters are delivering mail at all
times.

In an active/active configuration, no steps are necessary to activate the second datacenter's
Edge Transport servers because they are already running. In an active/passive configuration,
the DNS MX resource record for each SMTP domain needs to be updated as part of the
switchover from the primary datacenter to the standby datacenter. Although the active/active
configuration provides a simple datacenter switchover solution, it has the drawback of

<!-- p.2821 -->

requiring careful load monitoring to make sure that after the datacenter switchover, the Edge
Transport servers in the second datacenter can provide sufficient capacity to support the
increased load now flowing through it, as a result of the Edge Transport servers in the primary
datacenter being unavailable.

Even with an active/active configuration, it may be appropriate to update the MX resource
records for your Edge Transport servers during a datacenter switchover. Allowing the MX
resource record for the failed datacenter to continue to point at the failed datacenter means
that when the datacenter starts recovering, it could start experiencing connection attempts to
its Edge Transport servers. This could happen while the Edge Transport services are in an
unstable state (for example, because dependent services in the datacenter are being restored).

Assuming the DNS records are under the control of the organization, activating Edge Transport
servers involves updating the MX resource record for each SMTP domain hosted by the server.

  ７ Note

  If the MX resource record used by your organization isn't hosted by a DNS server under
  your organization's control, you might consider referencing a CNAME record in the MX
  resource record and using a CNAME record under the organization's control that can then
  be updated.

DNS updates enable incoming traffic, and outgoing traffic is handled by the activation of the
mailbox databases in a site that has functioning Edge Transport servers:

     When incoming SMTP connections are initiated using the updated name resolution
     information, SMTP clients will connect to the Edge Transport servers in the second
     datacenter. Traffic will be appropriately routed by the Edge Transport server, and no
     further changes are required.

     When outgoing SMTP connections are initiated, they will try the locally available Edge
     Transport server, and those messages will be queued or immediately sent based on the
     status of the receiving server.

Restoring Service to the Primary Datacenter
Generally, datacenter failures are either temporary or permanent. With a permanent failure,
such as an event that has caused the permanent destruction of a primary datacenter, there's no
expectation that the primary datacenter will be activated. However, with a temporary failure
(for example, an extended power loss or extensive but repairable damage), there's an
expectation that the primary datacenter will eventually be restored to full service.

<!-- p.2822 -->

The process of restoring service to a previously failed datacenter is referred to as a switchback.
The steps used to perform a datacenter switchback are similar to the steps used to perform a
datacenter switchover. A significant distinction is that datacenter switchbacks are scheduled,
and the duration of the outage is often much shorter.

It's important that switchback not be performed until the infrastructure dependencies for
Exchange have been reactivated, are functioning and stable, and have been validated. If these
dependencies aren't available or healthy, it's likely that the switchback process will cause a
longer than necessary outage, and the process could fail altogether.

Mailbox Server Role Switchback
The Mailbox server role should be the first role that's switched back to the primary datacenter.
The following steps detail the Mailbox server role switchback process:

   1. As part of the datacenter switchover process, the Mailbox servers in the primary
     datacenter were put into a stopped state. When the environment (such as primary
     datacenter, Exchange dependencies, and wide area network (WAN) connectivity) is ready,
     the first step is to put the Mailbox servers in the restored primary datacenter into a
     started state and incorporate them into the DAG. The way in which this is done depends
     on whether the DAG is in DAC mode.

      a. If the DAG is in DAC mode, you can reincorporate the DAG members in the primary
        site by using the Start-DatabaseAvailabilityGroup cmdlet. Then, to make sure that the
        proper quorum model is being used by the DAG, run the Set-
        DatabaseAvailabilityGroup cmdlet against the DAG without specifying any parameters.

      b. If the DAG isn't in DAC mode, you can reincorporate the DAG members by using the
        Add-DatabaseAvailabilityGroupServer cmdlet.

   2. After the Mailbox servers in the primary datacenter have been incorporated into the DAG,
     they will need some time to synchronize their database copies. Depending on the nature
     of the failure, the length of the outage, and actions taken by an administrator during the
     outage, this may require reseeding the database copies. For example, if during the
     outage, you remove the database copies from the failed primary datacenter to allow log
     file truncation to occur for the surviving active copies in the second datacenter, reseeding
     will be required. Each database can individually proceed from this point forward. After a
     replicated database copy in the primary datacenter is healthy, it can proceed to the next
     step.

        ７ Note

<!-- p.2823 -->

    This process doesn't require that all databases be moved at the same time. You are
    encouraged to move the majority of your organization's databases at one time, but
    some databases many linger in the second datacenter if there are issues associated
    with the database copies in the primary datacenter.

3. After a majority of the databases are in a healthy state in the primary datacenter, the
  switchback outage can be scheduled. When the scheduled time arrives, the following
  steps must be taken:

   a. During the datacenter switchover process, the DAG was configured to use an alternate
     witness server. The DAG must be reconfigured to use a witness server in the primary
     datacenter. If you're using the same witness server and witness directory that was used
     prior to the primary datacenter outage, you can run the Set-
     DatabaseAvailabilityGroup -Identity DAGName command. If you plan on using a

     witness server or witness directory that is different from the original witness server and
     directory, use the Set-DatabaseAvailabilityGroup command to configure the witness
     server and witness directory parameters with the appropriate values.

  b. The databases being reactivated in the primary datacenter should be dismounted in
     the second datacenter. You can use the Dismount-Database cmdlet to dismount the
     databases.

   c. After the databases have been dismounted, the URLs of the servers running Client
     Access services should be moved from the second datacenter to the primary
     datacenter. This is accomplished by changing the DNS record for the URLs to point to
     the Client Access services server or array in the primary datacenter. This will result in
     the system acting as though a database failover has occurred for each database being
     moved.

    ） Important

    Don't proceed to the next step until the URLs for the servers running Client Access
    services have been moved and the DNS TTL and cache entries have expired.
    Activating the databases in the primary datacenter prior to moving the URLs to the
    primary datacenter will result in an invalid configuration (for example, a mounted
    database that has no Client Access services running in its Active Directory site).

4. Because each database in the primary datacenter is in a healthy state, it can be activated
  in the primary datacenter by performing database switchovers. This is accomplished by
  using the Move-ActiveMailboxDatabase cmdlet for each database that will be activated.

<!-- p.2824 -->

   5. After each database is moved to the primary datacenter, it can be mounted by using the
        Mount-Database cmdlet.

After one or more databases are active and mounted in the primary datacenter, switchback
procedures for the other server roles can be performed.

Client Access services switchback
As part of the switchover process, the internal and external DNS records used by clients, other
servers, and IP gateways to resolve the service endpoints for Client Access services, Transport
and Unified Messaging services, and Edge Transport servers were modified to point to the
corresponding endpoints in the second datacenter. The switchback process for the other server
roles involves modifying those records to point to the restored service endpoints in the
primary datacenter.

As with the DNS changes that were made during the switchover to the second datacenter,
clients, servers, and IP gateways will continue to try to connect, and should automatically
connect after the TTL has expired for the original DNS entry, and after the entry is expired from
their DNS cache.

Reestablishing Site Resilience
After switchback to the primary datacenter is completed successfully, you can reestablish site
resilience for the primary datacenter by verifying the health and status of each mailbox
database copy in the second datacenter. In addition, if any database copies in the second
datacenter were originally blocked for activation, you can reconfigure those settings at this
time.

<!-- p.2825 -->

Perform a server switchover
07/23/2025

APPLIES TO:      2016      2019      Subscription Edition

A server switchover is part of preparing for a scheduled outage for the current Mailbox server.

What do you need to know before you begin?
     Estimated time to complete: 30 seconds per database

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Database availability groups"
     entry in the High availability and site resilience permissions topic.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the EAC to perform a server switchover
You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the"Mailbox database copies" entry in the High availability
and site resilience permissions topic.

   1. In the EAC, go to Servers > servers.

   2. Select the Mailbox server you want to switchover.

   3. In the details pane, select Server Switchover.

   4. On the Server Switchover page, do one of the following:

   5. Accept the default setting of Automatically choose a target server (in which case, the
     system automatically selects the best Mailbox server for each database being switched
     over), and then click save.

   6. Click Use the specified server as the target for switchover, click Browse to select a
     Mailbox server, and then click save.

   7. When the switchover has completed, click close to exit the Server Switchover page.

<!-- p.2826 -->

Use the Exchange Management Shell to perform a
server switchover
This example performs a server switchover for the server MBX1. The system automatically
selects the best Mailbox server for each active database on MBX1.

  PowerShell

  Move-ActiveMailboxDatabase -Server MBX1

This example performs a server switchover of the Mailbox server MBX4. When the command
completes, MBX5 hosts the active copy of the databases that were previously active on MBX4.

  PowerShell

  Move-ActiveMailboxDatabase -Server MBX4 -ActivateOnServer MBX5

For detailed syntax and parameter information, see Move-ActiveMailboxDatabase.

<!-- p.2827 -->

Backup, restore, and disaster recovery in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

Data protection planning is a complex process that relies on many decisions that you make
during the planning phase of your deployment. As part of your planning, it's important that
you understand the ways in which data can be protected, and to determine which method best
suits your organization's needs.

Traditionally, backups have been used for the following scenarios:

      Disaster recovery: In the event of a hardware or software failure, multiple database copies
      in a DAG enable high availability with fast failover and little or no data loss. This
      eliminates downtime and the resulting lost productivity that's a significant cost of
      recovering from a past point-in-time backup to disk or tape. DAGs can be extended to
      multiple sites and can provide resilience against disk, server, network, and datacenter
      failures.

      Recovery of accidentally deleted items: Historically, in a situation where a user deleted
      items that later needed to be recovered, it involved finding the backup media on which
      the data that needed to be recovered was stored, and then somehow obtaining the
      desired items and providing them to the user. With the Recoverable Items folder in
      Exchange 2016 and Exchange 2019, and the Hold Policy that can be applied to it, it's
      possible to retain all deleted and modified data for a specified period of time, so recovery
      of these items is easier and faster. This reduces the burden on Exchange administrators
      and the IT help desk by enabling end users to recover accidentally deleted items
      themselves, thereby reducing the complexity and administrative costs associated with
      single item recovery. For more information, see Messaging policy and compliance in
      Exchange Server and Data loss prevention in Exchange Server.

      Long-term data storage: Backups have also been used as an archive, and typically tape is
      used to preserve point-in-time snapshots of data for extended periods of time as
      governed by compliance requirements. The new archiving, multiple-mailbox search, and
      message retention features in Exchange Server provide a mechanism to efficiently
      preserve data in an end-user accessible manner for extended periods of time. This
      eliminates expensive restores from tape, and increases productivity. For more information,
      see In-Place Archiving in Exchange Server, In-Place eDiscovery in Exchange Server, and In-
      Place Hold and Litigation Hold in Exchange Server.

<!-- p.2828 -->

     Point-in-time database snapshot: If a past point-in-time copy of mailbox data is a
     requirement for your organization, Exchange provides the ability to create a lagged
     database copy in a DAG environment. This can be useful in the rare event that store
     logical corruption replicates to multiple database copies in the DAG, resulting in a need to
     return to a previous point in time. It may also be useful if an administrator accidentally
     deletes mailboxes or user data. Recovery from a lagged copy can be faster than restoring
     from a backup because lagged copies don't require a time-consuming copy process from
     the backup server to the Exchange server. This can significantly lower total cost of
     ownership by reducing downtime.

Because there are native Exchange Server features that meet each of these scenarios in an
efficient and cost effective manner, you may be able to reduce or eliminate the use of
traditional backups in your environment.

Exchange Native Data Protection
Microsoft's preferred architecture    for Exchange Server 2016 and Exchange Server 2019
leverages a concept known as Exchange Native Data Protection. Exchange Native Data
Protection relies on built-in Exchange features to protect your mailbox data, without the use of
backups (although you can still use those features and make backups). Exchange 2016 and
Exchange 2019 include several features that, when deployed and configured correctly, can
provide native data protection that eliminates the need to make traditional backups of your
data. Using the high availability features built into Exchange Server to minimize downtime and
data loss in the event of a disaster can also reduce the total cost of ownership of the
messaging system. By combining these features with other built-in features, such as Legal
Hold, you can reduce or eliminate your use of traditional point-in-time backups and reduce the
associated costs.

In addition to determining whether Exchange Server enables you to move away from
traditional point-in-time backups, we recommend that you evaluate the cost of your current
backup infrastructure. Consider the cost of end-user downtime and data loss when attempting
to recover from a disaster using your existing backup infrastructure. Also, include hardware,
installation, and license costs, as well as the management cost associated with recovering data
and maintaining the backups. Depending on the requirements of your organization, it's quite
likely that a pure Exchange 2016 or Exchange 2019 environment with at least three mailbox
database copies will provide lower total cost of ownership than one with backups.

There are several issues that you should consider before using the features built into Exchange
Server as a replacement for traditional backups. There may also be considerations unique to
your organization. Consider the following issues, and note that this isn't an exhaustive list:

<!-- p.2829 -->

     You should determine how many copies of the database need to be deployed. We
     strongly recommend deploying a minimum of three (non-lagged) copies of a mailbox
     database before eliminating traditional forms of protection for the database, such as
     Redundant Array of Independent Disks (RAID) or traditional VSS-based backups.

     You should clearly define the recovery time objective and recovery point objective goals,
     and you should establish that using a combined set of built-in features in lieu of
     traditional backups to enable you to meet these goals.

     You should determine how many copies of each database are needed to cover the various
     failure scenarios against which your system is designed to protect.

     You should determine whether eliminating the use of a DAG or some of its members
     captures sufficient costs to support a traditional backup solution. If so, you should
     determine whether that solution improves your recovery time objective or recovery point
     objective service level agreements (SLAs).

     You should determine whether you can afford to lose a point-in-time copy if the DAG
     member hosting the copy experiences a failure that affects the copy or the integrity of
     the copy.

     Exchange Server allows you to deploy much larger mailboxes, with a recommended
     maximum mailbox database size of 2 terabytes (when two or more highly available
     mailbox database copies are being used). Based on the larger mailboxes that most
     organizations are likely to deploy, you should determine your recovery point objective if
     you have to replay a large number of log files when activating a database copy or a
     lagged database copy.

     You should determine how you'll detect and prevent logical corruption in an active
     database copy from replicating to the passive copies of the database. This includes
     determining the recovery plan for this situation and how frequently this scenario has
     occurred in the past. If logical corruption occurs frequently in your organization, we
     recommend that you factor that scenario into your design by using one or more lagged
     copies, with a sufficient replay lag window to allow you to detect and act on logical
     corruption when it occurs, but before that corruption is replicated to other database
     copies.

One of the functions performed at the end of a successful full or incremental backup is the
truncation of transaction log files that are no longer needed for database recovery. If backups
aren't being taken, log truncation won't occur. To prevent a buildup of log files, you enable
circular logging for your replicated databases. When you combine circular logging with
continuous replication, you have a new type of circular logging called continuous replication
circular logging (CRCL), which is different from Extensible Storage Engine (ESE) circular logging.

<!-- p.2830 -->

Whereas ESE circular logging is performed and managed by the Microsoft Exchange
Information Store service, CRCL is performed and managed by the Microsoft Exchange
Replication service. When enabled, ESE circular logging doesn't generate additional log files
and instead overwrites the current log file when needed. However, in a continuous replication
environment, log files are needed for log shipping and replay. As a result, when you enable
CRCL, the current log file isn't overwritten and closed log files are generated for the log
shipping and replay process.

Specifically, the Microsoft Exchange Replication service manages CRCL so that log continuity is
maintained and logs aren't deleted if they're still needed for replication. The Microsoft
Exchange Replication service and the Microsoft Exchange Information Store service
communicate by using remote procedure calls (RPCs) regarding which log files can be deleted.

  ７ Note

  Be aware of changes in behavior for log truncation in Exchange 2019. One of the reasons
  for these changes is because Workload Management (WLM) prioritizes threads on a server
  and balances this prioritization across our Exchange services (as it's intended). This results
  in a higher threshold for required logs before truncation occurs. Also, this threshold is
  different if you compare this before and after active users are moved to these databases.

For truncation to occur on highly available (non-lagged) mailbox database copies, the
following must be true:

     The log file has been backed up, or CRCL is enabled.

     The log file is below the checkpoint.

     The other non-lagged copies of the database agree with deletion.

     The log file has been inspected by all lagged copies of the database.

For truncation to occur on lagged database copies, the following must be true:

     The log file is below the checkpoint.

     The log file is older than ReplayLagTime + TruncationLagTime.

     The log file is deleted on the active copy of the database.

Supported Backup Technologies

<!-- p.2831 -->

Exchange Server supports only Exchange-aware, VSS-based backups. Exchange Server includes
a plug-in for Windows Server Backup that enables you to make and restore VSS-based backups
of Exchange data. To back up and restore Exchange Server, you must use an Exchange-aware
application that supports the VSS writer for Exchange Server, such as Windows Server Backup
(with the VSS plug-in), Microsoft System Center 2012 - Data Protection Manager, or a third-
party Exchange-aware VSS-based application.

For detailed steps about how to back up and restore Exchange data using Windows Server
Backup, see Using Windows Server Backup to back up and restore Exchange data.

Exchange Server VSS Writer
Earlier versions of Exchange included two VSS writers: one inside the Microsoft Exchange
Information Store service (store.exe) and one inside the Microsoft Exchange Replication service
(msexchangerepl.exe). Back in Exchange 2013, the VSS writer functionality previously found in
the Microsoft Exchange Information Store service was moved to the Microsoft Exchange
Replication service. This architecture remains the same in Exchange 2016 and Exchange 2019.
This writer, named Microsoft Exchange Writer, is used by Exchange-aware VSS-based
applications to back up active and passive database copies, and to restore backed up database
copies. Although the writer runs in the Microsoft Exchange Replication service, it requires the
Microsoft Exchange Information Store service to be running for the writer to be advertised. As
a result, both services are required to back up or restore Exchange databases.

Exchange Server Recovery
Almost all of the configuration settings for Mailbox servers and Client Access services are
stored in Active Directory. As with previous versions of Exchange, Exchange 2016 and Exchange
2019 include a Setup parameter for recovering lost servers. This parameter, /m:RecoverServer, is
used to rebuild and re-create a lost server by using the settings and configuration information
stored in Active Directory. However, be aware that there are several settings which are not
restored, such as changes to local web.config and other configuration files. In addition, custom
registry entries are not restored. We recommend that you use a reliable change management
process to track and recreate these changes.

For detailed steps about how to perform a server recovery of a lost Exchange server, see
Recover an Exchange Server. For detailed steps about how to recover a lost server that's a
member of a database availability group (DAG), see Recover a database availability group
member server.

Unified Contact Store Recovery

<!-- p.2832 -->

When Microsoft Lync Server 2013 or Skype for Business Server 2015 is used in an Exchange
2016 or Exchange 2019 environment, the user's Lync/Skype for Business contact information is
stored in a special contact folder in the user's mailbox. This is referred to as the unified contact
store (UCS). If you restore a UCS-migrated mailbox, the instant messaging contact list for the
target user may be affected. If the user was migrated after the last backup, restoring the
mailbox will result in a complete loss of the user's contact list. In less severe cases,
modifications to the contact list made by the user since the last backup will be lost. To mitigate
this potential data loss, ensure the user is migrated back to the instant messaging server prior
to restoring the mailbox.

Recovery Database
A recovery database is a special kind of mailbox database that allows you to mount a restored
mailbox database and extract data from the restored database as part of a recovery operation.
You can use the New-MailboxRestoreRequest cmdlet to extract data from a recovery database.
After extraction, the data can be exported to a folder or merged into an existing mailbox.
Recovery databases enable you to recover data from a backup or copy of a database without
disturbing user access to current data.

Using a recovery database for a Mailbox database from any previous version of Exchange isn't
supported. In addition, the target mailbox used for data merges and extraction must be in the
same Active Directory forest as the database mounted in the recovery database.

For more information, see Recovery databases. For detailed steps about how to create a
recovery database, see Create a recovery database. For detailed steps about how to use a
recovery database, see Restore data using a recovery database.

Database Portability
Database portability is a feature that enables an Exchange mailbox database to be moved to
and mounted on any other Exchange Mailbox server in the same organization. By using
database portability, reliability is improved by removing several error-prone, manual steps from
the recovery processes. In addition, database portability reduces the overall recovery times for
various failure scenarios.

For detailed steps to use database portability, see Move a mailbox database using database
portability.

Dial Tone Portability

<!-- p.2833 -->

Dial tone portability is a feature that provides a limited business continuity solution for failures
that affect a mailbox database, a server, or an entire site. Dial tone portability enables a user to
have a temporary mailbox for sending and receiving e-mail while the original mailbox is being
restored or repaired. The temporary mailbox can be on the same Exchange Mailbox server or
on any other Exchange Mailbox server in your organization. This allows an alternative server to
host the mailboxes of users who were previously on a server that's no longer available. Clients
that support Autodiscover, such as Microsoft Outlook, are automatically redirected to the new
server without having to manually update the user's desktop profile. After the user's original
mailbox data has been restored, an administrator can merge a user's recovered mailbox and
the user's dial tone mailbox into a single, up-to-date mailbox.

The process for using dial tone portability is called a dial tone recovery. A dial tone recovery
involves creating an empty database on a Mailbox server to replace a failed database. This
empty database, referred to as a dial tone database, allows users to send and receive e-mail
while the failed database is recovered. After the failed database is recovered, the dial done
database and the recovered database are swapped, and then the data from the dial tone
database is merged into the recovered database.

For more information, see Dial tone portability. For detailed steps to perform a dial tone
recovery, see Perform a dial tone recovery.

<!-- p.2834 -->

Exchange Server: Use Windows Server
Backup to back up and restore Exchange
data
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

Microsoft's preferred architecture     for Exchange Server uses a concept known as Exchange
Native Data Protection. Exchange Native Data Protection relies on native Exchange features to
protect your mailbox data, without the use of traditional backups. But if you want to create
backups, Exchange includes a plug-in for Windows Server Backup (WSB) that enables you to
create Exchange-aware Volume Shadow Copy Service (VSS)-based backups of Exchange data.
To take Exchange-aware backups, you must have the WSB feature installed.

The plug-in, WSBExchange.exe, runs as a service named Microsoft Exchange Server Extension
for Windows Server Backup (the short name for this service is WSBExchange). This service is
automatically installed and configured for manual startup on all Mailbox servers. The plug-in
enables WSB to create Exchange-aware VSS backups.

Before using WSB to back up Exchange data, we recommend that you familiarize yourself with
the following features and options for the plug-in:

      Backups that are taken with WSB occur at the volume level, and the only way to perform
      an application-level backup or restore is to select an entire volume. To back up a database
      and its log stream, you must back up the entire volume containing the database and logs,
      not just the individual folders. You can't back up any data without backing up the entire
      volume containing the data.

      The backup must be run locally on the server being backed up, and you can't use the
      plug-in to take remote VSS backups. There is no remote administration of WSB or the
      plug-in. You can, however, use Remote Desktop Services or Terminal Services to remotely
      manage backups.

      The backup can be created on a local drive or on a remote network share.

      Only full backups should be taken. Log truncation will occur only after a successful
      completion of a VSS full backup of a volume or folders containing an Exchange database.

      When restoring data, it's possible to restore only Exchange data. This data can be
      restored to its original location or to an alternate location. If you restore the data to its
      original location, WSB and the plug-in automatically handle the recovery process,

<!-- p.2835 -->

      including dismounting any existing database and replaying logs into the restored
      database.

      The restore process doesn't support the Exchange recovery database (RDB). If you want
      to use an RDB, you must restore the data to an alternate location and then manually copy
      or move the restored data from that location into the RDB folder structure.

      When restoring Exchange data, all backed-up databases must be restored together. You
      can't restore a single database.

      Bare metal restores are supported when using WSB. However, the recommended recovery
      approach for Exchange servers is to recover the Exchange server and then restore the
      data. If you're using a third-party backup app (for example, non-Microsoft), then support
      for bare metal restores of Exchange may be available from your backup app vendor.

The following table describes the supportability of the backup and recovery options available
for Exchange Server with WSB.

                                                                                        ﾉ   Expand table

 If you...                    Then...

 Back up the full server...   A VSS copy backup will be performed, and the transaction logs for the
                              databases on the server will not be truncated.

 Perform a custom backup      A VSS full backup can be selected, allowing the transaction logs for the
 and select one or more       databases on the selected volumes to be truncated at the completion of a
 volumes to back up...        successful backup.

 Perform a custom backup      A VSS full backup can be selected and the log files will be truncated;
 and select one or more       however, restoration of the backup will be limited to file restore, as an
 folders to back up...        Application level restore will not be available as an option.

For detailed steps to back up Exchange using WSB, see Use Windows Server Backup to back up
Exchange.

For detailed steps to restore data from a backup taken with WSB, see Use Windows Server
Backup to restore a backup of Exchange.

<!-- p.2836 -->

Use Windows Server Backup to back up
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019       Subscription Edition

You can use Windows Server Backup to back up and restore Exchange databases. Exchange
includes a plug-in for Windows Server Backup that allows you to make Volume Shadow Copy
Service (VSS)-based backups of Exchange data.

What do you need to know before you begin?
      Estimated time to complete: 1 minute, plus the time it takes to back up the data

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Mailbox recovery" entry in the
      Recipients Permissions topic.

      The Windows Server Backup feature must be installed on the local computer.

      During the backup operation, a consistency check of the Exchange data files is run to
      make sure that the files are in a good state and can be used for recovery. If the
      consistency check succeeds, Exchange data is available for recovery from that backup. If
      the consistency check fails, the Exchange data isn't available for recovery. Windows Server
      Backup runs the consistency check on the snapshot taken for the backup. As a result,
      before copying files from the snapshot to backup media, the consistency of the backup is
      known, and the user is notified of the consistency check results.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online          , or Exchange Online Protection .

Use Windows Server Backup to back up Exchange
   1. Start Windows Server Backup.

   2. Select Local Backup.

   3. In the Actions pane, click Backup Once... to start the Backup Once Wizard.

<!-- p.2837 -->

 4. On the Backup Options page, select Different options, and then click Next.

 5. On the Select Backup Configuration page, select Custom, and then click Next.

 6. On the Select Items for Backup page, click Add Items to select the volume(s) to be
   backed up, and then click OK.

     ７ Note

     Choose volumes and not individual folders. The only way to perform an application-
     level backup or restore is to select an entire volume.

 7. Click Advanced Settings. On the Exclusions tab, click Add Exclusion to add any files or
   file types you want to exclude from the backup.

     ７ Note

     By default, volumes that contain operating system components or applications are
     included in the backup and can't be excluded.

 8. On the VSS Settings tab, select VSS full Backup, and then click OK, and then click Next.

 9. On the Specify Destination Type page, select the location where you want to store the
   backup, and then click Next.

        If you choose Local drives, the Select Backup Destination page appears. Select an
        option from the Backup destination dropdown, and then click Next.

        If you choose Remote shared folder, the Specify remote folder page appears.
        Specify a UNC path for the backup files, configure access control settings. Choose
        Do not inherit if you want the backup to be accessible only through a specific
        account. Provide a username and password for an account that has write
        permissions on the computer hosting the remote folder, and then click OK.
        Alternatively, choose Inherit if you want the backup to be accessible by everyone
        who has access to the remote folder. Click Next.

10. On the Confirmation page, review the backup settings, and then click Backup.

11. On the Backup Progress page, you can view the status and progress of the backup
   operation.

12. Click Close to exit the Backup Progress page at any time. Any backup in progress will
   continue to run in the background.

<!-- p.2838 -->

How do you know this worked?
To verify that you've successfully backed up the data, do any of the following:

     On the server on which Windows Server Backup was run, the last backup status will be
     displayed, which should say Successful. You can also verify that the backup completed
     successfully by viewing the Windows Server Backup logs.

     Open Event Viewer and verify that a backup completion event was logged in the
     Application event log.

     Run the following command in the Exchange Management Shell to verify that each
     database on the selected volume(s) was backed up successfully:

       PowerShell

        Get-MailboxDatabase -Server <ServerName> -Status | Format-List
        Name,*FullBackup

     The SnapshotLastFullBackup and LastFullBackup properties of the database indicate when
     the last successful backup was taken, and if it was a VSS full backup.

<!-- p.2839 -->

Restore a backup of Exchange using
Windows Server Backup
07/23/2025

APPLIES TO:       2016       2019      Subscription Edition

You can use Windows Server Backup to back up and restore Exchange databases. Exchange
includes a plug-in for Windows Server Backup that allows you to make and restore Volume
Shadow Copy Service (VSS)-based backups of Exchange data. For more information, see Using
Windows Server Backup to back up and restore Exchange data.

What do you need to know before you begin?
     Estimated time to complete: 1 minute, plus the time it takes to restore the data

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Mailbox recovery" entry in the
     Recipients Permissions article.

     The Windows Server Backup feature must be installed on the local computer.

     When you restore a database to its original location, the database can remain in a dirty
     shutdown state and be mountable by the system. When restoring to an alternate location
     (for example, in preparation to use a recovery database), the database must be manually
     brought into a clean shutdown state by using Exchange Server Database Utilities
     (Eseutil.exe).

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use Windows Server Backup to restore a backup of
Exchange
   1. Start Windows Server Backup.

   2. Select Local Backup.

   3. In the Actions pane, select Recover... to start the Recovery Wizard.

<!-- p.2840 -->

4. On the Getting Started page, do either of the following:

       If the data being recovered was backed up on the local server, select This server
       (ServerName), and then select Next.

       If the data being recovered is from another server, or if the backup being recovered
       is located on another computer, select Another server, and then select Next. On the
       Specify location type page, select Local drives or Remote shared folder, and then
       select Next. If you select Local drives, select the drive containing the backup on the
       Select backup location page, and then select Next. If you select Remote shared
       folder, enter the UNC path for the backup data on the Specify remote folder page,
       and then select Next.

5. On the Select Backup Date page, select the date and time of the backup that you want to
  recover, and then select Next.

6. On the Select Recovery Type page, select Applications, and then select Next.

    ７ Note

    If Applications isn't available as a selection, it indicates that the backup selected for
    restore was a folder-level backup, and not a volume level backup. You must perform
    backups at the volume level when backing up Exchange data with Windows Server
    Backup.

7. On the Select Application page, verify that Exchange is selected in the Applications field.
  Select View Details to view the application components of the backups. If the backup that
  you're recovering is the most recent, the Do not perform a roll-forward recovery of the
  application database check box is displayed. Select this check box if you want to prevent
  Windows Server Backup from rolling forward the database being recovered by
  committing all uncommitted transaction logs. Select Next.

8. On the Specify Recovery Options page, specify where you want to recover the data, and
  then select Next:

       Choose Recover to original location if you want to restore the Exchange data
       directly to its original location. If you use this option, you can't choose which
       databases are restored; all backed up databases on the volume are restored to their
       original locations.

       Choose Recover to another location if you want to restore individual databases and
       their files to a specified location. Select Browse to specify the alternate location. If
       you use this option, you can choose which databases are restored. After being
