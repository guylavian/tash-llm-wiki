---
title: "Active Directory Replication with Mesh Topology"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2263253/active-directory-replication-with-mesh-topology
question_id: 2263253
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory Replication with Mesh Topology

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2263253/active-directory-replication-with-mesh-topology (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have a total of three Active Directory Sites: NG1, NG2, and NG3. There is 1 domain controller placed in the NG1 site, 4 domain controllers placed in the NG2 site, and 4 domain controllers placed in the NG3 site. I have a total of 9 domain controllers. However, from a network security perspective, my network team suggested domain controller segregation. For example, NG1 can communicate with NG2, NG3 can also communicate with NG2, but there is no communication between NG3 and NG1. Even though NG2 and NG3 have a total of 8 domain controllers, from a network security perspective, each site contains 2 different network zones. For instance, NG1 is an Active Directory Site, but from a network perspective, it contains 2 different network zones called core and DMZ. The same applies to NG3. Therefore, the network team suggested that NG3 core domain controllers can contact only NG2 core domain controllers, and NG3 DMZ domain controllers can communicate or replicate only with NG2 DMZ. However, with this scenario, we sometimes face replication issues and cannot properly address which DC is affected.

We now want to rebuild our replication architecture with a mesh topology. What is Microsoft's best practice regarding this? Should we go with a mesh topology (where every domain controller can communicate with each other) or maintain this type of segregated replication topology? Please suggest a plan in summary. Please post the summary of the suggestion here and also provide a reference document where the mesh replication topology is mentioned.

Thanks in advance.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-05-04*

Active Directory automatically uses a spanning tree topology for inter-site replication. This is by design, not a configurable or optional setting. The Knowledge Consistency Checker (KCC) generates this topology to ensure efficient and loop-free replication between sites.
Reflect Real Network Segmentation in Site Design: If each AD site (e.g., NG1, NG3) contains multiple isolated network zones such as core and DMZ, those should be modeled as separate AD Sites. This ensures the replication topology aligns with actual network connectivity constraints.

Regarding your intent to allow communication between any pair of domain controllers, for inter-site repliation, that's accomplished by Site Link Bridging:

-  By default, site link bridging is enabled, allowing transitive replication paths through intermediate sites.

-  In a segmented network where certain paths (e.g., NG1 ↔ NG3) are blocked, you should disable site link bridging and manually create explicit site links to enforce only valid, routable replication paths.

To optimize your existing configuration, you might want to consider the following:

-  Redefine your AD Sites to match network segmentation:

-  NG1-Core, NG1-DMZ

-  NG2-Core, NG2-DMZ

-  NG3-Core, NG3-DMZ

-  Create site links only where communication is allowed:

-  NG1-Core ↔ NG2-Core

-  NG1-DMZ ↔ NG2-DMZ

-  NG3-Core ↔ NG2-Core

-  NG3-DMZ ↔ NG2-DMZ

-  Disable site link bridging, so replication follows only explicitly defined links.

-  Assign domain controllers appropriately and ensure bridgehead servers are chosen or managed to support proper replication.

This approach respects both Active Directory's design and your network security model, while eliminating replication ambiguity and improving manageability.

Otherwise, simply ensure that site link bridging is enabled. 

More at https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts and https://download.microsoft.com/download/5/2/f/52f23d76-7d56-44d6-ad25-a95bf0be5516/06_CHAPTER_3_Designing_the_Site_Topology.doc

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
