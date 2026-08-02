---
title: "FreeIPA kerberos login"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1074431/freeipa-kerberos-login
question_id: 1074431
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Volunteer Moderator"]
---
# FreeIPA kerberos login

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1074431/freeipa-kerberos-login (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,     

We’ve setup 66 PCs with Windows 11 to login using the FreeIPA Kerberos. This has been working without any problems since April 2022. All PCs share the very same Windows image via FOG server (Academic Volume License). The image is created in one of them and then uploaded to FOG server for deployment to all of them.     

One of The the PCs was used as an ‘image generator’ where the Windows would be updated to 22H2. Update went very smooth after removing Rx Reboot Restore (a DeepFreeze – kind – of software) which caused the update to fail.     

Right after the first reboot, once I tried to logon I got the message “There is a time and / or date difference between the client and the server”.  Note that:    

- 	All other 65 PCs login just fine    

- 	Time is in sync between the updated PC and the IPA server down to minute    

- 	I re-registered the updated PC as a different host so that to perform the entire procedure again in case something got busted during update.     

I did notice that:    

- 	All the working PCs do not have encryption protocols enabled, I did however enabled them in the updated PC in case this was the issue.    

- 	The 22H2 introduced KDC and Kerberos settings sections in Global Policy Editor, I changed a couple of settings to ‘Enabled’ but got the same results.     

Do you believe that it’s a new settings issue or one of the numerous bugs introduced with 22H2?    

Thank you for your time!    

Manos Georgoudakis

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-15*

Actually the problem is far more stranger than I thought. I enabled a registry key that enables proper logging of Kerberos transactions and indeed, the client appears to be sending random dates / times. The attached screenshot event viewer entries were generated within a SINGLE login attempt.     

    

Also note that the Windows 11 pc uses as NTP server the Kerberos host. The date / time of Windows 11 pc is accurate down to minute.     

    

I'm quite lost here, never seen anything like this before.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-08*

Hello there,

As you are facing this after the update this might most probably be an issue with 22H2. Meanwhile, make sure the computer is pointing the NTP server to the DC instead of any other NTP servers.

You can have a regular check to identify any notification released by Microsft regarding this https://learn.microsoft.com/en-us/windows/release-health/status-windows-11-22h2

You can also collect the Event logs and share them with the Microsoft team to get this sorted or get an appropriate workaround for this.  

-Download the process monitor tool.  

-  Get a dump from the process during the error message and share it through the feedback hub.

Process Monitor is an advanced monitoring tool for Windows that shows real-time file system, Registry, and process/thread activity. You can get the tool from here https://learn.microsoft.com/en-us/sysinternals/downloads/procmon

You can raise feedback to the Microsoft team. The Feedback Hub app lets you tell Microsoft about any problems you run into https://support.microsoft.com/en-us/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-11-03*

Hi    

In what country the computer are ? I ask as please validate the timezone and the hour please of the computer in problem..    

I tell that as in 22H2 there is a impact for computer in Jordan.     

On October 5, 2022, the Jordanian government made an official announcement ending the winter-time Daylight Saving Time (DST) time zone change. Starting at 12:00 a.m. Friday, October 28, 2022, the official time will not advance by an hour and will permanently shift to the UTC + 3 time zone.     

The impact of this change is as follows:     

​Clocks will not be advanced by an hour at 12:00 a.m. on October 28, 2022 for the Jordan time zone.     

​The Jordan time zone will permanently shift to the UTC + 3 time zone.     

Symptoms if no update is installed and the workaround is not used on devices in the Jordan time zone on October 28, 2022 or later:    

​Time shown in Windows and apps will not be correct.    

​Apps and cloud services which use date and time for integral functions, such as Microsoft Teams and Microsoft Outlook, notifications and scheduling of meetings might be 60 minutes off.    

​Automation using date and time, such as Scheduled tasks, might not run at the expected time.    

​Timestamp on transactions, files, and logs will be 60 minutes off.    

​Operations that rely on time-dependent protocols such as Kerberos might cause authentication failures when attempting to logon or access resources.    

​Windows devices and apps outside of Jordan might also be affected if they are connecting to servers or devices in Jordan or if they are scheduling or attending meetings taking place in Jordan from another location or time zone. Windows devices outside of Jordan should not use the workaround, as it would change their local time on the device.    

Workaround: You can mitigate this issue on devices in Jordan by doing either of the following on October 28, 2022, if an update is not available to resolve this issue for your version of Windows:    

​Select the Windows logo key, type "Date and time", and select Date and time settings. From the Date & time settings page, toggle Adjust for daylight saving time automatically to Off.    

​Go to Control Panel > Clock and Region > Date and Time > Change time zone and uncheck the option for “Automatically adjust clock for Daylight Saving Time”.
