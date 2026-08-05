---
title: "exchange 2013 cu 8 to cu 23 upgrade"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/317591/exchange-2013-cu-8-to-cu-23-upgrade
question_id: 317591
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# exchange 2013 cu 8 to cu 23 upgrade

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/317591/exchange-2013-cu-8-to-cu-23-upgrade (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. I have an exchange on-premises 2013 server environment like this: -Active Directory 1EA -Client Access 1EA (exchange 2013 cu8) -Mailbox Database 2EA (exchange 2013 cu8) The exchange version is 2013 CU 8. I am planning an upgrade to CU 23. During the upgrade process, There is setup.exe /prepareAD command execution. On which server should I execute this command? Case 1. When upgrading cu23 on a 3 EA server with cu 8 installed, execute it 3 times, one each. Case 2. Among the 3EA servers with cu 8 installed, after executing the setup.exe /prepareAD command only in 1EA, upgrade cu 23 without executing it on the rest of the servers. Case 3. Execute setup.exe /prepareAD only in Active Directory server. Which of the above 3 cases should I choose? Additional questions) Exchange 2013 When upgrading from cu 8 to cu 23, setup.exe /prepareschema Should I run this command too? As far as I know, the schema version is the same, so I don't think you need to run it, right?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

Hi,    

Normally the setup will aotumatically do the schema and AD updates for you, so it would be "case 4"- zero times, but personally I would always run those commands manually when upgrading (The computer where you'll run the command needs to be in the same Active Directory domain and site as the schema master. It'll also need to contact all of the domains in the forest on TCP port 389).    

Here is notes from official guidance:     

The AD preparation tasks are not required to be run separately to the upgrade of Exchange, unless in circumstances where you need to separate the tasks to different teams with different permissions, or if you have a multi-domain forest and want to control the AD changes.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
