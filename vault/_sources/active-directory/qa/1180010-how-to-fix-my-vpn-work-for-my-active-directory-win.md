---
title: "How to fix my VPN work for my Active Directory Window Server?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180010/how-to-fix-my-vpn-work-for-my-active-directory-win
question_id: 1180010
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# How to fix my VPN work for my Active Directory Window Server?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180010/how-to-fix-my-vpn-work-for-my-active-directory-win (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question



## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-14*

Hello TechQ

You can follow the next steps, but first check if you have disabled antivirus or firewall on both machines.

-  Ensure that the Required L2TP/IPsec Ports are enabled on VPN Server's side.

Login to the Router on VPN Server's side, and forward the following UDP ports to VPN Server's IP address: 1701, 50, 500 & 4500

-  Connect to VPN via another device or network.

Try connecting to L2TP VPN from another device (e.g. your mobile), or network (e.g. your Mobile's phone network).

-  Delete and recreate the VPN connection.

Sometimes VPN connection problems, are resolved after removing and re-adding the VPN Connection.

If you are using NAT in your network, you will need to add another configuration:

1.On the Destination server open Regedit

2.Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Sevices\PolicyAgent

3.Right click the right pane, and create New –> DWORD (32 bit) Value.

4.For the new key name type: AssumeUDPEncapsulationContextOnSendRule and press Enter.

-  Note: The value must be entered as shown above and with no space at the end.

-  Double click at AssumeUDPEncapsulationContextOnSendRule value, type 2 at Value data and click OK.

6.Close Registry Editor and reboot the machine.

Last but not least you can check if LCP is enabled for the PPP of the VPN client/server at:

In Settings, Ethernet, Right-click on the VPN connection and chose Properties.

At Options tab, click PPP Settings.

Check Enable LCP extensions and click OK.

At Security tab, check the following and click OK.

Allow these protocols

Challenge Handshake Authentication Protocol (CHAP)

Microsoft CHAP Version 2 (MS-SHAP v2)

Try to connect to VPN. The connection should be established now without problems. 

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-02-13*

Do not install the RRAS / VPN role on a domain controller. The multi-homing will always cause no end to grief for active directory DNS. Better to install the role on a dedicated member server.  

https://www.thomasmaurer.ch/2018/05/how-to-install-vpn-on-windows-server-2019/  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
