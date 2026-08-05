---
title: "Member server for Hyper-V Server, Exchange Server, VPN, NAT, NPS and RADIUS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/240279/member-server-for-hyper-v-server-exchange-server-v
question_id: 240279
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Member server for Hyper-V Server, Exchange Server, VPN, NAT, NPS and RADIUS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/240279/member-server-for-hyper-v-server-exchange-server-v (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have gone through some articles and videos.  

Some of articles and videos used member server for configuring Hyper-V Server, Exchange Server, VPN, NAT, NPS and RADIUS. Moreover, I read, troubleshooting becomes easier when we user member server. All roles are not recommended to add at AD-DC machine.  

Is member server recommended for all these configurations?  

Moreover, if we configure all roles in AD-DC machine, can we expect any issue in one role because of others?  

Please elaborate. I’ll be thankful for giving your time.  

With Regards  

NndnG

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-22*

Hi ，    

For the role of Hyper-V, AD, RASS/VPN and Radius, they are always installed separately.    

For the role of Exchange, as  Dave said, you have it asked in exchange forum for better answers.    

Best Regards,    

Candy    

--------------------------------------------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-21*

From a purely windows perspective install active directory domain series on it's own instance. RASS / VPN should also have its own instance due to the nature of multi-homing. For recommendations about NPS / Radius I'd reach out to subject matter experts in dedicated forums here.    

https://learn.microsoft.com/en-us/answers/topics/windows-network-access-protection.html    

and exchange server experts here.    

https://learn.microsoft.com/en-us/answers/topics/office-exchange-server-deployment.html    

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-01-21*

Mixing roles can cause conflicts plus it adds greatly to the complexity of configuration and for troubleshooting when problems arise. Better option is to install hyper-v as only role on host and stand up virtual machine guest for the various roles and or applications.  

--please don't forget to Accept as answer if the reply is helpful--
