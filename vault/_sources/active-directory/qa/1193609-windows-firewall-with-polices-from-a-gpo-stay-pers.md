---
title: "Windows Firewall with polices from a GPO - Stay persistent with firewall disabled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1193609/windows-firewall-with-polices-from-a-gpo-stay-pers
question_id: 1193609
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# Windows Firewall with polices from a GPO - Stay persistent with firewall disabled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1193609/windows-firewall-with-polices-from-a-gpo-stay-pers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Since the 1st of February, we have observed a new behaviour within an On-Prem AD and Windows 10. (After Patch Tuesday 31st Jan).

For any GPO defined with setting:

Computer Configuration/Policies/Windows settings/Security Settings/Windows Defender Firewall with Advanced Security

Regardless of state for the windows firewall, these GPO policies will persist.

I.e, even if the firewall is disabled via the GUI. Windows will keep applying any rules defined via GPO's.

Is this a bug or a feature?

Removing any mis-configured rules in this scenario can be difficult.

Any GPO rule can be found using Get-NetFirewallRule, the Name field will be a GUID and the DisplayName will be a user recongisable string.

They will have PolicyStoreSourceType GroupPolicy.

Remove-NetFirewallRule will not work with these rules.

Such that, I created a new policy to block some UDP traffic. The wizard had a target port input, but somehow lost that value. Thus it started to block all outgoing UDP traffic.

As a result, the AD server could not be reached to refresh the disabled GPO.

Resolution - To remove a Windows firewall rule from this scenario, the "Name" variable from the Get-NetFirewallRule needs to be removed from HKLM:\SOFTWARE\Policies\Microsoft\WindowsFirewall

I.e: Remove-ItemProperty  "HKLM:\SOFTWARE\Policies\Microsoft\WindowsFirewall\FirewallRules" -Name "{BC5EF541-FE5D-48C9-B941-1CAFA967471C}"

Then reboot the machine to take effect.

In my situation, I was fortunate enough that I could still open a PS-Session onto the affected machines.

Additionally - In a scenario where a AD server can't be reached. What tools can a sysadmin use to nuke out a policy without talking to the AD?

## Answer (community) — community member

*upvotes: 1 · updated: 2023-03-28*

Hello there,

A couple of things come to mind here:

-  Are you sure that you modified the correct GPO object? If the settings are still being applied it could be that you've got one or more GPOs still applying the setting in question.

2.Could an issue with replication latency. If the DC on which you modified the GPO setting hasn't fully replicated your changes, it could be that the client is picking up the older settings from a different DC

I suspect that after you deleted the GPO, the registry settings it had set didn't go nowhere. To check this, see HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall<all subkeys>|EnableFirewall in registry on a workstation (should be absent).

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer--
