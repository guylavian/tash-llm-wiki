---
title: "Remove a custom domain from Exchange hybrid and Tenant"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/401479/remove-a-custom-domain-from-exchange-hybrid-and-te
question_id: 401479
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Remove a custom domain from Exchange hybrid and Tenant

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/401479/remove-a-custom-domain-from-exchange-hybrid-and-te (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I have been asked to remove a custom domain from our Exchange Hybrid and O365 tenant.  

The reason for this is that we have sold the company and they have set up their own O365 tenant and want to retain use of the domain name for their tenant.  

The MX record for the custom domain is pointing to our On-prem Exchange server still, so that may make things easier for the mail flow.  

I need to to be able to send/ receive using the custom domain using our on prem Exchange servers for a short while until the sold company can get the MX records/SPF records changed etc. We have forwarding in place to temporarily forward emails onto their new email addresses.   

I have moved all of the objects which utilise the custom domain to a non-synched OU in AD so that O365 does not see the domain as "in use", so I theory I should be able to use the M365 Admin portal > Settings > Domains > Remove Domain  

I will also need to re-run the Exchange Hybrid Configuration Wizard and deselect the custom domain.  

My question is, do I have all of the steps to accomplish what I need to do listed above, and which order do I do them in?  

If I remove the custom domain from the hybrid and tenant, will the on premise Exchange servers still process emails for that domain if the MX record is pointing to the on prem Exchange servers?

## Answers

_No answers on this thread._
