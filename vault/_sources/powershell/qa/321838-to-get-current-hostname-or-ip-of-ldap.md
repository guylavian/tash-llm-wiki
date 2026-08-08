---
title: "to get current hostname or IP of LDAP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/321838/to-get-current-hostname-or-ip-of-ldap
question_id: 321838
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# to get current hostname or IP of LDAP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/321838/to-get-current-hostname-or-ip-of-ldap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

is that possible to get current hostname or IP of LDAP using by an application on the MS Server 2016?  

Sometimes one of the LDPA is down and application stops authentication and workaround is only clearing of DNS cache ipconfig /flushdns.  

I need to create a Power Shell for that, but I have no idea how to set variable with the name or IP address of the existing using LDAP server.  

Can you help please?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-03-22*

Hi,    

Thanks for posting in Q&A platform.    

Please try if `nslookup -type=srv _ldap._tcp.DOMAINNAME` or `nslookup -query=srv _ldap._tcp.DOMAINNAME` can help you.    

Best Regards,    

Sunny    

----------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-19*

Clear-DnsClientCache is the PowerShell equivalent of "ipconfig /flushdns"   

Is the machine on which you want to clear the cache the LDAP server or is it on a machine that uses the LDAP server? Neither "ipconfig /flushdns" nor Clear-DnsClientCache take any parameters, so it isn't clear why you want to get the IP address (or name) into a variable.  

How do you discover which machine needs to have its DNS cache cleared now? And how do you propose to execute a PowerShell script on the target machine?
