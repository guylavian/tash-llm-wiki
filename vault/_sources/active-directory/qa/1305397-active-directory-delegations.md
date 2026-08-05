---
title: "Active Directory delegations"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1305397/active-directory-delegations
question_id: 1305397
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory delegations

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1305397/active-directory-delegations (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

What permissions do i need to be able to delegate computer objects in Active Directory?  

I would like to be able to delegate access from one AD Computer Object to another AD Computer Object,  

in my specific case i would like to delegate a Windows Server Object Running Azure Application Proxy to another AD Server which is running a web-server, right now only our domain admins are able to do so & we would like to build a custom role.  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-15*

```
Hello E J,

Thank you for your question and for reaching out with your question today.

To delegate access from one Active Directory (AD) computer object to another, you will need the appropriate permissions within AD. Specifically, you will require the following permissions:

1. Delegate Control permission:
   - To delegate control from one computer object to another, you need the "Delegate Control" permission on the source computer object.
   - This permission allows you to specify which actions can be performed on the source computer object and delegate those permissions to a specific user or group.

2. Write All Properties permission:
   - To modify the necessary properties of the target computer object, you need the "Write All Properties" permission on the target computer object.
   - This permission allows you to modify the necessary attributes, such as the "msDS-AllowedToActOnBehalfOfOtherIdentity" attribute, which is used to grant access to the target computer object.

To grant these permissions, you will typically require the following roles or membership:

1. Domain Admins:
   - Members of the Domain Admins group have full administrative rights over the entire Active Directory domain. By default, they have the necessary permissions to delegate control and modify computer object properties.
   - However, it is not recommended to grant this level of access to regular users unless absolutely necessary for administrative purposes.

2. Custom Role:
   - To create a custom role with the necessary permissions, you can define a new role in Active Directory with specific privileges for delegating control and modifying computer object properties.
   - You can use the built-in Active Directory administrative tools, such as Active Directory Users and Computers, to create a custom role and assign the required permissions.
   - Ensure that the custom role has appropriate limitations and is only assigned to trusted administrators who need the specific delegation capabilities.

Please note that the exact steps for creating a custom role and assigning permissions may vary based on your specific AD environment and administrative tools.

I used AI provided by ChatGPT to formulate part of this response. I have verified that the information is accurate before sharing it with you.

If the reply was helpful, please don’t forget to upvote or accept as answer.

Best regards.
```
