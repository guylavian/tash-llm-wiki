---
title: "Exchange 2016 and Mangement Tools connection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/339818/exchange-2016-and-mangement-tools-connection
question_id: 339818
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 and Mangement Tools connection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/339818/exchange-2016-and-mangement-tools-connection (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can someone help me better understand how the PowerShell component of the Exchange Management Tools install connects to Exchange server 2016 please?  I've deployed Exchange into a dedicated network where clients can only connect over port TCP:443.  All other inbound traffic is blocked from clients.  This seems to be fine for Outlook connectivity, but the Exchange PowerShell component fails to connect with the error:  

Connecting to remote server hostname.domain.local failed with the following error message :  WinRM cannot complete the operation.  

I went as far as collecting a packet capture during the launch of the default Exchange Management Shell icon and all I saw was TCP:80 connection attempts from the client to the server.  I went and tried to configure the PowerShell virtual directory to use an "https://" based URL which matches the installed certificate, but the default Exchange Management Shell install still attempts to connect to the internal FQDN of the server using port 80.  What am I missing?  

I'm not interested in allowing inbound PowerShell management over the public internet, this is only for internal connections from workstations that will be used by admins for Exchange management tasks.  

Regards,  

Adam Tyler

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-03-31*

So, for Powershell, dont mess with those URLs    

If you are using a load balancer, you could use 443 and switch to basic auth on the PS dirs.    

What you would do is enable Basic Auth on the PS virtual dirs.    

then you would use remote PS and connect to the load balanced namespace over 443    

Example: ( No need to specify the version)    

https://techcommunity.microsoft.com/t5/exchange-team-blog/remote-powershell-proxying-behavior-in-exchange-2013-cu12-and/ba-p/604504    

Alternatively, you could do the same with kerberos and allow port 80:    

https://learn.microsoft.com/en-us/exchange/architecture/client-access/kerberos-auth-for-load-balanced-client-access?view=exchserver-2019    

BTW, if you wanted to really lock things down, spin up some jump boxes and allow port 80 only from those servers and that way admins run remote powershell from there only

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-01*

Hi Team, 

 

I allow port 80 to the server so that PS can work. But security team concern in why we are not using default port 

By default PowerShell will use the following ports for communication (They are the same ports as WinRM)

 

TCP/5985 = HTTP

 

TCP/5986 = HTTPS

 

Please guide on this

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-02*

@Andy David - MVP   Thanks again.  I've reverted the PowerShell virtual directory back to its default setting in my lab and opened port 80 inbound to the Exchange server.  Now the default install of Exchange tools on admin workstations seems to work.    

You made an interesting comment about a load balancer and leveraging the remote PowerShell virtual directory mechanism of Exchange.  Doesn't really apply to us since we just have the one Exchange server, but I'm curious.  The running recommendation is for all Exchange servers in the organization use the same internal/external service URL that matches the cert, then have that URL point to the load balancer.  At least for services like the Outlook Web App, ECP, OAB, EWS, MAPI, ActiveSync, and Autodiscover.  It's interesting that most of these services appear to just proxy from one Exchange server to another auto-magically if the mailbox of the querying user happens to be found elsewhere.    

PowerShell on the other hand is a bit different I notice.  Using the default install of Exchange tools and launching the Exchange Management Shell while port 80 was blocked to our new Exchange server caused the shell to timeout.  Once timed out on the shells first Exchange server choice, it tried to connect to an alternate Exchange server.  I guess for most tasks, it doesn't really matter where you are running the cmdlets.  You can craft the cmdlet to execute for mailboxes wherever they happen to reside.  Or make changes to other Exchange servers using cmdlets executed..  I don't really see the point of using a load balancer with PowerShell connections to Exchange at all.  Maybe I am missing something?    

Regards,    

Adam Tyler
