---
title: "GPO - Run only specified Windows applications"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199654/gpo-run-only-specified-windows-applications
question_id: 2199654
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-s"]
---
# GPO - Run only specified Windows applications

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199654/gpo-run-only-specified-windows-applications (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all, I've been using this GPO to restrict the access all the users have to the computers in our domain, but I still see the notification while running apps with child processes, is there an easy way Microsoft recommends to detect every executable behind an application? Or, is there any other tool Microsoft recommends for having all the users restricted?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-12*

Hello SWT Admin,  

Thank you for posting in Microsoft Community forum.

Because the gpo you mentioned is under User Configuration\Administrative Templates\System"Run only specified Windows applications" \type name of apps (for example notepad.exe).  

You can check if the gpo setting you configured is applied to all the user account in the OU (if you link the GPO to one OU).  

For checking User Configurations within gpresult, we can follow steps below.

1.Logon the machine using normal domain user account.

2.Create a folder named F1.

3.Open CMD (do not run as Administrator).

4.Type gpresult /h C:\F1\gpo.html and click Enter.

5.Open gpo.html and check gpo setting under "User Details".

Based on "but I still see the notification while running apps with child processes", you can add   

child processes within apps to GPO setting, and check if it helps.  

Q: is there an easy way Microsoft recommends to detect every executable behind an application?  

A: You can check the file type via app Properties.  

Q: Or, is there any other tool Microsoft recommends for having all the users restricted?  

A: You can also try do not run specified Windows applications gpo under User Configuration\Administrative Templates\System.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
