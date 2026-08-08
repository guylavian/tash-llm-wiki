---
title: "Send as alias behavior OWA/Desktop client"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160551/send-as-alias-behavior-owa-desktop-client
question_id: 1160551
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Send as alias behavior OWA/Desktop client

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160551/send-as-alias-behavior-owa-desktop-client (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey guys,

iam trying to send as a secondary smtp/alias, because we have different domains in use.

O365, Hosted.

When i send a mail with OWA the alias works perfectly. When i send from outlook desktop client i can choose my alias and it looks like its working but the sender is than overwritten by the primary smtp.

I tried 3 different outlook client versions but it wont work.

any ideas?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-16*

Hi @Max ,

The ability for Outlook clients to use and reserve aliases was added in February 2022.

You could refer to the following command to enable this feature for Exchange online mailboxes.

```
Set-OrganizationConfig - SendFromAliasEnabled $true
```

Note: This feature is in preview and not yet generally available. Admins should test and fully understand the client impact and known issues before enabling this feature in your tenant.

For more details on this feature, please refer to this link:

Sending From Email Aliases – Public Preview - Microsoft Community Hub

 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
