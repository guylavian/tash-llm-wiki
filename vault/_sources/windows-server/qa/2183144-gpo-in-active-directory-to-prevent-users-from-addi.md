---
title: "GPO in active directory to prevent users from adding printers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2183144/gpo-in-active-directory-to-prevent-users-from-addi
question_id: 2183144
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO in active directory to prevent users from adding printers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2183144/gpo-in-active-directory-to-prevent-users-from-addi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Need to create a Server Mgr GPO to prevent users from adding printers.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-28*

Hi Thomas Farley,

Thanks for your post. With the built-in function provided by windows server with printer server role, admin could publish the printer to users or computers via GPO:

-  Open Print Management--->Print Server-->Printers--->Deploy with Group Policy

-  In the Deploy with Group Policy dialog box, click Browse, and then choose or create a new GPO for storing the printer connections.

-  Specify whether to deploy the printer connections to users, or to computers:

To deploy to groups of computers so that all users of the computers can access the printers, select the computers that this GPO applies to (per machine) check box. To deploy to groups of users so that the users can access the printers from any computer they log onto, select the users that this GPO applies to (per user) check box.

More details could be referred to below link: Deploy Printers to Users or Computers via Group Policy https://theitbros.com/deploy-printers-in-domain-group-policy/

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.

Best Regards,

Ian Xue

If the Answer is helpful, please click "Accept Answer" and upvote it.
