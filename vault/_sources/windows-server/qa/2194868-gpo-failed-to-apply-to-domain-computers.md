---
title: "GPO failed to apply to domain computers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194868/gpo-failed-to-apply-to-domain-computers
question_id: 2194868
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# GPO failed to apply to domain computers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194868/gpo-failed-to-apply-to-domain-computers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've created a policy on GPO to block usb device for all domain users but it's not worked with some PCs. It seems like the policy couldn't apply to those PCs. Please help me to find the solution for this issue. Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2025-02-19*

Hello

The following is a collection of problems currently being experienced by other users online.

It sounds like you're having trouble with Group Policy not being applied to some domain computers, specifically the policy to block USB devices. There are several reasons why this could be happening, and here are some steps you can follow to troubleshoot and resolve the issue:

-  Verify GPO is Linked and Applied Correctly

Check GPO Link: Ensure that the GPO is linked to the correct Organizational Unit (OU) where the target computers reside.

Open Group Policy Management and verify that the GPO is applied to the correct OU or domain.

GPO Scope: Confirm that the security filtering on the GPO allows the intended computers or users to apply it. The default security filtering is usually set to apply to "Authenticated Users," but check to ensure it's not restricted to a specific group.

-  Force a Group Policy Update

On the problematic computers, run the following commands in Command Prompt (Run as Administrator):

gpupdate /force

gpresult /h gpresult.html  

This will generate a report of the Group Policy application. Check the generated gpresult.html file to see if there are any issues or errors.

You can also try restarting the affected machines to see if that resolves the issue.

-  Check Group Policy Processing

Event Logs: Check the Event Viewer on the affected PCs for any Group Policy errors. Look under Applications and Services Logs > Microsoft > Windows > GroupPolicy > Operational. This will give you detailed information on whether the policy is being applied or not.

Resultant Set of Policy (RSoP): You can also run Resultant Set of Policy (RSoP) on the affected machines:

Open Run and type rsop.msc.

This will show you the policies that are applied to the machine. Check if your USB block policy is listed.

-  Ensure the Policy Settings Are Correct

Double-check the settings in the GPO. For blocking USB devices, it might look like this:

Computer Configuration > Policies > Administrative Templates > System > Removable Storage Access

Set All Removable Storage classes: Deny all access to Enabled.

Verify that the policy is Enabled and not just Not Configured.

-  Group Policy Inheritance

Ensure that there are no conflicting policies that might be overriding the USB-blocking policy. Sometimes, settings in higher-level OUs (like the domain or parent OUs) can override child OU settings.

Group Policy Inheritance: Right-click the GPO in Group Policy Management and choose Group Policy Inheritance. This will show if other policies are overriding your USB block policy.

-  Check for Windows Firewall or Antivirus Interference

Some third-party antivirus software or Windows Defender may interfere with the application of GPOs or the enforcement of device control policies.

Temporarily disable the antivirus/firewall on the affected PCs and see if the policy gets applied after a reboot.

-  Check for GPO Processing Issues (Network Issues)

Sometimes GPOs fail to apply due to network issues, DNS problems, or issues with Active Directory replication. Ensure that the affected PCs can properly reach the domain controller, and that DNS is resolving correctly.

Check if Active Directory replication is occurring as expected.

-  Check GPO Permissions

Ensure that the Group Policy permissions for the GPO are set up properly and that the computers have permission to read and apply the policy.

Right-click on the GPO in Group Policy Management and select Edit.

Go to Delegation tab and make sure Authenticated Users or the specific computer group has the correct permissions.

I hope the above information is helpful to you.

Best regards

Runjie Zhai

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-25*

Hello LAM TUNG DINH,

Thank you for posting in Microsoft Community forum.

1.What specific GPO settings did you configure? Under user configuration or computer configuration?  

2.Where did you link this GPO?

If you link this GPO to OU with domain user objects and you configure user GPO settings, you should add the domain user objects to this OU.

If you link this GPO to OU with domain computer objects and you configure computer GPO settings, you should add the domain computer objects to this OU.

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
