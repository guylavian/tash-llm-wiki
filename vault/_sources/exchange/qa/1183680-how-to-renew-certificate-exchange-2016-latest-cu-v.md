---
title: "How to renew certificate exchange 2016 latest CU via ems"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1183680/how-to-renew-certificate-exchange-2016-latest-cu-v
question_id: 1183680
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to renew certificate exchange 2016 latest CU via ems

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1183680/how-to-renew-certificate-exchange-2016-latest-cu-v (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello we are trying to renew our wildcard certificate via EMS, as the options are no longer there in EAC.

We follow the instructions:https://learn.microsoft.com/en-us/exchange/architecture/client-access/renew-certificates?view=exchserver-2016

we are able to import the certificate and it shows as valid in EAC.

However, when we try to export this certifcate to a PFX, we get an error: A special Rpc error occurs on server "server": The private key couldn't be exported as PKCS-12. It either couldn't be  

accessed or isn't exportable.

Does anyone have had any issues before?

Sources on the internet show different cmds, and the info from Ms website does not seem to do the trick. 

Many thanks.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-03-06*

Hi @Jan De Smet  ,

Hi, Thank you for your reply. We have created a new request, from another server. We were able to import and export it. Thanks.

Glad to see that your issue had already been resolved and thanks for sharing the solution so that others experiencing the same thing can easily reference this! Since the Microsoft Q&A community has a policy that The question author cannot accept their own answer. They can only accept answers by others, I'll repost your solution in case you'd like to Accept the answer.

How to renew certificate exchange 2016 latest CU via ems

Issue Symptom: 

We are able to import the certificate via EMS, however when we try to export this certifcate to a PFX, we get an error: A special Rpc error occurs on server "server": The private key couldn't be exported as PKCS-12. It either couldn't be accessed or isn't exportable.

 Solution:

From another server, use the Get-ExchangeCertificate command to recreate the request, and then import and export certificates can be done normally.

Best regards,

Jarvis

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-24*

Hi @Jan De Smet  , 

A special Rpc error occurs on server "server": The private key couldn't be exported as PKCS-12. It either couldn't be accessed or isn't exportable.

According to the error message, it could be that the private key was not set as exportable when the certificate was renewed. Did you include the parameter `-PrivateKeyExportable` when renewing the certificate? If not, it’s suggested to renew the certificate by the following command so that the private key is exportable:

```
Get-ExchangeCertificate -Thumbprint | New-ExchangeCertificate -PrivateKeyExportable $true
```

The PrivateKeyExportable parameter specifies whether the certificate has an exportable private key, and the default value is $false. Please refer to: New-ExchangeCertificate (ExchangePowerShell) | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
