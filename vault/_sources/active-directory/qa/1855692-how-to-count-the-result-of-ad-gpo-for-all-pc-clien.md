---
title: "How to count  the result of AD GPO for all PC client"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1855692/how-to-count-the-result-of-ad-gpo-for-all-pc-clien
question_id: 1855692
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to count  the result of AD GPO for all PC client

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1855692/how-to-count-the-result-of-ad-gpo-for-all-pc-clien (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

For AD domain group policies issued, is there a way to count the effective status of all clients in the domain？Can I know how many client successfully  implement this one AD GPO?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-07*

Hello,

Thank you for posting in Q&A forum.

Yes, you can determine the effectiveness of Group Policy Objects (GPOs) in an Active Directory (AD) domain by checking the Group Policy results on client machines.

You can use the Group Policy Results Wizard. Use the Group Policy Results Wizard to determine which Group Policy settings are in effect for a user or computer by obtaining RSoP data from the target computer.

To run the Group Policy Results Wizard, follow these steps.

-  Open GPMC, right-click Group Policy Results, and select Group Policy Results Wizard.

2.Select Next to get started.

3.Select This computer then select Next. Optionally, you can select Another computer and enter the computer name, then select Next.

4.Select Current user then select Next. Optionally, you can select Select a specific user and select the username from the list of users that have logged on to the computer. Select Next to continue.

5.Review the Summary of Selections screen, then select Next to run the Group Policy results.

6.Select Finish to complete the wizard.

For more details, see: Group Policy Modeling and Results in Windows | Microsoft Learn

You can also use the gpresult command-line toolGPResult command-line tool to verify which Group Policy Objects are applied to a user or computer. GPResult is a command-line tool that displays the resulting policy set for a Group Policy Object. For a more detailed report, you can run "gpresult /h report.html" to generate an HTML report.

For detailed steps, see: GPResult Tool: How To Check What Group Policy Objects are Applied - Active Directory Pro

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
