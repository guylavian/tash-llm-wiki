---
title: "Windows server 2012 R2 Active Directory running ahead of time."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/649266/windows-server-2012-r2-active-directory-running-ah
question_id: 649266
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Windows server 2012 R2 Active Directory running ahead of time.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/649266/windows-server-2012-r2-active-directory-running-ah (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are having some weird issue going on out AD server is gradually running ahead of time currently it's 2 mins ahead. It is gradually getting increased last time we did few things which i can't remember that bring back to sync but we forgot what we did. It seems to be like every 2 month AD starts to runs forward. So far we tried resync manually set ntp settings through w32 command on cmd but nothing worked. We also tried manually setting time by going under Data and time settings but magically after setting time if we hit ok it somehow automatically get back to previous result which is 2 min ahead.  

P.S: Right now it's 2 min but we are guessing after 15 days it's gonna be 3 min ahead.  

Any suggestion or resolutions ? We are using physical server not under VMs.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-02*

Ok, you can try setting a new time source or also reset the time service.  

w32tm /unregister  

net stop w32time  

w32tm /register  

net start w32time  

w32tm /config /manualpeerlist:<ntp ip address> /syncfromflags:manual /reliable:yes /update  

net stop w32time  

net start w32time  

then check  

w32tm /query /source  

w32tm /query /configuration  

https://tf.nist.gov/tf-cgi/servers.cgi  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-02*

This is what i am referring to now i checked PDC emulator it is set to be as parent.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-02*

Are you asking about PDC emulator or something else?  

Some general info  

-  All domain members should use NT5DS domain time.   

-  Desktops and member servers sync with any domain controller.   

-  Domain controllers sync with PDC emulator (one per domain)   

-  PDC emulator in child domain can sync with any domain controller in parent domain.   

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.  

https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
