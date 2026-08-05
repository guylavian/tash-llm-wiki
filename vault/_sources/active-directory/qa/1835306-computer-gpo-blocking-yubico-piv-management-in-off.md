---
title: "Computer GPO blocking Yubico PIV management in offline AD domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1835306/computer-gpo-blocking-yubico-piv-management-in-off
question_id: 1835306
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Computer GPO blocking Yubico PIV management in offline AD domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1835306/computer-gpo-blocking-yubico-piv-management-in-off (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!   

I manage a small Windows Server 2022 AD on premise domain, which is completely detached from the outside network since March. 

I set up PIV logon to be required by all users in the domain, using user personal and root certificates residing in a personal assigned Yubikey 5. Everything was working well aside from the auto-enrollment policy to allow users to obtain certificate via domain policies. 

Some days ago nobody was able to login to the domain anymore. And despite confusing logs I thought my password policy configuration triggered password renewals for all users. Most of the users, never had to use their password to login into Windows clients, so most of them forgot and/or confused the domain account password with the smart card PIN. Now some of the SC are blocked, accounts as well but since certificates are not expired one administrator account that had no expiring password policy is still able to login to the PDC.I have no problem resetting users, psw and SC, but currently I am unable to run any certutil -sc commands. Whenever it requires a pin to be entered outside the windows logon scenario, the prompt for PIN fails saying "The operation is not permitted due to Computer Policy configuration".  

I am trying to troubleshoot this, but having difficulties since the amount of different policies configured and lack of experienced seniors. Could help me pointing out policy settings that can be responsible for this behavior? General tips and/or guides on how to correctly configure this SC logon are very welcomed. My configuration is based on Yubico and Microsoft Learn documentation.

I will provide more details if needed but since it's completely offline it could be difficult to exfiltrate logs.

Thank you very much in advance.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-23*

Hello Federico Gentile,  

Thank you for posting in Q&A forum.

Based on the description, I understand you set up PIV logon to be required by all users in the domain, but now nobody was able to login to the domain anymore. Now one administrator account that had no expiring password policy is still able to login to the PDC. Now you are unable to run any certutil -sc commands.

Based on the description "Whenever it requires a pin to be entered outside the windows logon scenario, the prompt for PIN fails saying "The operation is not permitted due to Computer Policy configuration".", you can try to export computer configurations on problematic machine (see steps below) and try to check the related /corresponding GPO settings (I'm sorry, I can't know the specific policy settings directly, but you can try to find the relevant policy on the machine in question).  

Meanwhile, what do you mean "outside the windows logon scenario"? Maybe there are Computer Policy settings to block to use PIN when it is not Windows logon scenario.

For checking Computer Configuration within gpresult, we can follow steps below.

Logon this machine using administrator account.

Open CMD (run as Administrator).

Type gpresult /h C:\gpo.html and click Enter.

Open gpo.html and check gpo setting under "Computer Details".

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
