---
title: "SCCM Co-management issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/100099/sccm-co-management-issue
question_id: 100099
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# SCCM Co-management issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/100099/sccm-co-management-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have recently started to move all our devices to a co-managed state to leverage the additional functionality that Intune will be able to provide our organisation in terms of managing our Windows 10 devices.  The move has been quite easy with very little issues, however I have a couple of devices that just won't receive the 2004 feature upgrade since becoming co-managed.  These devices receive both quality and driver updates via Intune without any issue, but just won't display the feature update. All of them are running 1909 and have the latest CU, SSU's installed.  Bothe the comanagement handler log and wuahandler logs both show that the devices updates are being managed by intune.  

There isn't any blockers present on these devices as I have ran the 2004 media to ensure that there was no issues with any drives, disk space etc and they all passed.  I have repaired the SCCM client and reinstalled it to no avail, I really don't want to rebuild these devices, but at the moment it seems like the only option that I have left.  Has anyone else experienced a similar issue?  

Thanks  

Billy

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-21*

Hi Jason,  

I can confirm that the answer you provide was correct and the devices were in fact being prevent from upgrading by the safeguard hold because of the Conexant audio issues.  

Thank you for help  

Regards  

Billy

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-21*

Hi Jason,  

Thanks for sharing the links it looks like you could onto something as they all have Conexant ISST audio installed, so that could be the reason why they aren't upgrading.  I will opt out of safeguard hold on one of the devices to see if that allows the device to upgrade, and let you know the results  

Thanks  

Billy

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-09-20*

As per the docs https://learn.microsoft.com/en-us/mem/intune/protect/windows-update-for-business-configure#limitations-for-windows-10-feature-updates,    

While Windows 10 feature updates remains in public preview, when co-managing devices with Configuration Manager and Intune, there is a limitation where feature update policies may not immediately take effect, causing devices to update to a later feature update than configured in Intune. This limitation will be removed with a future update to Configuration Manager.    

reference https://learn.microsoft.com/en-us/answers/questions/74051/intune-device-will-update-to-windows-10-version-20.html
