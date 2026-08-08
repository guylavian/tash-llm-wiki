---
title: "Interpreting LDAP nslookup output"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/363609/interpreting-ldap-nslookup-output
question_id: 363609
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Interpreting LDAP nslookup output

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/363609/interpreting-ldap-nslookup-output (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
C:\Users\myuser1>nslookup
Default Server:  ns-xxx.xxxx.com
Address:  1xx.xx.x.x

> set types=all

> _ldap._tcp

Server:  ns-xxx.xxxx.com
Address:  1xx.xx.x.x

Non-authoritative answer:
_ldap._tcp.Tech.xyz.com   SRV service location:
          priority       = 0
          weight         = 100
          port           = 389
          svr hostname   = SRV82.Tech.xyz.com
_ldap._tcp.Tech.xyz.com   SRV service location:
          priority       = 0
          weight         = 100
          port           = 389
          svr hostname   = SRV61.Tech.xyz.com
_ldap._tcp.Tech.xyz.com   SRV service location:
          priority       = 0
          weight         = 100
          port           = 389
          svr hostname   = SRV62.Tech.xyz.com
_ldap._tcp.Tech.xyz.com   SRV service location:
          priority       = 0
          weight         = 100
          port           = 389
          svr hostname   = SRV41.Tech.xyz.com
_ldap._tcp.Tech.xyz.com   SRV service location:
          priority       = 0
          weight         = 100
          port           = 389
          svr hostname   = SRV42.Tech.xyz.com
_ldap._tcp.Tech.xyz.com   SRV service location:
          priority       = 0
          weight         = 100
          port           = 389
          svr hostname   = SRV43.Tech.xyz.com
_ldap._tcp.Tech.xyz.com   SRV service location:
          priority       = 0
          weight         = 100
          port           = 389
          svr hostname   = SRV44.Tech.xyz.com
.
.
.
.
```

This command is executed on my windows pc, which is a domain user of the domain that I am trying to find its LDAP server..

are those servers(srv82, srv61, ...) replicants/clones? so they all LDAP servers?

if that's the case, there must be a server(primary server) with a different domain name that load balances randomly the LDAP requests over these guys?! and idk if there is a particular command for finding that as well...?!

Thanks :)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-26*

Hi,  

I hope things are going well on your end. Since I have not heard from you, I assume you are quite busy and may not be able to make progress on this issue at this time. Based on this status of this case, I will go ahead to temporarily mark it as inactive at this time.  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-22*

Hi,  

How are things going? Could you please send me an update so that we can continue to work on this problem and resolve it ? Thanks for your help.  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-20*

Hi Aaron，    

Thank you for posting in our forum    

When the communication is initiated, the selected Domain Controller will check that the client computer belongs to its Active Directory site. This is done by comparing the IP address of the client computers with Active Directory configured sites and subnets. Here, there will be two possible scenarios:    

•	The Windows computer and the selected Domain Controller belong to the same Active Directory site: In this situation, the following will happen:     

o	The selected Domain Controller provides the client computer with the site name    

    

•  The Windows computer caches the name of its AD site and the name of the used Domain Controller. The selected Domain Controller will be used as long as it is available. The Windows computer no longer needs to re-do the localization process each time it needs to communicate with a Domain Controller.     

•  The Windows computer and the selected Domain Controller do not belong to the same Active Directory site: In this situation, the following will happen:     

•	The selected Domain Controller provides the client computer with the site name and informs it that it is not the closest Domain Controller    

    

Remark 1: If the Windows computer fails to communicate with a selected Domain Controller, it will try to contact another one according to the priority and weight assigned to the SRV records.    

Remark 2: If a Windows computer already has its AD site cached and would like to localize a new Domain Controller (Example: The current Domain Controller in use is no longer available) then it will start directly with Step number 7 (We refer to the steps shown in the previous figure)    

Remark 3: The Windows computer AD site is stored in the following registry entry: HKLM\System\CurrentControlSet\Services\Netlogon\Parameters\DynamicSiteName    

     

Hope this information can help you    

Best wishes    

Vicky
