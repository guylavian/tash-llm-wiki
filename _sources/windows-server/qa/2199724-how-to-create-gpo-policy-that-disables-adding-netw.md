---
title: "How to create GPO policy that disables adding network drives to workstations"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199724/how-to-create-gpo-policy-that-disables-adding-netw
question_id: 2199724
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# How to create GPO policy that disables adding network drives to workstations

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199724/how-to-create-gpo-policy-that-disables-adding-netw (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Need help creating GPO policy that disables adding network drives to workstations.

## Answer (community) — community member

*upvotes: 3 · updated: 2023-03-01*

Hi Mateusz,

I am Mario and I am a independent advisor, and I would like to help you.

Here are the steps to create a GPO policy that disables adding network drives to workstations:

1-Open the Group Policy Management Console on your domain controller.

2- Navigate to the Group Policy Objects folder in the domain that you want to apply the policy to.

3-Right-click on the folder and select "Create a GPO in this domain, and Link it here..." 

4- Name the GPO something like "Disable Adding Network Drives".

5- Right-click on the new GPO and select "Edit".

6- In the Group Policy Management Editor, navigate to "User Configuration" > "Administrative Templates" > "Windows Components" > "File Explorer".

7- Find and double-click on the "Remove "Map Network Drive" and "Disconnect Network Drive"" policy.

8- Select the "Enabled" option, and click "OK".

9- Close the Group Policy Management Editor and link the GPO to the appropriate Organizational Unit or Security Group in Active Directory.

10- Wait for the Group Policy to replicate across your domain, or force replication using the command "gpupdate /force" on the client workstation.

After this policy is applied, users will no longer be able to add new network drives to their workstations using the "Map Network Drive" or "Disconnect Network Drive" options.

Hope this can help you solving the issue.

Is there anything else I can help you with?

Best regards,

Mário
