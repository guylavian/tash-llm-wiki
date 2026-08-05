---
title: "Error 500 new on-prem exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/368228/error-500-new-on-prem-exchange-2019
question_id: 368228
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Error 500 new on-prem exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/368228/error-500-new-on-prem-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are upgrading our exch 2016 to 2019. It's a hybrid environment with no on-prem mailboxes. Mails still flow through the local exchange though. I have updated dns entries n emails are flowing seemless through the new server.   

The issue:  

When I shutdown the 2016 exch, I can no longer login to ecp from server 2019 using https://fqdn/ecp or https://mail.domain/ecp . After I login with correct creds it presents "http error 500 server is currently unable to handle this request". I have recreated virtual directories on the new server via powershell but not getting anywhere.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2021-04-23*

Hi @as-1m       

Agree with Andy, please run this command Get-Mailbox -arbitration via EMS to check if the arbitration mailboxes are still on the Exchange 2016 server.    

If there are some, you may need to move them to the Exchange 2019 server.    

The cause of the issue may probably be the system mailboxes(Arbitration mailboxes) are unavailable, which are responsible for admin accounts without a mailbox to log in EAC.    

For more information on this topic, please refer to this link: HTTP 500 Internal Server Error when logging into Exchange 2013 Exchange Control Panel (ECP)    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-23*

It definitely was arbitration mailboxes. They were still on the 2016 server.   

Migrating them over fixed the prob
