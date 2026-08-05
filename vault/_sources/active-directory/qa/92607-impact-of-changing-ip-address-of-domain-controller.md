---
title: "Impact of Changing IP Address of Domain Controller, Exchange Mailbox Server, DHCP Server and ADCS server."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/92607/impact-of-changing-ip-address-of-domain-controller
question_id: 92607
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Impact of Changing IP Address of Domain Controller, Exchange Mailbox Server, DHCP Server and ADCS server.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/92607/impact-of-changing-ip-address-of-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Due to some restructure in network infrastructure, have to change local IP address of our DC Servers. We planned to change IP local IP Address of Domain Controllers (2 node), Exchange Mailbox Servers (2 node), ADCS Server (1 Node) and DHCP server (2 node) located in Data center. We have many applications dependent on ADDS and Exchange Server. I need to know what are the impacts and considerations of changing the following solution's local IP Address in the worst case scenario. Please help me with suggesting the list of Business Impacts and Role Back plan.  

Thanks in Advance.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 2 · updated: 2020-09-14*

Hello @Rony Paul  ,  

Thank you for psoting here.  

Based on the description, I understand the Domain Controller, Exchange Mailbox Server, DHCP Server and ADCS server are hosted on different machines.  

We can change the IP address of the domain controller as below.  

Change the IP address on DC and run the following command to make the changes take effect:  

Type ipconfig /flushdns and click Enter.  

Type Net Stop DNS and click Enter.  

Type Net Start DNS click Enter.  

Type Net Stop Netlogon click Enter.  

Type Net Start Netlogon click Enter.  

Type ipconfig /registerdns click Enter.  

For changing the IP address of the domain controller, we may consider:

If this DC was a DNS server, update the DNS client configuration on all member workstations, member servers, and other DCs that might have used this DNS server for name resolution. If it is required, modify the DHCP scope to reflect the change of this DNS server.  

If this DC was a DNS server, update the Forwarder settings and the Delegation settings on any other DNS servers that might have pointed to this DC for name resolution.  

For changing the IP address of the CA server.

We shouldn't have any worries about changing the IP address. The FQDN and the CA common name is what is important.  

The CA name (or common name) is critical because it is used to identify the CA object created in Active Directory. If you use the certserv webpage make sure it is accesed using the hostname and new IP address instead of the old IP address.  

All you should do is run ipconfig /registerdns. If it's not updated in your DNS give it a few minutes and check again. There should be a DNS A record with the new IP in DNS manager. Delete the old A record from DNS manager.  

If you use the certserv webpage make sure we can access by trying to access the http:\localhost(or new IP)\certsrv.  

Here is a similar case for your reference.  

Certificate Authority Question  

https://social.technet.microsoft.com/Forums/windowsserver/en-US/0b7c5911-0d3d-4c79-8728-e36d0fe9ee5e/certificate-authority-question?forum=winservergen  

Tip:  

-  Before make any changes in our AD domain environment, we had better check the following information:  

-  Check if AD environment is healthy. Check all DCs in this domain is working fine by running Dcdiag /v. Check if AD replication works properly by running repadmin /showrepl and repadmin /replsum.  

-  Back up all domain controllers.  

-  Check both SYSVOL folder and Netlogon folder are shared by running net share on each DC.  

-  Check we can update gpupdate /force on each DC successfully.  

-  Back up all DCs.  

-  We had better make any these changes during downtime.  

-  Risk factors  

If we change IP address of DCs incorrectly or the IP address of DCs are not changed successfully, user accounts or computer accounts can not be authenticated (users can not logon). Or applications can not be logged on.  

If DCs are also DNS servers, there will be DNS issues in your AD environment.  

-  We can change IP address on one DC (if it is also DNS server), then update all the DNS server of the worstations if needed, then make the other DC offline to see whether there is any issue, if everything is working fine, we can change the IP address of the other DC.  

Reference:  

How to change the IP address on a domain controller  

http://jaredheinrichs.com/how-to-change-the-ip-address-on-a-domain-controller.html  

For impact of Changing IP Address of Exchange Mailbox Server and DHCP Server, we can post our question on the network forum and Exchange forum respectively by typing the Exchange tag and DHCP tag respectively.  

Best Regards,  

Daisy Zhou  

============================================  

If the Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-09-13*

Hi,  

It's possible to change the IP of domain controller.  

To avoid any issue during the switch IP , you have to be sure that new IP have the same network flow as old IP before the switch IP.  

After the IP switch , check the DNS record of domain controller if it has the correct IP.  

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-09-11*

Should be minimal for the domain controllers. Should be able to minimize the disruption by doing the two domain controllers at different times like maybe an hour or so apart. Also note that if the subnet changes then you'll also want to recreate the reverse lookup zone.    

I'd ask new separate questions about exchange and cert server impacts in office-exchange-server-administration and windows-server-security    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-11*

Hi DSPatrick,  

Thanks for your reply. I want to know the risk factors if I change the IP addresses of the following servers.  

Best Regards,  

Rony Paul.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-09-11*

I'd plan on some minor disruption. May be able to minimize the disruption by doing the two domain controllers at different times like maybe an hour apart. If the subnet changes then you'll also want to recreate the reverse lookup zone.    

Better to ask a new separate question about exchange and cert server impacts in office-exchange-server-administration and windows-server-security    

--please don't forget to Accept as answer if the reply is helpful--
