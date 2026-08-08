---
title: "set proxy at computer level via gpo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2259988/set-proxy-at-computer-level-via-gpo
question_id: 2259988
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# set proxy at computer level via gpo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2259988/set-proxy-at-computer-level-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to change proxy settings at computer level via group polcy in Windows 10/11 but I note GPO gives it at user level, I would not like to enable loopback processing. 

Ideas?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-07-21*

Hello William,

   Thank you for posting question on Microsoft Windows Forum.

   Based on your query of changing proxy settings at computer level via group policy in Windows 10/11 without enabling loopback processing. You can consider to apply Make proxy settings per-machine policy which effectively tells the operating system to treat user-level proxy settings as if they were applied to the machine. So, even though you define the values for the proxy under User Configuration (which is the only place to do it through the graphical interface for IE/Edge proxy), the computer-level policy ensures those values apply universally to any user logging into that specific computer.

   The following points are for your reference regarding the above policy without the need of using loopback processing.

1.Enable "Make proxy settings per-machine (rather than per user)":

-  Create or edit a GPO linked to the OU containing your Windows 10/11 computer objects.

-  Navigate to Computer Configuration > Administrative Templates > Windows Components > Internet Explorer.

-  Enable the policy "Make proxy settings per-machine (rather than per user)".  

2.Define your proxy settings:

-  In the same GPO (or a separate one linked to the same computer OU), define your proxy settings under User Configuration > Preferences > Control Panel Settings > Internet Settings.

-  Right-click Internet Settings and choose New > Internet Explorer 10 (even for IE11/Edge).

-  Go to the Connections tab, click LAN settings, and configure your proxy server address and port.

-  Press F6 (the key to enable the setting and make the underline green) on the proxy settings fields to ensure they are applied by Group Policy Preferences.

3.Preventing Users from Changing Proxy Settings:

-  In the same GPO, navigate to Computer Configuration > Administrative Templates > Windows Components > Internet Explorer > Internet Control Panel.

-  Enable "Disable the Connections page" to prevent users from accessing the proxy settings at all.

Please note: Make sure to test the GPO changes thoroughly to ensure it is working as expected in testing environment before applying it to production environments.

You can refer to the following article for more information.

-  https://theitbros.com/config-internet-explorer-11-proxy-settings-gpo/#google_vignette

Hope the above information is helpful!
