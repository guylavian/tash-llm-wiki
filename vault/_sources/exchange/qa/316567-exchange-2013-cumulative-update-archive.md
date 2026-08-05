---
title: "Exchange 2013 Cumulative Update Archive"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/316567/exchange-2013-cumulative-update-archive
question_id: 316567
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 Cumulative Update Archive

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/316567/exchange-2013-cumulative-update-archive (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Morning All, I am facing on-going challenges with patching Exchange Server 2013, in several instances I have been unable to install CU23 and then the Security Update due to the C:\Windows\Installer Folder having been cleared out. At present the issue I have is not being able to download CU8, CU10. and CU13 as Microsoft no longer seem to offer a link to download them. Unfortunately I require these to have come from a verified source i.e. the manufacture "Microsoft" I cannot download them from just any site. Does Microsoft have a source that they can confirm is safe where I can get these from please. Thanks Chris

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

Hi @Chris Wager      

According to Microsoft policies, only the 2 latest CUs are support. In your scenario, I would suggest you deploy the new Exchange server(s) in your environment to replace the old server(s) then uninstall the old server(s).    

Or you may try the solution introduced here: Recover an Exchange Server    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
