---
title: "Exchange Admin Center"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1418235/exchange-admin-center
question_id: 1418235
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange Admin Center

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1418235/exchange-admin-center (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Why can't I see the users in exchange admin Center  that I see in 0365 management?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2023-11-07*

Hello @Barbara Matthews  ,

According to your description, the users seen in o365 management cannot be seen in the Exchange Admin Center. I would like to confirm with you whether the user is created in local AD and then synchronized to Azure AD and assigned a license directly. If so, it is an expected behavior that you cannot see those mailboxes on Exchange on-premises.

It is recommended that you try run Exchange Management Shell as administrator and run the following three cmdlets.

1.Run the Enable-MailUser cmdlet to enable mail for users who have not yet enabled mail.

```
Enable-MailUser -Identity ******@domain.com -ExternalEmailAddress  ******@company.mail.onmicrosoft.com
```

2.Run the Enable-RemoteMailbox cmdlet to link cloud mailboxes in the cloud-based service for existing users in on-premises Active Directory.

3.Connect to Exchange Online PowerShell and run the Get-Mailbox cmdlet to get the ExchangeGuid property and copy the value then run the Set-RemoteMailbox cmdlet to set the ExchangeGuid property on the AD local user object.

```
Get-Mailbox " ******@domain.com " | ft Identity,ExchangeGuidSet-RemoteMailbox " ******@domain.com " -ExchangeGuid "xxxxxxxx"
```

After this, you could check in the on-premises Exchange admin center that the Office 365 mailbox shows up.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-11-07*

Having mailboxes for the same user both in Exchange Online and on-premises is unsupported. The "standard" configuration would be to have the Exchange Online mailbox represented as a mail user in AD, which you can find under the Recipients > Contacts tab in the EAC. Another possibility is that the mailbox is provisioned directly in Exchange Online, in which case you will not have any matching user on-premises.
