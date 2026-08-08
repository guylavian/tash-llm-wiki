---
title: "[Migrated from MSDN Exchange Dev] Edge server support in hybrid deployment with centralized mail flow"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/134639/migrated-from-msdn-exchange-dev-edge-server-suppor
question_id: 134639
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# [Migrated from MSDN Exchange Dev] Edge server support in hybrid deployment with centralized mail flow

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/134639/migrated-from-msdn-exchange-dev-edge-server-suppor (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone,

Is the edge server supported supported in a hybrid deployment with centralized mail flow? Yes or No?

I Have configured edge server and bellow is the mail flow status

Mail from On-prem mailbox to on cloud mailbox: Success  

Mail from On-Cloud to On-Prem: Success  

Mail from external recipient to on cloud: Success  

Mail from on cloud to external recipient: Fail  

For the last scenario my edge server is rejecting internet bound messages from EOP with the error 550.5.7.4 unable to relay recipient in non-accepted domain.

I then gave the ms-Exch-SMTP-Accept-Any-Recipient extended rights on the edge server receive connector. This time the mails went trough EOP but then got stuck on the edge server where now I am receiving the error A matching connector cannot be found to route the external recipient.

I even changed the domain to * in the edge sync connector but after doing so all the emails in queue got flushed with an NDR message, interestingly those NDR's were not delivered to the cloud user where the mail had originated from

Source link: https://social.msdn.microsoft.com/Forums/office/en-US/b14b2184-9ff7-4821-a9eb-eeeff5c3930b/edge-server-support-in-hybrid-deployment-with-centralized-mail-flow?forum=exchangesvrdevelopment

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-22*

Thank you very much...that answers my question
