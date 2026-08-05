---
title: "how to deploy exe through GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5825037/how-to-deploy-exe-through-gpo
question_id: 5825037
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
answer_author_roles: ["Independent Advisor"]
---
# how to deploy exe through GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5825037/how-to-deploy-exe-through-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

how to deploy .exe through GPO to all clients, i want to push Trend Micro Agent that is in .exe with supporting folder and applications

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-03-17*

Hello,

Deploying a `.exe` installer like the Trend Micro Agent through Group Policy is not straightforward because GPO natively supports MSI packages for software installation under Computer Configuration → Policies → Software Settings → Software Installation. An `.exe` cannot be directly pushed in the same way. If you attempt to assign or publish an `.exe` via GPO, it will fail because Windows Installer service expects MSI metadata.

The correct approach is either to obtain the MSI version of the Trend Micro Agent from the vendor (Trend Micro usually provides MSI packages for enterprise deployment) or to wrap the `.exe` into an MSI using a repackaging tool such as Advanced Installer, WiX, or Microsoft’s Orca. Once you have an MSI, you can place it in a shared folder with read permissions for `Domain Computers` and then configure the GPO to install it at startup.

If you must deploy the `.exe` directly, the supported method is to use a GPO startup script. Place the `.exe` and its supporting folder on a network share, then configure a startup script under Computer Configuration → Windows Settings → Scripts (Startup/Shutdown). The script should call the installer silently with the appropriate command-line switches, for example:

Code

```
\\server\share\TrendMicroAgent\setup.exe /silent /norestart
```

Make sure the installer supports silent installation parameters; Trend Micro documentation specifies which switches are valid. The script runs under SYSTEM context, so the share must allow access for machine accounts.

I hope you've found something useful here. If it helps you get more insight into the issue, it's appreciated to accept the answer. Should you have more questions, feel free to leave a message. Have a nice day!

Domic Vo.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-03-16*

Group Policy software installation natively supports MSI packages, not arbitrary EXE installers. To deploy a Trend Micro EXE with supporting folders, use one of these approaches:

-  Repackage or obtain an MSI

-  Check whether Trend Micro provides an MSI-based installer for the agent.

-  If available, place the MSI on a network share (distribution point) and deploy it via GPO as assigned software:

-  Create a shared folder on a server and copy the MSI there. Ensure clients have read access.

-  In Active Directory Users and Computers, right-click the domain → Properties → Group Policy tab.

-  Create a new GPO or edit an existing one.

-  Under Computer Configuration → Software Settings → Software installation, right-click Software installation → New → Package.

-  In the Open dialog, type the full UNC path to the MSI (for example, `\\server\share\trendmicroagent.msi`). Do not use Browse.

-  Select Assigned → OK.

-  Close the editors. The agent installs when client computers start.

-  Use a startup script GPO for the EXE
   If only an EXE is available, use a computer startup script in a GPO to run the EXE from a network share or copied local folder. Typical pattern:

-  Create a share containing the EXE and its support folders.

-  Write a batch/PowerShell script that:

-  Copies the EXE and required folders locally (optional but recommended).

-  Runs the EXE silently with the vendor’s supported command-line switches.

-  Assign the script as a Computer Configuration → Windows Settings → Scripts (Startup) script in a GPO linked to the target OU.

-  Use Configuration Manager instead of pure GPO
   For more complex EXE deployments with supporting folders, Microsoft Configuration Manager is recommended. It can:

-  Distribute EXE installers and content folders.

-  Run custom command lines.

-  Handle retries, detection logic, and reporting.

If Trend Micro provides an MSI wrapper or transform, prefer method 1 so that deployment integrates cleanly with Group Policy’s software installation feature.

References:

-  Use Group Policy to remotely install software

-  Assign a package

-  Create a Group Policy Object

-  How to deploy clients to Windows computers in Configuration Manager
