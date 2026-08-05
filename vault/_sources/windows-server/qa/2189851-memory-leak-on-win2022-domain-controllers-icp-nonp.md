---
title: "Memory leak on Win2022 Domain Controllers - Icp nonpaged pool tag"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2189851/memory-leak-on-win2022-domain-controllers-icp-nonp
question_id: 2189851
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-performance-system-performance"]
---
# Memory leak on Win2022 Domain Controllers - Icp nonpaged pool tag

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2189851/memory-leak-on-win2022-domain-controllers-icp-nonp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Since sep 18th we've been seeing increasing non-paged pool usage on our 2022 domain controllers - need to reboot them a couple of times a week now.

Poolmon shows high utilization by tag Icp - it keeps increasing until server is non-responsive over 3-5 days

Icp seems to be related to SMB traffic. 2019 DC is not affected

Running build 20348.2700

fyi - Non-paged pool size can be seen in task manager - performance - memory. Should usually be below 1gb

Non-paged pool details can be seen with poolmon.exe (from WDK)

Anyone else seeing this?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-07*

Confirmed known issue by MS Support.

Mem leak caused by SenseNDR - should be fixed in October Patch Tuesday updates

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-30*

Hello,

Thanks for your sharing, this could help others with similar issues.

Best regards,

Molly

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-26*

FYI - Have a case with MS support on this. (actually useful this time)

Possible cause is the defender component. SenseNDR.exe

Could have been a signature update on the 18th.

And a little tip if you are looking for which drivers that are using some tag seen in poolmon:

cd C:\Windows\System32\drivers

findstr /M /S /L tagname *.sys

(PS! tagname case sensitive)

You can then check signature / details on the drivers to see last update / vendor etc.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-25*

Hi, thanks for your reply

1. There are no such service on the server.

2. Server is an Azure VM, Newly installed...

3. All updates installed. Running latest available build for 2022: https://support.microsoft.com/en-gb/topic/september-10-2024-kb5042881-os-build-20348-2700-5b548143-9613-4e5a-9454-8ed9be8b2bd2. Defender AV. 

Server was updated sep 11, but problem didn't start before sep 18. Perhaps some signature update for defender AV / ATP triggered it. 

Not aware of any system changes at that time either..

best regards

axel

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-25*

Hello,

Thank you for posting in Microsoft Community forum.

Based on the description, I understand your question is related to memory leak.

-  Try run below command to disable Network Data Usage Monitoring Driver (NDU), it is responsible for collecting data related to network usage, but itself may lead to memory leak.    sc config NDU start= disabled 

-  Try update network drivers in device manager:

Press Windows + 'R' and type devmgmt.msc to open Device Manager.

Locate the device and double-click on it to expand.

Double-click on the driver and go to the Drivers tab.

Click "Update Driver" and select "Automatic Search" for drivers.

-  Try install the latest windows update for Server 2022. Also, if you are using any 3rd party antivirus software, uninstall it and monitor the memory issue.

Have a nice day.

Best Regards,

Molly
