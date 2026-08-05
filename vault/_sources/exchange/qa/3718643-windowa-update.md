---
title: "Windowa update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3718643/windowa-update
question_id: 3718643
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: []
---
# Windowa update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3718643/windowa-update (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My pending windows update (Device health and performance) will not update with error code (0x80070424)

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-15*

Hi Caleb.    I'm Greg, an installation specialist, 10 years awarded Windows MVP, and Volunteer Moderator, here to help you. 

I'll give you everything possible for fixing failed Windows Updates, so that at least something will work.  Even if you've tried a step, please do it over in sequence.  Report back any steps that cannot be performed and why:

Some Updates will sort themselves out in a few days so I'd wait to see.  If not or they are bothering you then here are steps you can take:  

-  Run the Windows Update Troubleshooter from Windows Settings > Update & Security > Troubleshoot.  

-  There is a new guided walk-through from Microsoft for repairing Windows Update that leads up to resetting components if necessary:  https://support.microsoft.com/en-us/help/10164/....  Try running that first.

-  Type Services in Search box, run Services app as Administrator, open Windows Update Service and Background Intelligent Transfer Service and Stop both.

Press “Windows (flag) key + R,” copy and paste C:\Windows\SoftwareDistribution\ press the Enter button.

This folder has all the files related to Windows updates.

Open the “Download” folder, select and delete all the files.

Restart Windows Update and Background Intelligent Transfer services in Services app by opening both and choosing Start. 

-  If that fails try manually resetting Windows Update Service with the commands here:

 https://www.how2fixerror.com/manually-reset-win...

-  You can also install the Updates manually that fail to install, which are logged at Settings > Update & Security > Windows Update > Installed Update History, and then search for those to download and install from this Catalog:  https://www.catalog.update.microsoft.com/Search...

-  If they continue to fail and interfere, then you can block them using one of these methods:  https://www.howtogeek.com/224471/how-to-prevent...

-  If problems with Updates have become chronic and especially if you have other performance problems, go over this checklist to make sure the install is set up correctly, optimized for best performance, and any needed repairs get done:  http://answers.microsoft.com/en-us/windows/wiki...

Start with Step 4 to turn off Startup freeloaders which can conflict and cause issues, then Step 7 to check for infection the most thorough way, then step 10 to check for damaged System Files, and also Step 16 to test a new Local Admin account.  Then continue with the other steps to go over your install most thoroughly. 

-  If you have an older version or if nothing else works then while I am here to help you I would manually upgrade to the latest version by opening the Media Creation Tool from this link:  http://windows.microsoft.com/en-us/windows-10/m..., choose Download Tool Now, then open the tool and choose Upgrade This PC Now.   This saves your files, apps and most settings in place, is the most stable method to change versions, brings your Updates current, resolves most problems.

 If any problems report back the verbatim error and number, then continue with these steps for overcoming Version Upgrade problems:  http://answers.microsoft.com/en-us/windows/wiki...

I hope this helps. Feel free to ask back any questions and keep me posted.  If you'll wait to rate whether my post helped you, I will keep working with you until it's resolved.

________________________________________________________

Standard Disclaimer:   There are links to non-Microsoft websites. The pages appear to be providing accurate, safe information. Watch out for ads on the sites that may advertise products frequently classified as a PUP (Potentially Unwanted Products). Thoroughly research any product advertised on the sites before you decide to download and install it.
