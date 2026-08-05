---
title: "Windows 11 Notification Center screws with my graphics card"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4098435/windows-11-notification-center-screws-with-my-grap
question_id: 4098435
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Windows 11 Notification Center screws with my graphics card

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4098435/windows-11-notification-center-screws-with-my-grap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Since about October 19, 2023, a lot of times when the Notification Center gets invoked, one or both of my external displays goes super saturated/contrasty. Here's a simulation of how it looks:  

It looks almost exactly like two copies of the monitor image are being added together using a "color dodge" algorithm, which basically doubles pixel values and blows out anything over 50% brightness. This makes it impossible to see light gray lines and very difficult to read text, etc.  

This can happen both when I open the Notification Center manually (⊞+N), and when a notification pops up (like a Gmail desktop notification). It took me a long time to narrow down what's triggering it. Sometimes it also seems to happen without the notification center being activated.  

-  This happens with two separate monitors of different brands, plugged into two different ports with two different cables, so it's not the monitors or the cables.

-  It can happen with one monitor or both. Usually when one glitches, the other also glitches within a short period of time.

-  Changing monitor settings, display resolution, or color profiles never fixes it.

-  Messing with the graphics cards settings never fixes it.

-  Sometimes unplugging/replugging the monitor in question resets the color, but sometimes not.

-  Sometimes, disabling and re-enabling the NVidia graphics card driver fixes it, but sometimes not.

-  Sometimes, restarting resets the color, but sometimes not.

For reference, this is a Lenovo Legion 7i, running Windows 11 Home v 22H2. All graphics drivers are up-to-date. The most recent Windows update was KB5031323 on 10/12/23 and there are no pending updates.  

-  Processor: Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz 2.59GHz

-  RAM: 32.0 GB

-  OS build: 22621.2428

-  Experience: Windows Feature Experience Pack 1000.22674.1000.0

-  Display adapters: Intel(R) UHD Graphics and NVIDIA GeForce RTX 2070 with Max-Q Design

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-03*

We haven't heard from you in 96 hours, we will no longer observe this thread. If you do need further help please create a new thread to discuss those concerns.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-30*

Hello Peter Romero, 

Welcome to Microsoft Community and we regret the inconvenience caused to you. 

Thanks for sharing the steps and testing as much as possible to narrow down the troubleshooting. Since you encountered this issue on October 19, 2023 and if everything was working fine before then I think the cause of it might be Windows update.
Please check on your machine then please uninstall Windows updates to try again. Use the following steps:open Settings****Update and security >Windows updatesClick Advanced options
Click View your updates History

If you want to Uninstall updates, click uninstall updates on the top, the page installed updates would open and you can uninstall updates easily by right clicking the specific update.
Just type in Installed updates in the search bar on the taskbar and Install updates would be shown, which can also be used to uninstall updates.In addition this, if you install other third-party software or updates to certain programs, this problem may also occur. You can perform a clean boot****and close any non-Microsoft third-party apps then try again.
These steps of "clean boot" might look complicated at first glance. However, to avoid any trouble for you, please follow them in order and step-by step so that it will help you get you back on track.
Have a great day!

Please feel free to let me know if you have any further updates, thanks.

Best Regards,

Lenka-MSFT| Microsoft Community Support Specialist
