---
title: "Printer deployment via GPO working but not using OEM drivers?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/531316/printer-deployment-via-gpo-working-but-not-using-o
question_id: 531316
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-print-jobs"]
---
# Printer deployment via GPO working but not using OEM drivers?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/531316/printer-deployment-via-gpo-working-but-not-using-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I'm not entirely sure if this is related to the whole PrintNightmare mess or not.  

* All staff recently received new PCs. Staff do not have admin privileges on these new PCs.  

* We're using a GPO for printer deployment (Computer Configuration > Windows Settings > Deployed Printers) to push out our common printers.  

* The printers are showing up on staff PCs, but they are not getting the correct driver with them. This is especially problematic with copiers.

For example, on our Windows Server > Print Management > XeroxD125-copier > Advanced tab, the driver shown is the one we want--Xerox D95/D110/D125 C/P Class Driver. This driver has all the finishing options we want for handling collation, hole punching, the usual copier features etc.  

The copier is showing up on the client Win10 desktops under Devices and Printers, but if you go to the printer properties, under Advanced > Driver, the driver listed is "Microsoft enhanced Point and Print driver", not "Xerox D95/D110/D125 C/P Class Driver", and this doesn't have all the same finishing options that the other one has. Because the users don't have local admin privs, even switching to the other driver is not an option--it's greyed out.

I've tried the reghack detailed at https://support.microsoft.com/en-us/topic/kb5005652-manage-new-point-and-print-default-driver-installation-behavior-cve-2021-34481-873642bf-2634-49c5-a23b-6d8e9a302872 (HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows NT\Printers\PointAndPrint, DWord name RestrictDriverInstallationToAdministrators set to zero), on a test PC, but it doesn't seem to have helped here.

So, again, I'm not sure if this is related to the various summer updates for Print Nightmare, and these are new PCs. Any suggestions would be greatly appreciated. Thanks in advance!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-29*

if your selected Xerox driver is a v4 driver, you'll probably need the Print Experience App to accompany that  

https://www.support.xerox.com/en-us/product/xerox-d95-d110-d125/content/147197
