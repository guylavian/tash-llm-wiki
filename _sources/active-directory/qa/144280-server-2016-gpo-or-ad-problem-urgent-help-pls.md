---
title: "Server 2016 GPO or AD problem, urgent help pls"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/144280/server-2016-gpo-or-ad-problem-urgent-help-pls
question_id: 144280
fetched: 2026-07-25
answer_count: 12
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Server 2016 GPO or AD problem, urgent help pls

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/144280/server-2016-gpo-or-ad-problem-urgent-help-pls (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

I have a serious problem and so far no1 has a solution.  

Since a few weeks the server with 2016 standard does something weird.  

Since then when a user turns off the client and restarts windows goes back to original settings and all locally saves will be wiped...  

So today I installed ssd in a client and did a clean win10 pro install.  

Then connect to the domain and make a few security option on the client to block the use of control panel and usb ports.  

All is fine even I shut down and restart.  

But then I choose to login with another account which is registered in de AD. I get message windows is preparing....  

Then I switch back to the installed account on the laptop and got the same message " preparing windows " and all my settings are gone... even the test docfile on the desktop was wiped ...  

In the GPO there is nothing specific setup. Only users and computers...  

U must know that everything worked for at least 5 years since this server has been setup. Only since a few weeks this behavior shows up.  

Is there anywhere on this planet a human who can help me?  

Thx  

John

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-31*

If its only a single user the profile may be corrupt. If you logon with an account that has administrative rights, then after saving off docs, etc. from corrupt/abandoned profiles use Control Panel|Users and Passwords and delete the old profile stores. Then when you next logon a new profile is created from an image in \default user then you can copy your saved data back to new profile.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-31*

after several hours i see this when i log to user on to the domain    

    

i changed the profile to roaming but its till temporary profile...    

how can i change this ?    

thx

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-29*

As I said, hard to say. Yes malware on your network is possible. If you suspect policy, then you can unlink them for testing.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-29*

DSPatrick,  

u mean malware on the server ?  as i did clean install of win10 pro and the behavior is still there...  

thx

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-29*

Could be malware, hard to say. As to policy you could unlink them for testing.    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn581922(v=ws.11)?redirectedfrom=MSDN    

--please don't forget to Accept as answer if the reply is helpful--
