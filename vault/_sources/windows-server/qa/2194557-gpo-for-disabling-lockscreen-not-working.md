---
title: "GPO for disabling lockscreen not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194557/gpo-for-disabling-lockscreen-not-working
question_id: 2194557
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# GPO for disabling lockscreen not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194557/gpo-for-disabling-lockscreen-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello there

I am facing a challenge deploying GPO to disable lockscreen on some win10 pro pc`s 

the policy applying on the pc`s but the lockscreen still on after couple of minutes.

anyone face this issue before?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-03*

Hello   

Good day!

You can try to change the corresponding registry value to see if it helps.  

If no, maybe you can consider changing the version if needed.

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-03*

Thanks Daisy Zhou for your quick response 

as I test it now it seams that win10 pro machines gpo of lock screen don`t apply

and another testing machine with win10 ent. gpo worked fine.

so the issue is with the version 

is there any way to apply the lock screen policy on pro machines?

Best Regards 

Mark

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-03*

Hello Mark_734,  

Thank you for posting in Microsoft Community forum.

What specific GPO setting did you configure?  

You can try to check if GPO applying result via gpresult command.  

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
