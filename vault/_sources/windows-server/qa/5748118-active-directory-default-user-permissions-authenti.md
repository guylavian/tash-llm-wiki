---
title: "Active directory - default user permissions - authenticated users \"read permission\" is missing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5748118/active-directory-default-user-permissions-authenti
question_id: 5748118
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Active directory - default user permissions - authenticated users "read permission" is missing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5748118/active-directory-default-user-permissions-authenti (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I’m running into an issue with Active Directory permissions that I haven’t been able to resolve, and I’m hoping someone here has seen this before.

Problem Description

Under normal circumstances, user objects in Active Directory should inherit the standard “Read permissions” ACE assigned to Authenticated Users. This entry is also visible in the AD schema as part of the defaultSecurityDescriptor for the `user` class.

However, although the permission exists in the schema, it is not being propagated to actual user objects. When inspecting the Advanced Security Settings of affected user accounts, the “Read permissions” ACE is missing entirely. The screenshot below shows what should be assigned:

Impact

Some services rely on this permission to function correctly—most notably SQL Server, which requires basic read access to the AD object to resolve account attributes. Because this ACE is missing, SQL Server cannot use these accounts for authentication or service bindings.

What I've Checked So Far

-  The schema entry for `user` does contain the expected ACEs.

-  No custom inheritance blocks are enabled on the affected user objects.

-  “Protect object from accidental deletion” is not enabled.

-  “Read permissions” is also not being inherited from parent OU objects.

Questions for the Community

-  Has anyone experienced a situation where schema‑level ACEs fail to propagate to newly created user objects?

-  Is there a safe way to re‑apply the defaultSecurityDescriptor to existing user objects without manually editing ACEs one by one?

BR Stephan

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-01-30*

Hi StephanG,

Just checking in to see whether the issue has been resolved. Let me know if you need any further assistance from my side. If you found the answer helpful, selecting Accept Answer would be greatly appreciated.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-01-29*

Hi StephanG,

Well, you’re absolutely right that the “Read permissions” ACE for Authenticated Users is part of the defaultSecurityDescriptor for the user class in Active Directory. However, this descriptor only applies during object creation, and only if no custom security descriptor is explicitly defined. If user accounts were provisioned using scripts, third-party tools, or templates that override default ACLs, the expected ACE may not be applied.

Since you’ve confirmed that inheritance is not blocked and the schema is intact, the most likely cause is that the creation method bypassed default ACL propagation. Fortunately, you don’t need to manually edit each object. You can safely reapply the missing ACE using PowerShell or LDIFDE. A PowerShell script can iterate through affected users and add the “Read permissions” ACE for Authenticated Users in bulk, ensuring SQL Server and other services can resolve attributes correctly.

I also recommend checking whether any provisioning workflows or GPOs are applying custom ACLs that might be stripping this entry post-creation. Reviewing the Effective Access tab can help confirm whether the permission is truly missing or just not visible in the standard view.

I hope the explanation shared so far helps clarify or improve the situation. If this answer is helpful, please click “Accept Answer” to mark it as resolved so others can benefit as well 😊.

Jason.
