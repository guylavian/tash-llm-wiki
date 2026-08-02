---
title: "Can't change files in sysvol folder when access through UNC from DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/855024/cant-change-files-in-sysvol-folder-when-access-thr
question_id: 855024
fetched: 2026-07-25
answer_count: 10
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Can't change files in sysvol folder when access through UNC from DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/855024/cant-change-files-in-sysvol-folder-when-access-thr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

we're facing with weird issue, we can't change\add\create files under SYSVOL folder when we access through UNC from DCs.  

but if we access to the SYSVOL folder through UNC from other servers in domain there is no issue to change\add\create files.  

we're using domain admin user.  

all servers in the domain are Windows server 2019 and we have 2 DC. only one forest,domain and site   

so i think it's a default security policy in DCs, but i can't find where it's configured and it's seems to me very strange policy cause i didn't understand why there is need for it.  

Does anyone know where it's configured and why?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-05-22*

Can you create a test file in the sysvol folder on one of the DC's without using the UNC path i.e C:\windows\Sysvol?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-05-19*

Hi @Arnold MIshaev       

The usual reason why this happen is because UAC is enabled on the DC. The main issue with UAC is that Windows Explorer will start always started with reduced permissions and there is no way to start an new instance of Windows Explorer with Run As Administrator, as there can only be one instance running, so will always use the reduced permissions instance of Explorer.  The easiest way to confirm this is to start an instance of NotePad with Ran As Administrator right and try and create a file in the sysvol share.    

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-22*

@Gary Reynolds       

it's works i'm managed to create files    

but after that  i can't delete them from DC

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-21*

Hi @Gary Reynolds   @rr-4098       

I'm accessing via UNC path     

I've attached the screenshot of the "error" message

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-20*

Hi @Gary Reynolds       

Thanks for your respond.    

but i have disabled UAC via control panel then rebooted the server and it doesn't help.    

i also run "windows explorer" as Administrator and it appear to be same issue
