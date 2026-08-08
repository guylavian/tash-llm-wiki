---
title: "Windows 10 WiFi via GPO now showing correctly"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/811004/windows-10-wifi-via-gpo-now-showing-correctly
question_id: 811004
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# Windows 10 WiFi via GPO now showing correctly

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/811004/windows-10-wifi-via-gpo-now-showing-correctly (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have one single GPO created to configure 4 Wireless Profiles on my client machine. The WiFi SSIDs are as below:  

-  WifiOne  

-  WifiTwo  

-  WifiThree  

-  WifiFour  

When this policy updated on client machine, the user went to a site that has WifiOne and WifiTwo. Since both WiFis are in range, user is able to see both WiFi but when I right click each of them, WifiOne showing "Added by company policy" but WifiTwo is not showing that and user is able to edit WifiTwo. GPO is applied successfully by checking gpresult.  

May I know is this a normal behavior or how can I make both Wifi SSID to show "Added by company policy"?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-19*

Hello Marcus,  

The setup for new SSID through group policy is simple, and should not be cause for any misconfiguration.   

For reference the GPO is in Computer Configuration>Policies>Windows Settings>Security Settings>Wireless Network (IEEE 802.11) Polices and when right click and selecting New, you configure the parameters to deploy the Wireless Network to the clients.  

My suggestion is that either the policy is not applying correctly, or in most cases, the user has previously added manually the network, thus the setting can't overlap and prevails the original manual creation.   

1.To verify the GPO application to the PC you can run as administrator the next command: GPRESULT /H OUTPUT.HTML and the output file will show all the policies applying to the computer.  

-  On the other hand you can try to delete the WifiTwo profile using command prompt as: Netsh wlan delete profile <profilename>   

(You can reference to this article for more wireless profile modifications using command prompt: https://devblogs.microsoft.com/scripting/using-powershell-to-view-and-remove-wireless-profiles-in-windows-10-part-1/ )  

If that seems to work, you can even create a logon script that deletes the networks called Wifi* before the GPO applies, to ensure that the users always receive the Wireless Network confirmation correctly and with any updated settings.  

--If the reply is helpful, please Upvote and Accept as answer--
