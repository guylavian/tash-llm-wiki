---
title: "Active Directory Domain Services could not create the NTDS Settings object for this Active Directory Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2119630/active-directory-domain-services-could-not-create
question_id: 2119630
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Domain Services could not create the NTDS Settings object for this Active Directory Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2119630/active-directory-domain-services-could-not-create (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to add Windows Server 2019 as an additional AD server. When I try to promote the new server, I get the following error message:

The operation failed because:

Active Directory Domain Services could not create the NTDS Settings object for this Active Directory Domain Controller CN=NTDS Settings,CN=XXX ,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=XXX,DC=LOCAL on the remote AD DC XXX.XXX.LOCAL. Ensure the provided network credentials have sufficient permissions. "The Directory Service cannot perform the requested operation because a domain rename operation is in progress."

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-18*

Hello,

The error message indicates that the NTDS Settings object could not be created, and it mentions that a domain rename operation is in progress. Here are some steps you can take to troubleshoot and resolve this issue:

1.Check Domain Rename Status:

Ensure that there is no ongoing domain rename operation. You can check this by running the command:

repadmin /replsummary

If a rename is in progress, you may need to wait for it to complete or cancel it if it's stuck.

2.Verify Permissions:

Ensure that the account you are using to promote the new DC has sufficient permissions. The account should be a member of the Enterprise Admins or Domain Admins groups.

You can also check the effective permissions using ADSI Edit:

Open adsiedit.msc.

Navigate to the domain partition and check the permissions for your user account.

3.Remove Failed DC Accounts:

If the promotion attempt created a computer account for the new DC, you may need to delete it:

Use Active Directory Users and Computers or Active Directory Sites and Services to find and remove any failed DC accounts.

4.Restart the Server:

Sometimes, simply restarting the server can resolve transient issues.

5.Check for Existing NTDS Settings:

Ensure that there are no existing NTDS Settings objects that might conflict with the new DC. You can check this in Active Directory Sites and Services.

6.Review Event Logs:

Check the Event Viewer on both the new server and the existing DCs for any related error messages that might provide more context.

Best Regards,

Yanhong 

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-11-17*

Hi @Yateen Pawar  

You should use an admin account member of domain admins group to promote an additional domain controller.

Please don't forget to accept helpful answer
