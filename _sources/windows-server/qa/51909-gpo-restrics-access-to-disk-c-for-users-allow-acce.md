---
title: "GPO - restrics access to disk c:\\ for users. Allow access for domain administratos to network \\\\pcname\\c$"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/51909/gpo-restrics-access-to-disk-c-for-users-allow-acce
question_id: 51909
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO - restrics access to disk c:\ for users. Allow access for domain administratos to network \\pcname\c$

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/51909/gpo-restrics-access-to-disk-c-for-users-allow-acce (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

What is the proper way to restrict access to system disk to users? But at the same time:  

-  Allow the operation system, especially drivers, and already installed software work properly.  

-  Allow domain administrators to have access to user's system disks by "\pcname\c$"

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-21*

Hi, I create this GPO, but the users lost access to documents and desktop for example. I want to know if there is a way that the users can have access to C: ( but can't save or create files and folders) But also can continue to use the users normally(all users folders).

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-27*

Hello,

Thank you for posting here.

According to your description, as for the GPO to restrict users to access disk C:\, we could have a check whether this GPO is what we want.

User Configuration > Administrative Templates > Windows Components > Windows Explorer > Prevent access to drives from My Computer. It is set to "Enabled" with the option "Restrict C drive only".

This similar case is also discussed on our TechNet forum. Below is the link:  

https://social.technet.microsoft.com/Forums/en-US/f0e747b9-8952-46aa-ac4d-0d9ad341f4c8/how-to-restrict-users-to-access-windows-folder-on-local-drive-quotcquot?forum=winserverGP

For any question, please feel free to contact us.

Best regards,  

Hannah Xiong
