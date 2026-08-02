---
title: "Exchange Hybrid Wizard - what will happen if certificate has not all names in it ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/123440/exchange-hybrid-wizard-what-will-happen-if-certifi
question_id: 123440
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Hybrid Wizard - what will happen if certificate has not all names in it ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/123440/exchange-hybrid-wizard-what-will-happen-if-certifi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear community.  

We will configure Exchange Hybrid Wizard in the next days with the option "centralized mail flow"  

We have here about 10 accepted domains in our Exchange Server.  

I am not sure if we need to buy an new certificate so i would like to try the existing certificate.   

What can go wrong if there is a SAN Name missing in our existing certifcate ?  

Can i just buy a new certificate and install that on our exchange in the following days or will this lead to an mail flow interruption as long as the Hybrid Wizard is not successfully completed ?  

Thank you for your feedback!

## Answer (community) — community member

*upvotes: 1 · updated: 2020-10-12*

Just to put it all together, i need the following data in my certificate:  

Primary shared SMTP domain for ONE accepted domain: domainA.com  

Autodiscover for ALL Primary SMTP Domains: autodiscover.domainA.com autodiscover.domainB.com, ....C, ......D, ....E  

Transport: edge.domainA.com > hostname.domainA.com   

Can you please clarify this "You wouldnt need to add any new domain to the cert for SMTP mail flow in hybrid."  

Does this mean: When i successfully complete the Hybrid Wizard and after that i need to add a new domain, then i do not have to change my certificate ?  

Thank you again for your excellent help Andy.  

I wish such knowledge would be easier to find but there are so many things to consider. You start with one website, 30 minutes later you habe 15 pages open in the browser. The pages from microsoft are not hard to read, the problem is always.....does the described scenario match with my situation ? and will these changes interfere with something else in my domain.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-13*

Hi @IT Guy   ， do suggestions above help? You could accept the helpful reply above as answer.

In addition, you could also refer to below links to get more information related to your question:

Using the Autodiscover Domain feature to enable multiple SMTP domains in your hybrid configuration

and Exchange Queue & A: Handling hybrid environments

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in [our documentation][3] to enable e-mail notifications if you want to receive the related email notification for this thread.  

 

[3]: https://learn.microsoft.com/en-us/previous-versions/technet-magazine/dn249970(v=msdn.10)?redirectedfrom=MSDN

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-12*

Hello Andy  

Thank you for your feedback. Can you please help me with these questions, that would be awesome and help me a lot!  

Lets say i have 5 domains. DomainA, DomainB, C, D, E.   

Do i need these three entries.....like domainA.com, autodiscover.domainA.com and edge.domanA.com for all of the 5 domains?  

(for every domain i have users who have one of these five domains as the SMTP entry in their mailbox settings, this means that this is their primary SMTP address, so i need that specific domain also as an "Primary shared SMTP domain" name in the certficate, right ?  

What will happen when my boss says: "we bought DomainX.com, please add it to the accepted mail domains", will i need to get a new certificate again or is there an other way than buying a new certificate ? Would be great when i could manage these certificate name stuff maybe on the dns or somewhere else.  

Can you explain me what could be my Edge Transport Server ? I am 99.9% sure this is our exchange himself but i need to write that down with screenshots for a written document.  

Where can i find that information ? When i enter "Get-TransportServer" in the Exchange Management Shell" the output is the Exchange hostname. Thats it ?  

thank you very very much for your help !

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-12*

Which SAN name is missing? One of the accepted domains that is set as primary SMTP address for some users or some other name?    

For mail flow, it wont matter as long as the connector is configured using any existing subject name.    

https://learn.microsoft.com/en-us/exchange/certificate-requirements
