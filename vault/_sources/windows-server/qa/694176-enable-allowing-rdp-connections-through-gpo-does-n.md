---
title: "Enable allowing RDP connections through GPO does not work"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/694176/enable-allowing-rdp-connections-through-gpo-does-n
question_id: 694176
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Enable allowing RDP connections through GPO does not work

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/694176/enable-allowing-rdp-connections-through-gpo-does-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.  

I have a GPO that enables remote desktop on my computers  ("Computer Configuration >> Administrative Templates >> Windows Components >> Remote Desktop Services >> Remote Desktop Session Host >> Connections >> Allow users to connect remotely via Remote Desktop Services")  

 This GPO create the Key (HKLM\software\Policies\Microsoft\Windows NT\terminal services\fDennyTSConnections - value 0) in the computers.  

But RDP connections are not established (in remote desktop configuration we see that it is blocked by group policy but the RDP mark is as disabled).  

If I unlink the GPO and enable remote desktop manually, the RDP connections work correctly, so we suspect that there is a problem with the application of this GPO.  

What could be happening?  

PS: The rest of the GPOs work correctly.  

Best regards.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-01-14*

I was referring to the GPO "Allow users to connect remotely via Remote Desktop Services"  

sorry, I've already edited it

## Answer (community) — community member

*upvotes: 1 · updated: 2022-01-14*

Hello PompadourInformatica  

Not sure which specific policy you refer to inside the  folder, but unless is the fDenyTSConnections, any value as 0 would be a Disabled.   

I would try instead with the policy Computer Configuration >> Administrative Templates >> Windows Components >> Remote Desktop Services >> Remote Desktop Session Host >> Connections.   

On the right-side panel. Double-click on Allow users to connect remotely using Remote Desktop Services as Enabled.   

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-28*

With what user are you trying to RDP?    

Is that user member of the remote desktop users group on that machine? Otherwise it won't work. (admins will of course)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-29*

[11:35 AM] Nick Doud    

It used to be called Remote Desktop (TCP-In)    

NOW it is called Remote Desktop - User Mode (TCP-In)    

[11:36 AM] Nick Doud    

The GPO I have does the following things for Remote Desktop;    

Computer Configuration -> Policies ->Administrative Templates -> Windows Components -> Remote Desktop Services -> Remote DEsktop Session Host -> Connections -> "Allow users to connect remotely by using Remote Desktop Services" = Enabled    

Computer Configuration -> Policies -> Windows Settings -> Security Settings -> Local Policies -> User Rights Assignment -> "Allow log on through Terminal Services" = Administrators, DOMAIN\Domain Admins, Remote Desktop Users    

Computer Configuration -> Policies -> Windows Settings -> Security Settings -> Windows Firewall with Advanced Security -> Inbound Rules -> "Remote Desktop (TCP-IN)" = Enabled for Domain & Private

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-18*

I am experiencing the same issue. I set this up for my test groups and even a PC that already had it turned off was disabled after run gpupdate /force.
