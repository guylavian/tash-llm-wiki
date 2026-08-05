---
title: "Admin accounts cannot access ECP, Exchange 2019 CU12"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1182381/admin-accounts-cannot-access-ecp-exchange-2019-cu1
question_id: 1182381
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Admin accounts cannot access ECP, Exchange 2019 CU12

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1182381/admin-accounts-cannot-access-ecp-exchange-2019-cu1 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We migrated from Exchange 2010 to Exchange 2019 CU12. But none of original Org Management access accounts get access the ECP. We all get an http 500 error. I created a brand-new account and that works fine. The new account has a mailbox On Prem, but all the old admin accounts mailboxes are in O365. Any ideas on how to resolve this? I just looked through ADSI Edit, nothing jumped out at me, but there has to be something weird going on when I try to log into ECP from those accounts it immediately gives an http 500 error, doesn't even think about it.

I tried to access with this address https://SERVERNAME/ecp/?ExchClientVer=15.2 as well.

This is only using for SMTP relay and remote mailbox management.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-02-22*

it has been resolved now. issue was related to system mailbox which were missing.  I used the following command which is mentioned the article https://social.technet.microsoft.com/Forums/en-US/b9a99e81-2e0d-4d26-b408-1f78c66946e2/administrators-cannot-login-to-ecp and it works for me.

get-aduser -filter "Name -like 'SystemMailbox*'" -Server xxxxxxx -Property Mail | ? {$.mail -eq $null} | Foreach {Enable-Mailbox $.DistinguishedName -Database xx-DAGN1-xxx001}
