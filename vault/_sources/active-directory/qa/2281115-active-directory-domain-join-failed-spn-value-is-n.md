---
title: "Active Directory Domain Join failed- SPN value is not unique"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2281115/active-directory-domain-join-failed-spn-value-is-n
question_id: 2281115
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Active Directory Domain Join failed- SPN value is not unique

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2281115/active-directory-domain-join-failed-spn-value-is-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Friends,

I need assistance to resolve an issue when attempting to join a Windows 11 laptop to an Active Directory domain. The following error message is encountered: ******The following error occurred attempting to join the domain xxxx.com: the operation failed because SPN value provided for additional/modification is not unique forest wide.******The computer account and DNS record has already been deleted from the Domain Controller. While renaming the hostname of the client machine allows successful domain joining, the goal is to keep the hostname unchanged. Error screenshot is attached here.domain joining error.jpg

Guidance on resolving this issue would be appreciated.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-06-05*

Hello,

   Thank you for posting question on Microsoft Windows forum!

   Based on provided screenshot error message The operation failed because SPN value provided for addition/modification is not unique forest-wide which occurs when attempting to join a Windows 11 laptop to an Active Directory domain. It is probable of that Active Directory is still aware of the old hostname's SPN, preventing a new computer account with that same hostname from being created and registered with its default SPNs. This often happens if the computer account wasn't fully purged, or if there's an orphaned SPN. You can try the following potential troubleshooting steps.

1.Verify Computer Account Deletion:

-  Double-check Active Directory Users and Computers (ADUC): Even if you think it's deleted, thoroughly search for the computer object in all OUs, including the "Computers" container and any custom OUs you might have.

-  Check "Deleted Objects" container (if enabled): If your forest functional level supports the AD Recycle Bin, check the "Deleted Objects" container to ensure it's not merely in a soft-deleted state.

2.Checking for Orphaned SPNs:

-  Use setspn to query for the SPN: This is the most direct way to find the offending SPN. Open an elevated Command Prompt or PowerShell on a Domain Controller and run the following command to performs a duplicate SPN check across the entire forest.:

-  setspn -X   

-  If the environment has multiple domains, the SPN might exist elsewhere.

-  setspn -L hostname

-  Once you've identified the object, use setspn -D to delete the specific SPN. Be extremely careful with this command, as deleting the wrong SPN can cause service disruptions.

-  setspn -D <SPN> hostname

-  more information for SPN command https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/setspn

3.Check for Stale DNS Records:

-  While you mentioned DNS was deleted, it's worth a quick recheck, especially for any lingering PTR records if you use reverse DNS.

-  Open DNS Management: On a Domain Controller, open DNS Manager.

-  Check Forward Lookup Zones: Verify that there are no A records for the hostname.

-  Check Reverse Lookup Zones: If you use reverse lookup, ensure there are no PTR records for the IP address the laptop would acquire.

-  Force DNS Replication: If you have multiple DNS servers, force replication to ensure all servers are up to date.

4.Replication Status:

-  Ensure that Active Directory replication is healthy across all Domain Controllers. If replication is not working correctly, a deletion on one DC might not have propagated to others, leading to the SPN still existing on a different DC.

-  Use repadmin /showrepl: Run this command on a Domain Controller to check replication status. Address any replication errors.

5.Try Joining Again:

-  After performing the above steps, especially after successfully deleting any orphaned SPNs, attempt to join the Windows 11 laptop to the domain again with its original hostname.

Hope the above information is helpful!
