---
title: "Exchange 2016/hybrid ECP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1029634/exchange-2016-hybrid-ecp
question_id: 1029634
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016/hybrid ECP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1029634/exchange-2016-hybrid-ecp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Out of the blue I am unable to log into the Exchange ECP page. It brings up the logon page then thinks about it for a few seconds before giving me a 404.503 - Not found error.    

I recently updated to CU23, but after this I was able to log in just fine.     

The reason I need to log in is we found a shared mailbox we do not recognize, the email address is not in our namespace and I am unable to delete it in EOL because it is syncing from the on premises server. The mailbox appears to have been created before the CU23 update so it is not a case of someone hacking in, creating this and denying access.    

How can I fix the 404 error and is there another way to delete the shared mailbox without deleting all shared mailboxes?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-30*

So I solved both issues.    

ECP access - My boss had tried to add a filter to the IP address and domain restrictions in IIS, but had then left Edit Feature Settings disabled. As soon as this was enabled access to ECP came back.    

The rogue shared email - I gave the AD account an O365 license, changed the mail, proxy addresses and target address attributes so he had a primary address within our namespace, waited for AADC to sync and for EOL to show the changes. I then converted the now valid shared mailbox  to a user mailbox, removed the license and waited for the AADC sync to run again. The mailbox has gone away.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-29*

Hi there.    

So  I would use on-prem Powershell and connect to the on-prem Exch Server    

https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-servers-using-remote-powershell?view=exchange-ps#connect-to-a-remote-exchange-server    

then run:    

https://learn.microsoft.com/en-us/powershell/module/exchange/disable-remotemailbox?view=exchange-ps    

```
Disable-RemoteMailbox 
```

that will remove the shared mailbox in Exchange Online once it syncs via AADConnect,  but leave the AD Account intact.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-29*

Depends on what you mean by delete:

-   Delete the AD Account on-prem or run  

    Remove-RemoteMailbox <shared Maibox>  

    on-prem Exchange Powershell    https://learn.microsoft.com/en-us/powershell/module/exchange/remove-remotemailbox?view=exchange-ps

-   Or move the AD account to an OU that isnt sycned to Azure. the AD Account will remain but just not in Azure

-   You can mail disable the remote mailbox on-prem as well which leaves the AD Account intact:    https://learn.microsoft.com/en-us/powershell/module/exchange/disable-remotemailbox?view=exchange-ps
