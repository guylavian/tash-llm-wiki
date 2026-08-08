---
title: "Domain GPO - Item-Level Targeting for WMI Query -FeatureSettingOverride Registry"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2180394/domain-gpo-item-level-targeting-for-wmi-query-feat
question_id: 2180394
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Domain GPO - Item-Level Targeting for WMI Query -FeatureSettingOverride Registry

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2180394/domain-gpo-item-level-targeting-for-wmi-query-feat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

If you have Hyperthreading enabled, then set the value to 72, and QID will not be flagged.

If you have hyperthreading disabled, then set the value to 8264, and QID will not be flagged.

Get-WmiObject -Query "SELECT NumberOfCores,NumberOfLogicalProcessors from Win32_Processor"

I've been tasked with something I've never done before.  I'm up for the challenge, but locating the proper document or article has not been of any luck to me yet.

In our AD Structure we have an OU for all of our Servers separated into SubOUs for each site.

AD Structure is similar to:

MyDomain . com

-  Servers   <--- Baseline Security GPO is assigned here

-  Site1

-  Server1

-  Server2

-  Site2

-  Server3

-  Server4

-  Site3

-  Server5

-  Server6

We have a GPO assigned to all Servers with several settings in the GPO to meet our Baseline Security

In the GPO, there is a Registry setting that is being forced to all servers (Physical and Virtual).  This setting is telling All Servers that HyperThreading is Enabled.  But Obviously, on the VMs, HT is not enabled.  So, I need to edit the value for the VMs to a different value.

Instead of moving all Physical and Virtual to their own OU, I was told to use "Item-Level Targeting" (Which is new to me) to modify the registry value for the VMs. (Leaving the Baseline GPO registry setting in place)

The Registry value is:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management

FeatureSettingsOverride         with a set value of     0x00000048 (72)

So, I'd need a query similar to the below to run inside the Targeting Editor to compare 2 values from a WMI Query, and if the values are the same, Change the value from the above (0x00000048 (72)) to:   0x00002048 (8264)

WMI Query:   cpu get NumberOfCores,NumberOfLogicalProcessors

So, running the above wmiquery, I get the below:

NumberOfCores  NumberOfLogicalProcessors

2                             2

If NumberOfCores   =   NumberOfLogicalProcessors then change registry value to 0x00002048 (8264)

Any input is greatly appreciated.

I have been to many sites reading different articles, and I've not found anything relating to my need.

Thanks!!

B.

## Answers

_No answers on this thread._
