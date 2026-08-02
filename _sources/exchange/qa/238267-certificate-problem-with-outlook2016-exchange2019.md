---
title: "Certificate problem with Outlook2016 / Exchange2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/238267/certificate-problem-with-outlook2016-exchange2019
question_id: 238267
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Certificate problem with Outlook2016 / Exchange2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/238267/certificate-problem-with-outlook2016-exchange2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I have deployed Exchange 2019 in our environment, two servers, Mail-1 and Mail-2 in primary site and one, Mail-3 on secondary site, in DAG configuration and site resilience. They are all deployed with PKI certificate (ex: mail."company".com). Internal domain is company.local. I have problem with Outlook 2016, although its connected successfully with Exchange and mail can be sent and receive, on every Outlook start, I have certificate error and sometimes its ask me for credential. ![58781-1.jpg][1] All the time is pointing me to servers with local suffix. On Exchange servers, I did configure virtual directories, for OWA, ECP and MAPI with public url: ![58674-2.jpg][2] I did consult a lot of forum, but nothing helps. Anyone? Best regards, [1]: /api/attachments/58781-1.jpg?platform=QnA [2]: /api/attachments/58674-2.jpg?platform=QnA

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-21*

Hi @Aleksandar Babakov      

Is there any update about your issue? Have you tried running the iisreset command in your environment and verify the result again?    

Yes we should use the external name as well for internal urls, since .local cannot be added to a certificate    

Here is also a related thread for your reference, which lists all the configuration we need to check in detail: security warning on SSL certificate displaying internal server name    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-20*

Get-ClientAccessService | select name,autodiscoverserviceinternaluri:    

    

Certificate is with *.company.com, so its contain mail.company.com.    

I did additional changes to virtual directories, as suggested. All url, public and internal, are set with https://mail.company.com/.....    

Same thin again. Now only receive cert error for Mail-1.company.local and mail.company.local.    

Do I need to make restart on the Exchange servers, after making this changes?    

Best regards,    

Aleksandar B.
