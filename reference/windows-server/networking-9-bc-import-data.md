---
title: "Import Data Packages on the Hosted Cache Server (Optional)"
type: reference
domain: windows-server
slug: networking-9-bc-import-data
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/networking/core-network-guide/cncg/bc-hcm/9-Bc-Import-Data
family: networking
documentKind: "how-to"
abstract: "Learn how to import data packages and preload content on your hosted cache servers."
---

# Import Data Packages on the Hosted Cache Server (Optional)

# Import Data Packages on the Hosted Cache Server \(Optional\)

You can use this procedure to import data packages and preload content on your hosted cache servers.

This procedure is optional because you are not required to prehash and preload content on your hosted cache servers.

If you do not pre\-load content, data is added to the hosted cache automatically as clients download it over the WAN connection.

You must be a member of the Administrators group to perform this procedure.

## To import data packages on the hosted cache server

1. On the server computer, open Windows PowerShell with Administrator privileges.

2. Type the following command, replacing the value for the –Path parameter with the folder location where you have stored your data packages, and then press ENTER.

    ```
    Import-BCCachePackage –Path D:\temp\PeerDistPackage.zip
    ```

3. If you have more than one hosted cache server where you want to preload content, perform this procedure on each hosted cache server.

To continue with this guide, see [Configure Client Automatic Hosted Cache Discovery by Service Connection Point](10-Bc-Client-By-Scp.md).
