---
title: "Importing Exchange 2019 Certificates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1293284/importing-exchange-2019-certificates
question_id: 1293284
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
---
# Importing Exchange 2019 Certificates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1293284/importing-exchange-2019-certificates (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I just installed Microsoft Exchange 2019 for the first time.  

I am attempting to import the SSL certificate from GoDaddy When researching using PowerShell to import the certificate, I learn that a password is required. However GoDaddy does not provide one. Is this password something I choose or am I suppose to get one from GoDaddy?  

GoDaddy only has instructions to install certificates on 2016 using the EAC. If they have instruction to install via PowerShell I haven't been able to find them.  

Exchange 2019 and Windows 2022 are fully updated.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-30*

Hi @Kevin,

You can confirm your certificate file type, the password is only required if they are PKCS #12 certificate file and the file contains a private key or chain of trust.

https://learn.microsoft.com/en-us/exchange/architecture/client-access/import-certificates?view=exchserver-2019

 This password is the one you chose when you exported the certificate from GoDaddy. If GoDaddy did not provide you with a password for the certificate, it is likely that the certificate was not exported with a password. For more details you can ask GoDaddy's support team or go to their official forum for help.

https://community.godaddy.com/s/question/0D53t00006Vm5wqCAB/how-to-find-a-certificate-password

(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)

After you confirm, you can try to import your certificate without using a password according to the following document.

https://learn.microsoft.com/en-us/powershell/module/exchange/import-exchangecertificate?view=exchange-ps

Best Regards,

Dezhi

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation](https://aka.ms/msftqanotifications)"https://aka.ms/msftqanotifications)") to enable e-mail notifications if you want to receive the related email notification for this thread.
