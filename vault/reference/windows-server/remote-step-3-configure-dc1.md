---
title: "STEP 3 Configure DC1"
type: reference
domain: windows-server
slug: remote-step-3-configure-dc1
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/remote/remote-access/directaccess/tlg-otp-securid/STEP-3-Configure-DC1
family: remote
documentKind: "how-to"
abstract: "Learn how to verify that User1 has a User Principal Name defined on DC1."
---

# STEP 3 Configure DC1

# STEP 3 Configure DC1

DC1 acts as a domain controller, DNS server, and DHCP server for the corp.contoso.com domain. Configure DC1 as follows:

## Verify User1 has a User Principal Name defined on DC1

1.  On DC1, open Server Manager, and click **AD DS** in the left pane. Right-click **DC1** and select **Active Directory Users and Computers**. In the left pane expand **corp.contoso.com\Users**, and double-click User1.

2.  On the **Account** tab verify that **User logon name** is set to User1. If not, then enter **User1** in the **User logon name** field.

3.  Click **OK**. Close the **Active Directory Users and Computers** console.
