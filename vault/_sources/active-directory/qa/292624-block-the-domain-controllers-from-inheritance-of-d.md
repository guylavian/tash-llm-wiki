---
title: "block the domain controllers from inheritance of domain password policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/292624/block-the-domain-controllers-from-inheritance-of-d
question_id: 292624
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# block the domain controllers from inheritance of domain password policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/292624/block-the-domain-controllers-from-inheritance-of-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello MSFT,  

I have a question about domain password policy. I've learned that the domain password policy can be only configured at the domain level if you need to apply the policy to the domain user accounts. However Group Policy is executed by a domain controller with the role of PDC emulator. Here's the thing, if I block the domain controllers from inheritance, the domain password policy cannot be applied to the domain computers and domain users. In this case, is there a solution or workaround?  

By the way, is fine-grained password policy executed by PDC emulator server as well?  

Thanks in advance.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-02*

Hi FanFan,    

Thank you for the info but I think you didn't understand my questions. First of all, password policy is a part of Group Policy. And Group Policy is stored at SYSVOL folder, which will be copied to the PDC emulator server before distributing to the domain computers. So if I block the domain controllers from inheritance of GP/password policy/default domain policy at the domain level, the password policy won't be copied to the PDC emulator server. (At least in my test environment, it works like this.)     

Secondly, password policy at the OU level cannot be applied to domain users.     

    

    

So if the domain controllers is blocked from inheritance of the password policy, is there a workaround to apply the password policy to the domain computers? If FGPP is not distributed by PDC emulator server, I think it could be a workaround.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-02*

Hi,    

The password policy from the default domain policy is enforced by the domain , it means that the password can't be blocked.    

The password policy is a computer policy, all the PCs in the domain will apply the policy. This means that all the users logon to the PCs within the domain will apply the password policy.    

If you deploy the  fine-grained password policy for the specific users and groups, the fgpp will be executed .But  fine-grained password policy can't be only deployed to users and  global groups.    

For more information you can refer to :    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/account-policies    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-policy    

Best Regards,
