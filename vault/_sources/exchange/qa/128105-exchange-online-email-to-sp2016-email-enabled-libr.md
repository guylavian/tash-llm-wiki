---
title: "Exchange Online email to SP2016 email enabled library not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/128105/exchange-online-email-to-sp2016-email-enabled-libr
question_id: 128105
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-server-business", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Exchange Online email to SP2016 email enabled library not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/128105/exchange-online-email-to-sp2016-email-enabled-libr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We're testing Exchange Online functionality with SharePoint on prem 2016.     

When I'm sending an email with attachment from my scogordo@CONDOR  .com Outlook account to a SharePoint TestEmail library enabled to receive Incoming email to testEmail@CONDOR  .com, the TestEmail library receives and displays attachment.    

When doing the same with a test scogordoEXO@CONDOR  .com Exchange Online account, I don't see the item in the DROP folder nor does it arrive in TestEmail.    

I've verified that scogordoEXO@CONDOR  .com is an On Prem AD account with an EXO email address.    

What to check?    

Thanks!

## Answer (community) — community member

*upvotes: 1 · updated: 2020-10-16*

Hi @sco gordo       

Is there any problem if you use this exchange online account to send other emails?    

Please make sure that the exchange online account can be used normally in the environment.    

In addition, what configuration does your local exchange server use? Is hybrid configured?    

Looking forward to hearing from you.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
