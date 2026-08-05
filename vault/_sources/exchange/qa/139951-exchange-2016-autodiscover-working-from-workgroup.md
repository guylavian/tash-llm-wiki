---
title: "exchange 2016 autodiscover working from workgroup machines not from domain joined machines all on same lan"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/139951/exchange-2016-autodiscover-working-from-workgroup
question_id: 139951
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# exchange 2016 autodiscover working from workgroup machines not from domain joined machines all on same lan

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/139951/exchange-2016-autodiscover-working-from-workgroup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

from a client machine that is on a work group on the LAN i am able to connect to exchange through outlook   

this problem is only for outlook so i should be autodiscover, strangely from a domain joined machine it keeps asking for pwd?  

any thoughts

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-30*

during the profile creation outlook asks for pwd and never accepts it (yes)  

Do you mean that this phenomenon will not occur when bypass you NLB? (no) it will work over the NLB as well as directly, on 2 servers - other 2 are not working!  

Domain joined computer will use DC to DNS resolution, so have a check on DNS manager on your DC server, make sure all needed record could be resolution.(work group PC is having the same DNS  server on the NIC)

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-29*

Hi Kyle and sorry for the delayed response    

not able to create outlook profile keep asking for pwd    

the setup is as follows     

4 exchange severs all 2016 CU18     

2 working fine behind A10 NLB the others are the ones we have issues with and they are out of the NLB - not reachable to users     

i am trying to connect to those by chaining the hosts file to test - example 10.10.10.10 mail.mydomain.com    

so outlook wont go the the VIP DNS record     

during the profile creation outlook asks for pwd and never accepts it     

the moment i will change the hosts file to one of the other servers or remove the config - failing back to VIP - close out look and open it no pwd prompt

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-27*

@Maher Ramadan      

Do you try to reconfigure mailbox in Outlook on the domain-joined computer?    

If you cannot reconfigure Outlook profile, could you tell use which step that you get this issue? I also suggest you provide a screenshot about the log of "Test Email Autoconfiguration" to us, it will also help us to narrow down this issue:    

    

If you could recreate Outlook profile successfully but cannot open Outlook after configuration, or this issue occurs on step three (Log on the mail server) during configure Outlook profile, it means this issue doesn't related autodiscover. It may caused by the Outlook Anywhere/MAPI over HTTP in your organization, I would suggest you provide the result of command below to help us to narrow down the connection issue:    

```
Get-OutlookAnywhere -Server exch2016 | fl *Hostname,*Authentication*,*Ssl  
Get-OrganizationConfig | fl MapiHttpEnabled  
Get-MapiVirtualDirectory -Server exch2016 | fl *Authentication*,*url
```

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
