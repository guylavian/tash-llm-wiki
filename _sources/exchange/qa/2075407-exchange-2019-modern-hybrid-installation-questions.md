---
title: "Exchange 2019 Modern Hybrid Installation Questions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2075407/exchange-2019-modern-hybrid-installation-questions
question_id: 2075407
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 Modern Hybrid Installation Questions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2075407/exchange-2019-modern-hybrid-installation-questions (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Plan is to migrate to EOL from EOP 2016. No mailboxes or SMTP connectors will be left on site. EOP will be strictly for management.

I will need to migrate 2016 to 2019 on a temp box, then do another 2019 install on the permanent box that will also host Entra Connect Sync.

The first install on the temp box, I am guessing will be a full install and I will move the 3rd party cert before I decommission the 2016 box.

It is the installation to the permanent box I have questions about. Since it will be pretty much a management only box and the installation on the temp serve will be removed:

Can I install ex2019 with only minimal roles on the perm box?

What roles are required to maintain the modern hybrid management server EOP? Mailbox? CAS?

On the permanent server will I need to do a full install with hybrid until the temp ex2019 server is installed? Then remove the roles I don't need?

Do I really need to have a 3rd party cert for the EOP management server since NO ports will be open to the server?

Do I have a need to keep Split DNS on prem for the autodiscover. or mail. records? 

I see that some people say yes and no to the cert in my research. I have not been able to find something on the minimal install of exchange required.

I want to keep the EOP hybrid for a few months to see if I really need it, then when ex2019 goes end of life next year, I can decide what I am going to do since we will likely not want to spend money on maintaining an EOP presence as well as EOL.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-23*

Hi, @BP-7667  

Welcome back to the forum!

I'd like to offer some advice for you planning to migrate from EOP 2016 to EOL and install and configure Exchange 2019 on your persistent servers:

-  You can install only the minimum roles required for management. In order to maintain a modern hybrid management server EOP, the roles you need include mailbox roles and CAS, which are critical for managing mail flow and client connectivity. You can refer to step 8 in this article Install Exchange Mailbox servers using the Setup wizard | Microsoft Learn

-  On a permanent server, you need to first do a full installation with a hybrid configuration. Once a temporary Exchange 2019 server is decommissioned, while you can't selectively remove roles, you can disable or retire features that are not needed for management after the migration is stable, an approach that ensures that all necessary components are in place during the transition.

-  If the server does not have an open port, a third-party certificate is not required, but it is generally recommended to use a third-party certificate for secure communication and administrative purposes. Even if the server is not exposed, having a third-party certificate can help avoid potential problems in internal communication and management tasks.

-  If all mailboxes have been migrated to Exchange Online and no clients are connected to the on-premises Exchange server, you don't need to maintain split DNS or internal auto-discovery records that point to the on-premises server. However, autodiscovery is still used for some features in hybrid environments. We recommend that you point your autodiscover DNS records to Exchange Online to ensure that clients are connected correctly.

-  For detailed steps on the minimum installation of Exchange 2019, you can refer to the Exchange 2019 Build Guide. The guide provides detailed steps on how to configure the necessary roles and services Exchange Server 2019 system requirements, Exchange 2019 Requirements, Exchange 2019 Memory Requirements, Exchange 2019 Client Compatibility | Microsoft Learn

-  If you decide that you no longer need your on-premises Exchange server after a full migration to Exchange Online, you may consider retiring it. However, with Entra Connect Sync, recipient management becomes more complex without an on-premises Exchange server. You can try to manage it with the Exchange recipient management tool without the need for a local full Exchange server Manage recipients in Exchange Server 2019 Hybrid environments | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
