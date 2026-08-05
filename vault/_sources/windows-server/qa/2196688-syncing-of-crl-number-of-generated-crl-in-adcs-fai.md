---
title: "syncing of CRL number of generated CRL in ADCS failover cluster nodes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196688/syncing-of-crl-number-of-generated-crl-in-adcs-fai
question_id: 2196688
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
---
# syncing of CRL number of generated CRL in ADCS failover cluster nodes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196688/syncing-of-crl-number-of-generated-crl-in-adcs-fai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I like to know whether there is sync of CRL number of generated CRL in ADCS failover cluster nodes. 

Like to know where next crl number is stored.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-12*

Hi All,

In a simple ADCS service implemntion where current CRL Number is maintained so that ADCS service can generate CRL number sequentiallly.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-07*

ADCS CA database are stored in shared disk.  only Generated CRL is published in ldap. 

CA configurations are stored in registry that is also shared.

it will be very helpful if you point me exact location

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-07*

Hi KamalaKumar ShanmugaSundaram,

Thank you for posting in the Microsoft Community Forums.

In an ADCS (Active Directory Certificate Services) failover cluster, the CRL (Certificate Revocation List) numbers are usually synchronized across nodes. This is to ensure that each node in the cluster provides consistent and up-to-date certificate revocation information.

Regarding where the next CRL number is stored, this usually depends on the specific configuration of the ADCS and how the cluster is implemented. In general, however, in an ADCS, the CRL number and related information is stored in a certificate database. This database may be LDAP (Lightweight Directory Access Protocol)-based or some other type of database, depending on the version and configuration of the ADCS.

In a failover cluster, each node accesses this shared certificate database to ensure that they can provide consistent CRL information. Therefore, the next CRL number is also generated and stored in this database.

To view or manage CRL numbers and related information, you may need to have appropriate permissions and access to ADCS management tools or command-line interfaces. These tools typically allow you to view the status of CRLs, revoke certificates, generate new CRLs, and so on.

Note that specific implementations and configurations may vary depending on different ADCS versions and cluster environments.

Best regards

Neuvi
