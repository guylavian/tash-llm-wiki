---
title: "How to remove decommissioned Exchange 2013 servers?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1382425/how-to-remove-decommissioned-exchange-2013-servers
question_id: 1382425
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# How to remove decommissioned Exchange 2013 servers?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1382425/how-to-remove-decommissioned-exchange-2013-servers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

First my initial setup:

-  Hybrid with all mailboxes in the cloud

-  2 x Exchange 2013 servers just to relay email from internal apps to O365

Change:

-  With Ex2013 EOL, I added 2 x Exchange 2019 servers to the Org

-  Configured internal apps to relay thru these new servers fine

-  Using the console to create/manage mailbox settings for AD Sync to send to O365 

-  No mailboxes on-prem 

3 months ago I shutdown the 2 x Exchange 2013 servers (scream test passed), no complains, all services running fine via the new 2 x Exchange 2019 servers.

Last month we deleted the 2 x Exchange 2013 server VMs... not sure if this was a good idea as I now noticed that these servers still show on the EAC.

-  Is there a way to do a clean removal from the Org (and from the console)?

-  The Hybrid setup was done via one of these servers (now deleted and offline for 3 months) will this be affected? I don't think so since all is working with the server down but not sure if any references are being made back to the on-prem Org? 

Thanks! M

## Answers

_No answers on this thread._
