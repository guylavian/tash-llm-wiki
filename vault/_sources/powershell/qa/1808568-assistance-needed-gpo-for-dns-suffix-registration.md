---
title: "Assistance Needed: GPO for DNS Suffix Registration Not Applying"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1808568/assistance-needed-gpo-for-dns-suffix-registration
question_id: 1808568
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Assistance Needed: GPO for DNS Suffix Registration Not Applying

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1808568/assistance-needed-gpo-for-dns-suffix-registration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We are working on creating a Group Policy to automatically enable the option "Use this connection's DNS suffix in DNS registration" when users log in to their domain accounts.

We have created the GPO for this setting and tested it on one machine, but it is not applying as expected. Could you please assist us in troubleshooting this issue?

BR,

FirozDNS Suffix registration.PNG

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-11*

Hello Firoz Khan,  

Thank you for posting in Q&A forum.  

Do you configure the GPO settings below?

`Computer Configuration` -> `Policies` -> `Administrative Templates` -> `Network` -> `DNS Client` ->Register DNS records with connection-specific DNS suffix.

If so, you can follow these steps: 

1.Open the Group Policy Management Console (GPMC) on your Windows Server. 

2.Create a new Group Policy Object (GPO) or edit an existing GPO that is linked to the organizational unit (OU) or domain with AD computer objects. 

3.Navigate to: `Computer Configuration` -> `Policies` -> `Administrative Templates` -> `Network` -> `DNS Client` 

4.Look for the setting named Register DNS records with connection-specific DNS suffix. 

5.Double-click on this setting to configure it. Set it to Enabled. 

6.Click OK, and then close the Group Policy Management Editor. 

7.Apply the GPO to the appropriate OU or domain if it’s not already linked. 

This will configure the DNS client settings on the target computers to use the connection-specific DNS suffix in DNS registration. Remember that it can take a little time for Group Policy updates to propagate to all affected machines. You can force an immediate update by running `gpupdate /force` on a target machine.

After you configure all the setting above, you can check if the GPO is applied.

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
