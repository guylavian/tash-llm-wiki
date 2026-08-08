---
title: "exchange csr - hybrid agent"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/397945/exchange-csr-hybrid-agent
question_id: 397945
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# exchange csr - hybrid agent

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/397945/exchange-csr-hybrid-agent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello our exchange 2010 server was never setup with externally facing website (OWA) and thus we never had any 3rd party certificate installed for the exchange server.  However we are now trying to install the hybrid agent in order to move all the mail to o365 .   

i believe we need to have a 3rd party ssl certificate based on my findings and the MS documentation.   

I just want to confirm what name i should have on the certifcate and should it be a SAN cert or single name?  

Mail.domain.ca  

autodiscover.domain.ca  

is anything else required in order for the hybrid agent to work properly?  

How do i generate the CSR is there any steps listed for this ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-18*

Certificate ahs been installed on the exchange server, and assigned the required services.     

I'm still getting this error when trying to deploy the hybrid agent - Any Ideas?    

I checked the Win RM service and it's running

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-18*

Hi @dirkdigs   ,  

1.The following table outlines the minimum suggested FQDNs that should be included on certificates configured for use in a hybrid deployment.  

Please refer to: Certificate requirements for hybrid deployments  

2.As Andy said, please make sure to set up the correct DNS record.

3.You could following the steps in the Microsoft's official article to create the CSR.  

Please refer to: Generate Request for Third-Party Certificate Services

4.At least assign IIS and SMTP services for new third-party certificates.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-17*

which service do need to assign the new certificate ?    

The current certificate ((self-signed) has IMAP POP and SMTP services checked off .
