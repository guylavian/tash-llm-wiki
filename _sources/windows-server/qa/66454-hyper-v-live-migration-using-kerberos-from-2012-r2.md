---
title: "Hyper-V Live Migration using Kerberos from 2012 R2 to 2019 fails with error 0x80090322"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/66454/hyper-v-live-migration-using-kerberos-from-2012-r2
question_id: 66454
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-high-availability-virtualization-hyper-v", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Hyper-V Live Migration using Kerberos from 2012 R2 to 2019 fails with error 0x80090322

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/66454/hyper-v-live-migration-using-kerberos-from-2012-r2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!  

I have a Windows Server 2012 R2 Hyper-V Failover Cluster and I'm trying to Live Migrate VM's to a Windows Server 2019 Hyper-V Failover Cluster.  When I try to Live Migrate a non-clustered VM from one of the Windows Server 2012 R2 Hosts to one of the Windows Server 2019 Hyper-V Hosts, I get an error 0x80090322:  

move-vm : Virtual machine migration operation for 'WindowsAdminCenter' failed at migration source 'HYPER-V4'. (Virtual machine ID 39D45F49-72D2-4D19-B98A-9F55481A8047)  

The Virtual Machine Management Service failed to establish a connection for a Virtual Machine migration with host 'hyper-v01': The target principal name is incorrect. (0x80090322).  

The Virtual Machine Management Service failed to authenticate the connection for a Virtual Machine migration at the source host: The target principal name is incorrect. (0x80090322).  

I have both hosts (the 2012 R2 Hyper-V4 and the 2019 Hyper-V01) configured to use Kerberos Live Migration, and I have the SPN's configured for both CIFS and "Microsoft Virtual System Migration Service" (using both NetBIOS and DNS names) on both servers.  I've tried both the option "Use Kerberos Only" and "Use any authentication protocol".    

As a test I was able to Live Migrate from the 2012 R2 machine to another Hyper-V 2012 R2 server (which is not in the 2012 R2 Cluster) and that worked.  I'm just having trouble with getting the Live Migration working to Windows 2019.    

Some additional notes:  

-  I've tried "Use any available network for live migration" and "Use these IP addresses for live migration".  

-  I've tried removing the 2019 server from the cluster and Live Migration still doesn't work to it.  

-  This is a flat LAN - no routing between servers.  

-  Connectivity by IP & DNS works between servers.  

-  I've tried adjusting the Live Migration Settings on the 2012 R2 Cluster to only use the LAN network (the cluster & iSCSI connections are not connected between the 2012 R2 and the 2019 clusters).  

-  "setspn -X" doesn't show any duplicate SPN's  

Does anyone have any idea of what I should try next?  I'd certainly appreciate the guidance!  

Dave

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-19*

Here is what I came up with.  It doesn't make sense to me.  If someone can point anything out, I'd certainly be willing to listen.  

I couldn't get the Kerberos Live Migration to work from my Hyper-V 2012 R2 Cluster hosts to my Hyper-V 2019 Cluster hosts - I kept getting the 0x80090322 as documented above.  I know how to configure Constrained Delegation and to purge the Kerberos tickets.  I had no problem getting my Hyper-V 2012 R2 Hosts to Live Migrate to a test Windows Server 2019 Hyper-V box which wasn't in a cluster.  Just couldn't get the 2012 R2 to Live Migrate to the hosts in my 2019 Cluster.  

Even trying to use CredSSP on didn't seem to work until I tried doing a Live Migration to my 3rd Cluster Host on my 2019 Cluster.  I hadn't set up any Constrained Delegation at all for that Host.  I was able to use the "move-vm" from the 2012 R2 host to Live-Migrate a VM (removed from the 2012 R2 Cluster, of course) to this 3rd 2019 Cluster Server.  Yet, I couldn't get this to work to the other two Windows 2019 Clustered Hosts even if I removed the Constrained Delegation and set the 2019 servers back to "Do not trust this computer from delegation".  Doesn't make sense, why I couldn't seem to be able to get my two 2019 hosts working w/ CredSSP after trying to get the Kerberos Live-Migrations, but that's what I found.  

So this is what did work for me:  

2012 R2 Host:   

-  No constrained delegation configured for 2019 Host.  

-  Hyper-V Live Migration set to Kerberos  

2019 Host:   

-  "Do not trust this computer from delegation"  

-  Hyper-V Live Migration set to Kerberos  

RDP into 2012 R2 Host  

move-vm "VM" -IncludeStorage -DestinationHost hyper2019-3 -DestinationStoragePath "C:\ClusterStorage\volume\VM"  

My guess is that even if you have Hyper-V Live Migrations set to use Kerberos, if that doesn't work, then it will fall back to using CredSSP.  

After spending as much time on this as I have, and not wanting to break anything, I am quite willing to use CredSSP - even if I can only do it to one of my 2019 Hosts.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-13*

Yes, I've seen these guides, and I believe that I have followed everything accurately.

As a test, I installed a new 2019 Server w/ Hyper-V, didn't add it to a cluster, set up constrained delegation to this test server and was able to do Live-Migrations to the test 2019 box. But why can't I do it to my production 2019 Servers?

I am not using VMM. I am just trying to use the Hyper-V MMC and move-vm command to do my moves.

If my NTDS ports, you are referring to TCP/UDP ports, they should all be open without any firewall.

Here is my source computer:  

PS C:\Windows\system32> setspn -L ABC-hyper-vr1  

Registered ServicePrincipalNames for CN=ABC-HYPER-VR1,OU=DV Servers,DC=ABCDI,DC=company,DC=com:  

MSServerClusterMgmtAPI/ABC-HYPER-VR1  

MSServerClusterMgmtAPI/ABC-Hyper-VR1.ABCDI.company.com  

WSMAN/ABC-Hyper-VR1  

WSMAN/ABC-Hyper-VR1.ABCDI.company.com  

Microsoft Virtual Console Service/ABC-HYPER-VR1  

Microsoft Virtual Console Service/ABC-Hyper-VR1.ABCDI.company.com  

TERMSRV/ABC-HYPER-VR1  

TERMSRV/ABC-Hyper-VR1.ABCDI.company.com  

Microsoft Virtual System Migration Service/ABC-Hyper-VR1.ABCDI.company.com  

Microsoft Virtual System Migration Service/ABC-HYPER-VR1  

Hyper-V Replica Service/ABC-Hyper-VR1.ABCDI.company.com  

Hyper-V Replica Service/ABC-HYPER-VR1  

RestrictedKrbHost/ABC-Hyper-VR1.ABCDI.company.com  

HOST/ABC-Hyper-VR1.ABCDI.company.com  

RestrictedKrbHost/ABC-HYPER-VR1  

HOST/ABC-HYPER-VR1

Here is my 2019 production Server (which I can't Live Migrate to):  

PS C:\Windows\system32> setspn -L ABC-hyper-v01  

Registered ServicePrincipalNames for CN=ABC-HYPER-V01,OU=DV Servers,DC=ABCDI,DC=company,DC=com:  

MSServerClusterMgmtAPI/ABC-HYPER-V01  

MSServerClusterMgmtAPI/ABC-Hyper-V01.ABCDI.company.com  

WSMAN/ABC-Hyper-V01  

WSMAN/ABC-Hyper-V01.ABCDI.company.com  

Hyper-V Replica Service/ABC-HYPER-V01  

Hyper-V Replica Service/ABC-Hyper-V01.ABCDI.company.com  

Microsoft Virtual System Migration Service/ABC-HYPER-V01  

Microsoft Virtual System Migration Service/ABC-Hyper-V01.ABCDI.company.com  

Microsoft Virtual Console Service/ABC-HYPER-V01  

Microsoft Virtual Console Service/ABC-Hyper-V01.ABCDI.company.com  

TERMSRV/ABC-HYPER-V01  

TERMSRV/ABC-Hyper-V01.ABCDI.company.com  

RestrictedKrbHost/ABC-HYPER-V01  

HOST/ABC-HYPER-V01  

RestrictedKrbHost/ABC-Hyper-V01.ABCDI.company.com  

HOST/ABC-Hyper-V01.ABCDI.company.com

And finally, a test 2019 server which I can Live Migrate to:  

PS C:\Windows\system32> setspn -L ABC-2019test  

Registered ServicePrincipalNames for CN=ABC-2019TEST,CN=Computers,DC=ABCDI,DC=company,DC=com:  

Hyper-V Replica Service/ABC-2019TEST  

Hyper-V Replica Service/ABC-2019test.ABCDI.company.com  

Microsoft Virtual System Migration Service/ABC-2019TEST  

Microsoft Virtual System Migration Service/ABC-2019test.ABCDI.company.com  

Microsoft Virtual Console Service/ABC-2019TEST  

Microsoft Virtual Console Service/ABC-2019test.ABCDI.company.com  

WSMAN/ABC-2019test  

WSMAN/ABC-2019test.ABCDI.company.com  

TERMSRV/ABC-2019TEST  

TERMSRV/ABC-2019test.ABCDI.company.com  

RestrictedKrbHost/ABC-2019TEST  

HOST/ABC-2019TEST  

RestrictedKrbHost/ABC-2019test.ABCDI.company.com  

HOST/ABC-2019test.ABCDI.company.com

I believe that the constrained delegations are set correctly, but I certainly welcome a 2nd look.  

Dave

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-13*

I can't even get CredSSP to work - I still get the 0x80090322 error.    

I've gone into both hosts's Hyper-V Manager, changed the Live Migrations to CredSSP and even rebooted both hosts.  When I do the "move-vm" from the 2012 R2 box to the 2019, I still am getting "The target principal name is incorrect".  Isn't this a Kerberos error?    

I'd be happy if I could get either CredSSP or Kerberos to work.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-13*

Thanks MiguelFra,  

I have been initiating the live migration from the source Host.  It fails from the Hyper-V MMC and from powershell.  

There is no 3rd party firewall.  Windows defender firewall is off.  

No problem with either NetBIOS or DNS name resolution from source to destination.  

Dave

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-13*

Hello Dave,  

Try to initiate the live migration from the source server's own Hyper-V MMC.   

Also check that the target does not have any 3rd party firewall enabled, has RPC working and that from the source server the DNS and NetBIOS names of the target resolves to the target's correct IP address.
