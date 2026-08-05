---
title: "Mailbox does not share with users's email - Exchange Online Powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1366403/mailbox-does-not-share-with-userss-email-exchange
question_id: 1366403
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Mailbox does not share with users's email - Exchange Online Powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1366403/mailbox-does-not-share-with-userss-email-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My situation is - I have created a user on Azure AD with UPN "@domain.com" and its email is "@domain.com". Then, create one more user with UPN "******@domain.com" and assign it an exchange license. 

After that, I want to share its mailbox with the user with UPN "******@domain.com". The command that I use: 

```
Add-MailboxPermission -Identity ******@domain.com -User ******@domain.com -AccessRights FullAccess -InheritanceType All
```

According to Microsoft docs, the possible value that I can provide with -User attributes are:

-  Name

-  Alias

-  Distinguished name (DN)

-  Canonical DN

-  Domain\Username

-  Email address

-  GUID

-  LegacyExchangeDN

-  SamAccountName

-  User ID or user principal name (UPN)

So, according to that possible values the mailbox has to be shared with the user's email address.

My Output,

If email address is same as UPN then it shared successfully. 

If email address is different with UPN then it give error-

Error.png

Please help me with it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-09-12*

What you are describing is indeed a supported scenario, the cmdlet should accept any of the email addresses configured on a given mailbox as input for the -User parameter. However, assigning an Exchange license to the user doesn't necessarily mean that a mailbox will be provisioned, in which case Exchange might not "know" about any additional email addresses. In other words, you need to check whether the given address is a valid "recipient", which is easily done via the Get-Recipient cmdlet.
