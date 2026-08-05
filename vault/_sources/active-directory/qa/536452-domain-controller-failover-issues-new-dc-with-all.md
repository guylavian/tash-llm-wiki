---
title: "Domain Controller Failover Issues:  New DC with all FSMO roles never authenticates alone"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/536452/domain-controller-failover-issues-new-dc-with-all
question_id: 536452
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller Failover Issues:  New DC with all FSMO roles never authenticates alone

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/536452/domain-controller-failover-issues-new-dc-with-all (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The problem I am having is that if I take one of my two writable domain controllers offline, nobody seems to "fail over" to using the other domain controller like they're supposed to - applications we run within our network that use AD for authentication just keep asking for a username and password and never actually authenticate you, and external users reliant on a read-only DC on another network segment can't authenticate to our remote access website either.  

I currently have three domain controllers in my Domain: DC1, DC2, and RO1. DC1 and RO1 is Server 2019, DC2 is Server 2012R2. Both of the writable DCs are AD-integrated DNS servers, with their network adapters configured to point at each other.  

DC1 and DC2 are on the same subnet. RO1 is a read only controller out in a different network segment in order to support a remote access solution managed by the organization above me (who manages the general network I connect to).  

In the past, if I were to take one or the other local DCs offline, local users would fail over to whichever was actually still running (as expected), as would remote users as the RODC fetches the active one to authenticate.  

The current DC1 is a relatively new addition, replacing one called DC. DC1 was brought online and joined with DC and DC2, and everything seemed fine. I transferred all the FSMO roles that DC had over to its replacement, DC1 - netdom query fsmo shows all roles as being on the new DC1. We demoted and took DC offline to retire it since it was a Server 2012 machine and we're migrating away from those. Cleaned up a few errant DNS records that claimed the old DC was still around, but other than that everything chugged along as it had. Last patch cycle though, we had DC2 offline while the DC1 and RO1 remained active, but discovered the authentication related issues above. External users could not authenticate in at all, and users who were already logged in found our AD-authenticating applications suddenly asking them to log in again (to no avail).  

Unfortunately I'm not sure why this is. DC1, the new controller, is definitely recognized by the Domain. Replication happens fine - Repadmin /showrepl is successful, and /replsum has no errors reported. All involved internal machines can resolve their host names and ping each other. If I ping the domain, I can get either writable DC, same as if I tracert to the domain. I can make edits on DC1 and see them on DC2, and vice versa (and changes like group policy made on DC1 specifically definitely exist out in the greater network). I can take the RODC and tell it to load records from DC1 and DC2 without issue.  

If I take DC2 offline, however, that's when things go sideways. Ping or Tracert to our domain fails, external users get denied access, and internal users see our AD-authenticated applications fail and constantly call for a username and password. The opposite does not happen, however - if I take the new DC1 offline, local users sometimes have a slight chugging delay as if their machine was trying to contact DC1 before failing over to DC2 and authenticating successfully, and external users come in just fine.  

Internal clients have been tested using the DC/DNS servers in question as the DNS server entries on their network adapters.  

There's nothing super obvious in the Event Logs, and everything I can think of appears correctly configured. I'm not sure where to progress from here - has anyone had similar symptoms that they've been able to correct?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-02*

Hello,  

Thank you for your question.  

I would like to suggest you to check below troubleshooting steps.  

-  Please check if there is any DNS forwarder is configured in DNS along with DNS replication related event logs.  

-  also can you give DNS ips of all your three DCs to the clients machines.  

-  Please check again AD replication is in healthy state you can run below Microsoft GUI tool check the AD Health.  

https://www.microsoft.com/en-in/download/details.aspx?id=30005  

-  If you take D2 offline then please check the Event logs on client machines related to authentications and tracer to your Domain name.  

-  Please also check time is in Sync between your DC and client computers.  

If the reply was helpful, please don’t forget to upvote or accept as answer.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-01*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

`ipconfig /all > C:\problemworkstation.txt`  

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-01*

if I take one of my two writable domain controllers offline, nobody seems to "fail over" to using the other domain controller like they're supposed to  

I'd check the problem members have the address of other healthy domain controllers listed for DNS  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
