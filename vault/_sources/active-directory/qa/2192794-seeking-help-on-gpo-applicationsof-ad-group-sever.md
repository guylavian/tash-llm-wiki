---
title: "Seeking Help on GPO applicationsof Ad Group Sever Access"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2192794/seeking-help-on-gpo-applicationsof-ad-group-sever
question_id: 2192794
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: []
---
# Seeking Help on GPO applicationsof Ad Group Sever Access

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2192794/seeking-help-on-gpo-applicationsof-ad-group-sever (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am making changes to access to servers I help managed. At the moment, AD groups are controlled by Restricted Groups in the Computer Configuration > Windows Settings > Security Settings > Restricted Groups area of GPO.

I wish to maintain some of these groups only for the admin side and ma making geneal user now conditional on server names.

For this, I have applied settings under Computer Configuration > preferences > Control Panel and applied Item-Level targets.

Regardless of the item level targets or removing them, the groups I ask GPO to apply are just not being applied.

I am at wits end wondering why the direct way of adding AD groups under GPO works but tthe Control pnael section refuses to add anything I supply.

Is there another setting that I need to control to allow AD groups to be added from the 2 ways GPO allows ?

Help would be appreciated before I lose more hair from tearing it out.

Thank you

Clint

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-30*

Hello,

For the permissions to manage users and groups in Active Directory and GPO, you can check the following points: 

-  First, make sure you have sufficient permissions to modify and apply GPO. In addition, you also need to make sure that the members of the AD group have sufficient permissions to receive and apply GPO. General steps: Open AD Manager and select "Advanced Features" from "View" on the toolbar. Right-click the group you want to check, select "Properties", then select the "Security" tab, and click "Advanced" at the bottom. In the "Advanced" window, select the user or group you want to view, and click "View Effective Access" to view the effective permissions of the user or group in the AD group. 

-  Check the order in which GPOs are applied. The order in which GPOs are applied may affect the application of settings. By default, GPOs are processed in the order of local GPOs, site GPOs, domain GPOs, and organizational unit GPOs. If multiple GPOs are applied to the same object, the later applied GPO will overwrite the earlier applied GPO. 

-  Double-check your configuration of GPOs and AD groups to make sure they are correct. 

-  It takes some time for policy changes to take effect on the target machine. You can use the `gpupdate /force` command to force an immediate policy refresh.

References:

Appendix B - Privileged Accounts and Groups in Active Directory | Microsoft Learn

Group Policy processing for Windows | Microsoft Learn

We value your feedback, click Yes or No to help us improve the support experience.

Best regards,

Jacen Wang
