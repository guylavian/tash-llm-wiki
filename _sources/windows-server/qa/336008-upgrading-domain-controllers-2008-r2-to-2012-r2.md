---
title: "Upgrading Domain Controllers 2008 R2 to 2012 R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/336008/upgrading-domain-controllers-2008-r2-to-2012-r2
question_id: 336008
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
---
# Upgrading Domain Controllers 2008 R2 to 2012 R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/336008/upgrading-domain-controllers-2008-r2-to-2012-r2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We appear to have 2 domain controllers in our enclave system, both running Windows 2008 R2/64-bit.  They need to be upgraded or replaced by newer 2012 R2 versions of the same.  Of course I realize that in-place upgrades of them are strongly discouraged, but an apparent caveat to the replacement is that the newer DC's have to retain the same server names and IP addresses (I've been told there are 'things' in the enclave that point to the DC's strictly by IP or something, and thus any changes on the name/IP for them would cause those applications to break).  They are also functioning as primary/secondary DNS servers.  

Based on the whole 'they need to have the same machine info' angle, I was leaning towards attempting an in-place upgrade of both DC's maybe over a weekend where user impact would be minimal.  However I think in a perfect world it would be really nice to spin up two 'new' machine, get them all patched, etc., and then cut over to them.  I just have no idea how I would accomplish this while still maintaining the same machine names and IP's.... is that even possible?  

My apologies in advance for my lack of knowledge, I have never set up or administered a Windows DC (well, not in over a decade anyway) so I'm sure there's a ton of stuff I'm not even considering.  

I did quickly run a "dcdiag /a" on the current Master DC and it seemed to pass all tests with the exception of "test SystemLog".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-07-09*

Here's where I am in case anyone is following or cares; I ended up creating a new Windows Server 2016 VM to take over for one of the existing 2008 servers (the VM).  I installed the same Roles I see the original has, AD DS, DHCP, and DNS.  I promoted it to a DC.  I copied over the DHCP information (although I still need to 'complete DHCP configuration' apparently).  On the 2016 server, I run "dcdiag /test:replications" and everything looks good/passes tests.  Basically, at this point, I now have the 2 2008 servers running in conjunction with this 2016 server.  Once I complete the DHCP configuration and check to see if we have any scripts or tasks specifically pointing to the old 2008 server, I will demote the old 2008 server and remove him from the domain.  

One point of concern I have is that checking through Event Viewer on the new 2016 DC, I see multiple/regular "Warning" messages with EventID 16969 stating that "x remote calls to the SAM database have been denied in the past 900 seconds throttling window".  As well, I'm seeing "Error" messages (EventID 26) indicating that some user account does not have a suitable key for generating a Kerberos ticket.  I see similar errors on the older DC servers so I'm not super worried about them, but we are seeing some odd behavior where sometimes users are unable to launch a particular application in our enclave and having them log out/log back in often resolves the issue.  I'm thinking something isn't quite right with user credentials/authentication being passed correctly depending on which DC is getting their login request, but that's just a guess.  

Is there any 'good' way to track the warning messages regarding the SAM database remote calls being denied to a particular user or application?  I'm doing start to poke around a bit on the interwebs but I haven't found anything yet.  I do notice the frequency of the message and # of 'remote calls' goes way up during what I consider peak hours for our user base being online and trying to do work.  

Cheers!
