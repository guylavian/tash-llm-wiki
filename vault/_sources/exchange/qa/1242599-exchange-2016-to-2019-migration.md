---
title: "Exchange 2016 to 2019 Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1242599/exchange-2016-to-2019-migration
question_id: 1242599
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 to 2019 Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1242599/exchange-2016-to-2019-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm in the process of standing up Exchange 2019 servers in order to migrate off of Exchange 2016.  I'm just trying to nail down the required steps to ensure that users don't connect to Exchange 2019 before the servers are fully configured and operational as I've seen clients in the past auto connect and get presented with certificate prompts.

-  Install Exchange 2019.

-  Set-ClientAccessService -AutoDiscoverServiceInternalUri https://Exchange2019Srv/Autodiscover/Autodiscover.xml

-  Import existing Exchange 2016 certificate on 2019 servers.

-  Configure all Virtual Directories to mirror Exchange 2016.

-  Create databases and DAGs.

-  Add Exchange 2019 to send connectors.

-  Lastly, add DNS records for the Exchange 2019 servers for autodiscover.

Following these steps, I shouldn't have clients connect to Exchange 2019 before step 7, correct?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-18*

Use https://setup.microsoft.com/; you will find the detailed step. 
Very clear step-by-step.
I would move mailboxes at any time since 2016 can proxy to 2019; however, after step 5 makes sense for the bulk moves. 
You must ensure the client URLs and certificates on the 2019 servers match 2016, move mailboxes, and remove the send connector on the 2016 side.
Ensure the 2019 servers have the necessary firewall ports open to external (25. 443) and that DNS records are also updated.
For deciding best migration path - https://www.infosecurity-magazine.com/blogs/best-migration-exchange-office-365/
Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.
