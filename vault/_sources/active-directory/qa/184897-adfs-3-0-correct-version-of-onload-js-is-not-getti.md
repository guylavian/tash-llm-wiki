---
title: "ADFS 3.0 - Correct version of Onload.js is not getting applied/exported"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/184897/adfs-3-0-correct-version-of-onload-js-is-not-getti
question_id: 184897
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 3.0 - Correct version of Onload.js is not getting applied/exported

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/184897/adfs-3-0-correct-version-of-onload-js-is-not-getti (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I am trying to update the "expiredNotification" field on the "Update Password" page.  

I have done it in our System and User testing environments, but in Production environment, it is not working.  

Below are my observations -   

-  I apply the updated onload.js using the command - "Set-AdfsWebTheme -TargetName custom -AdditionalFileResource @{Uri='/adfs/portal/script/onload.js';path="c:\theme\script\onload.js"}"  

-  The command executes successfully.  

-  When I export the theme again, using the command - "Export-AdfsWebTheme –Name default –DirectoryPath c:\theme", I see my changes in the exported onload.js file.  

-  But on the Update Password page, my changes do not reflect.  

-  In IE debugger, I do not see the lines of code I had added.  

-  In IE debugger, I see that the version of onload.js is different from what gets exported, and few lines of code are different/commented.  

Why are differences in Onload.js being observed? How can I get hold of the correct version of Onload.js and apply updates on the top of it?  

Any help would be greatly appreciated, as I could not find any relevant discussions in the forums.  

Thanks in advance!  

Amrita

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-07*

Thanks Piaudonn,  

This indeed was not the active theme.  

You can ignore the typo in my description, I had just grabbed the commands from the documentation, to convey the issue.  

I am now updating the active theme, and will post again on how it goes..  

Thanks!

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-04*

Did you make sure your custom theme was selected with:  

```
Set-AdfsWebConfig -ActiveThemeName "custom"
```

Also, I assume this is a typo but your export (step 3) is for the default theme, not the custom.
