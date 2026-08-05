---
title: "Exchange 2016 Management Shell failed to connect after install the Windows Server Nov 2022 patch"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1094463/exchange-2016-management-shell-failed-to-connect-a
question_id: 1094463
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 Management Shell failed to connect after install the Windows Server Nov 2022 patch

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1094463/exchange-2016-management-shell-failed-to-connect-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,    

We have 2 Exchange 2016 servers install in Windows Server 2016. We just install the Windows Server patch KB5019964 and KB5017396 in one of the Exchange servers. After restart, the Exchange Management Shell failed to connect but no detail error message:     

Connecting to remote server XXXXX failed with the following error message:    For more information, see the about_remote_troubleshooting Help topic    

    

Seems other exchange services are working fine, only the EMS failed to connect. We tried to uninstall the patch but problem still exist.    

Any idea?    

Best Regards    

Chong

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-18*

Please check if there are some redirecting settings on the default website and on the Powershell virtual directory in IIS manager.    

Also check this article for more insight - https://www.bleepingcomputer.com/news/microsoft/windows-kerberos-authentication-breaks-after-november-updates/
