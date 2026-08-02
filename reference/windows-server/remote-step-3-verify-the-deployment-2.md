---
title: "Step 3 Verify the Deployment"
type: reference
domain: windows-server
slug: remote-step-3-verify-the-deployment-2
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/remote/remote-access/ras/manage-remote-clients/install/Step-3-Verify-the-Deployment_2
family: remote
documentKind: "how-to"
abstract: "Learn how to verify that you've correctly configured your deployment for remote management of DirectAccess clients."
---

# Step 3 Verify the Deployment

# Step 3 Verify the Deployment

This article describes how to verify that you've correctly configured your deployment for remote management of DirectAccess clients.

## To verify proper deployment

1. Connect a DirectAccess client computer to the corporate network and obtain the Group Policy Object.

1. On the client computer, select the **Network connections** icon in the notification area to access the DirectAccess Media Manager.

1. Select **DirectAccess Connection**. You'll see that the status is **Locally Connected**.

1. Remove the computer from the corporate network and connect it to a public network.

1. In the command prompt, type **nltest /dsgetdc: [fully qualified domain name]**. This command verifies that the corporate network is accessible to the client. If the domain controller isn't accessible, the error message ERROR_NO_SUCH_DOMAIN will display, reporting that the domain doesn't exist.
