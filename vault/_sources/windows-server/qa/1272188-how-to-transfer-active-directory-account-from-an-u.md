---
title: "How to transfer active directory account from an user to the replacement user."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1272188/how-to-transfer-active-directory-account-from-an-u
question_id: 1272188
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# How to transfer active directory account from an user to the replacement user.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1272188/how-to-transfer-active-directory-account-from-an-u (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When an user leaves and the user is replaced by another user, What is the best way to transfer the leaving user's Window Server 2019 account to the replacement user?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-08*

Decided to use a chunky method. 

Copied the left user account and changed the left user account copy to replacement user. Left password as is. (Replacement user already using the left user account.) If one tries to copy the left user redirected files/folders to replacement user, one run into the do not have access problem. Left the permissions as is. Instead, when to the computer being used and logged on as left user. Copied Desktop, Documents and Downloads to local C: drive. Verified there were no other locations for left user files/folders. Logged out. Logged in as replacement user. Copied the local stored left user Desktop, Documents and Downloads to the correct locations for replacement user. Deleted local stored left user files/folders. 

This is my answer to my question.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-01*

Looking at Active Directory Migration Tool version 3.2 https://www.microsoft.com/en-us/download/details.aspx?id=56570. The Active Directory Migration Tool version 3.2 (ADMT v3.2) provides an integrated toolset to facilitate migration and restructuring tasks in an Active Directory Domain Services infrastructure. NOTE: this tool has known problems and is in limited support – please carefully review the ADMT Known Problems and Support Statement link in Related Resources below before using. 

Sounds a bit risky. 

Why not make a copy of the leaving user account and the name changed to the replacement user? Then copy over the files/folders?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-01*

When an employee leaves a company and is replaced by a new employee, it's a good idea to transfer the leaving user's Windows Server 2019 account to the replacement user. This can help ensure a smooth transition and prevent any disruption to the new employee's work.

Here are the general steps to transfer a user's account to another user:

Create a new user account for the replacement user: Before you transfer the leaving user's account, create a new user account for the replacement user. Make sure the new user account has the necessary permissions and access to the resources that the leaving user had.

Transfer the leaving user's account: Use the Windows Server 2019 "User Account Migration and Merging" (ADMT) tool to transfer the leaving user's account to the new user account. The ADMT tool will transfer the user's profile, group memberships, and other account information to the new user account. You can download the ADMT tool from the Microsoft website.

Update permissions and access: Once the leaving user's account has been transferred to the new user account, update permissions and access for the new user account as needed. Make sure the new user has access to the resources that the leaving user had, and remove access for the leaving user's account.

Notify the relevant parties: Finally, notify relevant parties (such as IT, HR, and the new employee) that the transfer has been completed. Make sure the new user knows their login information and has access to the resources they need.

It's important to note that the specific steps for transferring a user's account may vary depending on your organization's policies and procedures. Make sure to follow any applicable guidelines and document your steps for future reference.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-01*

When an employee leaves a company and is replaced by a new employee, it's a good idea to transfer the leaving user's Windows Server 2019 account to the replacement user. This can help ensure a smooth transition and prevent any disruption to the new employee's work.

Here are the general steps to transfer a user's account to another user:

Create a new user account for the replacement user: Before you transfer the leaving user's account, create a new user account for the replacement user. Make sure the new user account has the necessary permissions and access to the resources that the leaving user had.

Transfer the leaving user's account: Use the Windows Server 2019 "User Account Migration and Merging" (ADMT) tool to transfer the leaving user's account to the new user account. The ADMT tool will transfer the user's profile, group memberships, and other account information to the new user account. You can download the ADMT tool from the Microsoft website.

Update permissions and access: Once the leaving user's account has been transferred to the new user account, update permissions and access for the new user account as needed. Make sure the new user has access to the resources that the leaving user had, and remove access for the leaving user's account.

Notify the relevant parties: Finally, notify relevant parties (such as IT, HR, and the new employee) that the transfer has been completed. Make sure the new user knows their login information and has access to the resources they need.

It's important to note that the specific steps for transferring a user's account may vary depending on your organization's policies and procedures. Make sure to follow any applicable guidelines and document your steps for future reference.
