---
title: "Can we host 2 different domains on single exchange server environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/286887/can-we-host-2-different-domains-on-single-exchange
question_id: 286887
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Can we host 2 different domains on single exchange server environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/286887/can-we-host-2-different-domains-on-single-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, guys hope you are doing well,   

I need help in exchange Server   

We have a situation. we are using domain1.com in our local environment which is running on Hmail and users can only send and receive emails internally we do not have any external connection for domain1.com.  

We have another domain that is domain2.com which is hosted somewhere else. Domain2.com users can send and receive external emails.  

Now we want to take both these domains into a single environment like an Exchange Server. Right now our domain controller is on domain1.com and users can also sign in to their PCs from domain1.com.  

We want to replace Hmail and External hosted environments with a single exchange server environment. like domain1.com will still be able to send and receive emails internally and domain2.com will be able to send and receive emails externally.   

My question is "Can we add both domains in a single environment like can we add domain2.com in the same single foreset and then some of our emails will be on domain1.com and some will be domain2.com?"

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-25*

Hi,    

Was domain2 hosted by other mail server or something? Since users can send externally, it should has its own DNS, that's where you should add the records.    

And for your reference, you can use SRV records for multiple Autodiscover domains to save time/costs: Using SRV records for multiple Autodiscover domains    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-24*

Yes, you would use accepted domains and Email Address Policies to help manage that.     

As long as the MX record for both domains points to your Exch org and you have them set as accepted domains, it will work    

https://learn.microsoft.com/en-us/exchange/mail-flow/accepted-domains/accepted-domains?view=exchserver-2019    

https://learn.microsoft.com/en-us/exchange/email-addresses-and-address-books/email-address-policies/email-address-policies?view=exchserver-2019
