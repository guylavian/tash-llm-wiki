---
title: "[Migrated from MSDN Exchange Dev] stumped on mail flow rule to emilinate duplicate disclaimers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/205381/migrated-from-msdn-exchange-dev-stumped-on-mail-fl
question_id: 205381
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] stumped on mail flow rule to emilinate duplicate disclaimers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/205381/migrated-from-msdn-exchange-dev-stumped-on-mail-fl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link] stumped on mail flow rule to emilinate duplicate disclaimers  

I'm trying to set up a mail flow rule on exchange admin center. We use office 365.  

I have added the confidentiality disclaimer, but I am trying to eliminate duplicate disclaimers from stacking up. It don't want to add the exception "exceptif subject contains RE: or FW:"  

I want the disclaimer applied if it is not already there. To do this, I have added a header "X-Disclaimer" and set the value to "Yes". then added the exception "exceptif header X-Disclaimer matches the text pattern 'Yes'"  I can confirm that the header is being applied, but it is still duplicating the disclaimer. Any help would be appreciated.  

Do the following...  

Set audit severity level to 'Do not audit' and Append the message with the disclaimer '…'.  

If the disclaimer can't be applied, take no action.  

and set message header 'X-Disclaimer' with the value 'Yes'  

Except if...  

'X-Disclaimer' header matches the following patterns: 'Yes'  

Rule comments  

Rule mode  

Enforce  

Additional properties  

Sender address matches: Header or envelope  

Version: 15.0.1.0

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-21*

Hi,    

I have tried in my environment, you could try using the below configuration to make your rule above work:    

Except if...    

'X-Disclaimer' header contains ''Yes''    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
