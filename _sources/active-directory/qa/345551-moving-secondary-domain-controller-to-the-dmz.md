---
title: "Moving secondary domain controller to the DMZ ."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/345551/moving-secondary-domain-controller-to-the-dmz
question_id: 345551
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Moving secondary domain controller to the DMZ .

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/345551/moving-secondary-domain-controller-to-the-dmz (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Team,  

I have one primary domain controller and one secondary domain controller. My manager wants my secondary domain controller to place in DMZ . What will be the difficulties i will face when i move the secondary domain controller to the dmz. Because we want our VPN Users to communicate that secondary domain controller only.  

Thank you  

Best Regards  

Shihas Shamsudheen

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-12*

Any progress or updates?  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-07*

Hi,    

Welcome to share here!    

If you want to Extended corporate forest into the perimeter network,  it is suggested to put the RODC in the DMZ because of the security and manageability benefits .    

However, if your current integrated application writes information to the directory, you might be blocked from using the new RODC role in the perimeter network. RODCs might also have application compatibility issues that require more planning and changes to your perimeter.    

Planning Deployment of AD DS in the Perimeter Network    

More details about  Deploying RODCs in the Perimeter Network    

If you decide to use a RODC in the DMZ, a new server is needed. (Or demote the second one and promote it to a RODC in DMZ)    

Hope the information will be helpful.    

Welcome to share here if you have any updates.    

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-06*

Just check that the ports between networks are flowing.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc758579(v=ws.10)?redirectedfrom=MSDN    

--please don't forget to Accept as answer if the reply is helpful--
