---
title: "Windows 11 authentication with kerberos trust: date/time difference between client and server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1281030/windows-11-authentication-with-kerberos-trust-date
question_id: 1281030
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Windows 11 authentication with kerberos trust: date/time difference between client and server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1281030/windows-11-authentication-with-kerberos-trust-date (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We operate a kerberos trust between our domain controllers and a Linux-based kerberos KDC for user authentication; users in Active Directory have an altSecurityIdentity field set pointing to "Kerberos:<username>@<REALM>" to authenticate user <username> via the kerberos KDC. We have a significant Linux install base, and this allows us to keep all password authentication in one source.

Windows 11 clients, once joined to our domain, report "There is a time and/or date difference between the client and server." Windows 10 clients and Server 2016/2019/2022 systems authenticate as expected without the time/date error. All are configured to sync clocks from a local NTP server on-site. Time and date, as seen on the desktop or via the "date" and "time" commands. Windows 11 clients do correctly report if the kerberos password is typed incorrectly.

Any idea why Windows 11 is failing these kerberos authentications? It's as if Windows 11 isn't using the same base time when authenticating against our KDCs, perhaps not applying timezone information appropriately.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-07*

It turns out this was an issue with the age of the KDC we had in service. 

Our KDC was running MIT Kerberos 1.15.1 from the CentOS 7 Linux distribution. Turns out it is afflicted by the issue detailed in this post: https://github.com/heimdal/heimdal/issues/1011  (The linked git issue was against the Heimdal Kerberos distribution, not MIT Kerberos...both distributions had the problem.)

The TGS request would come through with "until time" listed greater than what our old KDC could deal with and proceeded to fail with a less-than-intuitive response. 

Spinning up a Ubuntu Linux 22.04 KDC using MIT Kerberos 1.19.2 authenticates as expected.

It was time to update the old KDCs anyway. We are able to get a replica server for Windows 11 hosts to authenticate against as a short-term fix until all KDCs are running more modern code.

Thank you, Dave Patrick, for your detailed information on sync'ing clocks. I wish our problem were as simple as sync'ing clocks...certainly less work than upgrading KDCs.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-09*

Glad to hear of progress. You may need to reach out to the kerberos-based security identity provider for assistance with that issue.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-09*

For all other members and domain controllers you could do  

```
w32tm /unregister
net stop w32time
w32tm /register
net start w32time
w32tm /config /syncfromflags:domhier /update
net stop w32time
net start w32time
```

then check

```
w32tm /query /source
w32tm /query /configuration
```

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-09*

For the PDC emulator you can do   

```
w32tm /unregister
net stop w32time
w32tm /register
net start w32time
w32tm /config /manualpeerlist: /syncfromflags:manual /reliable:yes /update
net stop w32time
net start w32time
```

 then check

```
w32tm /query /source
w32tm /query /configuration
```

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-09*

Time zones don't really have anything to do with it. The times are all compared via UTC times.     

All are configured to sync clocks from a local NTP server on-site    

A better method is to make use of the windows time service. You could sync the PDC emulator with your local NTP source then let NT5DS domain time take care of the reset.    

Some general info

-  All domain members should use NT5DS domain time. 

-  Desktops and member servers sync with any domain controller. 

-  Domain controllers sync with PDC emulator (one per domain) 

-  PDC emulator in child domain can sync with any domain controller in parent domain. 

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.
https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
