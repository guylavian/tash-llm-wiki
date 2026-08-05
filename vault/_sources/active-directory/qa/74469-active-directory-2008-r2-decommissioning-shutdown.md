---
title: "Active Directory 2008 R2 Decommissioning (Shutdown as observation period)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/74469/active-directory-2008-r2-decommissioning-shutdown
question_id: 74469
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory 2008 R2 Decommissioning (Shutdown as observation period)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/74469/active-directory-2008-r2-decommissioning-shutdown (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts!  

We are planning to decommission an Active Directory 2008 Domain controller, we have already promoted a new Domain controller 2016 within same domain.   

As part of our pre requisites or preparation before decommission, we decided to shutdown first the AD 2008 and monitor the behavior and it will be affecting the production . Unfortunately, upon observation while the AD 2008 is currently shutdown and AD 2016 is up and running, we encountered some issues. We have some issue in Mapping with the file server if AD 2008 is shutdown.   

Issues :   

-  File Server is not accessible with or using IP address itself and it is accessible only using FQDN / computer name.  

  Ex.  

    Access both \172.22.100.100 and \fileserver.domain.com.ph is ok

-  .  If AD 2008 is up and running, both accessible using IP address itself and FQDN name.   

-  . Workstation computer don't have any ip address received if AD 2008 is shutdown.   

We have ensured the following prior with AD 2008 Decommission :   

-  Ensure that there's no other Application server /servers are relaying on AD 2008.  

 2 . All servers  has been pointed to AD 2016 as their DNS server  

-  DHCP server has been migrated already from 2008 to 2016.   

-  FSMO ROLES has been transferred   

-  Replication is currently on going within AD 2008 and 2016.  

-  Make sure that any system (server or workstation) are no longer authenticating to this server as the DNS server. (check Bridgehead server)  

-  No other AD integrated to application server and ensure there is no dependency remains for this server.   

-  Ensured the Certificate services is uninstall/ removed before decommissioning.   

 9 . Double check the DNS   

Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-08-25*

Hi,

When you shutdown a DC before demote it , the clients continue trying contact it , because a client get the list of available DC from DNS. If the DNS record have not been removed before the shutdown , it can generate a authenticate issue.

I suggest to you to try remove all DNS record related to old DC just after the shutdown and clear the client DNS cache ipconfig /flushdns.

* Please don't forget to mark this reply as answer if it help you *

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-24*

Hello HomerSibayan-2720,  

Thank you for posting here.  

Here are the answers for your references.  

From the issue you provided, I want to confirm the following questions:  

Q: File Server is not accessible with or using IP address itself and it is accessible only using FQDN / computer name.  

1. If we access file server with or using IP address, what error message do you receive?  

2. Please check the preferred DNS of this file server.  

If you can provide us with a screenshot of the inspection process and the error report, we would be very grateful and we can better troubleshoot  the problem for you.  

Q: Workstation computer don't have any ip address received if AD 2008 is shutdown.  

We can run ipconfig /renew to see if the new DHCP server can assign IP addresses for workstation computers, if no, maybe the DHCP server is not migrated successfully from old 2008 R2 to 2016.   

For migrating DHCP or reconfigure DHCP on this new 2016 DC, we can check if we have migrated DHCP server successfully based on the following two links.  

How to Migrate DHCP from Windows Server 2008 to 2012/2016  

https://brycematheson.io/how-to-migrate-dhcp-from-windows-server-2008-to-2012-2016/  

How to Migrate DHCP from Windows Server 2012 R2 to Server 2016  

https://www.faqforge.com/windows-server-2016/migrate-dhcp-windows-server-2012-r2-server-2016/  

Meanwhile, in order to better troubleshoot the problem, please confirm the following information:  

-  Is there only one domain (single forest, single domain)?  

-  There is only this 2008 (2008 R2) DC before adding 2016 DC in this domain?  

-  What are the forest functional level and domain functional level?  

-  Check if AD environment is healthy. Check whether all DCs in this domain is working fine by running Dcdiag /v on both DCs.  

-  Check fsmo by running netdom query fsmo on any one DC.  

-  Check if AD replication works properly by running repadmin /showrepl and repadmin /replsum on both DCs.  

-  Please running gpupdate /force on both DCs check GPO update status..  

If anything is unclear, please feel free to let us know.  

Best Regards,  

Stephanie Yu

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-24*

I'd check the DHCP server is handing out the correct ip addresses for active healthy domain controllers, then on problem members try doing ipconfig /renew. Also check the new DHCP server is authorized.      

https://learn.microsoft.com/en-us/powershell/module/dhcpserver/get-dhcpserverindc?view=win10-ps      

--please don't forget to Accept as answer if the reply is helpful--
