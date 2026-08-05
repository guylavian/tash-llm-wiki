---
title: "secondary domain controller recovery"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/466145/secondary-domain-controller-recovery
question_id: 466145
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# secondary domain controller recovery

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/466145/secondary-domain-controller-recovery (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am running two domain controllers in my network. One domain controller is primary domain controller holding all the FSMO roles and the other one is secondary domain controller. My secondary domain controller crashed and then I recovered that secondary domain controller using the non-authoritative backup restore. Now the problem is that when I restarted the domain controller after recovery, it was unable to login and was giving the error “the domain controller lost trust relationship with the primary". Can anybody help me how can I solve the problem and make my secondary domain controller up and running?  

Thanks and Regards

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-08*

Hello @Syed Ammar Haider  ,

Thank you for posting here.

For your issue, you can try the following steps to see if it helps.

1-If the secondary domain controller is a virtual machine, disable the Network card.
If the secondary domain controller is a physical machine, unplug the network cable.

2-Logon the secondary domain controller using cached domain Administrator.

3-Enable the network card if it is virtual machine or plug the network cable if it is physical machine.

4-Opem CMD (run as Administrator).

5-Run the command below on the secondary DC.

Netdom resetpwd /s:target_server /ud:mydomain\domain_admin /pd:*

In your case, target_server is the first DC (PDC) name.

/s:server is the name of the domain controller to use for setting the machine account password. This is the server where the KDC is running.
/ud:domain\User is the user account that makes the connection with the domain you specified in the /s parameter. This must be in domain\User format. If this parameter is omitted, the current user account is used.
/pd: specifies the password of the user account that is specified in the /ud parameter. Use an asterisk () to be prompted for the password.

For more information above reset machine account passwords of a Windows Server domain controller, please refer to link below.
Use Netdom.exe to reset machine account passwords of a Windows Server domain controller
https://learn.microsoft.com/en-US/troubleshoot/windows-server/windows-security/use-netdom-reset-domain-controller-password

If it works above (I mean you can run the command successfully), then sign out and sign in again using domain administrator to see if there is no error message.

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,
Daisy Zhou

============================================
If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-08*

Thanks for the reply, I got your point. But if I should not restore a domain controller in a multi-dc environment, then what is the purpose of "windows server backup utility"??
