---
title: "PS Script to return certificate information - ADCS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1194428/ps-script-to-return-certificate-information-adcs
question_id: 1194428
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# PS Script to return certificate information - ADCS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1194428/ps-script-to-return-certificate-information-adcs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

Id like to have a powershell script to return all certificates issued by my CA (adcs) as JSON. Something like this:

{  

"RequestID": "1582",  

"SerialNumber": "7c0000000hasmn128",  

"CertificateExpirationDate": "10/12/2023",  

}

I did some research but found nothing about return a json with these infos, and unfortunately I am not so good with development. 

Anyone can help me please?

Thanks in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-30*

Hello

Thank you for your question and reaching out. I can understand you are  having query\issues related  to get all certificate list from ADCS.

You can considering utilising the PKITools from Github module because it makes it simple to obtain issued certificates.

The module should be installable with the help of the following command:

Install-Module -Name PKITools

Then you can get list of certificates 

Get-IssuedCertificate | Format-Table

--If the reply is helpful, please Upvote and Accept as answer--
