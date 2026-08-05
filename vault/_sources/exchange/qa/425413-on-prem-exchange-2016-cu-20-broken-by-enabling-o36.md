---
title: "On Prem Exchange 2016 CU 20 Broken By Enabling O365 Teams"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/425413/on-prem-exchange-2016-cu-20-broken-by-enabling-o36
question_id: 425413
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# On Prem Exchange 2016 CU 20 Broken By Enabling O365 Teams

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/425413/on-prem-exchange-2016-cu-20-broken-by-enabling-o36 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Per my new Director I setup MS Teams as a standalone thing in O365.  It is not in any way connected to our domain outcompany.com.  When I set everything up I verified our domain ourcompany.com and was able to set everything up and hand it over to our Director.   

About 90 minutes later our on prem Exchange started prompting for a o365 login.  This Exchange server runs ourcompany.com for us.  It is in no way connected to o365 and I can't seem to figure out why it's happening.  We have 13 users testing Teams.  We have not purchased anything related to a hosted Exchange solution, just the base package for teams.  I can't find any info online describing this issue.  Has anyone seen this and can you assist?    

Edit:   

I have verified that our setup users can email from the o365 portal.  This is very confusing since our SPF records should cause these messages to fail.  I verified the mail routed through o365 and not our on prem server.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-08*

I've verified my DNS was all correct.  That includes both split and my authoritative DNS service.  I see no records pointing to anything we didn't setup.   

The emailing from the o365 portal is an odd one.  My manager logged into his account on o365 and sent an email to his gmail account and it showed up as his company email address.   I checked both our spam service and our on prem service and I don't see the message anywhere.  I have custom SPF records setup for our SPAM service. My best guess is that MS did something on their end that got picked up in my include all domain records command on our spf record.  I can see no other way that would allow them to email as our domain when they are not in our SPF records.     

We deleted our domain off of the o365 portal. Now that it's gone the problem has gone away.  Here's my thought on what's occurring. I just need to verify it.  Outlook searches for a o365 domain when it loads to see if it's active.  If it is then it prompts for the login.  We could potentially fix it from the client side if we could get a working reg key fix.  The one I tried did not work.  The best way to fix it would be to correct it on the o365 side but I'm not sure how to do that.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-08*

@IT Support      

I think this issue may related the way that you verify your domain in Office 365. What DNS record that you used to verified your domain? I would suggest you check whether "Autodiscover.domain.com" and "mail.domain.com" still point to Exchange on-premises.    

I have verified that our setup users can email from the o365 portal.    

Could you provide more tailed information about this one?  Do you mean Office 365 admin could send email to your Exchange on-premises?    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-07*

We've tried the regedit for testing with no luck.  I've now disabled the features via powershell as well.  I'm still having the issue.   

I found in the approved domains section that it built out an authorative domain for our company.  I changed it to relay to try and correct the problem but it hasn't made a difference yet.  I can't delete Exchange for some reason.  I also can't just shut off Exchange.  Seeing as how I didn't buy it, and I don't want it, how do I shut it off?  If I purchase a service I expect to get what I paid for, not all this up selling garbage.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-06-07*

Sounds like:  

https://medium.com/jj365/outlook-issue-with-direct-connect-to-office365-352dd29de65  

See the fixes and test it out
