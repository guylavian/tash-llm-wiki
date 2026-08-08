---
title: "Server 21H2, GPO allowing easeofaccess-mousepointer not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1465241/server-21h2-gpo-allowing-easeofaccess-mousepointer
question_id: 1465241
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 3
qa_tags: ["windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Server 21H2, GPO allowing easeofaccess-mousepointer not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1465241/server-21h2-gpo-allowing-easeofaccess-mousepointer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We run RDS on Server 2022. We have GPO's in place, to limit what the settings app shows for users. User Configuration --> Policies --> Administrative templates --> Control Panel --> Settings Page Visibility. So we use the per-user settings, to prevent local admin users from being 'locked out' as well. We use the 'showonly' option in the GPO. Now a customer wants to increase the size of their mouse-pointer. So, as per https://learn.microsoft.com/en-us/windows/uwp/launch-resume/launch-settings-app#ease-of-access I've put easeofaccess-MousePointer in the list of allowed items. But it doesn't show up. Any other item on the list works fine.

In a test environment I tested with hiding (hide:) as well, and I can hide every single item, except easeofaccess-MousePointer. Now there seems to be a debate whether we should use easeofaccess-mousepointer or easeofaccess-MousePointer, with capitals, but both don't work. The pre-21H1 name of easeofaccess-cursorandpointersize doesn't work either. When I run ms-settings:easeofaccess-MousePointer, with capitals, it shows up when it's not blocked (or as an admin for example), so my assumption is we should use the capitalized name. Using only lower-case easeofaccess-mousepointer just opens the main screen in settings.

To be clear again, hiding, or showing all other items, like easeofaccess-cursor works perfectly fine, just not the MousePointer. Is this a bug or am I still using the wrong canonical name, even though I use the name as per MS documentation?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-27*

Was racking my brain trying to figure out why I couldn't get this to work. 

Still an issue in server 2022 21H2 20348.2966 (December 2024).

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-22*

Hi, as stated I tried that, but it doesn't work. Opening the panel with ms-settings:easeofaccess-mousepointer if you DO have permissions, doesn't work, it just opens the main settings page. Running ms-settings:easeofaccess-MousePointer (ie. with capitals) DOES work for opening the panel if you have access but not for showing or hiding it in GPO. As the capitals work when opening the panel, my assumtion is that is the one that's supposed to work, but alas it doesn't.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-12-22*

Hello,

I think it should be "ms-settings:easeofaccess-mousepointer" and you are right.

You my check whether you have blocked a parent item?

You can try "start ms-settings:easeofaccess-mousepointer" in a cmd line and confirm if it will pop out.
