---
title: "Configure Outlook 365 App with 2010 Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/275154/configure-outlook-365-app-with-2010-exchange-serve
question_id: 275154
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Configure Outlook 365 App with 2010 Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/275154/configure-outlook-365-app-with-2010-exchange-serve (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am currently testing Office 365 business and want to use the Outlook application on my laptop to access our company exchange server which is 2010 and externally hosted.   

I am using onmicrosoft.com as my domain at the moment.  

Can someone help as to how I would configure either Exchange/Outlook 365 to work with Exchange Server 2010  

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-18*

You could at the following lines to C:\Windows\System32\drivers\etc\hosts  

10.0.0.65 mail.yourdomain.tld  

10.0.0.65 autodiscover.yourdomain.tld  

change 10.0.0.65 with the IP of your Exchange server.  

change yourdomain.tld with your domain.  

Consider this as a quick-fix, upgrade ASAP to a supported Exchange version.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-17*

Hi @James B      

Yes, like Andy said above, Microsoft 365 Apps is not supported for Exchange 2010 server.    

    

In addition, Exchange 2010 has reached its end of support, I would suggest you migrate to O365 or Exchange 2016. And the Exchange Deployment Assistant will be helpful to perform the migration.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-16*

Hi, thats not actually supported:    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019#clients    

You wouldnt use onmicrosoft.com however to connect to an Exchange 2010 server, thats used for Microsoft 365 domains. You would use your "real"  domain, not the onmicrosoft.com one.    

You should probably contact the admin for your company, but generally you enter your primary EMAIL address and Outlook automatically configures it.
