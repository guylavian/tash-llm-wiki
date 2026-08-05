---
title: "SCCM Driver tab is missing from boot image after adk upgrade"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1003093/sccm-driver-tab-is-missing-from-boot-image-after-a
question_id: 1003093
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-deployment"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SCCM Driver tab is missing from boot image after adk upgrade

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1003093/sccm-driver-tab-is-missing-from-boot-image-after-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have upgraded ADK on sccm (2103) server but now all of the boot images doesn't have driver tab    

Windows ADK for Windows 10, version 2004    

Windows PE add-on for the ADK, version 2004    

I have reboot server few times now

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-14*

Hi,    

Thanks very much for your feedback. We're glad that the issue is gone now. It's appreciated that you could  click "Accept Answer" to the helpful reply, this will help other users to search for useful information more quickly. Here's a short summary for the problem.    

Problem/Symptom:    

Boot images don't have driver tab after upgrade Windows ADK on SCCM version 2103.     

Solution/Workaround:    

After apply the patch it showing the driver tab now    

Best regards,    

Simon    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-13*

After apply the patch it showing the driver tab now

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-13*

After apply the patch it showing the driver tab now

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-12*

Hi,    

This may happen because ConfigMgr compares the version of the installed ADK to the version of the boot image, and if these do not match the tabs to modify the boot image will be hidden. We can only modify boot images in the ConfigMgr console that exactly match the the version of the ADK that is installed on the site server and/or SMS Provider.    

Please help try the following action:    

Right-click the default boot images and then check the box "Reload this boot image with the current Windows PE version from the Windows ADK" to update boot images.    

Similar thread for your reference:    

Missing tabs on Boot image after installing ADK for Windows 10 in ConfigMgr    

Hope it helps. Thanks for your time,    

Best regards,    

Simon    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
