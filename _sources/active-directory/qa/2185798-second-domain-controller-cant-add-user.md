---
title: "Second domain controller cant add user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185798/second-domain-controller-cant-add-user
question_id: 2185798
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Second domain controller cant add user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185798/second-domain-controller-cant-add-user (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,

We are experiencing an error when adding a user to our second domain controller. It says:

 Windows cannot set the password for <user> because

The specified directory object is not bound to a remote resource.

Windows cannot remove the newly created object automatically. Remove it manually or contact your system administrator.

https://answers-afd.microsoft.com/static/images/image-not-found.jpg

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-23*

Hello Ryuji Tuesca1,  

Thank you for posting in Microsoft Community forum.

-  Check whether the network connection between the second domain controller and other domain controllers is normal to ensure a stable network connection.

-  Check whether the replication status of the second domain controller is healthy to ensure that all domain controllers can properly replicate and synchronize the Active Directory data.

-  Confirm that the account you are using has the permission to add users, and you can perform the operation of adding users on the second domain controller.

-  Restart the domain controller: Try restarting the second domain controller to make sure that its configuration and status are normal.

Here is the documentation on checking for AD replication issues: Diagnose AD replication failures - Windows Server | Microsoft Learn

Please check if you have an Orphaned Domain controller in the domain, and you did not remove it completely.  

Here is a similar thread for your reference.

Active Directory: Cannot create new user on operations master, but can on other DCs in domain. | Microsoft Learn

I hope you the information above is helpful.

If you have any questions or concerns, please do not hesitate to let us know.

Best Regards,  

Daisy Zhou
