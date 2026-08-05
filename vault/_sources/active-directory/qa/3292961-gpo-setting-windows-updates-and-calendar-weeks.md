---
title: "GPO setting - Windows updates and calendar weeks"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3292961/gpo-setting-windows-updates-and-calendar-weeks
question_id: 3292961
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 83
qa_tags: []
answer_author_roles: ["Volunteer Moderator"]
---
# GPO setting - Windows updates and calendar weeks

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3292961/gpo-setting-windows-updates-and-calendar-weeks (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,

I know this question has tried to be answered in the past (2013) but still cannot get a definitive answer.

I am managing our server update environment via WSUS and GPO settings. 

WSUS has the below basic config:

Servers-pilot

Server-HA001

Server-HA002

Servers-Standard

Servers-Manual

All the updates are auto-approved via approval rules for categories. Everything on the WSUS side of things is good.

GPO basic settings:

There are 5 GPO's assigned to the  above WSUS containers. All server are getting their GPO's. An example of the GPO settings are below, only difference in them is day of install and week of install:

Policy
Setting
Comment

Configure Automatic Updates
Enabled

Configure automatic updating:
4 - Auto download and schedule the install
<br>
---
---
<br>
The following settings are only required and applicable if 4 is selected.
<br>
Install during automatic maintenance
Disabled
<br>
Scheduled install day:
7 - Every Saturday
<br>
Scheduled install time:
08:00
<br>
If you have selected “4 – Auto download and schedule the install” for your scheduled install day and specified a schedule, you also have the option to limit updating to a weekly, bi-weekly or monthly occurrence, using the options below:
<br>
Every week
Disabled
<br>
First week of the month
Disabled
<br>
Second week of the month
Disabled
<br>
Third week of the month
Disabled
<br>
Fourth week of the month
Enabled
<br>

<br>
Install updates for other Microsoft products
Disabled

My query:

Install time and install day work fine. The issue is around the **x week of the month.**I am seeing that when i set the above GPO, the install will happen either a week before the fourth week or it will install every week on the scheduled day.

In respect to the week of the month, does this start from Monday or Sunday for Microsoft, the complete week on from the specific day, e.g. Last Saturday is in week 4 and first Sunday is in first week.

I'm just trying to work out why the servers are patching outside of the GPO.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-04-03*

Hello,

Your question is beyond the scope of this forum. This, is a consumer focused forum.

I recommend you to repost your query to dedicated Windows Server forum at Technet for better assistance:

https://social.technet.microsoft.com/Forums/Windowsserver/en-US/home

Hope this helps!
