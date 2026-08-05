---
title: "How to fix Active Directory Group Policy errors 7017 and 1058?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2108623/how-to-fix-active-directory-group-policy-errors-70
question_id: 2108623
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# How to fix Active Directory Group Policy errors 7017 and 1058?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2108623/how-to-fix-active-directory-group-policy-errors-70 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all!

I have a lab set up for learning Active Directory. There are 2 domain controllers (DC1 and DC2) and one Windows 10 domain member (Win10).

DC2 doesn't seem to be applying GPOs as expected.  When I run a gpresult on DC2, it shows "2 Errors Detected" in the Summary section:

-  7017: 

The system calls to access specified file completed. \company.dev\SysVol\bohil.dev\Policies{995A8A95-5E43-447D-8164-CC4B7082D825}\gpt.ini The call failed after 0 milliseconds.

-  1058: 

The processing of Group Policy failed. Windows attempted to read the file \company.dev\SysVol\bohil.dev\Policies{995A8A95-5E43-447D-8164-CC4B7082D825}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following:
a) Name Resolution/Network Connectivity to the current domain controller.
b) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller).
c) The Distributed File System (DFS) client has been disabled.	

One thing I noticed as I start looking into this is the sysvol directories aren't the same on both domain controllers. Here's what I'm seeing:

\DC1\SYSVOL\company.dev\Policies  

\company.dev\sysvol\company.dev\Policies  

\DC2\SYSVOL\company.dev\Policies  

My research seems to be taking me down the road of Authoritative SYSVOL Restore, but I'm not sure I need to go there yet.  And, I don't know that would fix the problem.  Is there something I should be looking at to ensure I'm getting at the root cause of the problem?

Thanks!

## Answers

_No answers on this thread._
