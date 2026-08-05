---
title: "active directory check site topology not generating automatically"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1304187/active-directory-check-site-topology-not-generatin
question_id: 1304187
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# active directory check site topology not generating automatically

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1304187/active-directory-check-site-topology-not-generatin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i have multiple additional domain controller which replicate through sites link all work fine but active directory check site topology not auto generated .

even though all the network ports allowed.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-06-13*

Something here could help.  

https://theitbros.com/active-directory-sites-and-subnets/   

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-06-13*

The 5014 error may provide some clues.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-12*

If the Active Directory check site topology is not generating automatically despite having multiple additional domain controllers replicating through site links, here are some potential solutions:

1) Verify replication settings: Check the configurations of site links, replication schedules, and intervals to ensure they are set up correctly.

2) Check network connectivity: Ensure uninterrupted network connectivity between domain controllers by testing and resolving any network or firewall issues.

3) DNS configuration: Confirm that DNS settings on all domain controllers are accurate and functioning properly.

4) Force replication: Attempt to trigger the Active Directory check site topology by forcing replication between domain controllers using the command "repadmin /syncall /AdeP".

5) Monitor event logs: Check the event logs on domain controllers for relevant error messages or warnings related to replication or Active Directory.

6) Verify site topology settings: Double-check the accuracy of site topology settings in Active Directory Sites and Services, including sites, subnets, and site link configurations.

If the issue persists, consider seeking assistance from a system administrator or Active Directory specialist for further analysis and targeted troubleshooting.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-06-12*

You could check things out via PowerShell.  

https://techcommunity.microsoft.com/t5/itops-talk-blog/powershell-basics-how-to-check-active-directory-replication/ba-p/326364  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
