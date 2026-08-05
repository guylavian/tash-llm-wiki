---
title: "Create A GPO to disable USB Storage Devices"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198881/create-a-gpo-to-disable-usb-storage-devices
question_id: 2198881
fetched: 2026-07-25
answer_count: 10
has_accepted_answer: false
upvotes: 20
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# Create A GPO to disable USB Storage Devices

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198881/create-a-gpo-to-disable-usb-storage-devices (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Create A GPO to disable USB Storage Devices.

Hi All, newly setup environment.  ON prem AD syncing to AAD 

I need block access to all USB Removable storage devices but allow some users to have access.

My idea is to create the policy and link it to the computers OU, then under the policy delegation add a security group with users and deny the "Apply Group Policy." to that group. So, they will be exempt from the policy.

By doing this, if a user that has been assigned access via that group, logs in to any workstation, they will have access to USB Storage?

Even though the policy is assigned to workstations.

Keeping in mind of allowing all other peripherals like Keyboard, mouse for all users , just blocking storage devices

Thank you.

Desigan

## Answer (community) — community member

*upvotes: 7 · updated: 2023-12-08*

Hello Desigan Reddy,

To create a GPO to disable USB storage devices, you can follow these steps:

-  Open the Group Policy Management Console (GPMC) and create a new GPO.

-  Name the GPO and link it to the appropriate OU.

-  Navigate to Computer Configuration > Policies > Administrative Templates > System > Removable Storage Access.

-  Double-click on "Removable Disks: Deny execute access" and select "Enabled."

-  Click on "OK" to save the changes.

-  Double-click on "Removable Disks: Deny read access" and select "Enabled."

-  Click on "OK" to save the changes.

-  Double-click on "Removable Disks: Deny write access" and select "Enabled."

-  Click on "OK" to save the changes.

-  Close the Group Policy Management Editor.

-  Apply the GPO to the appropriate OU.

Regarding your question about allowing some users to have access to USB storage, you can create a security group and add the users who need access to it. Then, you can deny the "Apply Group Policy" permission to that group in the GPO delegation settings. This will exempt those users from the policy and allow them to access USB storage devices.

I hope this helps! Let me know if you have any further questions.

Best regards,

Qiuyang

## Answer (community) — community member

*upvotes: 2 · updated: 2023-12-08*

Hello Desigan Reddy,

Yes, you can attach the group policy to the Computers OU to apply it to all computers in that OU. And for the exclusions, you can create a security group and add the users you want to exclude, then deny the "Apply Group Policy" permission for that group in the Delegation tab of the Group Policy Management Console. Let me know if you have any other questions or concerns!

Best regards,

Qiuyang

## Answer (community) — community member

*upvotes: 1 · updated: 2024-01-08*

Hi Quiyang

I have created the policy and attached it to a test OU with 2 x users

It does work. I did create a global security group - added users and denied the policy from inheriting but after reboot and gpudate /force - still do not have access to USB

See attached - Can you guide where I am going wronfg

Once I can resolve then will apply it to all computers instead of users![](https://learn-attachment.microsoft.com/api/attachments/9a4da2a2-5a9f-4934-82b9-ef30103ecefe?platform=QnA

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-08*

Much Appreciated, thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-08*

Hi Qiuyang Xi

Thank you for that. So I should attach the group policy to the computers OU? 

Then for the exclusions, I add users to a security group and deny the "Apply Group Policy" permission.

Thank you
