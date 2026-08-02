---
title: "Active Directory domain services won't start following failed DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194348/active-directory-domain-services-wont-start-follow
question_id: 2194348
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active Directory domain services won't start following failed DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194348/active-directory-domain-services-wont-start-follow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We lost one of our DCs due to a hardware failure. Now the remaining DC won't start Directory Services because it can't find the other one to sync to.

The remaining DC is the holder of all FSMO roles.

I'm getting the following error:

This server is the owner of the following FSMO role, but does not consider it valid. For the partition which contains the FSMO, this server has not replicated successfully with any of its partners since this server has been restarted. Replication errors are preventing validation of this role. 

Operations which require contacting a FSMO operation master will fail until this condition is corrected. 

The error message suggests using NTDSUTIL to seize the role to the same server. Have tried that but it didn't help.

I'm unable to remove the old server using ntdsutil because it can't connect to the domain.

Any suggestions?

thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-07*

Hi Chris Hawkins 99,

It sounds like you may need to perform a metadata cleanup to remove the failed DC from Active Directory. This will allow the remaining DC to start Directory Services and properly replicate with its partners. 

To perform a metadata cleanup, you will need to use the ntdsutil command-line tool. Here are the general steps:

Open a Command Prompt window as an administrator: In the Start menu, right-click Command Prompt and click Run as administrator. If the User Account Control dialogue box appears, provide the Enterprise Administrator credentials as required and click Continue.

At the command prompt, type the following command and press Enter:

ntdsutil

At the ntdsutil: prompt, type the following command, and then press Enter:

metadata cleanup

At the metadata cleanup: prompt, type the following command, and then press Enter:

remove selected server <ServerName>

In the Server Removal Configuration dialog box, review the messages and warnings, and then click Yes to remove the server objects and metadata.

At this point, Ntdsutil confirms that the domain controller was successfully deleted. If you receive an error message indicating that the object could not be found, the domain controller may have been previously deleted.

At the metadata cleanup: and ntdsutil: prompts, type quit and press Enter.

To confirm the deletion of a domain controller, do the following:

Open Active Directory Users and Computers. In the domain of the deleted domain controller, click Domain Controllers. In the details pane, the object of the deleted domain controller should not be displayed.

Open Active Directory Sites and Services. Navigate to the Servers container and make sure that the server object of the deleted domain controller does not contain an NTDS settings object. You can delete the server object if no child objects are displayed below the server object. If child objects are present, do not delete the server object because it is being used by another application.

Best regards,

Qiuyang
