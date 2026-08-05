---
title: "Troubleshooting User GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2281508/troubleshooting-user-gpo
question_id: 2281508
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Independent Advisor"]
---
# Troubleshooting User GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2281508/troubleshooting-user-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am logged in to two computers with the same credential buts. One of the computers is missing two GPO's

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-06-09*

Hello,

   Thank you for posting question on Microsoft Windows forum!

   Based on your query of logging in to two computers with the same credential. But one computer is missing two GPOs that are applied to another. There are several reasons for causing the issue. You can try the following potential troubleshooting steps to pinpoint the cause.

1.Gather Information with gpresult:

-  On the problematic computer, open an elevated Command Prompt (Run as administrator) and run the following command:

-  gpresult /h C:\temp\non-workingreport.html

-  On the healthy computer, open an elevated Command Prompt (Run as administrator) and run the following command:

-  gpresult /h C:\temp\workingreport.html

-  Comparing the output of the above commands which generate HTML report for non-working and working with below points to spot any difference between healthy and affected computers.

-  Applied GPOs: Are the two missing GPOs listed here?

-  Denied GPOs: If they are denied, what is the "Denial reason"? This is crucial. Common reasons include:

-  Security Filtering: The computer object isn't in the correct security group or "Authenticated Users" is removed from the GPO's security filtering.  

-  WMI Filter: A WMI filter is attached to the GPO and is evaluating to false on this specific computer.

-  Link Disabled/Enforced: The GPO link is disabled at the OU level or "Enforced" is not checked when it should be (though this would usually affect all computers in that OU).

-  Out of scope: The GPO is not linked to an OU where the computer object resides.

2.Check Basic Connectivity and Domain Membership:

-  Network Connectivity: Ensure the problematic computer has full network connectivity to your domain controllers (DCs). Can it ping the DCs by IP address and FQDN?

-  DNS Resolution: Verify DNS resolution is working correctly on the problematic machine. Can it resolve the domain name and DC hostnames?

-  Domain Membership: Confirm the problematic computer is still correctly joined to the domain. If it's been disjoined or has a trust relationship issue, GPOs won't apply.

3.Verify GPO Configuration in Group Policy Management Console (GPMC) on a Domain Controller:

-  Open GPMC.

-  Locate the two missing GPOs.

-  Check where they are linked. Are they linked to the correct Organizational Unit (OU) where the problematic computer resides?  

-  Ensure the GPO link is Enabled.

4.Check Event Logs on the Problematic Computer:

-  Open Event Viewer (eventvwr.msc).

-  Navigate to Applications and Services Logs > Microsoft > Windows > GroupPolicy > Operational.  

-  Look for any errors or warnings related to Group Policy processing at the time of the gpupdate /force or computer startup. These logs might provide specific reasons for GPO failures.

Hope the above information is helpful!
