---
title: "Exchange Auditing and Quarantine question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2126257/exchange-auditing-and-quarantine-question
question_id: 2126257
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Auditing and Quarantine question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2126257/exchange-auditing-and-quarantine-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone ,

first of all I am sorry if this has been answered before but I really could not find the answer or

similar topic.

I have a big issue that persists over some years but I left it because I did not need that functionality,

but know I really need it.

I have 4 Exchange server 2016 , with more than 5000 users. And I live in a country where people have multiple nationality.

I have all servers set up to the last CU and SU .

The Problem is as following :

I needed to set up the audit on Exchange , and sadly it does not work like intended . If you put in a parameter you get an empty answer . If you put in the Command Search-AdminAuditLog whitout parameter it is working to an extend.

So I researched this issue and saw that a fix is there with a CU , but this didnt solve the problem as I was up to date. So I had to do the recommended work around , with the regional settings.

https://learn.microsoft.com/en-us/exchange/troubleshoot/compliance/search-adminauditlog-mailboxauditlog-return-no-result

With this the admin audit search worked but I got another big problem with this. And this issue I could not see it at any other place documented.

The Users on the several Exchange servers got put their mailbox into Quarantine (not all users).

So when an user send an email to an person that was affected got an reply that the message could not be delivered, because the inbox is in quarantine. Upon further investigation I found out that the users had a common setting in the regional / local settings EN-150 .

Taking an user out of it , makes him go in after a while automatically.

And I had to revert the changes I did with the configuration of the regional settings on the servers , so that the users do not get quarantined anymore.

But now I still cannot do any audit search.

So I desperately need help in this regard if possible please.

Thanks a lot in Advance

Best Regards

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-05*

Hi, @sgtDaniele  

It sounds like you're dealing with a complex issue involving Exchange audit logs and user mailboxes being quarantined due to locale.

Here are some suggestions:

-  Make sure that the CU you are applying is the latest CU for your version of Exchange. Sometimes, CUs may not be applied correctly, so double-check the installation logs.

-  Consider using the Search-UnifiedAuditLog command as an alternative, as it may provide more consistent results.

-  When the mailbox enters quarantine, check the event logs and Exchange logs for any specific errors or warnings.

-  Make sure there is no group policy to force the locale to be changed to "EN-150". Check that the user profile contains the "EN-150" setting. Sometimes, settings in the registry can cause the locale to be automatically restored.

-  If none of the above methods resolve the issue, it is recommended to contact the Microsoft support team to provide them with more comprehensive logs. Find Microsoft 365 for business support phone numbers by country or region - Microsoft 365 admin | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
