---
title: "Configure Automatic Update Via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2121543/configure-automatic-update-via-gpo
question_id: 2121543
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Configure Automatic Update Via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2121543/configure-automatic-update-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have windows server 2016 and 2019 in our environment which are getting updates via WSUS.  

We have configured automatic update via GPO to schedule the installation of updates.   

Below is our GPO setting , As per GPO it should install the update every Friday at 8:00 AM on Third Week of month, but we have observed that the update is getting install every Friday at 8:00 am instead of only Third week.  

Can anyone please help here?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-25*

Hello,

I suggest that if could try to create a scheduled task using Group Policy:

Navigate to GPO Scheduled Tasks:

Go to ‘Computer Configuration’ -> ‘Preferences’ -> ‘Control Panel Settings’ -> ‘Scheduled Tasks’

Create a new scheduled task:

Set the trigger for the third Friday of the month at 8:00 AM.

The action should run a script or use the wuauclt command to initiate the update process.

Example command to initiate updates:

wuauclt /updatenow

Best Regards, 

Hania Lian

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-11-21*

Hello @PrasadWF  

Thanks for using Q & A forum.

To suggest, disable 'scheduled install day' and Enable ' Third week of the month' this way it will work.

If the Answer is helpful, please click `Accept Answer` and Up-Vote, so that it can help others in the community looking for help on similar topics.
