---
title: "Deploying Fonts via GPO or alternative method Windows Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3237318/deploying-fonts-via-gpo-or-alternative-method-wind
question_id: 3237318
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 13
qa_tags: []
answer_author_roles: ["Volunteer Moderator"]
---
# Deploying Fonts via GPO or alternative method Windows Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3237318/deploying-fonts-via-gpo-or-alternative-method-wind (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,

We have recently purchased a package that contains fonts for the marketing team.

These need to be distributed throughout the organisation.

What is the best way to deploy this to every computer?

I've tried to follow a few GPO steps but it does not seem to work for me.

-  Edit 'Fonts Installation' GPO and navigate to: User Configuration > Preferences > Windows Settings > Files

-  Create New File: Right click > New > File

-  In Source file(s), enter location of the file

-  In Destination File: C:\Windows\Fonts\Orkney Bold Italic.tff

-  Click OK

-  Navigate to User Configuration > Preferences > Windows Settings > Registry

-  Create New Registry Item with the following attributes:   

HKEY_LOCAL_MACHINE   

SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts   

Value Name: [name of the font] (TrueType)   

e.g. Orkney Bold Italic (TrueType)

Value type: REG_SZ   

Value data: Orkney Bold Italic.ttf

-  Click OK

This does not seem to work for me.

I've managed to get the font to appear in the registry using the method above but it does not appear within the font selection itself?

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2019-09-25*

Hi Dwayne05 

Greetings! I am Vijay, an Independent Advisor. My apologies for asking you to seek help on Technet forum. Windows server related question is best answered at Microsoft's Technet forum where Windows server experts answer the questions. I would suggest that you should post simultaneously (i.e. cross-post) to Technet forum also.  

Technet Windows Server forum - https://social.technet.microsoft.com/Forums/en-...
