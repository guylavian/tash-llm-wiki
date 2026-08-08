---
title: "Exchange and Interesting Draft Emails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1023551/exchange-and-interesting-draft-emails
question_id: 1023551
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange and Interesting Draft Emails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1023551/exchange-and-interesting-draft-emails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are having something interesting happen with our Outlooks.    

A string of draft emails will pop up in all users draft boxes. They all have the title "Microsoft Outlook Test message XXXXXXX" The Xs are a random numbers.    

Our exchange server is patched up to CU22, and we have AV running, and we are behind a firewall.    

I reached out to a cyber contractor we have and they suspected compromise and we went through the list of remediation for malicious activity - checking for webshells, hidden accounts, mailboxes, checking logs for scripts, running the EOMT.ps1 and doing a full scan with our AV. Nothing found, they kept our ticket open and told me to keep an eye on it.    

A week later we all have a few more in our draft folders. Thought I would look out a little further for assistance.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-03*

Hi @TempDRK      

Thanks for sharing more information about this issue.    

You may also take a reference at the recent blogs about     

Analyzing attacks using the Exchange vulnerabilities CVE-2022-41040 and CVE-2022-41082    

Customer Guidance for Reported Zero-day Vulnerabilities in Microsoft Exchange Server    

Installing the latest SU and mitigation tools are the suggested way by Microsoft.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-30*

We were hit by ProxyShell.    

We have since patched and used mitigation tools.
