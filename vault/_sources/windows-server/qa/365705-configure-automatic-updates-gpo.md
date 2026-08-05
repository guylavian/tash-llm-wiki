---
title: "configure automatic updates GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/365705/configure-automatic-updates-gpo
question_id: 365705
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# configure automatic updates GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/365705/configure-automatic-updates-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi.  

I have over 30 Users, but they are never into the office everyday.  

So my problem is, that if i create a GPO of configure automatic updates, to update each monday at 11:00. If 10 is never online on monday, they never get the update from our Wsus server.  

So my question is, is there a way to configur configure automatic updates, so it will have more then 1 day that it will force the updateS?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-22*

1.despite those 10 computers never online on Monday, they can also get updates if you enable Configure Automatic Updates and WSUS related GPOs.  

2.I suggest to Enable Configure Automatic Updates and select 4 – Auto download and schedule the install, then according to your demand choose the following settings. You can specify the schedule by using the options in this Group Policy setting. If no schedule is specified, the default schedule for all installations will be every day at 3:00 A.M. If any updates require a restart to complete the installation, Windows will restart the computer automatically. (if a user is signed in to the computer when Windows is ready to restart, the user will be notified and given the option to delay the restart.)

If the Answer is helpful, please click "Accept Answer" and upvote it.  

Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
