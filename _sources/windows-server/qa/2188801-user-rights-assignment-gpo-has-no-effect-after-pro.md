---
title: "User Rights Assignment GPO has no effect after promoting Server 2022 to a domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188801/user-rights-assignment-gpo-has-no-effect-after-pro
question_id: 2188801
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# User Rights Assignment GPO has no effect after promoting Server 2022 to a domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188801/user-rights-assignment-gpo-has-no-effect-after-pro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently promoted a 2022 Windows server as a domain controller.  After promotion, I cannot login over RDP or console as a domain admin.  This is the 4th DC in our domain.  Single forest, single domain, functional level 2016.

The other three 2019 domain controllers are fine with logging in.  repadmin shows no errors and is replicating with all partners successfully.

The new DC has the same default domain controllers policy applied.  I am able to enter a PSSession with the new DC and check settings.  I can also connect over MMC consoles without issue.  

It is in a different site, but it is well connected, and the site links are setup with a quick sync time of 15 minutes.

Here is the RSOP;

As you can see there is no definition for Allow Logon Locally or Remote Desktop Services defined.  So, it is using the defaults of which Administrators is an allowed group.  I also enabled diagnostic logging in the registry to make sure settings were being applied.  

I have spent hours on troubleshooting, and I cannot figure out what is wrong.  We have other 2022 servers that have no issue with the User Rights Assignments, so I know it is not a policy version issue (old ADMX).  

I don't have any errors to go off of other than services that cannot start because the policy is not working.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-10*

Same story with privileges.  Same login user.

Working:

Broken:

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-10*

I have a bit more information to share.  I noticed that on my working domain controller, in the security event log there is an entry for Remote Interactive Logon and Interactive Logon that is not present on my non-working DC.

Working:

Broken:

Now trying to see if I can get any information about this discrepancy.
