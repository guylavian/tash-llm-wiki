---
title: "Query on Active Directory Groups"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5925610/query-on-active-directory-groups
question_id: 5925610
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Query on Active Directory Groups

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5925610/query-on-active-directory-groups (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I am using an Exchange Server Subscription Edition (SE) hybrid environment. User accounts are created on-premises and then migrated to Exchange Online.

We have several Active Directory security groups that were created directly in Active Directory. These groups were not created using the on-premises Exchange Admin Center or Exchange Management Shell. 

During the creation of these groups, the administrators populated the email-related attributes directly in Active Directory. i dont see these groups in Exchange onprem Admin center under groups tab

For example:

-  Group Name: `SomeGroup`

-  Email Address: `somegroup(at)mydomain.com`

These groups are synchronized to Microsoft Entra ID. In the Exchange Online Admin Center, I can see these groups listed as Mail-Enabled Security Groups, but the only email address displayed is: `somegroup(at)mydomain.onmicrosoft.com`

I have the following questions:

-  If a user sends an email to `somegroup(at)mydomain.onmicrosoft.com`, will the message be delivered to all members of the group?

-  Some of these groups appear in the Global Address List (GAL)/Address Book, while others do not. I am not sure why there is a difference in visibility, as all of these groups were created in the same way. Could someone please help me understand what might be causing this behavior?

## Answer (community) — community member

*upvotes: 0 · updated: 2026-06-20*

-  For `******@mydomain.onmicrosoft.com`

Mail-enabled security groups are Active Directory security groups that are mail-enabled and can be used to distribute messages to all members of the group.

From the provided information:

-  The groups are synchronized and appear in Exchange Online as Mail-Enabled Security Groups.

-  The primary SMTP address shown in Exchange Online is `******@mydomain.onmicrosoft.com`.

In Exchange/Exchange Online, the primary SMTP address is what is used for delivery. When a message is sent to that primary address, it is delivered to the group and then distributed to all group members.

Therefore, if a user sends an email to `******@mydomain.onmicrosoft.com`, it will be delivered to the mail-enabled security group and then to all members of that group, assuming:

-  The group is correctly mail-enabled.

-  The group is a supported type (universal mail-enabled security group or a mail-enabled non-universal group that is still managed).

Mail-enabled security groups are explicitly described as being usable to distribute messages to recipients:

-  “Mail-enabled security groups… can be used to assign access permissions to resources in Active Directory and can also be used to distribute messages.”

-  Why some groups appear in the GAL and others do not

For mail-enabled security groups and distribution groups, visibility in the Global Address List (GAL) is controlled by properties on the group object. The documentation highlights:

-  Groups have a Display name that appears in the global address list and on the To: line when email is sent to the group.

-  There is a Hide this group from address lists option. If this is selected, the group does not appear in the GAL, and senders must know the alias or email address to send messages.

Relevant points from the context:

-  “Display name: This value should help users immediately recognize what the group is used for. This name appears in the global address list…”

-  “Hide this group from address lists: Select this check box if you don't want users to see the group in the global address list. If this check box is selected, a sender has to know and type the group's alias or email address to send messages to the group.”

Given that some of the groups appear in the GAL and others do not, likely causes include:

-  Hide-from-address-lists setting differs: Some groups may have the “Hide this group from address lists” (or equivalent attribute) enabled, while others do not.

-  Display name / mail-enabled completeness: A group must be properly mail-enabled and have a display name for it to appear in the GAL. The context notes that missing display names can cause synchronization issues for mail-enabled groups.

To summarize:

-  Groups that are not hidden from address lists and are properly mail-enabled with a display name will appear in the GAL.

-  Groups configured to be hidden from address lists (or missing required mail-enabled attributes such as display name) will not appear in the GAL, even though they can still receive mail if addressed directly by SMTP address.

References:

-  Manage mail-enabled security groups in Exchange Server

-  Manage distribution groups

-  Recipients in Exchange Server

-  Recipients

-  Active Directory security groups

-  Mail-enabled groups that have an email address aren't synchronized to Microsoft 365
