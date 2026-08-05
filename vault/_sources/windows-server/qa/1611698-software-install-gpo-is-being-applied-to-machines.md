---
title: "Software Install GPO is being applied to machines but the .msi file is not running"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1611698/software-install-gpo-is-being-applied-to-machines
question_id: 1611698
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Software Install GPO is being applied to machines but the .msi file is not running

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1611698/software-install-gpo-is-being-applied-to-machines (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have created a software installation GPO and the software is on a network share and it is set to Assigned.  The GPO is applying to machines but the .msi file itself is not initializing.  What should I research to see what the issue is?  Thank you.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-11*

Hello Ryane Helder,  

Thank you for posting in Q&A forum.  

You can troubleshoot the issue as below.

1.Please check you can access the .msi file like \file server\share\file name.msi on client machines.  

And you can create a group and put all the machines that need to apply Software Install GPO to these machines to this group and assign this group to have read permission on the shared folder above.  

2.Because you assign a package via GPO, so you can create an OU and put all the machines that need to apply Software Install GPO to this OU and link the GPO (Computer Configuration*Software Settings**Software installation*) to this OU.  

3.For some specific GPO, if we want to refresh them, we must sign out and sign in to make user configuration to take effect (folder redirection or drive map via GPO). We must restart the machine 1-2 time to make computer configuration to take effect (such as install software via GPO).

For these GPO above, if you only run gpupdate /force or wait for the 90-120 minutes to want to GPO refresh, it will not.  

In your case, please restart the client machine 1-3 times and check if the software is installed in Control Panel on client machines.  

Reference:

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/use-group-policy-to-install-software

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-03-08*

Follow https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/troubleshoot-software-installations-debug-logging

hth

Marcin

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-08*

Hi @Anonymous  

The installation of MSI launched during the server restart.

You should be sure that the network is available during the server restart to be able to access on the share of the MSI file.

Did you try to force the gpo by running the following command :

`gpupdate /force `

Please don't forget to accept helpful answer
