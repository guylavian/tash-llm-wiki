---
title: "Exchange 2016 Microsoft Exchange Server Auth Certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1516677/exchange-2016-microsoft-exchange-server-auth-certi
question_id: 1516677
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 Microsoft Exchange Server Auth Certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1516677/exchange-2016-microsoft-exchange-server-auth-certi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

https://learn.microsoft.com/en-us/Exchange/plan-and-deploy/integration-with-sharepoint-and-skype/maintain-oauth-certificate?view=exchserver-2016

How to rotate the Exchange Server Auth Certificate

If I run New-ExchangeCertificate and Set-AuthConfig as document said, 49hours later,  1) do I need to run Set-AuthConfig -PublishCertificate and Set-AuthConfig -ClearPreviousCertificate, and 2)  do I need to Restart-Service MSExchangeServiceHost or OWAapppool\ECPapppool? 3) How to delete the old certificate, just delete it in ECP?

Thanks.

BTW， I don't want to use monitorexchangeauthcertificate.ps1 as the prompts are not same as the document list.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-30*

Hello Emma Yoyo  

1.It is recommended to run Set-AuthConfig -PublishCertificate and Set-AuthConfig -ClearPreviousCertificate  

2.Personally it is not necessary to restart.  

3.To delete the old certificate, you can do so in the Exchange Admin Center (EAC) or by using the Remove-ExchangeCertificate cmdlet in the Exchange Management Shell.  

Kind Regards  

If the answer is helpful, please click "Accept Answer" and kindly upvote it.
