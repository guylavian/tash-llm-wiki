---
title: "Error in  ExchangeServer Setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1031799/error-in-exchangeserver-setup
question_id: 1031799
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Error in  ExchangeServer Setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1031799/error-in-exchangeserver-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question



## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-04*

It seems like a permission issue. Would you try the solutions in the following links:    

Exchange Server Troubleshooting: Unable to upgrade with error code '3221684229'    

update Exchange 2016 to CU 9, update Mailbox Role Access Denied Error?    

Exchange Service Pack or Rollup or Cumulative Update fails with error code '3221684229' and message 'Access is denied.'    

Also, check this thread for help - https://learn.microsoft.com/en-us/answers/questions/774581/ms-exchange-2019-install-error-active-directory-op.html

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-03*

Hi @Netanel.Amran   ,    

Could you describe your AD environment? Is it a fresh installation?    

Based on the error messages, I have found a similar thread on your issue and the solution is Install exchange server in unattended mode or run setup.exe as administrator. Check if above solution work for you.    

Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /mode:Install /r:MB    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-02*

Hi @Netanel.Amran  ,    

Have you run the setup process as administrator?
