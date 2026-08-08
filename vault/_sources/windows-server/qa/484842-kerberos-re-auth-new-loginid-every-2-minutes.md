---
title: "Kerberos Re-Auth (new LoginID) Every 2 minutes?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/484842/kerberos-re-auth-new-loginid-every-2-minutes
question_id: 484842
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Kerberos Re-Auth (new LoginID) Every 2 minutes?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/484842/kerberos-re-auth-new-loginid-every-2-minutes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So I have a question that I cant seem to find the answer to anywhere and was looking for some guidance.  

So when I remote login to a server via RDP or connect to a SQL instance via SMSS, I am noticing that in the Security event log, every 2 minutes, there is a kerberos login for my user (I am actively logged in and have not logged out during that time) with the event ID 4624.  The only difference in the entries is the LoginID changes and everything else stays the same minus the timestamp of course.  

Does anyone know why this happens?  I would love for it alert the first time I login and not notify with a security event for each re-auth because this lab enviornment doesnt even use kerberos.  

Thanks in advance for anyone knows what I might be missing here.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-23*

Hi,  

It's strange as you said above.  

Since the port is different every time, the session is different every time. We may try to figure out the port on the server which the clients try to connect.  

Also, we may try to confirm if there are any time limitation for tcp\ip connection on the server.  

Best Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-22*

No; this happens for all users who access the machines.    

No, the user is just their user account    

Sure, I have attached photos of the events and you can see the only difference in the event is that it happens every 2 minutes with a different LoginID and of course the port is different with each one    

Network capture yielded the same results: every 2 minutes kerberos re-auth tickets when there is no Kerberos on the domain for this lab environment

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-22*

Yes this happens everytime.  

With our current NIST audit settings in place, we get roughly 4-8 logon messages in our SEM for everything from NTLMSSP, Kerberos, Windows:Network, SQL, etc.  

I was trying to figure out why the Kerberos one happens at logon and with one LoginID and then every 2 minutes it comes in again and the only difference is the LoginID even though I have not logged out of the system and it repeats until you logout of the system.  When I log off the system, i get the same number of messages for logoff as I do when I initially logon but I dont get repeating alerts every 2 minutes after I logout.  That only happens when I am logged into the system.  

Just not sure why Kerberos is showing an audit success every 2 minutes with different LoginIDs (My LoginGUID stays the same...but the LoginID changes).  The most I can think of is that one of the audit settings like Audit Kerberos Authentication Service might be causing an issue or if something else is going on.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-22*

Hi,    

The event happens regularly, right?    

Form my side, i will enable the audit policy for log off too.    

And check if the log off events will happen as the logon events.    

https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-logoff    

Best Regards,
