---
title: "Print Nightmare patch + Ghost printers & printer GPO error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/616012/print-nightmare-patch-ghost-printers-printer-gpo-e
question_id: 616012
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-print-jobs"]
---
# Print Nightmare patch + Ghost printers & printer GPO error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/616012/print-nightmare-patch-ghost-printers-printer-gpo-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Recently i have had a few users notice that there are some ghost/duplicate printers on their Windows 10 desktops. They can still print fine but it shows each printer as double or tipple, some saying they are offline (when they are not) as the next one beside is it the same printer but its online.    

This is not a wide spread issue, perhaps a handful of users so far that i have found.    

The printers are pushed out via GPO on Windows Server 2012 R2 Standard, fully patched. I checked to see if there are any duplicate printers being pushed (none found).    

I noticed when i do a gpupdate /force this error appears:    

    

    

which lead me to dig deeper and find this post: https://learn.microsoft.com/en-us/answers/questions/567987/windows-failed-to-apply-the-deployed-printer-conne.html    

The Reg key fixed the GPO error but caused another issue now the user cannot remove any printer from their computer (gives permission errors).    

From what iam reading this mess was all caused by the Sept print nightmare patch which iam reluctant to remove right now.    

Any ideas? I cant find much more online and it keeps referencing articles such as the above with the reg entry.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-21*

Hi @Derek Aleixo       

Ghost devices are the previously installed devices which are not connected but the drivers for that device is still present in the computer and sometimes shows in the devices list.    

To get rid of unwanted drivers, devices, or services, use the following steps:    

Open the Start menu.    

Swipe to the upper right corner to bring charm bar.    

Type cmd in search box.    

Select cmd from the displayed list, right click and Open as administrator.    

At the command prompt, type in set devmgr_show_nonpresent_devices=1 and press Enter.    

(Note that nothing seems to happen. This is expected. You are actually setting an environment variable which is going to help you to see hidden devices.)    

On the next command prompt line, type devmgmt.msc and press Enter. This will launch the Windows Device Manager Console.    

In the Device Manager Console, from the View menu, select Show Hidden Devices.    

As you expand the different drivers and devices in the device manager, you will see not only the items that Windows currently detects as installed on your PC; but you will also see drivers, devices, and services which have been loaded in the past but were not uninstalled or are not currently started. You can find your offending device, right-click, and choose uninstall to remove it from the system completely.    

---------    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-15*

Just going to add here that I am having the exactly same problem.  

Did you ever figure it out?  One similarity is that it is also occurring with Xerox copiers.  For me, its only the Xerox copiers doing it.... Maybe a clue.  

Are you using the Global Print Driver?  I would love to figure this out.  Its causing us too many support calls...
