---
title: "GPO Wallpaper on the client The background becomes a solid color that should be a background picture"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2192790/gpo-wallpaper-on-the-client-the-background-becomes
question_id: 2192790
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# GPO Wallpaper on the client The background becomes a solid color that should be a background picture

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2192790/gpo-wallpaper-on-the-client-the-background-becomes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I created a GPO Wallpaper, the result is that some users have a solid color background which should be a background picture, what should I do?  

Please help

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-17*

Hello anakPembelajar,

Thank you for posting in Microsoft Community forum.

What group policy setting did you configure? Under user configuration and computer configuration?

You can check if the group policy setting is applied.

For checking Computer Configuration within gpresult, we can follow steps below.

Logon this machine using administrator account.

Open CMD (run as Administrator).

Type gpresult /h C:\gpo.html and click Enter.

Open gpo.html and check gpo setting under "Computer Details".

For checking User Configurations within gpresult, we can follow steps below.

Logon the machine using normal domain user account (that applies this gpo).

Create a folder named F1 in C drive.

Open CMD (do not run as Administrator).

Type gpresult /h C:\F1\gpo.html and click Enter.

Open gpo.html and check if there are these gpo settings under "User Details".

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
