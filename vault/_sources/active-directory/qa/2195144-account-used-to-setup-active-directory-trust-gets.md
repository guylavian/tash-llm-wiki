---
title: "Account used to setup active directory trust gets disabled."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195144/account-used-to-setup-active-directory-trust-gets
question_id: 2195144
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Account used to setup active directory trust gets disabled.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195144/account-used-to-setup-active-directory-trust-gets (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I will like to know What happens when an account used to set up active directory trust with another domain gets disabled?

My understanding is for  most part the trust will function as its established based on cryptographic keys or shared secrets during the trust creation process, However if and when the need for validation ,it will fail for obvious reasons.

Will there be any impact as far as the authentication and authorization process ?

I could not find any specific document which can help clear this ? 

Inputs are appreciated !!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-14*

Hello himvy,  

Thank you for posting in Microsoft Community forum.  

For creating forest trust, you must be a member of the Domain Admins group (in the forest root domain) or the Enterprise Admins group in Active Directory, or you must have been delegated the appropriate authority.   

Why do you want to disable the AD account that set up active directory trust?  

Such specific questions can be difficult to find a suitable answer on the Internet, and I think you may need to test such questions based on your own AD environment and the scope of application of trust and type of trust, because the complexity of each AD environment and the type of trust and scope of application are different.  

For example:  

1.You can verify the trust to see if the AD trust can be verified successfully.  

2.Check if the user can logon to trusted domain or/and trusting domain.  

3.Check if the user can access the resource in trusted domain or/and trusting domain.  

4.Other functions in your domain.  

If the AD account that set up active directory trust cannot be disabled and you must disable it, I think you need to replace the AD account that set up active directory trust (I mean you may need to set up again using another AD account).  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
