---
title: "Exchange Management Shell not working after Exchange 2019 CU14 install"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1605447/exchange-management-shell-not-working-after-exchan
question_id: 1605447
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Management Shell not working after Exchange 2019 CU14 install

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1605447/exchange-management-shell-not-working-after-exchan (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Installed CU14 on a 2019 Exchange server. It is only used for SMTP relay and does not host any mailboxes. I am now getting this error when attempting to go into the management shell:  

New-PSSession : [server.domain.com] Connecting to remote server server.domain.com failed with the following error message : The WinRM client cannot process the request. It cannot determine the content type of the HTTP response from the destination computer. The content type is absent or invalid. For more information, see the about_Remote_Troubleshooting Help topic.

Also getting error from ECP:  

The following information can be helpful to determine why the assembly 'Microsoft.Exchange.Clients.Strings, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' could not be loaded.

I've confirmed the certificate is in the IIS bindings on the Backend Web Site. Also ran UpdateCAS.ps1 and UpdateConfigFiles.ps1 but still having the issue. Hoping someone here can help before opening a ticket with Microsoft.

Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-03-01*

Did you ensure that you met all the EP requirements before applying CU14?

https://techcommunity.microsoft.com/t5/exchange-team-blog/released-2024-h1-cumulative-update-for-exchange-server/ba-p/4047506
