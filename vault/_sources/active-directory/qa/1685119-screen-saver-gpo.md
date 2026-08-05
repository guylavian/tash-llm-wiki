---
title: "Screen Saver & GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1685119/screen-saver-gpo
question_id: 1685119
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Screen Saver & GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1685119/screen-saver-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've created a screen saver to be run across the domain, and placed in C:\Windows\System32 of the domain controller. Then I created a GPO and enabled screen saver in User Configuration > Policies > Administrative Templates > Control Panel > Personalization.

And in the Force Specific Screen Saver, I gave the path C:\Windows\System32\MyScreenSaver.scr, after enabling it of course, and after enabling and specifying the timeout as well.

But it looks like the domain wouldn't copy this screen saver to the client computers to run it.

What am I missing here?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-23*

Hello,

Based on this setup guide , it appears several steps were overlooked. Additionally, your current steps only apply where the Group Policy is set up, not the entire domain.

First, ensure the Authenticated Users group has read permissions on the C:\Windows\System32 folder. Typically, it’s better to use a shared network folder, like the SYSVOL directory on a Domain Controller, that all users can read from to store the screensaver file. This way, the folder will be synced to the clients' public user profile using Group Policy Preferences (GPP).

Meanwhile, you need to export the relevant registry value from a reference computer and then import it into the Group Policy.

Finally, enable the "Force specific screen saver" policy and specify "PhotoScreensaver.scr" as the screensaver. 

If the Answer is helpful, please click "Accept Answer" and upvote it.
