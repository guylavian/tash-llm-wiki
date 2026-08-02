---
title: "Deploy Windows Server Update Services"
type: reference
domain: windows-server
slug: administration-deploy-windows-server-update-services
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-server-update-services/deploy/deploy-windows-server-update-services
family: administration
documentKind: "how-to"
abstract: "Windows Server Update Service (WSUS) topic - An overview of the deployment process with links to the four steps to accomplish it"
---

# Deploy Windows Server Update Services

# Deploy Windows Server Update Services



Windows Server Update Services (WSUS) enables information technology administrators to deploy the latest Microsoft product updates. WSUS is a Windows Server server role that can be installed to manage and distribute updates. A WSUS server can be the update source for other WSUS servers within the organization. The WSUS server that acts as an update source is called an upstream server.

In a WSUS implementation, at least one WSUS server in the network must connect to Microsoft Update to get available update information. You can determine, based on network security and configuration, how many other servers connect directly to Microsoft Update.

This guide provides conceptual information for planning and deploying Windows Server Update Service.

-   [Plan your WSUS deployment](../plan/plan-your-wsus-deployment.md)

-   [Step 1: Install the WSUS Server Role](1-install-the-wsus-server-role.md)

-   [Step 2: Configure WSUS](2-configure-wsus.md)

-   [Step 3: Approve and Deploy Updates in WSUS](3-approve-and-deploy-updates-in-wsus.md)

-   [Step 4: Configure Group Policy Settings for Automatic Updates](4-configure-group-policy-settings-for-automatic-updates.md)
