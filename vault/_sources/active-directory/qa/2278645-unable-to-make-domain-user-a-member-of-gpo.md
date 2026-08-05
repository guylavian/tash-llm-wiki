---
title: "Unable to make domain user a member of GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2278645/unable-to-make-domain-user-a-member-of-gpo
question_id: 2278645
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Unable to make domain user a member of GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2278645/unable-to-make-domain-user-a-member-of-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm setting up a new AD Domain Controller. I've done this several times in the past and have had no problem, but this time I cannot make a new domain user a member of the folder redirection GPO. I must be missing a step. Here's what I've done:

-  In Group Policy Management I right-clicked on my domain hprs.local and added a 'New Organizational Unit' which I called "HPRS Groups". 

-  I then right-clicked on "HPRS Groups" and did 'Create a GPO in this domain, and Link it here ...". I named that GPO "HPRS Folder Redirection".

-  I right-clicked on "HPRS Folder Redirection" then 'Edit'. and went to User Configuration > Policies > Windows Settings > Folder Redirection.

-  In the right panel I right-clicked Desktop > Properties. In the 'Target' tab I selected "Basic: Redirect everyone's folder to the same location", and I set the Root Path to "\mail.hprs.local\Users". This is how I've always done it. That folder does exists on the DC. I repeated this for Documents, Downloads and Favorites.

-  Back on the GP Management page I clicked on "HPRS Folder Redirection" and verified its location was "HPRS Groups" and the Path was "hprs.local/HPRS Groups". I also verified that Security Filtering had "Authenticated Users".

-  I then opened ADUC and added domain user mark and went to the 'Member Of' tab. This user was listed as a member of 'Domain Users'.

-  I then clicked 'Add' and under "Enter the object name to select" I typed "hprs folder redirection", did 'Check names', but got the message "An object named 'HPRS Folder Redirection' cannot be found. Check the selected object types ...". I tried several variations on abbreviating the name, tried selecting the alternate object type and even recreated the GPO directly under the hprs.local domain without a "HPRS Groups" OU. Nothing worked.

The above procedure has always worked the several times I've set up a AD/DC before. What am I missing?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-27*

Thanks for the feedback. The network share is correct. Comments ... Your step 1 & 2, no problem, did that. 

For your step 2 you wrote: "Link the GPO to the OU that contains the user accounts you want the policy to apply to. Example: If your user “mark” is in an OU called `HPRS Users`, you need to link the GPO to `HPRS Users`.

So, as to "Link the GPO to the OU that contains the user accounts", I created the GPO before configuring any user accounts. I believe that's how I did id before. Is that wrong? 

Maybe I'm thinking too hard. My personal notes on this from some time ago say, "Link the new GPO policy (if not done already) to an OU with a user account that can be used to test this policy. This user must log on to a Windows computer to allow proper processing of this policy."

I'm sure I got that from someone else. When I go to create users, how do I "link the new GPO ... to an OU with a user account..."? Does havint the GPO filtering as "Authenticated Users" and creating the user as a 'Member of' "Domain Users" (which is hprs.local\Users) automatically do the "link"?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-05-25*

You're trying to add a user to a GPO using the “Member Of” tab in Active Directory Users and Computer (ADUC). GPOs are not group accounts. They cannot be added to users’ group memberships. You cannot make a user a “member of a GPO” because a GPO is not a security group or user object.
When you typed "HPRS Folder Redirection" into the "Enter the object name to select" field in the Member Of tab, ADUC couldn't find it — because it's not a group, it's a policy object, and ADUC is only searching for groups, users, or computers.

To make it work: 

-  Create the GPO as you did — named `HPRS Folder Redirection`.

-  Configure folder redirection settings under:

```
User Configuration > Policies > Windows Settings > Folder Redirection
```

-  Link the GPO to the OU that contains the user accounts you want the policy to apply to.

-  Example: If your user “mark” is in an OU called `HPRS Users`, you need to link the GPO to `HPRS Users`.

-  If the GPO is only linked to `HPRS Groups` but the user is in a different OU, the GPO will not apply.

-  Security Filtering:

-  The GPO by default applies to Authenticated Users, meaning it affects all users in the OU where it's linked.

-  If you want the GPO to apply to only specific users or groups, you should:

-  Leave `Authenticated Users` with the read only permissions.

-  Add the user (e.g., `mark`) or a security group (e.g., `FolderRedirectionUsers`) that contains the user.

-  Then go to the Delegation tab → Advanced, and ensure the user or group has:

-  Read

-  Apply Group Policy

-  Verify the Folder Share:

-  Ensure the root path (e.g., `\\mail.hprs.local\Users`) is:

-  A valid network share.

-  Accessible by the user account.

-  Has correct NTFS and share permissions for redirection (users must have write access to their folder or to the root folder with auto folder creation enabled).

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
