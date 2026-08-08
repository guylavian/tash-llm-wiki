---
title: "GPO password minimum length limited to 14 characters"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/560646/gpo-password-minimum-length-limited-to-14-characte
question_id: 560646
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# GPO password minimum length limited to 14 characters

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/560646/gpo-password-minimum-length-limited-to-14-characte (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've dug through threads where this question has been asked before but found no answers to this question.  

We have a Windows 2016 domain running with an extensive set of group policies.  

The domain controllers are running Windows Server 2016 Version 1607 (OS Build 14393.4651) and are updated to the latest patch levels.  

When I attempt to edit a GPO for restricted accounts as required by corporate measure plans, the minimum password length is limited to 14 characters. The measure plan requires 15 or more.  

Powershell shows the following  

PS C:\Users\adminXXXXX> Get-ADObject (Get-ADRootDSE).schemaNamingContext -Property objectVersion  

DistinguishedName : CN=Schema,CN=Configuration,DC=aaaaa,DC=bbbbb,DC=ccc  

Name              : Schema  

ObjectClass       : dMD  

ObjectGUID        : e450e53f-24cc-47c0-956f-d1d1f53d381d  

objectVersion     : 87  

I updated the schema to Server 2019   

I mounted a Server 2019 ISO and executed F:\support\adprep>adprep /forestprep  

which reported   

Current Schema Version is 87  

Upgrading schema to version 88  

Verifying file signature  

Connecting to "DC01.xxxx.net"  

Logging in as current user using SSPI  

Importing directory from file "F:\support\adprep\sch88.ldf"  

Loading entries........  

7 entries modified successfully.  

The command has completed successfully  

Connecting to "DC01.xxxx.net"  

Logging in as current user using SSPI  

Importing directory from file "F:\support\adprep\PAS.ldf"  

Loading entries....................  

26 entries modified successfully.  

The command has completed successfully  

Adprep successfully updated the forest-wide information.  

I then executed adprep /domainprep  

Which reported  

Adprep successfully updated the domain-wide information.  

PS C:\Users\adminbakejx> Get-ADObject (Get-ADRootDSE).schemaNamingContext -Property objectVersion  

DistinguishedName : CN=Schema,CN=Configuration,DC=jocy,DC=siemens,DC=net  

Name              : Schema  

ObjectClass       : dMD  

ObjectGUID        : e450e53f-24cc-47c0-956f-d1d1f53d381d  

objectVersion     : 88  

I am at a loss as to how to get the GPO set to more than 14 characters.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-03-25*

15 characters and more   

https://support.microsoft.com/en-us/topic/minimum-password-length-auditing-and-enforcement-on-certain-versions-of-windows-5ef7fecf-3325-f56b-cc10-4fd565aacc59

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-13*

This sounds like an OS version issue on your domain controllers. We had to upgrade the OS to Server 2019 in order to be able to enable the "relax minimum password length limits". Once that is enabled you can modify/increase the password length beyond 14. This is a good time to update your ADMX files in the central store as well.

This page will be helpful and keep in mind that the client version matters as well if not patched with the proper KB.

https://support.microsoft.com/en-us/topic/minimum-password-length-auditing-and-enforcement-on-certain-versions-of-windows-5ef7fecf-3325-f56b-cc10-4fd565aacc59

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-08*

I have this exact same problem and was really excited when i found this thread. Too bad it doesn't have an answer.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-22*

I am certainly missing new policies. The underlying question is how to get them updated at the domain level.    

This policy may comer into play with some of our Windows 10 workstations and VMs, it is the 2016 and 2019 servers that need to recognize it though.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-21*

Hello John,  

I think you are missing the new policies after Windows version 2004 which introduces a new Group Policy setting that allows you to configure the minimum password length to a value greater than 14.  

But to let the new settings apply to workstations, we need to activate the Relax minimum password length limits setting, which was added with Windows 10 2004, the Group Policy Management Editor allows up to 128 characters.  

Hope this helps in your case,   

Regards,  

--If the the reply is helpful, please Upvote and Accept as answer--
