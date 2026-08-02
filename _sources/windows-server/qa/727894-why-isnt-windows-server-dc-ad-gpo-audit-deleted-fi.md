---
title: "Why isn't Windows Server DC AD GPO Audit Deleted Files working?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/727894/why-isnt-windows-server-dc-ad-gpo-audit-deleted-fi
question_id: 727894
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Why isn't Windows Server DC AD GPO Audit Deleted Files working?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/727894/why-isnt-windows-server-dc-ad-gpo-audit-deleted-fi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A folder is getting deleted and I don't know how.  It is in a shared folder on a DC.  

I created a GPO, linked it to the Domain Controllers OU, and enabled object access.  

I went to the shared folder and enabled auditing for "everyone" and checked, "delete subfolders and files", "delete", and "change permissions".  

I ran GPUPDATE /FORCE on the DC with the share.  

I deleted some files but they do not show up in the Event Log Security section.  I waited a few days and checked again but no "Deleted" entries or IDs for deletions.  

I know that auditing is enabled for the folder because the Log shows file access events for files in the folder.  

I searched for solutions but keep being sent to sites that sell software for this task so, if there is a trick to making this work natively, I doubt those sites would want to share it.  

Does someone know how to make this work natively or must I find a 3rd-party solution?  

Thank you in advance!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-11*

I see someone has been deleting my responses to these posts so I will try to respond again.  

These did not solve the problem and only repeat what I stated in the original question.  

Please help.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-16*

Hello @Jax Planet       

Yes, this is possible by native tools and you don't need any third-party tools to achieve this.     

Maybe you are missing this before you set up auditing for files and folders, you must enable object access auditing. To do this, define auditing policy settings for the object access event category. If you don't enable object access auditing, you'll receive an error message when you set up auditing for files and folders, and no files or folders will be audited.    

If you define this policy setting, you can specify whether to audit successes, audit failures, or not audit the event type at all. Success audits generate an audit entry when a user successfully accesses an object that has an appropriate SACL specified.     

Here is a link to help you with applying the policy.    

Audit object access    

https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-object-access    

Hope this resolves your Query!!    

--    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-02-13*

Take a look at the following article and just for test and see if it work on few files and folders and see if it works, take a look at:    

https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/apply-a-basic-audit-policy-on-a-file-or-folder    

Apply these policies in addition to the delete one and see if it works?
