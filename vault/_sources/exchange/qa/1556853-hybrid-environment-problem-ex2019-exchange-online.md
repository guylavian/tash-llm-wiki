---
title: "Hybrid environment problem Ex2019 - Exchange Online 365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1556853/hybrid-environment-problem-ex2019-exchange-online
question_id: 1556853
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Hybrid environment problem Ex2019 - Exchange Online 365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1556853/hybrid-environment-problem-ex2019-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning dear colleagues, I have a problem sending mail from Ex2019 to Exchange Online, it remains queued on my server and does not go to the output connector that was created in the wizard, the related error in the queues is the following  

 
 454 4.7.5 Certificate validation failure, reason:untrustedroot};{MSG=};{FQDN=*-mail-onmicrosoft-com.mail.protection.outlook.com.  

 
I already verified the certificate and it is active and working, it is the same one that my connection has in my 365 administration.  

 
In the information of the message in the queue I see that it is using the output connector but for some reason it cannot make the sending channel from Ex2019 to O365 and thus send it abroad; I have internal communication on both routes, input and output, that means that the connector works, but the external output of my Ex2019 remains stuck.  

 
Thank you very much in advance for the help.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-26*

this is when i send to from Local, to 365

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-22*

Hi @Benyamin Marcos Carranza  ,

 454 4.7.5 Certificate validation failure, reason:untrustedroot};{MSG=};{FQDN=*-mail-onmicrosoft-com.mail.protection.outlook.com.

According to this error message, it could be related to the root certificates on the affected on-prem server. Please try to download the certificate chains via the link below and then install them on the Exchange 2019 server.   

https://learn.microsoft.com/en-us/purview/encryption-office-365-certificate-chains  

After that, restart the "Microsoft Exchange Transport" and the “Microsoft Exchange Frontend Transport” service, wait for a few minutes and check if it can fix the issue.  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
