---
title: "[Migrated from MSDN Exchange Dev]Outlook 2016 Voting Buttons"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/152334/migrated-from-msdn-exchange-dev-outlook-2016-votin
question_id: 152334
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
---
# [Migrated from MSDN Exchange Dev]Outlook 2016 Voting Buttons

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/152334/migrated-from-msdn-exchange-dev-outlook-2016-votin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted  on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

Exchange 2016 CU16 in hybrid mode using Outlook 2016.  

When sent email with voting buttons, the buttons do not appear from some senders and they do from others. All clients are Outlook 2016 in HTML mode (have tried Rich Text and still the same). The majority of users see the voting buttons but not all and the ones that do not are able to see them if sent from another user. Tried viewing from OWA and the same results.  

Anyone have a clue why this is happening?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-05*

Hi,  

Based on my knowledge, this problem may occur if remote domain settings are missing or are set incorrectly.  

If Exchange online user’s can't view voting options of on-premises users. Please following the steps and see if the issue is resolved.  

1.Connect to Exchange on-premises PowerShell.  

2.Run the following commands, in which "<contoso>.mail.onmicrosoft.com" is the mail routing domain for the Exchange Online tenant. If you have multiple primary SMTP address spaces for users in your organization, repeat these steps for each domain.

```
Set-RemoteDomain "contoso.mail.onmicrosoft.com" -TNEFEnabled $true -AllowedOOFType "InternalLegacy"
```

3.Test to verify that the problem is resolved.

If the on-premises users can't view voting options of Exchange Online users. This scenario occurs because Exchange Online strips out the Transport Neutral Encapsulation Format (TNEF) content (specifically, the voting buttons). To prevent Exchange Online from removing the TNEF content when an email message is sent to an on-premises user, enable TNEF on the remote domains. To do this, use the one or both of following methods.Please following the steps and see if the issue is resolved:  

Run the following PowerShell command in Exchange Online, wait 30 minutes, and then test again.

```
Set-RemoteDomain "default" -TNEFEnabled $true -AllowedOOFType "InternalLegacy"
```

For more information:Out-of-office replies and voting options in email between on-premises and Exchange Online users appear incorrectly

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
