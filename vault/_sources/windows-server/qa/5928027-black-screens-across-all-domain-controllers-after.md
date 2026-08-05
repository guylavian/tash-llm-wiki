---
title: "Black screens across all domain controllers after changing bypass traverse checking setting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5928027/black-screens-across-all-domain-controllers-after
question_id: 5928027
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
answer_author_roles: ["Independent Advisor"]
---
# Black screens across all domain controllers after changing bypass traverse checking setting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5928027/black-screens-across-all-domain-controllers-after (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

These are the changes I made to our DC settings in order to get Splunk upgraded, according to their documentation: 

https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.4/install-splunk-enterprise-on-windows/choose-the-windows-user-splunk-enterprise-should-run-as

-  Permission to log on as a service.

-  Permission to log on as a batch job.

-  Permission to replace a process-level token.

-  Permission to act as part of the operating system.

-  Permission to bypass traverse checking.

In a different GPO to the default domain controller GPO, I defined these policies and gave it to the SYSTEM and SERVICE account, like the documentation said. The Splunk upgrade didn't work until I made these changes. As a result of these changes, both DCs are on, but now the screens are black when you log in. I did some research and it seems that changing the "Bypass traverse checking" is the culprit, if you remove "Everyone," "Authenticated Users," etc. However, when I did secedit /export /cfg C:\secpol.cfg, the text file shows that all the default groups are in there, except for LOCAL SYSTEM (even though I explicitly defined it in the GPO). I added that into the text file and ran secedit /configure /db path\to\secedit.sdb /cfg C:\secpol.cfg /areas USER_RIGHTS through PDQ, but I keep getting an error output that's basically the manual for the secedit command. When I compare the syntax of my command with the example syntax, I can't see where I did anything wrong. I am not able to boot into safe mode with networking, as the screen freezes on the windows logo.

Assistance is greatly appreciated and urgently needed! I know it's best practice not to run other things on a domain controller. This is a network I inherited and our version of Splunk was flagged as a critical vulnerability.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-06-23*

Hi Washington, Candace N

What you’re running into is a classic case of user rights assignments on a domain controller being way more sensitive than Splunk’s docs make it sound. The “Bypass traverse checking” setting is indeed the usual culprit when logon screens go black, because if you strip out groups like Everyone or Authenticated Users, you basically cut off the OS from being able to enumerate paths for normal logons. Adding SYSTEM back in doesn’t fully fix it if those defaults are missing.

The secedit command error you’re seeing is usually about syntax or the database path . Double‑check that your `/db` argument points to a valid `.sdb` file and that you’re not accidentally overwriting a locked database. Also, when you export and re‑import, you need to make sure the policy refresh actually applies; sometimes PDQ pushes don’t trigger a full user rights refresh until after a reboot.

 think  the safest way forward is to roll back the GPO changes for “Bypass traverse checking” to defaults (restore Everyone, Authenticated Users, etc.), then reapply Splunk’s required rights only to the Splunk service account, not SYSTEM or SERVICE globally. Running Splunk directly on a DC is always dicey, but since you inherited this setup, the rollback plus a clean redeploy of Splunk’s rights should get you back to a working login state.
