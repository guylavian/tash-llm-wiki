---
title: "Local GPO Windows 10 System Defined Device Setup Classes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4215331/local-gpo-windows-10-system-defined-device-setup-c
question_id: 4215331
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 7
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Local GPO Windows 10 System Defined Device Setup Classes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4215331/local-gpo-windows-10-system-defined-device-setup-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

As per Microsoft's " System-Defined Device Setup Classes Available to Vendors" there is no difference between USB Drive and Hard Disk Drives, at least not that I know of or have found an answer online.

Why do we need know the difference between them is explained below:

I'm/We are trying to implement a GPO that will prevent all USB Mass Storage devices from being used on domain systems, except for the ones that we specifically allow via GPO.

The specific GPOs are "Allow installation of devices that match any of these device IDs" (I would add the Hardware IDs of those specific USB Mass Storage Drives ) , "Allow installation of devices using drivers that match these device setup classes (We are
 allowing all classes except " Disk Drives  

Class = DiskDrive  

ClassGuid = {4d36e967-e325-11ce-bfc1-08002be10318}  

This class includes hard disk drives. See also the HDC and SCSIAdapter classes.)" and "Prevent installation of devices not described by other policies"

Under:

computer config>admin templates>system>device installation>restrictions

I know the limitation of the above approach. I know that if a USB device already has a driver installed on the machine this GPO won't be able to stop it.

Again we are trying to find the answer to the following question:

How to differentiate between Hard Disk Drives and USB Drives in the context of the Microsoft documentation above.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2021-01-08*

Good day Safi13! I am Independent Advisor Paul R. and also a Microsoft/Windows user like you and I am glad to be able to provide assistance to you today. I would suggest to post this query to our neighbor forum from the link below. They are more oriented on with regards to domain/GPO related queries/issues and there will be IT Pros/System Admins/Server Admins/AD Admins who are available that will be able to fulfill your query as we are more of home/personal consumer based forum.

https://social.technet.microsoft.com/Forums/en-...

https://docs.microsoft.com/en-us/answers/topics...

Regards,

Paul R.
