---
title: "Have to remove/disable the firewall rules in GPO and gpupdate /force successfully without any error."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2142378/have-to-remove-disable-the-firewall-rules-in-gpo-a
question_id: 2142378
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Have to remove/disable the firewall rules in GPO and gpupdate /force successfully without any error.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2142378/have-to-remove-disable-the-firewall-rules-in-gpo-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts,

We are creating firewall rules in GPO, and we are applying firewall rules from GPO to all the member servers. Now we wanted to remove all the firewall rules which we created from GPO. If you are removing the rules and trying to update the GPO. gpupdate /force is working only in Domain controller, Gpupdate /force is failing in all the member servers after we removed the firewall GPO’s.

Also I have made the firewall rules via GPO as not configured as shown in the picture below. Still, I am able to see all firewall on the member server, which we have applied in the domain controller

Could someone please let me know how to remove the firewall rules or disable the firewall from GPO and update the GPO with any issue??

I am looking forward to hearing from you.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-10*

Hello

Thank you for posting in Q&A forum.

Here are a few steps you can take to troubleshoot the issue:

- 	Ensure that the necessary ports for Group Policy updates are open. Ports 137, 139, and 445 are commonly required for these updates

- 	Check the event logs on the member servers for any errors related to Group Policy processing. Look for specific error codes that might indicate what is blocking the updates

- 	Verify that there are no network connectivity issues between the domain controller and the member servers. Sometimes, network issues can prevent Group Policy updates from being applied.

- 	Ensure that the GPO changes have been replicated across all domain controllers. You can use the repadmin /syncall command to force synchronization.

- 	If the issue persists, you might need to reset the GPO settings on the member servers. This can be done by deleting the Registry.pol files located in the C:\Windows\System32\GroupPolicy\Machine and C:\Windows\System32\GroupPolicy\User directories and then running gpupdate /force again.

- 	Create a new GPO with the desired firewall settings and apply it to a test group of member servers to see if the issue persists.

-  If you link the GPO to custom OU or domain or Domain Controller OU?

If there is only firewall group policy setting within the GPO, you can delete this GPO or unlink the GPO from OU, and then update GPO on one machine.

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
