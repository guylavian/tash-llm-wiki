---
title: "Computer Policy GPO fails to apply"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5700344/computer-policy-gpo-fails-to-apply
question_id: 5700344
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
answer_author_roles: ["Independent Advisor"]
---
# Computer Policy GPO fails to apply

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5700344/computer-policy-gpo-fails-to-apply (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Domain Structure: two domains , domain A and domain B, both these domains have two way trust configured.  Endpoint : target machine is a W365 Machine, domain joined to domain B.             GPO Config : local admin gpo is configured for the target machine in domain B, global security group of domain A is updated in the configuration of gpo to be added to administrators group of Target machine in domain B. Validations : gp update/ force doesn't fail... Completes successfully.. but registry.pol file is not updating the time stamp,event logs shows no error, did reboots still no success, gp result showed error code referring to trust relationship failure.., but able search and set the same group in security permissions in that impacted machine but not resolving in gpupdate.. This policy works fine for a set of users and doesn't for another set of users...  please advise what need to be checked specifically between those two sets to identify the root cause of the issue and it's solution...

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-01-09*

Hello Praveen Kumar,

The fact that the GPO applies correctly for some users but fails for others, despite the two-way trust being configured, points to a trust resolution or SID translation issue between domain A and domain B. When you add a global security group from domain A into a GPO in domain B, the Group Policy engine on the client machine must be able to resolve the group’s SID across the trust. If gpresult is showing a trust relationship failure, it means the machine cannot resolve the SID of the domain A group at policy application time, even though you can manually add the group in local security settings. Manual addition works because the Security Accounts Manager (SAM) can resolve the group interactively, but the GPO engine relies on Kerberos trust validation and domain controller referrals.

The first thing to check is whether the affected users’ machines can query domain A’s domain controllers at the time of policy application. Run `nltest /dsgetdc:DomainA` from the impacted machine and confirm it can locate a domain controller in domain A. If this fails or points to an unreachable DC, the GPO will not be able to resolve the group SID. Also check DNS resolution: ensure that the DNS suffix search list includes both domains, or that conditional forwarders are correctly configured between domain A and domain B.

Next, compare the group membership and SID history between the set of users where the policy works and those where it fails. Use `whoami /groups` on both sets of machines to see if the domain A group SID is being resolved correctly. If the failing set shows unresolved SIDs (e.g., S-1-5-21-… without a friendly name), that confirms a trust resolution problem.

Another point to validate is whether the group from domain A is a Global group or a Universal group. Global groups from one domain cannot always be resolved across trusts for certain policy types, especially if the trust is external. Universal groups are recommended in multi-domain environments because their membership is replicated to the Global Catalog. If the working set of users are members of a Universal group and the failing set are in a Global group, that would explain the inconsistency.

Finally, check the event logs under Applications and Services Logs > Microsoft > Windows > GroupPolicy > Operational. Even if you don’t see errors in the System log, the Group Policy Operational log often shows detailed trust or SID translation failures.

I hope you've found something useful here. If it helps you get more insight into the issue, it's appreciated to accept the answer. Should you have more questions, feel free to leave a message. Have a nice day!

Domic Vo.
