---
title: "Server 2019 Domain Controller Issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/500225/server-2019-domain-controller-issues
question_id: 500225
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Server 2019 Domain Controller Issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/500225/server-2019-domain-controller-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We currently have a single domain with 2 domain controllers.  One DC is running Server 2012R2 and the other is running Server 2016.  I am in the process of upgrading all of our servers to Server 2019.  The DCs are some of the last servers to be done.  I built up a new server in VMware and loaded Server 2019 Datacenter.  I have it on the network and fully patched.  I joined it to the domain.  I went to Server Manager -> Add Roles and Features -> and selected Active Directory Domain Services and clicked next.  The Roles and Feature installer added DNS and proceeded to install everything and rebooted.  After reboot, Server Manager said I need to Promote to a Domain Controller so I clicked the button and went through the steps and entered a DSRM password.  Server rebooted when everything was complete.  

When I go to the virtual machine console, I cannot log into the server.  It says "Incorrect password".  I know the password is correct because I can log onto other servers using the same credentials.  If I try to use any domain account, I get the same message.  If I try to use RDP to log in, I get the same message.  I can connect to the server using Server Manager or Powershell and manage it that way so I know authentication is working.  I have built two different servers and had the same issue both times.  Using Server Manager I removed the Active Directory Domain Services role and after the server rebooted, I was able to log in again.  I added the role again and had the same result.  

I am at a loss on this.  Searching the Internet hasn't produced any useful answers.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-06*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-04*

Already did that... several times.  Does the same thing every time.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-04*

After reboot, Server Manager said I need to Promote to a Domain Controller so I clicked the button and went through the steps and entered a DSRM password    

This sounds problematic, if it were me I'd clean install it, patch fully and try it again. Perform the cleanup here if necessary before stand up the new oe again.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-03*

Yes, server records are showing up correctly in DNS.  Repadmin /replsummary is OK.  No errors  

I created a temp admin account with a simple password and entered it.  I clicked the "eye" button to view the password and it is correct.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2021-08-03*

Hi  

When you promote are your DNS record set correctly into the server ? and from another DC can you run repadmin /replsummary to make sure the replication is ok ?  

I would add, can you check to make sure the keyboard layout is ok for the "new account", or check to see the password after you typed it ?  I ask as for the domain profile I know if your domain admin password contain special entry, an error in the keyboard layout can hurt your login.   

Thanks  

Philippe
