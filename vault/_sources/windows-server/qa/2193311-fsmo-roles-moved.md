---
title: "FSMO roles moved"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193311/fsmo-roles-moved
question_id: 2193311
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# FSMO roles moved

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193311/fsmo-roles-moved (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I moved PDC role few months ago. when im running netdom query FSMO it show correct new server, but if i look under sites and services both old and new server shows DC under DC type column. Can i assume that it is safe to decomm my old server that hosted PDC role eventhough its still showing DC type under sites and services

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-16*

Hi Tool Shed1,

It is not safe to assume that it is safe to decommission the old server just because it is still showing as a DC under the DC type column in Sites and Services. This is because the DC type column in Sites and Services is not updated in real-time and may take some time to reflect the changes made to the FSMO roles. 

To ensure that the old server can be safely decommissioned, you should perform the following steps:

-  Verify that the new server is functioning correctly as the PDC emulator by running the command "netdom query FSMO" and ensuring that the PDC role is listed as being held by the new server.

-  Verify that the new server is replicating correctly with the other domain controllers in the environment by running the command "repadmin /showrepl" and ensuring that there are no errors.

-  Verify that all necessary services and applications are functioning correctly on the new server.

-  Once you have verified that the new server is functioning correctly and is replicating with the other domain controllers, you can safely decommission the old server.

It is important to note that decommissioning a domain controller should be done carefully and with proper planning to avoid any potential issues or data loss.

Best regards,

Qiuyang
