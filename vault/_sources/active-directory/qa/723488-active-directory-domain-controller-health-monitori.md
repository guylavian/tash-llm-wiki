---
title: "Active Directory / Domain Controller / Health monitoring tools"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/723488/active-directory-domain-controller-health-monitori
question_id: 723488
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory / Domain Controller / Health monitoring tools

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/723488/active-directory-domain-controller-health-monitori (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Looking for opinions/advice on what tools other companies use to monitor their Active Directory health in regards to the infrastructure of AD, not the administration of it?  What I mean by that, for example, is a tool that'll provide details on the health of replication, site status, group policy state, dns, etc.  Many tools I'm finding track the details of user or group management, but I'm looking more for the health of our domain.    

We used to use Solar Winds, but due to the not so distant past issue they had with their exposed vulnerability, the company made the decision to remove that from our environment.  I'm looking for a replacement.  We recently had, for example, an issue with one of our sysvols and a tool maybe would have caught that before we stumbled upon it.  

I know we can use built - in tools (dcdiag, replmon, event monitoring, etc) but looking for a global tool we don't have to put some effort into automating.    

Thanks in advance for any advice / suggestions / opinions.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-02-06*

hello,    

in our side we used : SCOM and if you have a hybrid environment you can deploy Azure AD connect Health for AD and ADFS :    

https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-health-agent-install

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-25*

You can also try InfraSOS Active Directory Health Check Tool.  Perform over 150 checks against for AD for replication issues, AD configuration, DNS, GPOs, Permissions, DC Hardware, Security Assessments & more.. https://infrasos.com/active-directory-reporting/health-check-tool/

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-12*

You can also check SmartProfiler for Active Directory which ships with a DC Health Checker component - can be scheduled and notify you via email if any DC Health issues occur. Check out here: https://microsoft-assessment.com/

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-04*

Glad to hear, you're welcome. These are microsoft forums, so I'd suggest reaching out to the third-party vendors (or ask in their forums) about specifics on their tools.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-04*

dcdiag, repadmin are my goto tools. Another one is the replication status tool.   

https://www.microsoft.com/en-us/download/details.aspx?id=30005  

Other than that it sounds like you're looking for some third party tools then I'd check the vendor site for more info on them.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
