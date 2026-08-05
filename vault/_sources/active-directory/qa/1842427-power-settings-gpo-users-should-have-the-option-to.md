---
title: "Power Settings GPO - users should have the option to modify their settings afterwards"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1842427/power-settings-gpo-users-should-have-the-option-to
question_id: 1842427
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Power Settings GPO - users should have the option to modify their settings afterwards

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1842427/power-settings-gpo-users-should-have-the-option-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm building a GPO that modifies the power settings. It creates a brand new power plan with specific settings that I want to apply through Computer>Preferences> Control Panel> Settings> Power options> Power plan > Create power plan and the options I want. Including the button behaviour.   

 I'm also setting the behaviour of the buttons through Administrative Templates > System / Power Settings.

In both scenarios (battery and plugged in)

Power button = Sleep

Sleep button = Sleep

Lid switch = Sleep

However if I set it like that, the settings will be grayed out for my users and they will not be able to change them if they want.   

If button behaviour is not configured or set as disabled. The users will be able to select their settings, but the default is shown is Hibernate. I would want to have them as Sleep through the GPO but still allowing the user to change it.   

Is there a way to do this?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2025-04-30*

Hi Alan,

Better later than never right! You have 2 main GPO types. Preferences and Policies that behave a little differently. A Preference sets a setting to what you would like and allows the user to change it later. A policy sets a setting as you would like it and does not allow the user to make a change. 

Look at the "Power Options" settings under Computer Configuration\Preferences\Power Options to accomplish what you're looking to do.
