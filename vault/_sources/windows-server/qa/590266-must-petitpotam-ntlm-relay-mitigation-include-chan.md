---
title: "Must PetitPotam NTLM relay mitigation include changing your CA server's CDP & AIA extensions?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/590266/must-petitpotam-ntlm-relay-mitigation-include-chan
question_id: 590266
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-development-iis"]
---
# Must PetitPotam NTLM relay mitigation include changing your CA server's CDP & AIA extensions?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/590266/must-petitpotam-ntlm-relay-mitigation-include-chan (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are looking to mitigate the PetitPotam vulnerability on our internal 2Tier active Directory CA hierarchy. There is a very clear MS document here...  

https://support.microsoft.com/en-gb/topic/kb5005413-mitigating-ntlm-relay-attacks-on-active-directory-certificate-services-ad-cs-3612b773-4043-4aa9-b23d-b87910cd3429  

The very first instruction says "We recommend enabling EPA and disabling HTTP on AD CS servers."   

However...there are no additional instructions on editing the CDP / AIA extensions in the subordinate CA server config.  

My question is - what happens to already issued certificates without HTTPS in their certificate configuration and surely we need to add HTTPS extensions to the Subordinate CA configuration?   

I'm worried that simply following this document will have a detrimental affect on my PKI infrastructure?  

Any advice, explanations would be most gratefully welcomed!  

Regards,  

durrie

## Answer (community) — community member

*upvotes: 1 · updated: 2021-10-14*

Hello @Heath Durrett       

Basically all your HTTP certificates would stop working as you enable EPA, require SSL and disable HTTP over ADCS. This is the "modern" safety rule for your environment, not only for PetitPotam, but for many other attacks. It's been many years that most issuing instances have moved to the SSL protocol and HTTPS, however is true that some signing is still done on HTTP mostly for backwards compatibility and historical purposes.     

Hope this helps with your query,    

------    

--If the reply is helpful, please Upvote and Accept as answer--
