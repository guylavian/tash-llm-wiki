---
title: "Exchange On-Prem Server Database disk space full"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1305009/exchange-on-prem-server-database-disk-space-full
question_id: 1305009
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange On-Prem Server Database disk space full

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1305009/exchange-on-prem-server-database-disk-space-full (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I am in need of help ASAP, we currently have a single Exchange Server and the Disk Drive where the Database lives is full and I was wondering if it is possible to move the database and log files to anotehr drive, if I run the Move-Database "DBName" -EDBFilePath "NewPath" -LogFolderPath "NewPath"    will this destroy my email database or what steps / services need to be off, can I maybe move the Database to one Drive while moving the LogFolderPath to a seperate drive? I need help asap is someone can even provide a phone number to MS Support to talk with ACTUAL PEOPLE I have tried every number I can find and all I get is automation, why does MS Support suck so much? WE ARE WILLING TO PAY FOR HELP WITH THIS ISSUE.

Please help, you can call me at: <phone number removed for security> (Cell) my name is MARK, I am in a desperate crush, mailflow has stopped due to space issues.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-16*

As a follow up to this issue, it has been resolved by me, MICROSOFT WAS USELESS AND I COULDN'T EVEN TALK TO A REAL HUMAN. I moved my mailbox database to a new larger drive and ran several eseutil commands to verify health and wellness of all the databases and once repaired I re-mounted the mailbox database, Archive Database, and Public Folders and the mailflow is now successful, although after this maybe three days later all of our users are now unable to send or recieve emails from Gmail, this is really strange!!! Hybrid exchange users who are using MS 365 can send to Gmail but not receive, on-prem users can not send nor recieve only from Gmail, all others are recieved no problem. After rsearching this it appears that this has Been an issue with Exchange for some time.... Microsoft again...lol if I had enough pull I would completely elimiate all things MS they are worthless....

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-14*

I have called the number 4 times on this site and I never get a human, it is usless as with everything MS we are paying for support but can never seem to get any, waste of money, we have to resort to third party support since MS does help!!! Provide me a phone number with actual support people and I’d call. Please only respond with relevant information!
