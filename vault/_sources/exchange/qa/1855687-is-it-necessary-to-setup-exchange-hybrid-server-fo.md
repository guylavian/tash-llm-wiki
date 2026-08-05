---
title: "Is it necessary to setup exchange hybrid server for exchange online mailbox management?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1855687/is-it-necessary-to-setup-exchange-hybrid-server-fo
question_id: 1855687
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Is it necessary to setup exchange hybrid server for exchange online mailbox management?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1855687/is-it-necessary-to-setup-exchange-hybrid-server-fo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have a exchange 2003 environment and want to move the mailbox to exchange online. If we need to migrate mailbox to EXO, it needs to:

-  migrate exchange to exchange 2010

-  move all mailbox to exchange 2010

-  setup AADC to sync AD user 

-  setup exchange hybrid to move the mailbox from exchange 2010 to EXO

-  migrate exchange 2010 to exchange 2016 for the EXO mailbox management

As migrate exchange 2003 to 2010 may have problem and need to migrate mailbox 2 times (EX2003 > EX2010 > EXO). We have an idea (option 2) that just export the exchange 2003 mailbox and create mailbox in EXO:

-  Export mailbox to .pst

-  setup AADC to sync AD user

-  Create mailbox on EXO directly

-  Add .pst in user outlook profile 

So, if option 2 is work, do we need to setup a new exchange 2016 for EXO mailbox management? 

As if setup exchange 2016 is necessary for the management, we need to decommission exchange 2003 and then setup a new exchange 2016 server for hybrid.

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-08-07*

See, you can do with both options but it depends upon if you need Exchange 2016 or not.

You need to setup Exchange 2016 if you want to manage Exchange Online mailboxes from on-premises. But if you can manage everything directly through EXO there is no need for hybrid functionalities.

If we compare, then direct migration with PST is simpler to option 1 which is more complex due to multiple migration.
