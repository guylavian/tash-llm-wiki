---
title: "Empty Sysvol and Missing Netlogon after Migrating to Win2019 DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/625535/empty-sysvol-and-missing-netlogon-after-migrating
question_id: 625535
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Empty Sysvol and Missing Netlogon after Migrating to Win2019 DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/625535/empty-sysvol-and-missing-netlogon-after-migrating (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

After transferring FSMO roles from 2012 to 2019 and demoting 2012, Sysvol is empty and the Netlogon folder is missing in 2019 DC. There is only one DC running now which is 2019 but the status of the SysVol registry keys are still showing the new DC under seeding container.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-12*

After transferring FSMO roles from 2012 to 2019 and demoting 2012, Sysvol is empty and the Netlogon folder  

That may have been a fatal move. There is nothing to do here, you can try a complete rebuild but no guarantees.  

https://gist.github.com/RavuAlHemio/00e51d3ea64731be9d43b01eda18734f  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-12*

I found the Policies folder in the demoted DC. Isn't it enough to copy the policies to the new dc or do I still have to go for NON-authoritative restoration?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-12*

C:\>repadmin /replsummary  

Replication Summary Start Time: 2021-11-12 21:21:38

Beginning data collection for replication summary, this may take awhile:  

....

Source DSA largest delta fails/total %% error

Destination DSA largest delta fails/total %% error

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-12*

post the output of a repadmin /replsummary please
