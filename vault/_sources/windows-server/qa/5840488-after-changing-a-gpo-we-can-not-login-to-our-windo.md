---
title: "After changing a GPO we can not login to our windows server 2022 dc"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5840488/after-changing-a-gpo-we-can-not-login-to-our-windo
question_id: 5840488
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
answer_author_roles: ["Independent Advisor"]
---
# After changing a GPO we can not login to our windows server 2022 dc

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5840488/after-changing-a-gpo-we-can-not-login-to-our-windo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

By adopting this policy reccomended by defender we are locked out from our domain controller

Need remediation urgently

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-03-27*

Hello Merkouris Bouchlas,

What has happened here is that the GPO you applied contained a security baseline setting that directly impacted logon capability on the domain controller. Microsoft Defender baselines often include policies such as “Deny log on locally” or “Deny log on through Remote Desktop Services” for certain groups, or restrictive User Rights Assignments that inadvertently block administrators from signing in. Once that policy is applied to the DC, you can be locked out entirely.

The immediate remediation is to access the domain controller in Directory Services Restore Mode (DSRM). Reboot the server, press F8, and choose DSRM. Log in with the DSRM password you set when promoting the DC. From there, you can either disable the problematic GPO or edit the SYSVOL copy of the policy. Another option is to boot into Safe Mode with Networking, log in with the DSRM account, and use gpmc.msc or regedit to roll back the change. If you have another domain controller that is still accessible, you can also modify or delete the GPO from that system, and replication will remove the lockout policy from the affected DC.

If you cannot access Group Policy Management, you can manually move or rename the GPO folder under \<domain>\SYSVOL<domain>\Policies{GUID} so that it no longer applies. Once the DC reboots, it will stop enforcing the locked policy. After regaining access, carefully re‑apply the Defender baseline but exclude the settings that deny interactive or RDP logon for administrators.

In short, you need to use DSRM or Safe Mode to bypass the GPO enforcement, then roll back or delete the offending policy. This is the supported way to recover from a lockout caused by GPO misconfiguration on a domain controller.

I hope you've found something useful here. If it helps you get more insight into the issue, it's appreciated to accept the answer. Should you have more questions, feel free to leave a message. Have a nice day!

Domic Vo.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-03-27*

Because the exact Defender-recommended GPO setting is not specified, only general, supported recovery options from the context can be provided.

If the GPO change has locked out sign-in to the domain controller (for example, by breaking authentication or Netlogon behavior), the practical remediation is to prevent the problematic policy from applying to the DC long enough to revert it.

Use one of these approaches:

-  Boot the DC so the GPO does not apply

-  If the DC is a virtual machine, start it in an isolated network (no connection to the production domain network) so it cannot contact a writable DC or SYSVOL share to refresh Group Policy.

-  Sign in using cached credentials or local Administrator (if available).

-  In Group Policy Management, unlink or disable the GPO that was changed, or move the DC computer object to an OU where the GPO does not apply.

-  Force a policy update (`gpupdate /force`) and then reboot the DC back on the production network.

-  Stop Netlogon before shutting down/restarting during remediation

-  If the DC is still reachable but authentication is unstable, stopping Netlogon before shutdown can reduce further authentication issues while recovering:

-  On the DC, run: `net stop netlogon && net stop kdc` before reboot.

-  Optionally, configure this as a shutdown script in Local Group Policy so it runs automatically:

-  Run `gpedit.msc` on the DC.

-  Go to Computer Configuration > Windows Settings > Scripts > Shutdown.

-  Add a script with the command: `net stop netlogon && net stop kdc`.

-  After stabilizing, revert or adjust the offending GPO and then remove this temporary shutdown script.

-  Revert password or security policies if they broke DC authentication

-  If the change was to password policy or a security option that affects DC authentication (for example, Netlogon or NTLM restrictions), revert those settings in the Default Domain Policy or in the GPO linked to the Domain Controllers OU:

-  Ensure password and account policies are correctly set in Default Domain Policy, not in conflicting GPOs linked to the Domain Controllers OU.

-  If Block Policy Inheritance is enabled on the Domain Controllers OU, clear it so the domain-level policy (with working settings) applies again.

-  After adjusting, run on the DC: `secedit /refreshpolicy machine_policy /enforce`.

-  If the change was related to Netlogon / “Allow vulnerable Netlogon secure channel connections”

-  If Defender recommended tightening Netlogon secure channel behavior and the DC is now denying accounts:

-  Confirm that the DC has successfully applied and replicated the intended GPO configuration:

-  On the DC, run `gpupdate /force`.

-  Then run `gpresult /h c:\gpresult.html` and review which GPOs are applied and what settings are in effect.

-  If a specific group was configured in Domain controller: Allow vulnerable Netlogon secure channel connections, verify that:

-  Group membership has replicated to the DC that is denying connections.

-  The GPO containing the setting has replicated and is applied on that DC.

-  If necessary, temporarily relax or remove the restrictive Netlogon setting in the GPO, force replication, and then re-apply a corrected configuration.

-  If still locked out or no admin access is possible

-  If no administrative sign-in is possible on any DC after the GPO change, direct assistance from Microsoft Support is required. A support engineer can work with the environment (for example, via Directory Services Restore Mode or offline GPO editing) to roll back the change.

Once access is restored, review Defender’s recommendation and re-implement it in a staged manner:

-  Test on a non-production OU or lab domain first.

-  Apply to a subset of DCs and verify authentication, Netlogon, and Group Policy behavior.

-  Only then roll out broadly.

References:

-  Changes are not applied when you change the password policy

-  How to manage the changes in Netlogon secure channel connections associated with CVE-2020-1472

-  Domain members fail authentication when domain controller is shut down
