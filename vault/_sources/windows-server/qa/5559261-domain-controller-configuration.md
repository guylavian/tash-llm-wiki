---
title: "Domain Controller Configuration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5559261/domain-controller-configuration
question_id: 5559261
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Domain Controller Configuration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5559261/domain-controller-configuration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,

We currently have 4 domain controllers, with 3 located in the Data Center (DC) and 1 in the Disaster Recovery (DR) site. At present, client computers are authenticating against all domain controllers randomly.

Our requirement is to ensure that authentication requests are handled only by the 3 DC-based domain controllers, while the DR domain controller should remain in place solely for replication purposes.

I am looking for a reliable solution that can forward authentication traffic exclusively to the DC domain controllers and not to the DR domain controller.

Best regards,

## Answer (community) — Independent Advisor

*upvotes: 1 · updated: 2025-09-18*

Hi Parsian,

To achieve this, I recommend adjusting the Active Directory site topology and subnet configurations. Ensure that your client machines are associated with a site that includes only the DC-based domain controllers. This way, clients will preferentially authenticate with domain controllers in their assigned site.

Additionally, you can modify the DC Locator process by setting registry-based site affinity or using Group Policy to influence domain controller selection. Another approach is to configure the DR domain controller with a lower priority by adjusting its DNS SRV record weight, making it less likely to be selected for authentication.

It’s also a good idea to monitor authentication traffic using tools like Event Viewer or Network Monitor to confirm that the changes are working as expected.

If this answer helped resolve your issue, feel free to hit “Accept Answer” so we know you’re all set 😊

T&B, Harry.
