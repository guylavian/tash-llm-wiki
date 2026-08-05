---
title: "GPOs missing Win10  'Relax mimimum password length limits' settings"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/690915/gpos-missing-win10-relax-mimimum-password-length-l
question_id: 690915
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# GPOs missing Win10  'Relax mimimum password length limits' settings

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/690915/gpos-missing-win10-relax-mimimum-password-length-l (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to create a GPO to get Windows 10 systems in compliance with CIS level 1 standards.    As the environment I am working in is security conscious and adverse to change they do not want any AD/GPO tools on general servers/workstations.  I have created the Central Store for the ADMX templates and have the lasts ones in the 'Policy Definitions' folder (21H2 from Nov 21).  It does not matter if I try to create the GPO on a 2012R2, 2016 or 2019 server/dc that setting is not there.  When editing the settings it does show it is reading the templates from the Central Store.  As per the documentation I have that setting should be available to any system with the 'Windows 10 update 2004 from May 2020' or newer ADMX template files.    

Any assistance is greatly appreciated.  

Thanks, Ed

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-30*

I am also seeing this issue on my environment.  I have 3 DCs, two of them are 2016 and one 2019.  We are running Windows 10 21H1 and 21H2 clients so If I download the latest templates for those clients from Microsoft, shouldn't it include the settings introduced in 2004 version?  Also, if I download the 2004 version and import those in my central store, would I loose anything?  Seems like I would be going backward.  Why would the later versions of the GPO Templates not include those settings?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-12*

Hi there,  

It seems you are missing the policies after Windows version 2004 which introduced a new Group Policy setting that allows you to configure the minimum password length to a value greater than 14.  

To activate the Relax minimum password length limits setting, which was added with Windows 10 2004, you can check with the below article and see if you have updated your PC with the specific KB update. This Group Policy Management Editor allows up to 128 characters.  

Minimum Password Length auditing and enforcement on certain versions of Windows  

https://support.microsoft.com/en-us/topic/minimum-password-length-auditing-and-enforcement-on-certain-versions-of-windows-5ef7fecf-3325-f56b-cc10-4fd565aacc59  

--If the reply is helpful, please Upvote and Accept it as an answer--
