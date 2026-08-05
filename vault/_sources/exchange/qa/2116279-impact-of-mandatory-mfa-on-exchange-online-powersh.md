---
title: "Impact of Mandatory MFA on Exchange online powershell module"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2116279/impact-of-mandatory-mfa-on-exchange-online-powersh
question_id: 2116279
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Impact of Mandatory MFA on Exchange online powershell module

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2116279/impact-of-mandatory-mfa-on-exchange-online-powersh (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Microsoft has announced that MFA is mandatory for all azure sign-ins (https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/update-on-mfa-requirements-for-azure-sign-in/ba-p/4177584). We have a couple of questions in this regard:

·       Does this change impact exchange online powershell while trying to use Connect-ExchangeOnline(https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell?view=exchange-ps) cmdlet using the -Credential flag. Currently we use the Connect-ExchangeOnline in unattended scripts using some service accounts which have MFA disabled and whose username and password are provided as PsCredential.

·       We can change it to use certificate-based authentication. But we want to know if it has any throttling impacts if we use cmdlets like Get-MobileDeviceStatistics repeatedly in the same session. Currently we use that cmdlet in a loop to pull the device information of all our customer mailboxes after Connecting to Exchange Online. With service account sometimes we see some throttling errors. In that case, we workaround the problem by using a different service account to Create a new session until the throttling restrictions are lifted on the original service account.

## Answers

_No answers on this thread._
