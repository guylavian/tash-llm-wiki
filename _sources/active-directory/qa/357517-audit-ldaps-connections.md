---
title: "Audit LDAPS connections"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/357517/audit-ldaps-connections
question_id: 357517
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Audit LDAPS connections

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/357517/audit-ldaps-connections (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have more and more Active directory migration to do and lot of customer ignore if they have applications with LDAPS or not.  

Is there a way to find all communications done with LDAPS protocol like it exists for ldap ?  

Network listener on 636 port could be use but not really easy to use during several days...  

If there is something to enable to see all source IP with ldaps communication it should be perfect :)  

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-16*

Hello @matteu31  ,    

Let's first be clear about what you want - do you want to log which clients use LDAP and TLS or just the clients that use LDAP and TLS by connecting to port 636? Connecting to port 636 is deprecated (see, for example, https://www.openldap.org/faq/data/cache/605.html) and the LDAP StartTLS is the preferred method (first connect to port 389 and then send a StartTLS request).    

If you want to log clients connecting to port 636, then logging traffic at the network level is probably the easiest way and can be done over weeks and months (the amount of data is modest). One way of doing this would be to issue the command:    

logman start LDAPS-Audit -ets -p Microsoft-Windows-TCPIP ut:TcpipListener -o LDAPS-Audit.etl    

This captures one event for each TCP "accept". It will log events for all ports, so it will need to be filtered for port 636. The event includes both local and remote addresses and ports and that is all that you seem to need.    

    

Gary

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-16*

Hello,  

I find lot of documentation about ldaps but it doesn't what I would like. In your link, we can identify what ldap connection are done WITHOUT ldaps. What I would like is, what connections are done WITH ldaps :) (if it exists ^^)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-15*

Hello  

Thank you for your answer.  

What you show here is audit connection but not ldaps only. 4624 is created when you logon with ldap also.  

The idea is to identify only ldaps connections.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-15*

Hello @matteu31  ,

Thank you for posting here.

Here is a test in my lab, I can audit LDAPS connections successfully.

Here are the steps for your reference.

I have a forest/root domain b.local (one DC named vchzho841vm) and a child domain bb.b.local (one DC dfs1, IP address192.168.2.75).

1.On DC in child domain, I logged on this DC using domain Administrator credential in child domain.

2.And I open ldp.exe (port 636, SSL)and connect to DC in the root doamin.  

3.Bind with BB\administrator.  

4.Then query someghing.

5.On DC the root domain, open Event Viewer and I can see Event ID 4624 with source IP and credential.

Here is a similar case, we can refer to it.

Log LDAP access of the Active directory  

https://serverfault.com/questions/193100/log-ldap-access-of-the-active-directory

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
