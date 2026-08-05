---
title: "Frequent Event Log errors related to GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188695/frequent-event-log-errors-related-to-gpo
question_id: 2188695
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Frequent Event Log errors related to GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188695/frequent-event-log-errors-related-to-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We currently have 3 different versions of Server in our environment.

2016

2019

2022

All the 2016's and 2019's have multiple Application event log errors with the following:

"Security policies were propagated with warning. 0x57 : The parameter is incorrect."

When I launch RSOP.MSC on the system with the error, I can see that there is a warning under “Computer Configuration”.  Going into the properties it tells me that the Warning is within the Security Settings.  Drilling down into Security Settings, I can see that the Password Policy has some issues.  The 2022's don't have this issue.  All systems use the same "Default Domain Policy"

![](https://learn-attachment.microsoft.com/api/attachments/f241086f-3d44-41cf-8d73-a81d8c9110e9?platform=QnA"https://learn-attachment.microsoft.com/api/attachments/bb019b42-d056-4ec2-9b6d-f651a269f103?platform=QnA" title="filestore.community.support.microsoft.com" rel="ugc nofollow">  

Any advice how to proceed next would be greatly appreciated.

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-09*

First, make sure that Default Domain Policy is correctly applied to all servers. You can use the following command to view the Group Policy Result Set (RSOP):

As stated in my initial posting, I have already verified that the GPO is applied to the servers I checked. "All systems use the same Default Domain Policy"

2. Check the specific settings of the password policy

Since the problem points to the password policy, you should check the following points:

Ensure that the password policy settings are consistent across all servers and meet your security requirements.

Again as stated before (not sure why I have to repeat myself), it's all across the same. I have posted a pic showing one difference that's on the 2022 with red arrows and question marks.

Check if any other Group Policy Objects (GPOs) override the default password policy settings.

There is no override. They all use the same GPO called "Default Domain Policy"

Check to see if any custom GPOs have been incorrectly linked to OUs (organizational units) or sites, which could lead to policy conflicts.

There is no conflict that I can see

3. Check Group Policy Inheritance and Linking

Use the Group Policy Management Tool (GPMC) to check the linking and inheritance settings for group policies.

Ensure that no unnecessary GPOs are linked to OUs that contain these servers, especially those that may contain conflicting settings.

This seems like a very generic request. Please be more specific.

4. Review event logs

Carefully review the system logs and security logs for any other errors or warnings related to password policies or group policies.

Pay particular attention to any errors related to LDAP (Lightweight Directory Access Protocol), as password policies are often stored in Active Directory.

Again, see my original post about the event logs

-  Registry and Winlogon Logs

If winlogon.log does not provide enough information, you may consider increasing the level of detail in the log or looking at other relevant registry entries. Note, however, that direct modification of the registry can be risky, so make sure you know what you're doing or back up the registry before making changes.

Another possible tool is Process Monitor (from the Sysinternals suite), which captures all registry accesses and system calls related to winlogon.

Again, see my original post releted to winlogon logs (was my original post obscured somehow??)

6 Upgrading or patching the server

If possible, consider updating Windows Server 2016 and 2019 systems to the latest patch level. This can address known security and compatibility issues.

We regular update and patch as they come through

Question, are you able to understand this?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-09*

Hi Brendan_007,

Thank you for posting in the Microsoft Community Forums.

-  Verify Group Policy settings

First, make sure that Default Domain Policy is correctly applied to all servers. You can use the following command to view the Group Policy Result Set (RSOP):

bash

gpresult /h C:\gpresult.html

This will generate an HTML file under the specified path, which you can open in your browser to view the detailed Group Policy settings and applications.

-  Check the specific settings of the password policy

Since the problem points to the password policy, you should check the following points:

Ensure that the password policy settings are consistent across all servers and meet your security requirements.

Check if any other Group Policy Objects (GPOs) override the default password policy settings.

Check to see if any custom GPOs have been incorrectly linked to OUs (organizational units) or sites, which could lead to policy conflicts.

-  Check Group Policy Inheritance and Linking

Use the Group Policy Management Tool (GPMC) to check the linking and inheritance settings for group policies.

Ensure that no unnecessary GPOs are linked to OUs that contain these servers, especially those that may contain conflicting settings.

-  Review event logs

Carefully review the system logs and security logs for any other errors or warnings related to password policies or group policies.

Pay particular attention to any errors related to LDAP (Lightweight Directory Access Protocol), as password policies are often stored in Active Directory.

-  Registry and Winlogon Logs

If winlogon.log does not provide enough information, you may consider increasing the level of detail in the log or looking at other relevant registry entries. Note, however, that direct modification of the registry can be risky, so make sure you know what you're doing or back up the registry before making changes.

Another possible tool is Process Monitor (from the Sysinternals suite), which captures all registry accesses and system calls related to winlogon.

6 Upgrading or patching the server

If possible, consider updating Windows Server 2016 and 2019 systems to the latest patch level. This can address known security and compatibility issues.

Best regards

Neuvi
