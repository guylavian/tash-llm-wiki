---
title: "Exchange 2016 post migration issue with Outlook 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/334733/exchange-2016-post-migration-issue-with-outlook-20
question_id: 334733
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 post migration issue with Outlook 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/334733/exchange-2016-post-migration-issue-with-outlook-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings all. I'm wrapping up a migration from on-prem Exchange 2010 to on-prem Exchange 2016. Specs are below: Exchange 2016 CU 18 Outlook 2016 Pro Plus 16.0.5134.100 32-bit Outlook 2019 Pro Plus 1808 10372.20060 64-bit We tried and failed to move public folders using the migration scripts. In terms of Outlook client functionality everything appeared fine up to that point. We then deleted the existing public folder deployment from 2010 and created a new empty structure on Exch 2016. The client then started importing everything in from PST which was also working fine. Weirdly, we observed that as soon as the new PFs came live on 2016 all of the Outlook 2019 clients started prompting for a password upon connection. The 2016 Outlook clients are fine. OWA is fine. When the Outlook 2019 user connects and is prompted all they have to do is click on the "Need Password: prompt at the bottom at which point the dialog goes away and they can work fine. Then at some point - 10m, 1 hr, 2hrs? - the prompt will reappear. We have tried everything from blowing away the profile, logging in on a new machine with a new profile, checking the RCP stats - everything looks normal and shows the Outlook 2019 users connected to the new single Exchange 2016 server. Any help would be greatly appreciated. Thanks.

## Answers

_No answers on this thread._
