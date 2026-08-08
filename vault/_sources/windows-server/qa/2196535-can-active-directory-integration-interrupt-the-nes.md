---
title: "Can Active Directory integration interrupt the nested Vm feature?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196535/can-active-directory-integration-interrupt-the-nes
question_id: 2196535
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Can Active Directory integration interrupt the nested Vm feature?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196535/can-active-directory-integration-interrupt-the-nes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have domain joined endpoints in which the users are not able to use the nested VM feature.  

Is it because of Active directory or due to some group policies applied from the DC?

## Answer (community) — community member

*upvotes: 0 · updated: 2025-02-26*

Hello  

Thank you for your reply.  

Please try to check on one endpoint system.

Please check if the endpoint system (when it is in domain) can use the nested VM feature using local account signed in.

Please check if the endpoint system (when it is in domain) can use the nested VM feature using domain account signed in.

Please check if the endpoint system (when it is not in domain) can use the nested VM feature using local account signed in.

Please note:

Windows Client for IT Pros and Windows Server forums are moving to Microsoft Q&A

We’re transitioning to Microsoft Q&A for a more streamlined experience. Starting February 26th*, new questions can only be posted on* Microsoft Q&A. Existing discussions will remain accessible here.

Beginning March 3rdcustomers looking for support on Answers will be automatically redirected to Microsoft Q&A.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2025-02-13*

Sorry for not being clear.  

"Domain joined endpoint" means endpoint systems connected to Active directory  and "nested VM" means virtual machine inside a virtual machine.  

We are using Oracle Virtualbox for VM.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-02-13*

Hello Monika Bisht1,  

Thank you for posting in Microsoft Community forum.

1.What do you mean "domain joined endpoints"?  

2.What is the "nested VM feature"? Would you please describe it in detail? 

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
