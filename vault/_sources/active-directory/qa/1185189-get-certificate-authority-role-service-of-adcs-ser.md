---
title: "Get certificate authority role service of ADCS server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1185189/get-certificate-authority-role-service-of-adcs-ser
question_id: 1185189
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
---
# Get certificate authority role service of ADCS server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1185189/get-certificate-authority-role-service-of-adcs-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How can we know which Role Services were selected in the wizard of the ADCS server has configured first time using any cmdlet or command line as like i.e. certutil ?

[ ] Certification Authority : used to issue certificates to users, computers, and services, and to manage certificate validity.

[ ] Certificate Enrollment Policy Web Service : allows users and computers to retrieve information about their certificate enrollment policy.

[ ] Certificate Enrollment Web Service : allows external clients who are not part of the domain network to connect to a CA via Web browser to request certificates.

[ ] Network Device Enrollment Service : allows routers and other network devices that do not have domain accounts to obtain certificates.

[ ] Online Responder : receives and processes requests on the status of the certificates and sends back signed responses containing requested certificate status information.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-02-28*

Hi,

Not possible unless the configuration settings was exported during the setup, you can check event logs and install successful IDs. If you planning to reinstall go with the standard Certificate Authority installation process - https://learn.microsoft.com/en-us/windows-server/networking/core-network-guide/cncg/server-certs/install-the-certification-authority

Hope this helps.

JS

==

Please Accept the answer if the information helped you. This will help us and others in the community as well.
