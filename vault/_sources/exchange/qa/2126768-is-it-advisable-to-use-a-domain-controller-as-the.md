---
title: "Is it advisable to use a domain controller as the witness server for the Database Availability Group in Exchange Server?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2126768/is-it-advisable-to-use-a-domain-controller-as-the
question_id: 2126768
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Is it advisable to use a domain controller as the witness server for the Database Availability Group in Exchange Server?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2126768/is-it-advisable-to-use-a-domain-controller-as-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have on-premise exchange server setup in windows server 2019 standard environment. Two for primary site and two for DR site with one Witness server (Domain Controller). Is it recommended to use DC as DAG witness or not. If not, how does it impact. Kindly share the recommended architecture for the witness server. Thank you

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-06*

Hi @Narayan Das Kohli  ,

Welcome to the Microsoft Q&A platform!

Microsoft generally does not recommend using a domain controller (DC) as a database availability group (DAG) witness server. Here are the reasons and recommended architectures:

Why not use a DC as a DAG witness server?

-  The witness server should be a minimal role server to reduce the attack surface. DCs have broader roles and run more services, which increases risk.

-  The additional load on the DC affects its primary function, which can affect the overall performance of the network.

-  Combining roles makes troubleshooting more complex and time-consuming.

Recommended architecture for a witness server :

-  Ideally, the witness server should be a dedicated server that does not perform any other roles. This minimizes security risks and simplifies management.

-  If possible, place the witness server in a third site. This helps ensure that the witness server is available even if one of the primary sites fails.

-  Make sure the witness server is configured with the necessary permissions and belongs to the same Active Directory domain as the DAG members.

For detailed guidance on setting up a DAG and preferred architecture, you can refer to Microsoft's Exchange 2019 preferred architecture.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
