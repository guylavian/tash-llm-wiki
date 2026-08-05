---
title: "How to disable Exchange Online organization-wide without removing Exchange License"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1487096/how-to-disable-exchange-online-organization-wide-w
question_id: 1487096
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online"]
---
# How to disable Exchange Online organization-wide without removing Exchange License

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1487096/how-to-disable-exchange-online-organization-wide-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our organization current uses GMail for email, however we wish to begin leverage Microsoft 365 A5 for security of OneDrive, Teams, and Desktops of course, as well as any future workloads we leverage Azure for.

I would like to disable Exchange Online org-wide (for now), to prevent having unmonitored email systems associated to our users.

I've tried simply adjusting our license assignment to not include Exchange Online (Plan 2), but this fails, because the following services depend on this feature being licensed:

-  Office 365 Privileged Access Management

-  Customer Lockbox

-  Microsoft Defender for Office 365 (Plan 2)

-  Microsoft MyAnalytics (Full)

PAM and Defender for Office 365 are big ones, so clearly I can't simply remove the Exchange Online license, but it appears I can't disable mailboxes (though I'd love a way to prevent them from being created in the first place) without removing the Exchange Online license, and if the license gets re-added, the mailboxes will get recreated. It seems there must be some way to disallow users to use Exchange while not breaking the PAM and Defender features that protect things other than Exchange.

## Answers

_No answers on this thread._
