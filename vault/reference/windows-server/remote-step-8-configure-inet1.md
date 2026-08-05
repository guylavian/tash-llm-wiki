---
title: "STEP 8 Configure INET1"
type: reference
domain: windows-server
slug: remote-step-8-configure-inet1
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/remote/remote-access/directaccess/tlg-multisite/STEP-8-Configure-INET1
family: remote
documentKind: "how-to"
abstract: "Learn how to configure a DNS entry for 2-EDGE1 on INET1."
---

# STEP 8 Configure INET1

# STEP 8: Configure INET1

To enable client computers to connect to Remote Access servers over the Internet, you must configure a DNS entry for 2-EDGE1 on INET1.

### To create the 2-EDGE1 DNS entry

1.  On the **Start** screen, type**dnsmgmt.msc**, and then press ENTER.

2.  In the console tree, open **Forward Lookup Zones**, click **contoso.com**, then right-click **contoso.com**, and then click **New Host (A or AAAA)**.

3.  In **Name**, type **2-EDGE1**. In **IP address**, type **131.107.0.20**. Click **Add Host**, click **OK**, and then click **Done**.
