---
title: "Activesync Issues Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/224511/activesync-issues-exchange-2019
question_id: 224511
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Activesync Issues Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/224511/activesync-issues-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi I have a Exchange 2019 server running and my mobile device will not sync with any user. Functionality with Outlook client and OWA is working perfectly. When i add my account to outlook app on my phone i can connect to Exchange, my folders appear but with nothing in them and exchange never syncs? When i try to send an email i get some sort of time out error "EasSendFailedTransientException: An EAS Send command failed: The EAS command failed with Status ServerError, Code =110 and HttpStatus OK. The EAS command failed with status ServerError Failure code 547" Can anyone please assist me here?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-11*

Hi,    

Let's start with basic settings:    

-  Run Get-CASMailbox user | fl ActiveSyncEnabled to check if Activesync is enabled for the user.    

-  Create a new rule and assign the rule to user:    

New-ActiveSyncMailboxPolicy -Name "Test ActiveSync Policy"    

Set-CASMailbox user -ActiveSyncMailboxPolicy "Test ActiveSync Policy"    

-  Check default organization setting with Get-ActiveSyncOrganizationSettings | ft DefaultAccessLevel    

-  Check the authentification method for Activesync VD: Get-ActiveSyncVirtualDirectory | ft server,basic*    

-  Go to IIS Manager and recycle Activesync app pool, go to default-web-site and select Microsoft-Server-ActiveSync, make sure http redirect is not configured.    

Please run a test in EXRCA and be free to post the error information back with personal data covered: https://testconnectivity.microsoft.com/tests/Eas/input    

And enable Active sync mailbox logging for a testing mailbox and re-connect the mailbox on mobile device, then check the log:    

```
Set-CASMailbox user -ActiveSyncDebugLogging:$True  
Get-ActiveSyncDeviceStatistics -Mailbox user -GetMailboxLog:$True -NotificationEmailAddresses ******@contoso.com
```

You can get some help analyzing the log from this blog:https://techcommunity.microsoft.com/t5/exchange-team-blog/under-the-hood-exchange-activesync-mailbox-log-analysis/ba-p/591224    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
