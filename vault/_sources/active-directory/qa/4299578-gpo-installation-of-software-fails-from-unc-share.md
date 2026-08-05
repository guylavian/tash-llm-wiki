---
title: "GPO installation of software fails from UNC share using FQDN of windows domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4299578/gpo-installation-of-software-fails-from-unc-share
question_id: 4299578
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# GPO installation of software fails from UNC share using FQDN of windows domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4299578/gpo-installation-of-software-fails-from-unc-share (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, 

I spent almost all day on this one so thought I'd share!

IMPACT: GPO install of MSI software fails. Event log: “The install of application XXXX from policy YYYY failed. The error was : %%1612”

Running gpresult /h output.html showed the following:

Software Installation
Failed
578 Millisecond(s)
23/12/2022 11:11:32 AM
View Log

Software Installation failed due to the error listed below.  <br>  <br>The installation source for this product is not available. Verify that the source exists and that you can access it.  <br>  <br>Additional information may have been logged. Review the Policy Events tab in the console or the application event log for events between 23/12/2022 11:11:32 AM and 23/12/2022 11:11:32 AM.
<br>
:---

CAUSE: Intranet site is identified as Internet site - Windows Client | Microsoft Learn

"This behavior may occur if an FQDN or IP address contains periods. If an FQDN or IP address contains a period, Internet Explorer identifies the Web site or share as in the Internet zone.

"you may be prompted or prevented from opening files on an intranet Web site or Universal Naming Convention (UNC) share in programs that use the Internet Explorer Security Manager to determine whether a file is located in a trusted security zone.

This happened to me despite UNC path being the FQDN of the windows domain!

RESOLUTION: change GPO UNC path to use \hostname not \FQDN eg. \host not \host.mydomain.com

I really hope this saves you some time if you are getting this error!

Regards,

Richard.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2022-12-23*

Hello Richard,

Good day! I'm John DeV a Windows user like you and I'll be happy to assist you today.

Due to the scope of your question, it is best to ask this on Microsoft Site Q&A which is a technical community platform where most of the members were IT professionals that would greatly help you with the issue.

Microsoft Site Q&A

https://learn.microsoft.com/en-us/answers/topic...

Kindly include other necessary tags

Kind regards,

John DeV

Independent Advisor
