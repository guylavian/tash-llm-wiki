---
title: "Integrate ADFS ( WS 2019) with an external Identity Provider: check user authorizations / permissions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/118335/integrate-adfs-ws-2019-with-an-external-identity-p
question_id: 118335
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Integrate ADFS ( WS 2019) with an external Identity Provider: check user authorizations / permissions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/118335/integrate-adfs-ws-2019-with-an-external-identity-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

I have setup an enviroment with an ADFS ( WS 2019) and an external Identity Provider.  

My goal is that once a user has been authenticated by the external Identiy Provider that ADFS will query AD to get retrieve his / her permissions (i.e. based on AD Security membership or check if the user is disabled or if the user has been deleted).  

Is it supported such scenario ?  

Any helps about what I should do ?  

Thanks in advance  

Giovanni

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-07*

Hi @Pierre Audonnet - MSFT   ,    

Thanks for your help.    

With some luck, I have been able to resolve these issues.    

Regarding your question, I'm using the Identity Provider to introduce a passwordless authentication for AD DS users because passwordless authentication is not available in AD FS natively.     

Thanks,    

Giovanni

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-06*

Yes it is possible to do that as long as the external identity provider can provide a unique identifier to anchor the user to an object in AD DS. If you have a specific example (with the actual claim types and the logic for the mapping and the group lookup up) we can help you with the rules here.  

By the way, why use an external provider if at the end you are authenticating AD DS user? Why not using the Active Directory claim provider directly?
