---
title: "Taking domain controller & workstations to new physical location"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/807494/taking-domain-controller-workstations-to-new-physi
question_id: 807494
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Taking domain controller & workstations to new physical location

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/807494/taking-domain-controller-workstations-to-new-physi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a client running Server 2012 R2 as the sole DC (yes, I know...Russian roulette) with 15 employees.  Five of the employees will be leaving the company in a few months and starting a new company, but they will be allowed to keep their workstations.  The new company will need a server (they want on-premise vs. cloud), but they will never go beyond 10-15 employees.  I will be procuring a Dell server for their needs, and the plan is to install Server 2019 Essentials.  They want the server at the current location so they can begin migrating their data to it.  I have several questions, since I've not done this before.  My thinking is that when the time comes to move to the new location, preserving their domain logins will help minimize having to join all workstations to a new domain & migrating their data/settings to the new profiles.  So with that being said,  

-  Can a secondary DC just simply move locations & still function without "seeing" the main DC ever again?  

-  If not, then the best solution would be to just backup data/settings and join the workstations to a new domain that's created at the new company's physical location?  

Any other advice that you can think of that I should know about would be greatly appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-04-13*

The DC that is currently running, what version of Windows is that running? "server 2012 standard or essentials?"  

If the server is running essentials, then you will not be allowed/able to add another Domain controller to the environment, just as the Server 2019 essentials will not be allowed to exist in a existing domain with more than one DC. (or well, it will, but if i recall correctly, there is a fairly strict time limit as to when it will break)  

Can a secondary DC just simply move locations & still function without "seeing" the main DC ever again?  

 DSPatrick already answered this one, it's not really an issue but requires some cleaning up afterwards  

If not, then the best solution would be to just backup data/settings and join the workstations to a new domain that's created at the new company's physical location?  

That would be my solution to it. I understand why you gain som advantages by being able to "save" the users the trouble of changing the domain, but it would be the best choice in my opinion for multiple reasons - the primary reason being that  we are talking a limited amount of users, so the time you are saving by not having to create the users from scratch will be spend on cleaning up after the now dead DC. And you will under all cirkomstances have to move the files etc.  

You are allowed to have multiple essentials on the same network, just not in the same domain, so i would configure the new 2019 as a "fresh" domain. Then connect to the old fileshare using SMB, and copy the files that they need.  Then create the users that should be in the new domain.  

Then for the client i would take a backup of the user configuration on the clients, change the DNS of this client to point to the new domain, and join the new domain, and restore the profile on the new user. If they have e-mail attached, and this e-mail is in O365, i would migrate this data afterwards, there are multiple ways to archieve this.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-12*

I haven't installed the new server yet.  Trying to get the plan together before I get started.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-04-11*

Can a secondary DC just simply move locations & still function without "seeing" the main DC ever again?    

Probably. After move you'll just need to seize role    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

then perform cleanup to remove the remnants of other one.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
