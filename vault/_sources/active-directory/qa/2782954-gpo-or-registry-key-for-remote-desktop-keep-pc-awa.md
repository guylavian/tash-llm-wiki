---
title: "GPO or registry key for Remote Desktop : Keep PC awake for connection when it is plugged in"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2782954/gpo-or-registry-key-for-remote-desktop-keep-pc-awa
question_id: 2782954
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 106
qa_tags: []
---
# GPO or registry key for Remote Desktop : Keep PC awake for connection when it is plugged in

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2782954/gpo-or-registry-key-for-remote-desktop-keep-pc-awa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When Remote Desktop is enabled in Group Policy, the Remote Desktop settings on the workstations are greyed out as expected. See screenshot below. However, I'm unable to set the "Keep my PC awake for connections when it is plugged in" setting which is new
 in Windows 10 1709 if Remote Desktop is enabled via GPO. I can't find this setting in GPO or in the registry. Does anyone know how to set this setting via GPO or the registry? Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2018-01-27*

Hi Levi,

This issue which does not allow you to make changes on some particular settings is a normal behavior of the PC if you’re using Remote Desktop. If your device is associated with a certain organization, a company, or what not, we suggest contacting your local
 IT guy to perform the registry edit. You can also attempt to perform the following command in the registry as well:

-  Press Windows Key + R on your keyboard.

-  Type regedit and press Enter.

-  Now navigate to HKEY_CURRENT_USER > SOFTWARE > Policies > Microsoft > Windows > CurrentVersion > PushNotifications.

-  Look for NoToastApplicationNotification, double-click on that.

-  Now change the value from 1 to 0.

-  Click OK.

You can also check **Microsoft TechNet Forum**if
 you’re still not able to resolve the issue. They should be able to walk you through the process of making changes on particular settings via Remote Desktop.

If you have other queries, don’t hesitate to reach out.

NOTE: Registry editors bypass the standard safeguards provided by the administrative tools which prevents you to enter conflicting settings. Taking that into consideration, Microsoft suggests to avoid making changes on the registry unless there is no alternative to avoid degrading the performance of your device or at times, may even cause further issues. Since you’ve already tinkered the registry, we suggest posting your query on*Microsoft TechNet Forum**. The forum is mostly consists of Professional Technicians who can guide you throughout the whole process of resolving your concern.*
