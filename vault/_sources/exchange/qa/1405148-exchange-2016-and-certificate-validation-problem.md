---
title: "Exchange 2016 and certificate validation problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1405148/exchange-2016-and-certificate-validation-problem
question_id: 1405148
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 and certificate validation problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1405148/exchange-2016-and-certificate-validation-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have a new exchange 2016.

I have certificate with values:

-  contoso.com

-  autodiscover.contoso.com

-  mail.contoso.com

-  antyspam.contoso.com(used on Fortimail)

Test connectivity looks good but has issue with the SSL certificate.

Analyzing the certificate chains for compatibility problems with versions of Windows.
The test passed with some warnings encountered. Please expand the additional details.
Additional Details
The Microsoft Connectivity Analyzer can only validate the certificate chain using the Root Certificate Update functionality from Windows Update. Your certificate may not be trusted on Windows if the "Update Root Certificates" feature isn't enabled.

The certificate is applied on send connector and receive connector "Client Frontend".

FQDN have value "mail.contoso.com" on these connectors.

These issue with the certificate gives me errors on Magento server(used IMAP protocol) where I can't send e-mails if I validating certificate.

Root CA and Intermediate CA of this certificate are applied on exchange host.

Any ideas?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-27*

Hello @drClays  ，

Based on the information you provided and my research, seems that the warning is just a warning from an exchange perspective. It generally has no actual impact and can be ignored.

 As regards to how to suppress this warning message, a user shared his resolution steps in the following similar thread, and you can have a look to see if it can be applied to your situation:

GoDaddy UCC Certificate: "ExRCA can only validate the certificate chain using the Root Certificate Update functionality from Windows Update"

Additionally, considering that your main concern about the certificate is the errors on Magento server, I’d like to suggest also trying to contact Magento support to see if they can provide some insights on this situation.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
