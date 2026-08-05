---
title: "Push shortcut to all users Desktops using GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1371669/push-shortcut-to-all-users-desktops-using-gpo
question_id: 1371669
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Push shortcut to all users Desktops using GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1371669/push-shortcut-to-all-users-desktops-using-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, i’ve created a GPO for putting shortcut to users Desktop using GPO for Computer Configuration (Preferences-Shortcuts)…I have a problem where my shortcut is not applied to some computers. I’ve tried everything and I can’t get it worked. What is the proper way for putting shortcut to Desktop on users computers? Also I’ve put shortcut to public Desktop and there shortcut is created but it is not visible on users Desktop regardless. Thank you! BR

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-19*

I've managed to find out how to solve this. It's not the solution but it works. I have shortcut configured for both Computer Configuration|Preferences|Windows Settings|Shortcut and also User Configuration|Preferences|Windows Settings|Shortcut in one GPO. It seems that for some users shortcut is applied from Computer Configuration and for some users shortcut is applied from User Configuration. And also for some users, shortcut is applied regardless if it's Computer or User Configuration. For those users who have been applied with shortcut only from Computer Configuration, shortcut from User Configuration is not applied and vice versa. I don't know why it's like that but I've tested it and confirm it. I have now problem that for some users I'll have duplicate shortcut but better something than nothing.

If anybody have idea why is it like this, would be grateful. BR

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-19*

I wonder if some computers are missing a Windows update. Can you compare this between a working and a non-working computer?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-19*

Thank you Matt!

I've already tried that and every possible solution using GPO for shortcut that I could think of. I've put shortcuts on Computer Configuration|Preferences|Windows Settings|Shortcut and also User Configuration|Preferences|Windows Settings|Shortcut. I've played with it's settings, changing Target type from URL to something else, changing Location from Desktop to All Users Desktop. What I can confirm that deleting some other shortcut from the Desktop using the same policy was successful. I've managed to find on some user this error 0x80070005 for this policy. This is access denied if I'm not mistaken, but I am unsure why do I have it because all of my PCs are in the same OU and all of my users are in the same OU. My computers have the same windows image, etc. Thank you! BR

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-18*

On the computer that is not receiving the shortcuts run the gpresult /r command and verify the GPO is applied to the computer. Make sure to run the command prompt as administrator or it will fail to get computer GPOs. 

Here is a guide with steps on creating shortcuts with GPO.   

https://activedirectorypro.com/group-policy-desktop-shortcuts/

Here are some additional GPO troubleshooting steps.   

https://activedirectorypro.com/group-policy-guide/#troubleshooting-group-policy
