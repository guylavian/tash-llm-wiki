---
title: "Enable USB ports blocked by active directory policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/765824/enable-usb-ports-blocked-by-active-directory-polic
question_id: 765824
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Enable USB ports blocked by active directory policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/765824/enable-usb-ports-blocked-by-active-directory-polic (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a GPO in my active directory that restricts USB device connections to all client machines in the company, at this time I needed to connect a camera via USB to access the video recordings, to access the camera is necessary to move the client machine to an organizational unit that does not have the USB restriction GPO, I would like to know if there is some kind of configuration either on the client machine or in the GPO that allows me to connect only that camera via USB port. Thank you in advance for your help.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 2 · updated: 2022-03-10*

Most of the time, what the GPO does is blocking USB Storage Device. So it should not affect other devices unless they also have a USB Storage presentation. But an export of the effective GPO will tell us (you can generate this with the command `gpresult /h GPO.html`).   

But maybe that's not a GPO that is blocking the ports, and you might have other products (or BIOS features) which go further than just disabling USB storage.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-04-01*

Hello @Eduar Muñoz Murcia

I think this is what you need:

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc731387(v=ws.10)?redirectedfrom=MSDN

In case this helped kindly mark the answer as Accepted

BR

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-23*

I'm not an AD administrator, but I have a security question related to this thread: can we setup a GPO that blocks usb storage devices, but allows us to specifically allow company USB drives that we control?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-15*

Hi @Eduar Muñoz Murcia       

You can deny certain types of device access. For example, you can restrict USB storage devices but allow other types of USB device. This may work for you depending on the reason why you’re restricting USB?    

Open Computer Configuration => Administrative Templates => System => Removable Storage Access => in the right pane, open Removable Disks: Deny Execute Access.    

I do hope this answers your question.    

Thanks.    

--    

--If the reply is helpful, please Upvote and Accept as answer--
