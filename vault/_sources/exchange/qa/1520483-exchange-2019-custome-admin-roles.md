---
title: "Exchange 2019 Custome Admin Roles"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1520483/exchange-2019-custome-admin-roles
question_id: 1520483
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2019 Custome Admin Roles

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1520483/exchange-2019-custome-admin-roles (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Experts,
I have a very unique requirements. If anybody can help me to do it.
Our Environment is single AD Single Domain, with 2 Exchange Servers.
We have 4 domains configured in Exchange Server.
Now we need to create the admin who can create and see just a users for the domain he is assigned to.
What I mean is that if we give access of domain1.com to the *** Email address is removed for privacy *** then he must be able to do all the Admin tasks for that domain.
But he will not be able to access any other domains users and tasks.
I have played with the roles but I couldn't get the job done.
Can anyone help me for this kind of configuration.
Thanks.
Ali.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-05*

I couldn't check it now.
I will check on weekend and will confirm you.
Thanks,
Ali.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-01*

Hi @Shafaqat Ali,

Now we need to create the admin who can create and see just a users for the domain he is assigned to

If in Active Directory you have four separate organization units for each of these domains, in Exchange you can refer to the following documentation to create a custom scope to only allow the admin to be able to manage one specific organization unit:

Understanding management role scopes

However, to my knowledge it may not be possible to restrict admins from seeing other domains' users, but they will have no permission to manage these users.

Below is an example:

1.create a custom scope to only allow writing to the domain1 OU

2.create a role group and select this scope, add Mail Recipient creation role to allow creating mailboxes, add an admin to this group

3.when this admin tries to create a mailbox in other OU than the domain1 OU, he gets an error that this is out of his write scope

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
