---
title: "Exchange 2019 CU8 Connectivity Issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/411064/exchange-2019-cu8-connectivity-issues
question_id: 411064
fetched: 2026-07-25
answer_count: 11
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 CU8 Connectivity Issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/411064/exchange-2019-cu8-connectivity-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, we are running Exchange 2019 CU8 in a 2 node DAG with 300+ mailboxes.  We have just recently upgraded from 2013 in March because of the zero-day exploit.  The migration went well, but we are now having intermittent connectivity issues with slow sync speeds.   

Here are the issues that have been reported:   

Outlook on Windows - messages getting stuck in the Outbox.  

Outlook on Mac users are getting "An unknown error has occurred in Outlook." "Mail could not be sent." "Error code: -17884" - This happens a lot.  

OWA will show all folders and sub-folders, but the Outlook application does not.  

Sending emails with attachment (nothing that large) take over a minute and sometimes fail.  

In general, folder syncs seem to be a lot slower.  

I have checked and made sure that all FQDNs are correct for all virtual directories and Outlook Anywhere.  

I have checked and made sure that MAPI over HTTP is enabled for everyone.  

I have run the Healthchecker.ps1, and everything looks good.  

I am running out of ideas here.  I was debating about updating to CU9, but I wanted to make this post first and see what recommendations we get.  

I really appreciate any help you can provide,  

Michael

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-27*

I've done some more testing and the non MAPI over HTTP and it is defiantly better for Windows machine, but no change for Mac users.  Any way to make the to improve the Mac users?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-27*

You are correct, we did not have issues on 2013.  Only on after we upgraded.  

Also, I think the non-MAPI connection is working better for PCs, but not for Mac clients.  Is there any way to test to see what connection the Mac client is using?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-26*

Hi Andy,  

I have tried that and it has not help, but maybe I am missing something.  

Other than PS command (Set-CasMailbox <user or mailbox ID> -MapiHttpEnabled $false) and restarting Outlook is there anything else I need to do to make sure that MAPI is not enable for that user?  

Michael

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-26*

Disable MAPI over HTTP for a test user and see if that improves things for that user  

```
Set-CasMailbox  -MapiHttpEnabled $false
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-26*

Also, I thought this might be helpful. I have run the Get-ActiveExchangeUsers.ps1 script and got the following results:  

Get-ActiveExchangeUsers.ps1 -Summary  

Outlook Web App : 43  

ActiveSync      : 183  

OutlookAnywhere : 4  

RPC User Count  : 45  

EWS User Count  : 163  

MAPI User Count : 10  

MAPI FE AppPool : 0  

MAPI BE AppPool : 0  

Get-ActiveExchangeUsers.ps1 -HTTPProxyAVGLatency  

Server          : Server1  

Autodiscover    : 4  

EAS             : 3  

EWS             : 63  

MAPI over Http  : 3  

OutlookAnywhere : 4364  

OWA             : 3  

OWACalendar     : 1  

ECP             : 0  

Powershell      : 3  

OAB             : 7  

Server          : Server2  

Autodiscover    : 3  

EAS             : 98  

EWS             : 2  

MAPI over Http  : 3  

OutlookAnywhere : 6287  

OWA             : 17  

OWACalendar     : 3  

ECP             : 0  

Powershell      : 3  

OAB             : 5
