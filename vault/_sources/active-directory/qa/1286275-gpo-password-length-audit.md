---
title: "GPO password length audit"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1286275/gpo-password-length-audit
question_id: 1286275
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO password length audit

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1286275/gpo-password-length-audit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

With the new-ish password guidelines focusing on longer, but static, passwords I updated GPOs to include "minimum password length audit" to the proposed new limit. However I haven't found any guidance on where to get these audit results, or how long until I can expect them to start showing up. Where are these results posted?

Additionally I found some discussions about having different AD server versions and these settings. I needed to build new servers to obtain the "Relax minimum password length limits" and "Minimum password length audit" options in Group Policy Management. Even though the OS appears to be patched, these options were not on the existing servers. Will I see some inconsistencies until I move DSMO roles to the new servers?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-17*

Hello Skygordon,

Thank you for posting in our Q&A forum.  

Here is a document that might help you. It contains the following information.  

Supported versions of Windows.  

Deployment guidelines.  

Policy path and setting name.  

When Windows event ID will log.  

Windows event ID and log messages.  

For more information, you can read it.  

https://support.microsoft.com/en-us/topic/minimum-password-length-auditing-and-enforcement-on-certain-versions-of-windows-5ef7fecf-3325-f56b-cc10-4fd565aacc59#:~:text=If%20the%20Relax%20minimum%20password%20length%20limits%20setting,to%200%20means%20that%20no%20password%20is%20required.  

Hope the information above is helpful. If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
