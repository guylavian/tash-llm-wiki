---
title: "AD Forest Recovery - Remove the global catalog"
type: reference
domain: active-directory
slug: ad-ds-ad-forest-recovery-remove-gc
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-remove-gc
family: ad-ds
documentKind: "how-to"
abstract: "Learn more about: AD Forest Recovery - Removing the global catalog"
---

# AD Forest Recovery - Remove the global catalog

# Active Directory Forest Recovery - Remove the global catalog

 Use the following procedure to remove the global catalog from a DC.

 Restoring a global catalog server from backup could result in the global catalog holding newer data for one of its partial replicas than the corresponding domain that is authoritative for that partial replica. In such a case, the newer data won't be removed from the global catalog and might even replicate to other global catalog servers. As a result, even if you did restore a DC that was a global catalog server, either inadvertently or because that was the solitary backup you trusted, you should remove the global catalog soon after the restore operation is complete. When the global catalog is removed, the computer removes all its partial replicas.

## Remove the global catalog using Active Directory Sites and Services

1. Open Server Manager, select **Tools** and select **Active Directory Sites and Services**.
1. In the console tree, expand the **Sites** container, and then select the appropriate site that contains the target server.
1. Expand the **Servers** container, and then expand the *server* object for the DC from which you want to remove the global catalog.
1. Right-click **NTDS Settings**, and then select **Properties**.
1. Clear the **Global Catalog** check box.
   :::image type="content" source="media/removegc1.png" alt-text="Remove GC":::
1. Select **Apply**.

## Remove the global catalog using Repadmin

Open an elevated command prompt, type the following command, and press ENTER:

   ```cli
   repadmin.exe /options DC_NAME –IS_GC
   ```

## Next steps

[!INCLUDE [ad-forest-recovery-guide-links](includes/ad-forest-recovery-guide-links.md)]
