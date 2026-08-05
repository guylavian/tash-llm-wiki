---
title: "Cannot create software deploy GPOs in domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185612/cannot-create-software-deploy-gpos-in-domain
question_id: 2185612
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# Cannot create software deploy GPOs in domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185612/cannot-create-software-deploy-gpos-in-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I just took on IT management of a site, and am having difficulty deploying our remote management software throughout the domain via a GPO.  I keep getting error codes %%1603 and %%2.  I have confirmed that the security settings on the files in question are shared and accessible by the system and domain admin accounts.  I can also manually run that installer from its shared directory on an endpoint, but the GPO continues to fail.

Stuck...

## Answer (community) — community member

*upvotes: 1 · updated: 2023-09-27*

Hello Cole Renfroe,  

Thank you for posting in Microsoft Community forum.  

1.Ensure your installer package is .msi file.  

2.You can use Computer Configuration*Software Settings**Software installation* to assign a package OR use User Configuration*Software Settings**Software installation* to publish a package.  

For more information and detailed steps, please read information in the link below.  

Use Group Policy to remotely install software  

Use Group Policy to remotely install software - Windows Server | Microsoft Learn  

After you deploy software installation via GPO, you can restart the client machines two or three times to make GPO take effect.  

And you can also check if GPO takes effect using steps below.  

For checking Computer Configuration within gpresult, we can follow steps below.  

Logon this machine using administrator account.

Open CMD (run as Administrator).

Type gpresult /h C:\gpo.html and click Enter.

Open gpo.html and check gpo setting under "Computer Details".

For checking User Configurations within gpresult, we can follow steps below.

Logon the machine using normal domain user account.

Create a folder named F1.

Open CMD (do not run as Administrator).

Type gpresult /h C:\F1\gpo.html and click Enter.

Open gpo.html and check gpo setting under "User Details".

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-06*

Hello Cole Renfroe,  

Thank you for your reply.  

Does the problem occur on only one machine or all the machines in the OU?  

You can try to troubleshoot based on the link below.  

MSI installation error 1603 - Windows Server | Microsoft Learn  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-28*

Created a computer policy software deploy GPO pointed at a publicly accessible network share with the .msi file in question.  No transform file is needed, so this is a pretty straightforward policy.  Other than it is set to uninstall the software when the policy no longer applies to an AD object.

When I restart or even run gpresult /sync, the machine says its applying the policy during windows OS bootup.  The software doesnt end up getting installed though, so in the windows event viewer I look up the application of that GPO and it retuns that it failed with error code %%1603.  I have occasionally seen error %%2 in those event logs.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-28*

Hello Cole Renfroe,  

Thank you for your reply.  

1.Where did you see "error codes %%1603 and sometimes %%2"?  

Would you please describe the detailed steps that you deployed the software installation GPO?  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-27*

I have confirmed the GPO is applying to the machines.  It is going in under the computer policy side of the GPO structure.  I am getting error codes %%1603 and sometimes %%2.  

Package is an .msi file as well.  Computers have been restarted many dozens of times with the same error codes in the event log, never successfully running the .msi installer.
