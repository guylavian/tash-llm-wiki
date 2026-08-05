---
title: "Ldap mnemonics not applying"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1089167/ldap-mnemonics-not-applying
question_id: 1089167
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Ldap mnemonics not applying

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1089167/ldap-mnemonics-not-applying (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to capture any direct dependancies to a DC that I want to decommission. I am following these guidelines: https://www.devopsage.com/domain-controller-decommission-step-by-step-process-to-identify-apps-connected-to-a-specific-dc/.  I have configured the "DC locator DNS records not registered by the DCs" gpo and one of the mnemonics that I have configured is LDAP.  When I query dns for _ldap._tcp.<DnsDomainName> record the server name still comes up in the list.  All the other mnemonic records that I included no longer return the server name.  I suspect it might be due to a know issue about using upper case in the dc server host name.  Is it fine to delete the _ldap._tcp.<DnsDomainName> dns record for the server?  Removing that GPO should get it republished?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-10*

The answer is...   

This was definitely related to the the dc name case issue.  First issue is is that the Microsoft article https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/optimize-dc-location-global-catalog is missing some srv records that the mnemonics remove.  That means that the best way to verify is to use the C:\Windows\System32\config\netlogon.dns file.  Copy it before applying the settings, then after they are applied, verify that the netlogon.dns file has been modified. After that check if the srv records defined in the old netlogon.dns file are actually removed.  I made a script verify those entries and also let me know if there are duplicates. https://github.com/Misha305/PoshScripts/blob/main/DCNetlogonDNSChecker.ps1

In my case I still have a handful of 2012r servers and 2016 server (this one created the duplicates I suspect).  I also have a 3rd party ipaddress management system.  When I tried to delete the duplicate srv records with a powershell command against the 2012 r2 servers they were immediately there again.  When I tried to delete them against the 2016 server they would go away for a couple of minutes, but then be re-added again.  DNS server logs showed that the Ipam server was re-adding them again.  Interstingly enough, while DNS saw the duplicates the ipam server did not.  

To actually delete the records, I had to delete them from ipam,  query the 2016 server until one of the duplicate records had been removed via replication.  Once it was removed I removed the remaining via pwershell against the 2016 server and queried all the dns servers in my environment the changes had replicated and the records were all gone.  I used another script to query dns to make this a little easier. https://github.com/Misha305/PoshScripts/blob/main/DCPublishedDNSCheck.ps1

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-16*

I think my problems may be due to this https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/dns-registers-duplicate-srv-records-for-dc.  The dc in question has uppercase letters in its name.  I am seeing duplicate entries with an all lowercase entry and an uppercase one.  I have some 2012r2 Ad integrated DNS servers and one 2016 AD integrated dns server.  It is not a PDC though.  The 2016 server has the patch applied but the servers were probably added before then.  I tried on a dc that had a lowercase hostname and the gpo applied as expected.  Is there a command to force re-registration of the dns records required by a dc?  I would like to remove dns entries and have them recreated to see if that produces duplicates.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-15*

Hi     

Have a look at the official Microsoft content for the mnemonic names and yes they are case sensitive - https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/optimize-dc-location-global-catalog    

Is there a specific mnemonic that is not working or it all of them?    

Gary.
