---
title: "Create the BranchCache File Servers Organizational Unit"
type: reference
domain: windows-server
slug: networking-create-the-branchcache-file-servers-organizational-unit
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/networking/branchcache/deploy/Create-the-BranchCache-File-Servers-Organizational-Unit
family: networking
documentKind: "how-to"
abstract: "Learn how to create an organizational unit (OU) in Active Directory Domain Services (AD DS) for BranchCache file servers."
---

# Create the BranchCache File Servers Organizational Unit

# Create the BranchCache File Servers Organizational Unit

You can use this procedure to create an organizational unit (OU) in Active Directory Domain Services (AD DS) for BranchCache file servers.

Membership in **Domain Admins**, or equivalent is the minimum required to perform this procedure.

### To create the BranchCache file servers organizational unit

1.  On a computer where AD DS is installed, in Server Manager, click **Tools**, and then click **Active Directory Users and Computers**. The Active Directory Users and Computers console opens.

2.  In the Active Directory Users and Computers console, right-click the domain to which you want to add an OU. For example, if your domain is named example.com, right click **example.com**. Point to **New**, and then click **Organizational Unit**. The **New Object - Organizational Unit** dialog box opens.

3.  In the **New Object - Organizational Unit** dialog box, in **Name**, type a name for the new OU. For example, if you want to name the OU BranchCache file servers, type **BranchCache file servers**, and then click **OK**.
