---
title: "WinRM issue on Domain Controller - no access to remote execute PowerShell script"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4104811/winrm-issue-on-domain-controller-no-access-to-remo
question_id: 4104811
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# WinRM issue on Domain Controller - no access to remote execute PowerShell script

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4104811/winrm-issue-on-domain-controller-no-access-to-remo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've created a script that self-provisions a virtual server on behalf of a user, that script at the end calls a remote script on the domain controller to handle the rebooting of the device, and manage the device while its rebooting (because Restart-Computer -Wait doesn't work).

Once the machine finishes restarting, the domain controller invokes other scripts on it to install the software required for that particular build.

Now, I previously had everything working, except the acquisition of files from the domain controller's share (back on the target machine). For all I can understand, the "double-hop" was causing issues with using credentials and accessing the PSDrive that's mapped using the set up credential object in the script. Copy-Item wouldn't work with just providing the network path and a credential to access the path (dumb in itself).

So, following several "solutions" to the "double-hop" issue is to enable CredSSP and allow the sharing of credential objects. This was all configured, and now the first hop doesn't work, I simply receive the following error message:

"The WinRM client sent a request to an HTTP server and got a response saying the requested HTTP URL was not available. This is usually returned by a HTTP server that does not support the WS-Management protocol."

This is the simple piece of script that no longer works:

$user = "domain\admin"

[securestring]$secStringPassword = ConvertTo-SecureString "password" -AsPlainText -Force

[pscredential]$cred = New-Object System.Management.Automation.PSCredential ($user, $secStringPassword)

$session = New-PSSession -Name Session -ComputerName NASEC-DC-01 -Credential $cred

I'm executing this locally while logged onto the first machine, trying to hit the domain controller, and I get absolutely nothing - no session, no mapped drives - nothing.

What does the error message actually mean? What is it I need to check to fix this?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2023-08-11*

Good day Steven! I am glad to be able to provide assistance to you today. I would suggest to post this query to our neighbor forum from the link below as this is best suited in there. They are more oriented on with regards to this type queries/issues and there will be IT Pros/System Admins/Server Admins/AD Admins who are available that will be able to fulfill your query out there.

https://learn.microsoft.com/en-us/answers/

Regards,

Paul R.
