---
title: "Changing Out Domain Controller Certificates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/319131/changing-out-domain-controller-certificates
question_id: 319131
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Changing Out Domain Controller Certificates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/319131/changing-out-domain-controller-certificates (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good afternoon community, So I've been working on a fairly large rip and replace project gutting out some old systems, including the previous implementation of Windows Certificate Authority services. The old PKI had skeletons, and I decided to build out a new side-by-side PKI to start over fresh rather than export and import onto a new server and potentially run into issues. So far everything has been going very well. My PKIVIEW looks super clean, my auto-enroll GPO is working as intended, and my template security settings are all looking good as well. RADIUS and HTTPS look perfect too on the systems that deal with those processes. A lot of this I knew would be fine ahead of time, but IT paranoia and all that. The last step that I've been thinking over is our domain controllers. I know their certs which were issued by the old PKI are at least used for LDAPS, but as I've been digging around I'm not really sure what else they are leveraged on. I wanted to switch them over to the new Kerberos Authentication Template signed by the new subordinate off of the old Domain Controller template signed by the predecessor. The Root & Subordinate CAs are already trusted on all domain joined devices, and any systems that are outside of AD I've imported both to those systems trust stores as well. With that in mind, as long as I request the new Kerberos Authentication certificate on my DCs and restart them, they should start using the new certificate (due to the expiry date being the farther out) upon service startup when it comes back online. I can also add the old Domain Controller certificate to the Superseded Templates tab on the new Kerberos Authentication template. I'm curious if anyone in the community has done a DC certificate swap before, and is willing to share any repercussions of the change with me? Thanks!

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-03-17*

Just do it as planned.
