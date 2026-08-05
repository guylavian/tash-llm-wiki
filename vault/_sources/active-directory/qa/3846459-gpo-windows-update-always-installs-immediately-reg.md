---
title: "GPO - Windows Update - Always installs immediately regardless of setting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3846459/gpo-windows-update-always-installs-immediately-reg
question_id: 3846459
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# GPO - Windows Update - Always installs immediately regardless of setting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3846459/gpo-windows-update-always-installs-immediately-reg (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In Windows 11 23H2, and Windows 11 24H2, we have a GPO configured to download updates automatically from our WSUS server, but not to instal, only to notify.  However it always installs, no matter what configuration I have tried.  The same behaviour is observed with using Windows Update instead of WSUS, so I assuming this is either a change in behaviour in Windows 11, or some option I have configured which is overriding the GPO somehow.

Windows computers are activated with Enterprise licenses.

Below are the settings I currently have configured from the Windows Update option:

Windows Components/Windows  Update/Manage end user experience

Policy
Setting
Comment

Allow  updates to be downloaded automatically over metered connections
Disabled

Configure Automatic  Updates
Enabled

Configure automatic updating:
7 - Auto Download, Notify to install, Notify to Restart
<br>
---
---
<br>
The following settings are only required and applicable if 4 is  selected.
<br>
Install during automatic maintenance
Disabled
<br>
Scheduled install day:
0 - Every day
<br>
Scheduled install time:
03:00
<br>
If you have selected “4 – Auto download and schedule the install”  for your scheduled install day and specified a schedule, you also have the  option to limit updating to a weekly, bi-weekly or monthly occurrence, using the  options below:
<br>
Every week
Enabled
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
Disabled
<br>

<br>
Install updates for other Microsoft products
Disabled

Policy
Setting
Comment

---
---
---

Display options for  update notifications
Enabled

Specify the update notifications display options :
0 (default) – Default OS Windows Update notifications
<br>
---
---
<br>

<br>
Apply only during active hours
Disabled

Policy
Setting
Comment

---
---
---

Remove  access to "Pause updates" feature
Enabled

Remove  access to use all Windows Update features
Disabled

Specify  deadline for automatic updates and restarts for quality update
Enabled

Deadline (days):
2
<br>
---
---
<br>
Grace period (days):
1
<br>

<br>
Don't auto-restart until end of grace period
Enabled

Policy
Setting
Comment

---
---
---

Turn  off auto-restart for updates during active hours
Enabled

Active Hours
<br>
---
<br>
Start:
8 AM
<br>
End:
6 PM

Windows Components/Windows  Update/Manage updates offered from Windows Update

Policy
Setting
Comment

Disable safeguards for  Feature Updates
Disabled

Do not include  drivers with Windows Updates
Enabled

Enable optional updates
Disabled

Manage preview builds
Disabled

Select the target  Feature Update version
Disabled

Select  when Preview Builds and Feature Updates are received
Enabled

How many days after a Feature Update is released would you like to defer the  update before it is offered to the device?
35
<br>
---
---
<br>
Pause Preview Builds or Feature Updates starting:
2025-04-01
<br>
(format yyyy-mm-dd example:  2016-10-30)

Policy
Setting
Comment

---
---
---

Select when Quality  Updates are received
Enabled

After a quality update is released, defer receiving it for this many  days:
0
<br>
---
---
<br>
Pause Quality Updates starting

<br>
(format yyyy-mm-dd example: 2016-10-30)

I also noticed some odd inconsistences with the options to delay the installation of feature updates.  It's description reads:

"Note, Quality Updates will still be offered even if Features Updates are paused."

But what I have observed is if you set a long another period to defer them, changing the "35" above to "365", then you don't even get quality updates offered.  Change that to a lower number,, and the quality updates are eligible again.

I have a VM configured for these tests so I can very quickly snapshot back to the pre-patched state, and run them again.  I always confirm checking the registry values by hand to double check correct application of any updated settings before checking for an update.

Any insight into this would be most welcome.

## Answer (community) — Independent Advisor

*upvotes: 1 · updated: 2025-04-03*

Glad to help!

## Answer (community) — community member

*upvotes: 0 · updated: 2025-04-03*

Thank you, I just raised a new thread there.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-04-03*

Hi, I am Dave, I will help you with this.

I apologize, Community is just a home user to user consumer forum, due to the scope of your question, can you please post this question to our sister forum on Microsoft Q&A (The System Administrators and IT Pro Forum).

Over there you will have access to a host of System Administrators and WSUS experts and will get a knowledgeable and quick answer to this question.

https://docs.microsoft.com/en-us/answers/index....
