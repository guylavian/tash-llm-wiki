---
title: "how to change language pack in windows 10 by GPO."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1428109/how-to-change-language-pack-in-windows-10-by-gpo
question_id: 1428109
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# how to change language pack in windows 10 by GPO.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1428109/how-to-change-language-pack-in-windows-10-by-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello. how i can change text in language cfg. i need to change popup windows, tells that software is blocked by your system administrator. 

i want to change this text at: software blocked. please call in helpdesk. 

thank a lot for answer.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-24*

Hello

To change the language pack in Windows 10 by Group Policy, you can follow these steps:

Open the Group Policy Editor by pressing Win + R keys together on your keyboard and type: gpedit.msc.

Navigate to Computer Configuration\Administrative Templates\Control Panel\Regional and Language Options.

Enable the policy option Force selected system UI language to overwrite the user UI language.

Set it to Enabled.

As for changing the text in the language configuration file, it’s important to note that these files are part of the operating system and are not meant to be edited directly. Modifying these files could potentially cause system instability or other unexpected issues.

However, you can customize the message displayed to users when a software is blocked by the system administrator. This can be done through the Group Policy Editor:

Navigate to Computer Configuration\Windows Settings\Security Settings\Local Policies\Security Options.

Look for the policy settings Interactive logon: Message text for users attempting to log on and Interactive logon: Message title for users attempting to log on.

Double-click on each of them, and in the window which opens, enter the title or the text, as the case may be.
