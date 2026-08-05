---
title: "Domain Controller continuous reboot after installing update KB5082198"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5862013/domain-controller-continuous-reboot-after-installi
question_id: 5862013
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Domain Controller continuous reboot after installing update KB5082198

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5862013/domain-controller-continuous-reboot-after-installi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have installed the update KB5082198 on one of our Domain Controller hosted on a Virtual Machine. 

Since then, the Domain Controller is rebooting again and again : each time trying to install the update for some times and then rebooting. 

Has anyone encountered the same problem and how did you solved it ?

Thanks in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-04-17*

KB5082198 is not covered in the provided material, but there is directly relevant guidance for domain controllers that get stuck in a reboot/rollback loop after an OS update or in-place upgrade.

For a DC that repeatedly reboots while trying to complete an update, the supported recovery pattern is to allow the setup/servicing engine to detect the failed upgrade and roll back to the previous OS state:

-  Continue rebooting the affected domain controller.

-  After the permanent hang/loop is detected, reboot the server twice in succession.

-  Setup should then detect the failed upgrade attempt and automatically roll back the system to the previous OS version and state.

-  After rollback, the DC should return to its previous, healthy state without data loss.

If the DC remains stuck and cannot complete rollback, the documented workaround is to:

-  Bring up new, healthy domain controllers (preferably on different physical or virtual machines) running the target OS version instead of trying to in-place upgrade the problematic DC.

-  Once the new DCs are promoted and replicating correctly, retire or rebuild the problematic DC.

These steps avoid leaving the forest dependent on a DC that is stuck in an unstable update state and align with recommended practice for domain controller OS upgrades.

References:

-  Domain Controllers in-place upgrade hangs at black screen
