---
title: "Rename Primary Domain Controller windows server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/244388/rename-primary-domain-controller-windows-server-20
question_id: 244388
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Rename Primary Domain Controller windows server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/244388/rename-primary-domain-controller-windows-server-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have a Windows Server 2019 as a Primary Domain Controller, I renamed it by following the instructions from here https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc794951(v=ws.10)?redirectedfrom=MSDN

I renamed the server using netdom and after renaming it server successfully I noticed a couple of errors below after rebooting the server. Although the error states that it will retry after 60 min however I don't see the error after that. I also restarted the Active Directory Domain Services manually the service restarted successfully without those errors. Any ideas to resolve these issues?

-   This computer is now hosting the specified directory instance, but Active Directory Web Services could not service it. Active Directory Web Services will retry this operation periodically.    Directory instance: NTDS  

    Directory instance LDAP port: 389  

    Directory instance SSL port: 636

-   The DFS Replication service failed to contact domain controller to access configuration information. Replication is stopped. The service will try again during the next configuration polling cycle, which will occur in 60 minutes. This event can be caused by TCP/IP connectivity, firewall, Active Directory Domain Services, or DNS issues.

Additional Information:  

Error: 160 (One or more arguments are not correct.)

Thanks in advance.  

John

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-01*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-28*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-25*

Simplest solution may be to transfer the roles to another healthy one, decommission / demote / rebuild this one with the desired naming.  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-25*

HI @Anonymous  ,    

Thanks for providing the info, I did try adding entry to registry ie Parent Computer = "dc1.xcompany.com" but for some reason the registry I added disappears after rebooting the server. Any idea?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-25*

These ones might help.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/newly-promoted-domain-controller-fail-advertise    

https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/active-directory-web-services-event-1202/ba-p/1514401    

--please don't forget to Accept as answer if the reply is helpful--
