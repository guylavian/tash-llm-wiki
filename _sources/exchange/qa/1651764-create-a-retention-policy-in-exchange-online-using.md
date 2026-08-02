---
title: "Create a retention policy in Exchange Online using PowerShell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1651764/create-a-retention-policy-in-exchange-online-using
question_id: 1651764
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# Create a retention policy in Exchange Online using PowerShell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1651764/create-a-retention-policy-in-exchange-online-using (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How can I use PowerShell to create a retention policy that deletes emails older than two weeks for a specific account in Exchange Online? I want to ensure that only the intended account is affected by the policy. Additionally, how can I verify that the policy has been properly applied? Would the following script accomplish this?

```
# Connect to the tenant's Exchange Online using PowerShell

New-RetentionPolicy -Name "TwoWeeksRetention" -RetentionPolicyTagLinks "DeleteAfter14Days"

Set-Mailbox -Identity "******@contoso.com" -RetentionPolicy "TwoWeeksRetention"

# Verify the Retention Policy

Get-Mailbox -Identity "******@contoso.com" | Select-Object RetentionPolicy
```

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-29*

Hi Andy,

I left it over the weekend and I can now see that all e-mails older then 14 days for the selected account had been deleted!

Thank you for your assistance!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-26*

Hi Andy,

Thank you for your reply.

I have tried your recommended solution but I can't see that e-mails older then 2 weeks are being deleted..

Does it take a while before the policy starts deleting older e-mails or could it be something else that is being difficult? FYI, the M365 tenant where I'm applying this retention policy and it's retention policy tag doesn't have any other retention policy's that could interfere.
