---
title: "Inline upgrade of Exchange Server 2016 into 2019 after the Windows Server upgrade."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1537651/inline-upgrade-of-exchange-server-2016-into-2019-a
question_id: 1537651
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Inline upgrade of Exchange Server 2016 into 2019 after the Windows Server upgrade.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1537651/inline-upgrade-of-exchange-server-2016-into-2019-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Folks,

I need some help and clarification to perform the inline upgrade for both OS and Exchange Server below to the latest edition:

```
VM1 (Site 1)
Windows Server 2016
Exchange Server 2016

VM1 (Site 2)
Windows Server 2016
Exchange Server 2016

...
VM1 (Site N)
Windows Server 2016
Exchange Server 2016
```

Inline upgrade:

-  Insert Windows Server 2022 .ISO file and then upgrade the OS.

-  Install Exchange Server 2019 after the Windows Server has been updated to Windows Server 2022.

Can someone please confirm if this is the supported method or must not be done in that way?

There are no mailboxes on-premise running on the Exchange Server 2016 it is just there for the sake of Hybrid Exchange requirements.

https://learn.microsoft.com/en-us/lifecycle/products/exchange-server-2016

Thank you in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-19*

If you can spin new Windows Server 2022 virtual machines from scratch, install Exchange from scratch, and migrate mailboxes, I highly recommend choosing this route instead of performing an in-place upgrade. While Windows Server does a fantastic job in terms of the in-place upgrade process, I wouldn't say the same about Exchange. Unlike pure in-place upgrades, migration does not require any significant downtime, which is another solid argument to go in this direction.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-19*

Hello,

Upgrade your operating system to Windows Server 2022 before installing Exchange Server 2019. This is consistent with Microsoft's Exchange Server 2016 Product Lifecycle Guidelines and is a supported approach.

However, before proceeding with the upgrade, it is important to ensure that your environment meets the minimum requirements for Windows Server 2022 and Exchange Server 2019. You should also perform a thorough backup of your current environment to ensure you can recover if any issues arise during the upgrade. For more information you can refer to:
https://learn.microsoft.com/en-us/windows-server/get-started/upgrade-overview
https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.
