---
title: "Mail URL change with Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/144029/mail-url-change-with-exchange-2016
question_id: 144029
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Mail URL change with Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/144029/mail-url-change-with-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We are planning to change the mail related URLs. As a test just we created an internal record mail.newdomain.com which points to the same IP as existing mail.currentdomain.com and it works internally through OWA. Now we will change only the internal URLs with Exchange for below folders  

OwaVirtualDirectory  

EcpVirtualDirectory  

OabVirtualDirectoryM  

MapiVirtualDirectory  

ActivesyncVirtualDirectory  

PowerShellVirtualDirectory  

WebservicesVirtualDirectory  

AutoDiscoverService  

Hope this won't affect existing internal users (outlook users) and any externally connecting users (both activesync, OWA & Outlook anywhere)  

Once we completed this activity then we will configure external URLs. Need your assistance

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-12*

I have one more Q here. Once we change internal autodiscover URL to new domain, which differs from AD domain, will the SCP works internally or it's a must that the autodiscover.newdomain.com CNAME record should be there with internal DNS?  

Also will the serviceBindingInformation updates automatically in AD once we update autodiscover internal URL?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-04*

Hi All  

We are changing the internal URLs by tomorrow evening. Will it affect internal users in any way? We are in the expectation that the changes won't require any downtime and doing after working hours

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-03*

Thank You All  

We decide to start by changing all internal URLs by this weekend, we believe this won't affect users in anyway, right?  

Once this works fine internally, then we will modify external URLs.   

What's your suggestion?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-30*

Hi @LMS      

We could refer to the link below to check if you have any point missed, the article gives an introduction to the configurations we need to change for all urls in detail.    

Exchange Autodiscover – A Guide to Making Exchange Work Properly     

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Also remember to update the certificate with all SAN you used in the urls included.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-29*

Additional to the urls mentioned, you must need to change -AutoDiscoverServiceInternalUri also using the cmdlet Set-ClientAccessServer
