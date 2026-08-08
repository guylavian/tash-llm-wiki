---
title: "OWA URL and Domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/251750/owa-url-and-domain
question_id: 251750
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# OWA URL and Domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/251750/owa-url-and-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently setup an E1 Exchange plan and wanted to try and create a DNS cname to forward from my own domain to the hosted exchange. The forward should remain transparent so as to always show my domain name and never microsoft domain since these emails and users are expecting that all the communication between our users is strictly internal and not on public microsoft websites or domains.  

At least that's the goal. But first things first, the OWA url. I tried the good old domainname.onmicrosoft.com/owa but that doesn't work anymore?? Why?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-02*

So based on that description, the "new" version of exchange is the current subscription code based version making the new version of exchange the same product as E1 and if it's 2019 isn't making users and administrators login to outlook.com for management and administration, it will be once the next in-place upgrade is applied. Does that sound about right?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-02*

More on the next version:  

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-news-and-announcements-microsoft-ignite-2020-edition/ba-p/1662224  

The next version of Exchange Server will support in-place upgrades from Exchange Server 2019 for a period of approximately two years following release. This feature will allow the admin to easily upgrade existing servers running Exchange Server 2019 to the subscription-based codebase without needing to add servers or move mailboxes.  

The next version of Exchange Server will continue to support side by side deployment and migration from earlier versions of Exchange as has been the case over the last few releases but we have increased the number of versions it can be installed alongside. Customers with Exchange Server 2013, 2016 or 2019 can install the next version of Exchange Server into their existing Exchange Organization.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-01*

Blockquote

About the logon URL, you can add your company branding to the Sign In page, then you will could use "https://outlook.com/yourdomain.com"; to access the custom logon page.

Above information could help you customize your Office 365.

Blockquote

This is what I call a "consolation prize". I am looking into my options now but it's because abundantly clear that microsoft has no regard for it's clients boundaries and has no intention of even providing methods of white labeling. Furthermore, it appears that putting everyone on the same authentication page is showing it's faults in implementation since as of this morning ALL of Microsoft 365 is having issues.

Blockquote

Personally, Exchange online have many difference with Exchange on-premises, it’s not an Exchange on-premise which managed by Microsoft cloud, it is a standalone version of Exchange. You don’t need to make too many changes to your Exchange online.

Blockquote

This wasn't the case just a couple years ago. BPOS and Hosted Exchange such as E1 were and had been seperate products but it appears that Microsoft is getting even greedyer and is pulling everything and everyone into "Microsoft 365" like a black hole. Furthermore, i in fact had begun looking into having my own exchange server and since the current version of exchange is last years 2019, I went in search for Exchange 2021 and it appears that Microsoft is doing away with Exchange mostly with the exception of only Enterprise class corporations. There is no beta nor does it look like there will be a trial version available for anyone. I think if i recall it requires installing a whole VM lab to get a trial going. I don't remember but i didn't dig much since it appears that Microsoft has also done away with the open licensing portal where I used to be able to be able to download upcoming versions of software thanks to software assurance and that was the final straw, I'm looking at alternative and same goes for all my clients. Microsoft has no business sticking it's name out past it's customers.

Me personally, i wouldn't even want to show that Microsoft was hosting my email at all! Microsoft has been hacked beyond belief at levels that may very well have compromised every computer running a Microsoft application it. So it's kind of even embarrassing to show I'm hosted and not at the very least running my own private exchange servers.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-01*

@Network.Domains      

You can verify your own domain name in Office 365 admin center, then you will could change email address from "user@keyman  .onmicrosoft.com" to "******@yourdomain.com". For more detail information, you can have a look about this article: Add a domain to Microsoft 365    

About the logon URL, you can add your company branding to the Sign In page, then you will could use "https://outlook.com/yourdomain.com" to access the custom logon page.    

Above information could help you customize your Office 365.     

Personally, Exchange online have many difference with Exchange on-premises, it’s not an Exchange on-premise which managed by Microsoft cloud, it is a standalone version of Exchange. You don’t need to make too many changes to your Exchange online.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-30*

"They arent using "public" domains however, so I am not sure what the concern is." . That's a strange view after you just said that users have to go to:  

https://outlook.office.com/mail/inbox  

or //outlook.com/owa/contoso.com  

Where exactly do you think people who have a free and public email address go to to login to their outlook.com email address? That is a public and free internet email address provided by microsoft and is really under Microsoft's domain. As in they in control of the information with it. Having company email under some other domain means that it is no long within exclusive privacy and control of the company. While I understand that it's not that simple, at the very minimum some impression that the company is in control of the email is mandatory. The way you're describing it now, might as well just have all the employees sign up for free microsoft accounts cuz it's all the same.   

What I'm asking for isn't hard to understand, in fact it wasn't hard to implement. Access to the OWA url was possible via the "domainname.onmicrosoft.com" domain before via the typical Ms Exchange URLs for OWA,ECP, etc... The E1 that i signed up for is Microsoft Exchange is it not?   

Just because microsoft is hosting it doesn't mean it has to get all pulled together into Microsoft's domain without any means of distinction from a personal or business or worse yet who's business domain people are logging into. By forcing people to login to go to and login to microsoft.com, outlook.com or office.com then where exactly does it tell them they are logging into MY companies PRIVATE email system?
