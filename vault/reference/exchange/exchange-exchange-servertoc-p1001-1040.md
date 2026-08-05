---
title: "Exchange Server — pages 1001-1040"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1001-1040
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1001-1040
family: exchange
documentKind: "doc"
abstract: "Exchange servers and the Exchange Trusted Subsystem also have permissions to create security principals in Active Directory on behalf of users and third-party programs that integrate with RBAC. RBAC split permissions is a good choice for your organization if the following are tr"
---

# Exchange Server — pages 1001-1040

<!-- p.1001 -->

Exchange servers and the Exchange Trusted Subsystem also have permissions to create security
principals in Active Directory on behalf of users and third-party programs that integrate with
RBAC.

RBAC split permissions is a good choice for your organization if the following are true:

      Your organization doesn't require that security principal creation be performed using only
      Active Directory management tools and only by users who are assigned specific Active
      Directory permissions.

      Your organization allows services, such as Exchange servers, to create security principals.

      You want to simplify the process required to create mailboxes, mail-enabled users,
      distribution groups, and role groups by allowing their creation from within the Exchange
      management tools.

      You want to manage the membership of distribution groups and role groups within the
      Exchange management tools.

      You have third-party programs that require that Exchange servers be able to create
      security principals on their behalf.

If your organization requires a complete separation of Exchange and Active Directory
administration where no Active Directory administration can be performed using Exchange
management tools or by Exchange services, see the Active Directory Split Permissions section
later in this topic.

Switching from shared permissions to RBAC split permissions is a manual process where you
remove the permissions required to create security principals from the role groups that are
granted them by default. The following table shows the roles that enable the creation of
security principals in Exchange and the management role groups they're assigned to by
default.

                                                                                  ﾉ   Expand table

 Management role                                               Role group

 Mail Recipient Creation role                                  Organization Management

                                                               Recipient Management

 Security Group Creation and Membership role                   Organization Management

By default, members of the Organization Management and Recipient Management role groups
can create security principals. You must transfer the ability to create security principals from the

<!-- p.1002 -->

built-in role groups to a new role group that you create.

To configure RBAC split permissions, you must do the following:

   1. Disable Active Directory split permissions if it's enabled.

   2. Create a role group, which will contain the Active Directory administrators that will be
     able to create security principals.

   3. Create regular and delegating role assignments between the Mail Recipient Creation role
     and the new role group.

   4. Create regular and delegating role assignments between the Security Group Creation and
     Membership role and the new role group.

   5. Remove the regular and delegating management role assignments between the Mail
     Recipient Creation role and the Organization Management and Recipient Management
     role groups.

   6. Remove the regular and delegating role assignments between the Security Group
     Creation and Membership role and the Organization Management role group.

After completing these steps, only members of the new role group that you create will be able
to create security principals, such as mailboxes. The new group will only be able to create the
objects. It won't be able to configure the Exchange attributes on the new object. An Active
Directory administrator, who is a member of the new group, will need to create the object, and
then an Exchange administrator will need to configure the Exchange attributes on the object.
Exchange administrators won't be able to use the following cmdlets:

     New-Mailbox

     New-MailContact

     New-MailUser

     New-RemoteMailbox

     Remove-Mailbox

     Remove-MailContact

     Remove-MailUser

     Remove-RemoteMailbox

Exchange administrators will, however, be able to create and manage Exchange-specific
objects, such as mail flow rules (also known as transport rules), distribution groups, and so on

<!-- p.1003 -->

and manage Exchange-related attributes on any object.

Additionally, the associated features in the EAC and Outlook on the web (formerly known as
Outlook Web App), such as the New Mailbox Wizard, will also no longer be available or will
generate an error if you try to use them.

If you want the new role group to also be able to manage the Exchange attributes on the new
object, the Mail Recipients role also needs to be assigned to the new role group.

For more information about configuring a split permissions model, see Configure Exchange
2013 for split permissions.

Active Directory split permissions
With Active Directory split permissions, the creation of security principals in the Active
Directory domain partition, such as mailboxes and distribution groups, must be performed
using Active Directory management tools. Several changes are made to the permissions
granted to the Exchange Trusted Subsystem and Exchange servers to limit what Exchange
administrators and servers can do. The following changes in functionality occur when you
enable Active Directory split permissions:

        Creation of mailboxes, mail-enabled users, distribution groups, and other security
        principals is removed from the Exchange management tools.

        Adding and removing distribution group members can't be done from the Exchange
        management tools.

        All permissions granted to the Exchange Trusted Subsystem and Exchange servers to
        create security principals are removed.

        Exchange servers and the Exchange management tools can only modify the Exchange
        attributes of existing security principals in Active Directory.

For example, to create a mailbox with Active Directory split permissions enabled, a user must
first be created using Active Directory tools by a user with the required Active Directory
permissions. Then, the user can be mailbox-enabled using the Exchange management tools.
Only the Exchange-related attributes of the mailbox can be modified by Exchange
administrators using the Exchange management tools.

Active Directory split permissions is a good choice for your organization if the following are
true:

        Your organization requires that security principals be created using only the Active
        Directory management tools or only by users who are granted specific permissions in

<!-- p.1004 -->

     Active Directory.

     You want to completely separate the ability to create security principals from those who
     manage the Exchange organization.

     You want to perform all distribution group management, including creation of
     distribution groups and adding and removing members of those groups, using Active
     Directory management tools.

     You don't want Exchange servers, or third-party programs that use Exchange on their
     behalf, to create security principals.

Notes:

     Switching to Active Directory split permissions is a choice that you can make when you
     install Exchange by using the Setup wizard or the /ActiveDirectorySplitPermissions
     command line switch with Setup.exe (and you must always specify the /PrepareAD switch
     along with the /ActiveDirectorySplitPermissions switch).

     You can also enable or disable Active Directory split permissions after you've installed
     Exchange by rerunning Setup.exe from the command line. To enable Active Directory split
     permissions, use the value /ActiveDirectorySplitPermissions:True . To disable it, use the
     value /ActiveDirectorySplitPermissions:False .

     If you have multiple domains within the same forest, you must also do one of the
     following steps:

         Specify the /PrepareAllDomains switch when you apply Active Directory split
         permissions.

         Run Setup.exe with the /PrepareDomain switch in each domain. You must prepare
         every domain that contains Exchange servers, mail-enabled objects, or global catalog
         servers that could be accessed by an Exchange server.

     You can't enable Active Directory split permissions if you've installed Exchange 2010 or
     later on a domain controller.

     After you enable or disable Active Directory split permissions, we recommend that you
     restart the Exchange servers in your organization to force them to pick up the new Active
     Directory access token with the updated permissions.

Exchange achieves Active Directory split permissions by removing permissions and
membership from the Exchange Windows Permissions security group. This security group, in
shared permissions and RBAC split permissions, is given permissions to many non-Exchange
objects and attributes throughout Active Directory. By removing the permissions and

<!-- p.1005 -->

membership to this security group, Exchange administrators and services are prevented from
creating or modifying those non-Exchange Active Directory objects.

For a list of changes that occur to the Exchange Windows Permissions security group and other
Exchange components when you enable or disable Active Directory split permissions, see the
following table.

  ７ Note

  Role assignments to role groups that enable Exchange administrators to create security
  principals are removed when Active Directory split permissions is enabled. This is done to
  remove access to cmdlets that would otherwise generate an error when they're run
  because they don't have permissions to create the associated Active Directory object.

                                                                                       ﾉ   Expand table

 Action                Changes made by Exchange

 Enable Active         The following actions happen when you enable Active Directory split permissions
 Directory split       either through the Setup wizard or by running Setup.exe with the /PrepareAD and
 permissions during    /ActiveDirectorySplitPermissions:true command line switches:
 first Exchange
 Server installation        An organizational unit (OU) named Microsoft Exchange Protected Groups is
                            created.
                            The Exchange Windows Permissions security group is created in the
                            Microsoft Exchange Protected Groups OU.
                            The Exchange Trusted Subsystem security group isn't added to the Exchange
                            Windows Permissions security group.
                            Creation of non-delegating management role assignments to management
                            roles with the following management role types is skipped:
                            MailRecipientCreation and SecurityGroupCreationandMembership .
                            Access control entries (ACEs) that would have been assigned to the Exchange
                            Windows Permissions security group aren't added to the Active Directory
                            domain object.

                       If you run Setup.exe with the /PrepareAllDomains or /PrepareDomain switch, the
                       following actions happen in each child domain that's prepared:

                            All ACEs assigned to the Exchange Windows Permissions security group are
                            removed from the domain object.
                            ACEs are set in each domain with the exception of any ACEs assigned to the
                            Exchange Windows Permissions security group.

 Switch from shared    The following actions happen when you run the setup.exe command with the
 permissions or        /PrepareAD and /ActiveDirectorySplitPermissions:true command line switches:
 RBAC split

<!-- p.1006 -->

 Action               Changes made by Exchange

 permissions to             An OU named Microsoft Exchange Protected Groups is created.
 Active Directory           The Exchange Windows Permissions security group is moved to the
 split permissions          Microsoft Exchange Protected Groups OU.
                            The Exchange Trusted Subsystem security group is removed from the
                            Exchange Windows Permissions security group.
                            Any non-delegating role assignments to management roles with the
                            following role types are removed: MailRecipientCreation and
                            SecurityGroupCreationandMembership .
                            All ACEs assigned to the Exchange Windows Permissions security group are
                            removed from the domain object.

                      If you run Setup.exe with either the /PrepareAllDomains or /PrepareDomain switch,
                      the following actions happen in each child domain that's prepared:

                            All ACEs assigned to the Exchange Windows Permissions security group are
                            removed from the domain object.
                            ACEs are set in each domain with the exception of any ACEs assigned to the
                            Exchange Windows Permissions security group.

 Switch from Active   The following actions happen when you run Setup.exe with the /PrepareAD and
 Directory split      /ActiveDirectorySplitPermissions:false switches:
 permissions to
 shared permissions         The Exchange Windows Permissions security group is moved to the
 or RBAC split              Microsoft Exchange Security Groups OU.
 permissions                The Microsoft Exchange Protected Groups OU is removed
                            The Exchange Trusted Subsystems security group is added to the Exchange
                            Windows Permissions security group.
                            ACEs are added to the domain object for the Exchange Windows
                            Permissions security group.

                      If you run setup with either the /PrepareAllDomains or /PrepareDomain switch, the
                      following actions happen in each child domain that's prepared:

                            ACEs are added to the domain object for the Exchange Windows
                            Permissions security group.
                            ACEs are set in each domain including ACEs assigned to the Exchange
                            Windows Permissions security group.

                      Role assignments to the Mail Recipient Creation and Security Group Creation and
                      Membership roles aren't automatically created when switching from Active
                      Directory split to shared permissions. If delegating role assignments were
                      customized prior to Active Directory split permissions being enabled, those
                      customizations are left intact. To create role assignments between these roles and
                      the Organization Management role group, see Configure Exchange Server for
                      shared permissions.

After you enable Active Directory split permissions, the following cmdlets are no longer
available:

<!-- p.1007 -->

     New-Mailbox

     New-MailContact

     New-MailUser

     New-RemoteMailbox

     Remove-Mailbox

     Remove-MailContact

     Remove-MailUser

     Remove-RemoteMailbox

After you enable Active Directory split permissions, the following cmdlets are accessible but
you can't use them to create distribution groups or modify distribution group membership:

     Add-DistributionGroupMember

     New-DistributionGroup

     Remove-DistributionGroup

     Remove-DistributionGroupMember

     Update-DistributionGroupMember

Some cmdlets, although still available, may offer only limited functionality when used with
Active Directory split permissions. This is because they may allow you to configure recipient
objects that are in the domain Active Directory partition and Exchange configuration objects
that are in the configuration Active Directory partition. They may also allow you to configure
Exchange-related attributes on objects stored in the domain partition. Attempts to use the
cmdlets to create objects, or modify non-Exchange-related attributes on objects, in the domain
partition will result in an error. For example, the Add-ADPermission cmdlet will return an error
if you attempt to add permissions to a mailbox. However, the Add-ADPermission cmdlet will
succeed if you configure permissions on a Receive connector. This is because a mailbox is
stored in the domain partition while Receive connectors are stored in the configuration
partition.

Additionally, the associated features in the EAC and Outlook on the web, such as the New
Mailbox wizard, will also no longer be available or will generate an error if you try to use them.

Exchange administrators will, however, be able to create and manage Exchange-specific
objects, such as mail flow rules, and so on.

<!-- p.1008 -->

For more information about configuring an Active Directory split permissions model, see
Configure Exchange 2013 for split permissions.

<!-- p.1009 -->

Configure Exchange Server for split
permissions
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Split permissions enable two separate groups, such as Active Directory administrators and
Exchange administrators, to manage their respective services, objects, and attributes. Active
Directory administrators manage security principals, such as users, that provide permissions to
access an Active Directory forest. Exchange administrators manage the Exchange-related
attributes on Active Directory objects and Exchange-specific object creation and management.

Exchange Server 2016 and Exchange Server 2019 offer the following types of split permissions
models:

      RBAC split permissions: Permissions to create security principals in the Active Directory
      domain partition are controlled by Role Based Access Control (RBAC). Only those who are
      members of the appropriate role groups can create security principals.

      Active Directory split permissions: Permissions to create security principals in the Active
      Directory domain partition are completely removed from any Exchange user, service, or
      server. No option is provided in RBAC to create security principals. Creation of security
      principals in Active Directory must be performed using Active Directory management
      tools.

The model that you choose depends on the structure and needs of your organization. Choose
the procedure that follows that's applicable to the model you want to configure. We
recommend that you use the RBAC split permissions model. The RBAC split permissions model
provides significantly more flexibility while providing the same administration separation as
Active Directory split permissions.

For more information about shared and split permissions, see Split permissions in Exchange
Server.

For more information about management role groups, management roles, and regular and
delegating management role assignments, see the following topics:

      Understanding Role Based Access Control
      Understanding management role groups
      Understanding management roles
      Understanding management role assignments

<!-- p.1010 -->

What do you need to know before you begin?
     Estimated time to complete each procedure: 5 minutes

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Active Directory split
     permissions" entry in the Role management permissions topic.

     The permissions model that you select will be applied to all Exchange 2010 or later
     servers in your organization.

     To download the latest version of Exchange, see Updates for Exchange Server.

     To open the Exchange Management Shell, see Open the Exchange Management Shell.

   Tip

  Having problems? Ask for help in the Exchange Server        forums.

Switch to RBAC split permissions
After you've switched to RBAC split permissions, only Active Directory administrators will be
able to create Active Directory security principals. This means that Exchange administrators
won't be able to use the following cmdlets:

     New-Mailbox
     New-MailContact
     New-MailUser
     New-RemoteMailbox
     Remove-Mailbox
     Remove-MailContact
     Remove-MailUser
     Remove-RemoteMailbox

Exchange administrators will only be able to manage the Exchange attributes on existing Active
Directory security principals. However, They will be able to create and manage Exchange-
specific objects, such as mail flow rules (also known as transport rules) and distribution groups.
For more information, see the "RBAC Split Permissions" section in Split permissions in Exchange
Server.

To configure Exchange for split permissions, you must assign the Mail Recipient Creation role
and the Security Group Creation and Membership role to a role group that contains members

<!-- p.1011 -->

that are Active Directory administrators. You must then remove the assignments between those
roles and any role group or universal security group (USG) that contains Exchange
administrators.

To configure RBAC split permissions, do the following steps:

   1. If your organization is currently configured for Active Directory split permissions, do the
     following steps:

      a. On the target server, open File Explorer, right-click on the Exchange ISO image file, and
        then select Mount. Note the virtual DVD drive letter that's assigned.

     b. Open a Windows Command Prompt window. For example:

              Press the Windows key + 'R' to open the Run dialog, type cmd.exe, and then
              press OK.
              Press Start. In the Search box, type Command Prompt, then in the list of results,
              select Command Prompt.

      c. In the Command Prompt window, run the following command to disable Active
        Directory split permissions:

          ７ Note

                  The previous /IAcceptExchangeServerLicenseTerms switch will not work
                  starting with the Exchange Server 2016 and Exchange Server 2019
                  September 2021 Cumulative Updates (CUs). You now must use either
                  /IAcceptExchangeServerLicenseTerms_DiagnosticDataON or
                  /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF for unattended and
                  scripted installs.

                  The examples below use the
                  /IAcceptExchangeServerLicenseTerms_DiagnosticDataON switch. It's up to you
                  to change the switch to
                  /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF.

          DOS

           Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD
           /ActiveDirectorySplitPermissions:false

<!-- p.1012 -->

  d. Restart all Exchange servers in your organization or wait for the Active Directory access
    token to replicate to all of your Exchange servers.

2. Do the following steps in the Exchange Management Shell:

  a. Create a role group for the Active Directory administrators. In addition to creating the
    role group, the command creates regular role assignments between the new role
    group and the Mail Recipient Creation role and the Security Group Creation and
    Membership role.

       DOS

       New-RoleGroup "Active Directory Administrators" -Roles "Mail Recipient
       Creation", "Security Group Creation and Membership"

       ７ Note

       If you want members of this role group to be able to create role assignments,
       include the Role Management role. You don't have to add this role now. However,
       if you ever want to assign either the Mail Recipient Creation role or Security
       Group Creation and Membership role to other role assignees, the Role
       Management role must be assigned to this new role group. The steps that follow
       configure the Active Directory Administrators role group as the only role group
       that can delegate these roles.

  b. Create delegating role assignments between the new role group and the Mail
    Recipient Creation role and Security Group Creation and Membership role by running
    the following commands:

       PowerShell

       New-ManagementRoleAssignment -Role "Mail Recipient Creation" -SecurityGroup
       "Active Directory Administrators" -Delegating
       New-ManagementRoleAssignment -Role "Security Group Creation and Membership"
       -SecurityGroup "Active Directory Administrators" -Delegating

  c. Add members to the new role group by running the following command:

       PowerShell

       Add-RoleGroupMember "Active Directory Administrators" -Member <user to add>

<!-- p.1013 -->

d. Replace the delegate list on the new role group so that only members of the role
  group can add or remove members by running the following command:

    PowerShell

    Set-RoleGroup "Active Directory Administrators" -ManagedBy "Active
    Directory Administrators"

    ） Important

    Members of the Organization Management role group, or those who are assigned
    the Role Management role, either directly or through another role group or USG,
    can bypass this delegate security check. If you want to prevent any Exchange
    administrator from adding himself or herself to the new role group, you must
    remove the role assignment between the Role Management role and any
    Exchange administrator and assign it to another role group.

e. Find all of the regular and delegating role assignments to the Mail Recipient Creation
  role by running the following command:

    PowerShell

    Get-ManagementRoleAssignment -Role "Mail Recipient Creation" | Format-Table
    Name, Role, RoleAssigneeName -Auto

f. Remove all of the regular and delegating role assignments to the Mail Recipient
  Creation role that aren't associated with the new role group or any other role groups,
  USGs, or direct assignments you want to keep by running the following command.

    PowerShell

    Remove-ManagementRoleAssignment <Mail Recipient Creation role assignment to
    remove>

    ７ Note

    If you want to remove all of the regular and delegating role assignments to the
    Mail Recipient Creation role on any role assignee other than the Active Directory
    Administrators role group, use the following command. The WhatIf switch lets you
    see what role assignments will be removed. Remove the WhatIf switch and run the
    command again to remove the role assignments.

<!-- p.1014 -->

          PowerShell

          Get-ManagementRoleAssignment -Role "Mail Recipient Creation" | Where {
          $_.RoleAssigneeName -NE "Active Directory Administrators" } | Remove-
          ManagementRoleAssignment -WhatIf

     g. Find all of the regular and delegating role assignments to the Security Group Creation
        and Membership role by running the following command.

          PowerShell

          Get-ManagementRoleAssignment -Role "Security Group Creation and Membership"
          | Format-Table Name, Role, RoleAssigneeName -Auto

     h. Remove all of the regular and delegating role assignments to the Security Group
        Creation and Membership role that aren't associated with the new role group or any
        other role groups, USGs, or direct assignments you want to keep by running the
        following command:

          PowerShell

          Remove-ManagementRoleAssignment <Security Group Creation and Membership
          role assignment to remove>

          ７ Note

          You can use the same command in the preceding Note to remove all of the
          regular and delegating role assignments to the Security Group Creation and
          Membership role on any role assignee other than the Active Directory
          Administrators role group, as shown in this example.

          PowerShell

          Get-ManagementRoleAssignment -Role "Security Group Creation and Membership"
          | Where { $_.RoleAssigneeName -NE "Active Directory Administrators" } |
          Remove-ManagementRoleAssignment -WhatIf

For detailed syntax and parameter information, see the following topics:

     New-RoleGroup
     New-ManagementRoleAssignment
     Add-RoleGroupMember
     Set-RoleGroup

<!-- p.1015 -->

     Get-ManagementRoleAssignment
     Remove-ManagementRoleAssignment

Switch to Active Directory split permissions
You can configure your Exchange organization for Active Directory split permissions. Active
Directory split permissions completely remove the permissions that allow Exchange
administrators and servers from creating security principals in Active Directory or modifying
non-Exchange attributes on those objects. When you are done, only Active Directory
administrators will be able to create Active Directory security principals. This means that
Exchange administrators won't be able to use the following cmdlets:

     Add-DistributionGroupMember
     New-DistributionGroup
     New-Mailbox
     New-MailContact
     New-MailUser
     New-RemoteMailbox
     Remove-DistributionGroup
     Remove-DistributionGroupMember
     Remove-Mailbox
     Remove-MailContact
     Remove-MailUser
     Remove-RemoteMailbox
     Update-DistributionGroupMember

Exchange administrators and servers will only be able to manage the Exchange attributes on
existing Active Directory security principals. However, they will be able to create and manage
Exchange-specific objects, such as transport rules and Unified Messaging dial plans.

  ２ Warning

  After you enable Active Directory split permissions, Exchange administrators and servers
  will no longer be able to create security principals in Active Directory, and they won't be
  able to manage distribution group membership. These tasks must be performed using
  Active Directory management tools with the required Active Directory permissions. Before
  you make this change, you should understand the impact it will have on your
  administration processes and third-party applications that integrate with Exchange and
  the RBAC permissions model.

<!-- p.1016 -->

  For more information, see the "Active Directory split permissions" section in Split
  permissions in Exchange Server.

To switch from shared or RBAC split permissions to Active Directory split permissions, do the
following steps:

   1. On the target server, open File Explorer, right-click on the Exchange ISO image file, and
     then select Mount. Note the virtual DVD drive letter that's assigned.

   2. In a Windows Command Prompt window, run the following command to enable Active
     Directory split permissions:

       ７ Note

             The previous /IAcceptExchangeServerLicenseTerms switch will not work starting
             with the Exchange Server 2016 and Exchange Server 2019 September 2021
             Cumulative Updates (CUs). You now must use either
             /IAcceptExchangeServerLicenseTerms_DiagnosticDataON or
             /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF for unattended and
             scripted installs.

             The examples below use the
             /IAcceptExchangeServerLicenseTerms_DiagnosticDataON switch. It's up to you to
             change the switch to /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF.

       DOS

        Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD
        /ActiveDirectorySplitPermissions:true

   3. If you have multiple Active Directory domains in your organization, you must either run
     Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareDomain in each

     child domain that contains Exchange servers or objects or run Setup.exe
     /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAllDomains from a site

     that has an Active Directory server from every domain.

   4. Restart all Exchange servers in your organization or wait for the Active Directory access
     token to replicate to all of you Exchange servers.

<!-- p.1017 -->

Configure Exchange Server for shared
permissions
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

If you've never configured your organization for split permissions, you don't need to perform
this procedure. Exchange Server 2016 and Exchange Server 2019 are configured for shared
permissions by default.

Shared permissions enable you, as an Exchange administrator, to create Active Directory
security principals, such as users, and then configure them as Exchange recipients. Unlike split
permissions, which separate management tasks between groups of Exchange administrators
and Active Directory administrators, there's no separation of tasks with shared permissions.

For more information about shared and split permissions, see Split permissions in Exchange
Server.

You can configure your Exchange organization for shared permissions if you've previously set
your organization for split permissions. The procedure to switch to shared permissions is
different depending on whether you're currently using Role Based Access Control (RBAC) split
permissions or Active Directory split permissions. Choose the procedure that follows that's
applicable to your current configuration. If the following are true, your organization is using
Active Directory split permissions:

      The Microsoft Exchange Protected Groups organizational unit (OU) exists.

      The Exchange Windows Permissions security group is located in the Microsoft Exchange
      Protected Groups OU.

      The Exchange Trusted Subsystem security group is a member of the Exchange Windows
      Permissions security group.

      There are no regular management role assignments to the Mail Recipient Creation role or
      Security Group Creation and Membership role.

For more information about management role groups, management roles, and regular and
delegating management role assignments, see the following topics:

      Understanding Role Based Access Control

      Understanding management role groups

      Understanding management roles

<!-- p.1018 -->

     Understanding management role assignments

What do you need to know before you begin?
     Estimated time to complete each procedure: 5 minutes

     Procedures in this topic require specific permissions. See each procedure for its
     permissions information.

     The Exchange organization must currently be configured for RBAC or Active Directory
     split permissions.

     The permissions model that you select will be applied to all Exchange 2010 or later
     servers in your organization.

     You must have permissions to delegate the Mail Recipient Creation management role and
     the Security Group Creation and Membership management role to the Organization
     Management management role group or another role group that's assigned the Mail
     Recipients role.

     To download the latest version of Exchange on the target computer, see Updates for
     Exchange Server.

     To open the Exchange Management Shell, see Open the Exchange Management Shell.

   Tip

  Having problems? Ask for help in the Exchange Server      forums.

Switch from RBAC split permissions to shared
permissions
You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "Role groups" entry in the Role management
permissions topic.

To switch from RBAC split permissions to Exchange shared permissions, you must assign the
Mail Recipient Creation role and the Security Group Creation and Membership role to a role
group that's also assigned the Mail Recipients role and has Exchange administrators as
members. In the default shared permissions configuration, the Organization Management role

<!-- p.1019 -->

group contains each of these roles. Because of this, the Organization Management role group
is in this procedure.

Configure shared permissions
To configure shared permissions on the Organization Management role group, do the
following steps using an account that has permissions to delegate role assignments for the
Mail Recipient Creation role and the Security Group Creation and Membership role:

   1. Add delegating role assignments for the Mail Recipient Creation role and Security Group
     Creation and Membership role to the Organization Management role group using the
     following commands.

        PowerShell

        New-ManagementRoleAssignment -Role "Mail Recipient Creation" -SecurityGroup
        "Organization Management" -Delegating
        New-ManagementRoleAssignment -Role "Security Group Creation and Membership" -
        SecurityGroup "Organization Management" -Delegating

        ７ Note

        The role group (in this procedure, the Active Directory Administrators role group)
        that has delegating role assignments for the Mail Recipient Creation role and
        Security Group Creation and Membership role must be assigned the Role
        Management role to run the New-ManagementRoleAssignment cmdlet. The role
        assignee that can delegate the Role Management role must assign that role to the
        Active Directory Administrators role group.

   2. Add regular role assignments for the Mail Recipient Creation role to the Organization
     Management and Recipient Management role groups using the following commands.

        PowerShell

        New-ManagementRoleAssignment -Role "Mail Recipient Creation" -SecurityGroup
        "Organization Management"
        New-ManagementRoleAssignment -Role "Security Group Creation and Membership" -
        SecurityGroup "Recipient Management"

   3. Add a regular role assignment for the Security Group Creation and Membership role to
     the Organization Management role group using the following command.

        PowerShell

<!-- p.1020 -->

         New-ManagementRoleAssignment -Role "Security Group Creation and Membership"
        -SecurityGroup "Organization Management"

For detailed syntax and parameter information, see New-ManagementRoleAssignment.

Remove permissions from Active Directory
administrators (Optional)
You can optionally remove the permissions granted to Active Directory administrators if you no
longer want them to be able to create or manage Active Directory objects using the Exchange
management tools. If you want to remove permissions from Active Directory administrators,
perform this procedure.

  ７ Note

  Although you can remove permissions for Active Directory administrators to manage
  Active Directory objects using the Exchange management tools, Active Directory
  administrators can continue to manage Active Directory objects using Active Directory
  management tools, if their Active Directory permissions allow it. They won't, however, be
  able to manage Exchange-specific attributes on Active Directory objects. For more
  information, see Split permissions in Exchange Server.

To remove Exchange-related split permissions from Active Directory administrators, do the
following steps:

   1. Remove the regular and delegating role assignments that assign the Mail Recipient
     Creation role to the role group or universal security group (USG) that contains the Active
     Directory administrators as members using the following command. This command uses
     the Active Directory Administrators role group as an example. The WhatIf switch lets you
     see what role assignments will be removed. Remove the WhatIf switch, and run the
     command again to remove the role assignments.

       PowerShell

        Get-ManagementRoleAssignment -Role "Mail Recipient Creation" | Where {
        $_.RoleAssigneeName -EQ "Active Directory Administrators" } | Remove-
        ManagementRoleAssignment -WhatIf

   2. Remove the regular and delegating role assignments that assign the Security Group
     Creation and Membership role to the role group or USG that contains the Active

<!-- p.1021 -->

     Directory administrators as members using the following command. This command uses
     the Active Directory Administrators role group as an example. The WhatIf switch lets you
     see what role assignments will be removed. Remove the WhatIf switch, and run the
     command again to remove the role assignments.

       PowerShell

        Get-ManagementRoleAssignment -Role "Security Group Creation and Membership" |
        Where { $_.RoleAssigneeName -EQ "Active Directory Administrators" } | Remove-
        ManagementRoleAssignment -WhatIf

   3. Optional. If you want to remove all Exchange permissions from the Active Directory
     administrators, you can remove the role group or USG in which they're members. For
     more information about how to remove a role group, see Manage role groups.

For detailed syntax and parameter information, see Get-ManagementRoleAssignment or
Remove-ManagementRoleAssignment.

Switch from Active Directory split permissions to
shared permissions
You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "Active Directory split permissions" entry in the Role
management permissions topic.

To switch from Active Directory split permissions to Exchange shared permissions, you must
rerun Exchange Setup to disable Active Directory split permissions in the Exchange
organization, and then create role assignments between a role group and the Mail Recipient
Creation role and Security Group Creation and Membership role. In the default shared
permissions configuration, the Organization Management role group contains each of these
roles. Because of this, the Organization Management role group is in this procedure.

  ） Important

  The Setup.exe command in this procedure makes changes to Active Directory. You must
  use an account that has the permissions required to make these changes. This account
  might not be the same account that has permissions to create role assignments using the
  New-ManagementRoleAssignment cmdlet. Use the account, or accounts, with the
  permissions necessary to successfully complete each step in this procedure.

To switch from Active Directory split permissions to shared permissions, do the following steps:

<!-- p.1022 -->

1. On the target server, open File Explorer, right-click on the Exchange ISO image file that
   you downloaded, and then select Mount. Note the virtual DVD drive letter that's
   assigned.

2. Open a Windows Command Prompt window. For example:

         Press the Windows key + 'R' to open the Run dialog, type cmd.exe, and then press
         OK.

         Press Start. In the Search box, type Command Prompt, then in the list of results,
         select Command Prompt.

3. In the Command Prompt window, run the following command:

７ Note

      The previous /IAcceptExchangeServerLicenseTerms switch will not work starting with
      the Exchange Server 2016 and Exchange Server 2019 September 2021 Cumulative
      Updates (CUs). You now must use either
      /IAcceptExchangeServerLicenseTerms_DiagnosticDataON or
      /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF for unattended and scripted
      installs.

      The examples below use the /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
      switch. It's up to you to change the switch to
      /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF.

PowerShell

Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD
/ActiveDirectorySplitPermissions:false

4. In the Exchange Management Shell, run the following commands to add regular role
   assignments between the Mail Recipient Creation role and Security Group Creation and
   Management role and the Organization Management and Recipient Management role
   groups.

      PowerShell

      New-ManagementRoleAssignment "Mail Recipient Creation_Organization
      Management" -Role "Mail Recipient Creation" -SecurityGroup "Organization
      Management"
      New-ManagementRoleAssignment "Security Group Creation and Membership_Org

<!-- p.1023 -->

       Management" -Role "Security Group Creation and Membership" -SecurityGroup
       "Organization Management"
       New-ManagementRoleAssignment "Mail Recipient Creation_Recipient Management" -
       Role "Mail Recipient Creation" -SecurityGroup "Recipient Management"

  5. Restart all Exchange servers in your organization.

For detailed syntax and parameter information, see New-ManagementRoleAssignment.

<!-- p.1024 -->

Recipients in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016         2019        Subscription Edition

The people and resources that send and receive messages are the core of any messaging and
collaboration system. In an Exchange organization, these people and resources are referred to
as recipients. A recipient is any mail-enabled object in Active Directory to which Microsoft
Exchange can deliver or route messages.

Exchange recipient types
Exchange includes several explicit recipient types. Each recipient type is identified in the
Exchange admin center (EAC) and has a unique value in the RecipientTypeDetails property in
the Exchange Management Shell. The use of explicit recipient types has the following benefits:

      At a glance, you can differentiate between various recipient types.
      You can search and sort by each recipient type.
      You can more easily perform bulk management operations for selected recipient types.
      You can more easily view recipient properties because the EAC uses the recipient types to
      render different property pages. For example, the resource capacity is displayed for a
      room mailbox, but isn't present for a user mailbox.

The following table lists the available recipient types. These recipient types are discussed in
more detail later in this topic.

                                                                                              ﾉ    Expand table

 Recipient type        Description

 Dynamic               A distribution group that uses recipient filters and conditions to derive its
 distribution          membership at the time messages are sent.
 group

 Equipment             A resource mailbox that's assigned to a resource that's not location-specific, such as a
 mailbox               portable computer, projector, microphone, or a company car. Equipment mailboxes
                       can be included as resources in meeting requests, providing a simple and efficient
                       way of using resources for your users.

 Linked mailbox        A mailbox that's assigned to an individual user in a separate, trusted forest.

 Mail contact          A mail-enabled Active Directory contact that contains information about people or
                       organizations that exist outside the Exchange organization. Each mail contact has an
                       external email address. All messages sent to the mail contact are routed to this
                       external email address.

<!-- p.1025 -->

Recipient type   Description

Mail forest      A mail contact that represents a recipient object from another forest. Mail forest
contact          contacts are typically created by Microsoft Identity Integration Server (MIIS)
                 synchronization.
                 Note: Mail forest contacts are read-only recipient objects that are updated only
                 through MIIS or similar custom synchronization. You can't use the EAC or the
                 Exchange Management Shell to remove or modify a mail forest contact.

Mail user        A mail-enabled Active Directory user that represents a user outside the Exchange
                 organization. Each mail user has an external email address. All messages sent to the
                 mail user are routed to this external email address.
                 A mail user is similar to a mail contact, except that a mail user has Active Directory
                 logon credentials and can access resources.

Mail-enabled     A mail-enabled Active Directory global or local group object. Mail-enabled non-
non-universal    universal groups were discontinued in Exchange Server 2007 and can exist only if they
group            were migrated from Exchange 2003 or earlier versions of Exchange. You can't use
                 Exchange Server 2013 to create non-universal distribution groups.

Mail-enabled     An Exchange public folder that's configured to receive messages.
public folder

Distribution     A distribution group is a mail-enabled Active Directory distribution group object that
groups           can be used only to distribute messages to a group of recipients.

Mail-enabled     A mail-enabled security group is an Active Directory universal security group object
security group   that can be used to assign access permissions to resources in Active Directory and
                 can also be used to distribute messages.

Microsoft        A special recipient object that provides a unified and well-known message sender that
Exchange         differentiates system-generated messages from other messages. It replaces the
recipient        System Administrator sender used for system-generated messages in earlier versions
                 of Exchange.

Room mailbox     A resource mailbox that's assigned to a meeting location, such as a conference room,
                 auditorium, or training room. Room mailboxes can be included as resources in
                 meeting requests, providing a simple and efficient way of organizing meetings for
                 your users.

Shared mailbox   A mailbox that's not primarily associated with a single user and is generally
                 configured to allow access for multiple users.

Site mailbox     A mailbox comprised of an Exchange mailbox to store email messages and a
                 SharePoint site to store documents. Users can access both email messages and
                 documents using the same client interface. For more information, see Site mailboxes.

                 Note: The site mailboxes are being retired and will be out of service and/or removed.
                 For more information see, Retirement of site mailboxes.

<!-- p.1026 -->

 Recipient type     Description

 User mailbox       A mailbox that's assigned to an individual user in your Exchange organization. It
                    typically contains messages, calendar items, contacts, tasks, documents, and other
                    important business data.

 Microsoft 365 or   In hybrid deployments, a Microsoft 365 or Office 365 mailbox consists of a mail user
 Office 365         that exists in Active Directory on-premises and an associated cloud mailbox that
 mailbox            exists in Exchange Online.

 Linked user        A linked user is a user whose mailbox resides in a different forest than the forest in
                    which the user resides.

Mailboxes
Mailboxes are the most common recipient type used by information workers in an Exchange
organization. Each mailbox is associated with an Active Directory user account. The user can
use the mailbox to send and receive messages, and to store messages, appointments, tasks,
notes, and documents. Mailboxes are the primary messaging and collaboration tool for the
users in your Exchange organization.

Mailbox components
Each mailbox consists of an Active Directory user and the mailbox data that's stored in the
Exchange mailbox database (as shown in the following figure). All configuration data for the
mailbox is stored in the Exchange attributes of the Active Directory user object. The mailbox
database contains the actual data that's in the mailbox associated with the user account.

  ） Important

  When you create a mailbox for a new or existing user, the Exchange attributes required for
  a mailbox are added to the user object in Active Directory. The associated mailbox data
  isn't created until the mailbox either receives a message or the user signs in to it.

<!-- p.1027 -->

  Ｕ Caution

  If you remove a mailbox, the mailbox data stored in the Exchange mailbox database is
  marked for deletion and the associated user account is also deleted from Active Directory.
  To retain the user account and delete only the mailbox data, you must disable the mailbox.

Mailbox types
Exchange supports the following mailbox types:

     User mailboxes: User mailboxes are assigned to individual users in your Exchange
     organization. User mailboxes provide your users with a rich collaboration platform. Users
     can send and receive messages, manage their contacts, schedule meetings, and maintain
     a task list. They can also have voice mail messages delivered to their mailboxes. User
     mailboxes are the most commonly used mailbox type and are typically the mailbox type
     assigned to users in your organization.

     Linked mailboxes: Linked mailboxes are mailboxes that are accessed by users in a
     separate, trusted forest. Linked mailboxes may be necessary for organizations that deploy
     Exchange in a resource forest. The resource forest scenario allows an organization to
     centralize Exchange in a single forest, while allowing access to the Exchange organization
     with user accounts in one or more trusted forests.

     As stated earlier, every mailbox must have a user account associated with it. However, the
     user account that accesses the linked mailbox doesn't exist in the forest where Exchange
     is deployed. Therefore, a disabled user account that exists in the same forest as Exchange
     is associated with each linked mailbox. The following figure illustrates the relationship
     between the linked user account used to access the linked mailbox and the disabled user
     account in the Exchange resource forest associated with the linked mailbox.

<!-- p.1028 -->

Linked mailbox

Microsoft 365 or Office 365 mailboxes: When you create a Microsoft 365 or Office 365
mailbox in Exchange Online in a hybrid deployment, the mail user is created in Active
Directory on-premises. Directory synchronization, if it's configured, automatically
synchronizes this new user object to Microsoft 365 or Office 365, where it's converted to a
cloud mailbox in Exchange Online. You can create Microsoft 365 or Office 365 mailboxes
as regular user mailboxes, resource mailboxes for meeting rooms and equipment, and
shared mailboxes.

Shared mailboxes: Shared mailboxes aren't primarily associated with individual users and
are generally configured to allow access by multiple users.

Although it's possible to assign additional users the logon access permissions to any
mailbox type, shared mailboxes are dedicated for this functionality. The Active Directory
user associated with a shared mailbox must be a disabled account. After you create a
shared mailbox, you must assign permissions to all users that require access to the shared
mailbox.

Resource mailboxes: Resource mailboxes are special mailboxes designed to be used for
scheduling resources. Like all mailbox types, a resource mailbox has an associated Active
Directory user account, but it must be a disabled account. The following are the types of
resource mailboxes:

  Room mailboxes: These mailboxes are assigned to meeting locations, such as
  conference rooms, auditoriums, and training rooms.

  Equipment mailboxes: These mailboxes are assigned to resources that aren't location-
  specific, such as portable computers, projectors, microphones, or company cars.

  You can include both types of resource mailboxes in meeting requests, providing a
  simple and efficient way for your users to use resources. You can configure resource

<!-- p.1029 -->

        mailboxes to automatically process incoming meeting requests based on the resource
        booking policies that are defined by the resource owners. For example, you can
        configure a conference room to automatically accept incoming meeting requests
        except recurring meetings, which can be subject to approval by the resource owner.

System mailboxes

System mailboxes are created by Exchange in the root domain of the Active Directory forest
during installation. Users or administrators can't sign in to these mailboxes. System mailboxes
are created for Exchange features such as Unified Messaging (UM), migration, message
approval, and In-Place eDiscovery. This table lists information about system mailboxes as
they're displayed in Active Directory.

  ７ Note

  Unified Messaging is not available in Exchange 2019

                                                                                   ﾉ   Expand table

 Mailbox           Name

 Organization      SystemMailbox {bb558c35-97f1-4cb9-8ff7-d53741dc928c}

 Message           SystemMailbox {1f05a927-xxxx-xxxx-xxxx-xxxxxxxxxxxx_}
 approval
                   where xxxx-xxxx-xxxx-xxxxxxxxxxxx is a randomly assigned and unique GUID for each
                   Exchange forest

 UM data storage   SystemMailbox {e0dc1c29-89c3-4034-b678-e6c29d823ed9}

                   This mailbox exists in Exchange 2016, not in Exchange 2019

 Discovery         DiscoverySearchMailbox {D919BA05-46A6-415f-80AD-7E09334BB852}

 Federated email   FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042

 Migration         Migration.8f3e7716-2011-43e4-96b1-aba62d229136

If you want to decommission the last Mailbox server in your Exchange organization, you should
first disable these system mailboxes by using the Disable-Mailbox cmdlet. When you
decommission a Mailbox server that contains these system mailboxes, you should move the
system mailboxes to another Mailbox server to make sure that you don't lose functionality.

Planning for mailboxes

<!-- p.1030 -->

Mailboxes are created in mailbox databases on Exchange servers that have the Mailbox server
role installed. To help provide a reliable and effective platform for your mailbox users, detailed
planning for the deployment of Mailbox servers and databases is essential. To learn more
about planning for Mailbox servers and databases, see Planning and deployment.

Distribution groups
Distribution groups are mail-enabled Active Directory group objects that are primarily used for
distributing messages to multiple recipients. Any recipient type can be a member of a
distribution group.

  ） Important

  Note the terminology differences between Active Directory and Exchange. In Active
  Directory, a distribution group refers to any group that doesn't have a security context,
  whether it's mail-enabled or not. In Exchange, all mail-enabled groups are referred to as
  distribution groups, whether they have a security context or not.

Exchange supports the following types of distribution groups:

     Distribution groups: These are Active Directory universal distribution group objects that
     are mail-enabled. They can be used only to distribute messages to a group of recipients.

     Mail-enabled security groups: These are Active Directory universal security group objects
     that are mail-enabled. They can be used to assign access permissions to resources in
     Active Directory and can also be used to distribute messages.

     Mail-enabled non-universal groups: These are Active Directory global or local group
     objects that are mail-enabled. You can create or mail-enable only universal distribution
     groups. You may have mail-enabled groups that were migrated from previous versions of
     Exchange that aren't universal groups. These groups can still be managed by using the
     EAC or the Exchange Management Shell.

        ７ Note

        To convert a domain-local or a global group to a universal group, you can use the
        Set-Group cmdlet in the Exchange Management Shell.

Dynamic distribution groups

<!-- p.1031 -->

Dynamic distribution groups are distribution groups whose membership is based on specific
recipient filters rather than a defined set of recipients.

Unlike regular distribution groups, the membership list for dynamic distribution groups is
calculated each time a message is sent to them, based on the filters and conditions that you
specify. When an email message is sent to a dynamic distribution group, it's delivered to all
recipients in the organization that match the criteria defined for that dynamic distribution
group.

  ） Important

  A dynamic distribution group includes any recipient in Active Directory that has attributes
  that match the group's filter at the time a message is sent. If a recipient's properties are
  modified to match the group's filter, that recipient could inadvertently become a group
  member and start receiving messages that are sent to the dynamic distribution group.
  Well-defined, consistent account provisioning processes can reduce the chances of this
  issue occurring.

To help you create recipient filters for dynamic distribution groups, you can use precanned
filters. A precanned filter is a commonly used filter that you can use to meet a variety of
recipient-filtering criteria. You can use these filters to specify the recipient types that you want
to include in a dynamic distribution group. In addition, you can also specify a list of conditions
that the recipients must meet. You can create precanned conditions based on the following
properties:

     Custom attributes 1-15
     State or province
     Company
     Department
     Recipient container

You can also specify conditions based on recipient properties other than those previously
listed. To do this, you must use the Exchange Management Shell to create a custom query for
the dynamic distribution group. Remember that the filter and condition settings for dynamic
distribution groups that have custom recipient filters can be managed only by using the
Exchange Management Shell. For an example of how to create a dynamic distribution group by
using a custom query, see Manage dynamic distribution groups.

Mail contacts

<!-- p.1032 -->

Mail contacts typically contain information about people or organizations that exist outside
your Exchange organization. Mail contacts can appear in your organization's shared address
book (also called the global address list or GAL) and other address lists, and can be added as
members to distribution groups. Each contact has an external email address, and all email
messages that are sent to a contact are automatically forwarded to that address. Contacts are
ideal for representing people external to your Exchange organization (in the shared address
book) who don't need access to any internal resources. The following are mail contact types:

     Mail contacts: These are mail-enabled Active Directory contacts that contain information
     about people or organizations that exist outside your Exchange organization.
     Mail forest contacts: These represent recipient objects from another forest. These
     contacts are typically created by directory synchronization. Mail forest contacts are read-
     only recipient objects that can be updated or removed only by means of synchronization.
     You can't use Exchange management interfaces to modify or remove a mail forest
     contact.

Mail users
Mail users are similar to mail contacts. Both have external email addresses, both contain
information about people outside your Exchange organization, and both can be displayed in
the shared address book and other address lists. However, unlike a mail contact, mail users
have Active Directory logon credentials and can access resources to which they are assigned
permissions.

If a person external to your organization requires access to resources on your network, you
should create a mail user instead of a mail contact. For example, you may want to create mail
users for short-term consultants who require access to your server infrastructure, but who will
use their own external addresses.

Another scenario is to create mail users in your organization for users who you don't want to
maintain an Exchange mailbox. For example, after an acquisition, the acquired company may
maintain their separate messaging infrastructure, but may also need access to resources on
your network. For those users, you may want to create mail users instead of mailbox users.

  ７ Note

  In the EAC, you use the Recipients > Contacts page to create and manage mail users.
  There isn't a separate page for mail users.

Mail-enabled public folders

<!-- p.1033 -->

Public folders are intended to serve as a repository for information shared among many users.
Mail-enabling a public folder provides an extra level of functionality to users. In addition to
being able to post messages to the folder, users can send email messages to, and sometimes
receive email messages from, the public folder. Each mail-enabled folder has an object in
Active Directory that stores its email address, address book name, and other mail-related
attributes.

You can manage public folders by using either the EAC or the Exchange Management Shell. For
more information about managing public folders, see Public folders.

Microsoft Exchange recipient
The Microsoft Exchange recipient is a special recipient object that provides a unified and well-
known message sender that differentiates system-generated messages from other messages. It
replaces the System Administrator sender that was used for system-generated messages in
earlier versions of Exchange.

The Microsoft Exchange recipient isn't a typical recipient object, such as a mailbox, mail user, or
mail contact, and it isn't managed by using the typical recipient tools. However, you can use
the Set-OrganizationConfig cmdlet in the Exchange Management Shell to configure the
Microsoft Exchange recipient.

  ７ Note

  When system-generated messages are sent to an external sender, the Microsoft Exchange
  recipient isn't used as the sender of the message. Instead, the email address specified by
  the ExternalPostmasterAddress parameter in the Set-TransportConfig cmdlet is used.

Recipients documentation
The following table contains links to topics that will help you learn about and manage
Exchange recipients.

                                                                                     ﾉ   Expand table

 Topic                   Description

 Create user mailboxes   Learn how to create user mailboxes using the Exchange admin center or the
 in Exchange Server      Exchange Management Shell.

 Manage user mailboxes   Learn how to create user mailboxes, change mailbox properties, and bulk-edit
                         selected properties for multiple mailboxes.

<!-- p.1034 -->

Topic                        Description

Manage distribution          Learn how to create and manage distribution groups, and create a group
groups                       naming policy for your organization.

Manage dynamic               Learn how to create dynamic distribution groups and manage dynamic
distribution groups          distribution group properties, such as using custom attributes and other
                             properties to determine group membership.

Manage mail contacts         Learn how to create and manage mail contacts.

Manage mail users            Learn how to create and manage mail users.

Create and manage            Learn how to create room mailboxes and manage room mailbox properties,
room mailboxes               such as enabling recurring meetings and configuring booking and scheduling
                             options.

Manage equipment             Learn how to create equipment mailboxes, configure booking and scheduling
mailboxes                    options, and manage other mailbox properties.

Disconnected                 Learn about the two types of disconnected mailboxes and how to work with
mailboxes                    them.

Custom attributes            Learn how to add information about a recipient by using custom attributes.

Filters in recipient Shell   Learn how to use precanned or custom filters with commands to filter a set of
commands                     recipients.

Manage permissions           Learn how to use the EAC or the Exchange Management Shell to assign
for recipients               permissions to users and groups.

Automatic Mailbox            Learn about how automatic mailbox distribution works and how to control
Distribution                 which mailbox databases are selected for new and moved mailboxes.

<!-- p.1035 -->

Create user mailboxes in Exchange Server
Article • 04/30/2025

APPLIES TO:         2016        2019     Subscription Edition

User mailboxes are Exchange mailboxes that are associated with people, typically one mailbox
per person. Each user mailbox has an associated Active Directory account that gives the person
access to the mailbox to send and receive email messages, and create meetings and
appointments.

When you create a new user mailbox in Exchange, you also create the corresponding Active
Directory user at the same time. Or, you can create a new mailbox for an existing Active
Directory account that doesn't have an associated mailbox. This is known as mailbox-enabling
an existing user.

You can create user mailboxes in Exchange Server by using the Exchange admin center (EAC) or
the Exchange Management Shell. The following table describes some of the important
properties for user mailboxes.

                                                                                           ﾉ   Expand table

 Property     Required or          Description
              optional

 Alias        Optional             The Exchange alias (also known as the mail nickname) for the mailbox.
                                   The maximum length is 64 characters. Valid characters are letters,
                                   numbers and ASCII text characters that are allowed in email addresses.
                                   For example, periods are allowed, but each period must be surrounded
                                   by other valid characters (for example, pilar.pinilla).
                                   The alias value is used to generate the primary email address (<alias>@
                                   <domain>). If you don't specify an alias value, the username part of the
                                   account name (user principal name) is used.
                                   The alias value must be unique.
                                   Note: Don't use apostrophes (') or quotation marks (") in the alias.
                                   Although these characters are allowed, they might cause problems later.

 Display      EAC: Required        Identifies the mailbox in the EAC, and in address lists in Outlook and
 name         Exchange             Outlook on the web (formerly known as Outlook Web App). The
              Management           maximum length is 256 characters. Spaces and other text characters are
              Shell: Optional      allowed.
                                   In the EAC, the display name is populated by the values that you enter
                                   for the first name, middle initial, and last name, but you can specify a
                                   custom value.
                                   In the Exchange Management Shell, if you don't specify a value for the
                                   display name, the value of the Name property is used.

<!-- p.1036 -->

 Property   Required or        Description
            optional

                               The display name value doesn't need to be unique, but having multiple
                               mailboxes with the same display name would be confusing.

 Name       Required           Specifies the name of the object in Active Directory. Only administrators
                               see this value in Exchange or Active Directory management tools. The
                               maximum length is 64 characters. Spaces and other text characters are
                               allowed.
                               The name value must be unique.

What do you need to know before you begin?
     Estimated time to complete each user mailbox task: 2 to 5 minutes.

     For more information about the EAC, see Exchange admin center in Exchange Server. To
     learn how to open the Exchange Management Shell in your on-premises Exchange
     organization, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Recipient Provisioning
     Permissions" section in the Recipients Permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

Create user mailboxes
The procedures in this section describe how to create a new mailbox and the associated Active
Directory user account.

Use the EAC to create user mailboxes
   1. In the EAC, go to Recipients > Mailboxes.

   2. Click New (   ) and then select User mailbox.

<!-- p.1037 -->

  Note: A linked mailbox is a local mailbox that's associated with a user account in a
  different (trusted) Active Directory forest. For more information, see Manage linked
  mailboxes.

3. On the New user mailbox page, configure the following settings. Settings marked with an
  asterisk (*) are required.

       Alias
       Existing user or New user: Select New user.
       First name
       Initials
       Last name
       * Display name: By default, this field is populated with the names you enter in the
       First name, Initials, and Last name fields, but you can override it. The maximum
       length is 256 characters.
       * Name: By default, this field is populated with the names you enter in the First
       name, Initials, and Last name field, but you can override it. The maximum length is
       64 characters, and the value must be unique in your organization.
       Organizational unit: Typically, the default location for the user account is the Users
       container. To change it, click Browse and select the OU or container where you want
       to create the account.
       * User logon name: This is the Active Directory user account that's created and
       associated with the mailbox.

  Notes:

       Don't use apostrophes (') or quotation marks ("). Although these characters are
       allowed, they might cause problems later (for example, assigning access permissions
       to the mailbox).

<!-- p.1038 -->

           If this value is different than the Alias value, the user's email address and account
           name will be different (important if the email domain and the Active Directory
           domain are the same).
           * New Password: Verify the value complies with your organization's password
           length, complexity, and history requirements.
           * Confirm password
           Require password change on next logon: Select this check box to force the user to
           change the initial password when they first sign in to the mailbox.

   4. You can click Save to create the mailbox and the associated Active Directory user account,
     or you can click More options to configure the following additional settings:

           Mailbox database: Click Browse to select the mailbox database that holds the
           mailbox.

           Create an on-premises archive mailbox for this user: Select this check box to create
           an archive mailbox for the mailbox, and then click Browse to select the mailbox
           database that holds the archive mailbox. Items are automatically moved from the
           primary mailbox to the archive based on the retention policy settings. For more
           information, see In-Place Archiving in Exchange Server.

           Address book policy: ABPs define a global address list (GAL), an offline address
           book (OAB), a room list, and a set of address lists. An ABP gives the user access to a
           customized GAL in Outlook and Outlook on the web. For more information, see
           Address book policies in Exchange Server.

     When you're finished, click Save.

Use the Exchange Management Shell to create user mailboxes
To create a user mailbox in the Exchange Management Shell, use the following syntax:

  PowerShell

  New-Mailbox -Name <Name> -UserPrincipalName <UPN> -Password (Read-Host "Enter
  password" -AsSecureString) [-Alias <Alias>] [-FirstName <FirstName>] [-LastName
  <LastName>] [-DisplayName <DisplayName>] -[OrganizationalUnit <OU>]

This example creates a new mailbox and Active Directory user account for Pilar Pinilla with the
following settings:

     Required parameters:
        Name: Pilar Pinilla. This value is also used for the display name, because we aren't
        using the DisplayName parameter.

<!-- p.1039 -->

        UserPrincipalName: The Active Directory account name is pilarp@contoso.com .
        Password: You're prompted to enter the password.

     Optional parameters:
        FirstName: Pilar
        LastName: Pinilla
        The alias value is pilarp because we aren't using the Alias parameter, and pilarp is
        taken from the UserPrincipalName parameter value.

  PowerShell

  New-Mailbox -Name "Pilar Pinilla" -UserPrincipalName pilarp@contoso.com -Password
  (Read-Host "Enter password" -AsSecureString) -FirstName Pilar -LastName Pinilla

For detailed syntax and parameter information, see New-Mailbox.

How do you know that you've created user mailboxes?
To verify that you've successfully created a user mailbox, use either of the following procedures:

     In the EAC, go to Recipients > Mailboxes, and verify the mailbox is displayed in the list.

     In the Exchange Management Shell, replace <Name> with the Name parameter value
     that you used, and run the following command:

        PowerShell

        Get-Mailbox -Identity <Name> | Format-List
        Name,DisplayName,Alias,PrimarySmtpAddress,Database

Create mailboxes for existing user accounts
When you mailbox-enable a user account, you can only select existing Active Directory users
that aren't already mail-enabled (no mail users or accounts that already have an associated
mailbox).

Use the EAC to create mailboxes for existing user accounts
   1. In the EAC, go to Recipients > Mailboxes.

   2. Click New (    ) and then select User mailbox.

<!-- p.1040 -->

3. On the New user mailbox page, configure the following settings.

       Alias: This setting is optional.

       Notes:

          Don't use apostrophes (') or quotation marks ("). Although these characters are
          allowed, they might cause problems later.

          If this value is different than the username part of the user principal name, the
          user's email address and account name will be different (important if the email
          domain and the Active Directory domain are the same).

       Existing user or New user: Verify Existing user is selected, and then click Browse to
       select an available account.

4. You can click Save to create the mailbox, or you can click More options to configure the
  following additional settings:

       Mailbox database: Click Browse to select the mailbox database that holds the
       mailbox.

       Create an on-premises archive mailbox for this user: Select this check box to create
       an archive mailbox for the mailbox, and then click Browse to select the mailbox
       database that holds the archive mailbox. Items are automatically moved from the
       primary mailbox to the archive based on the retention policy settings. For more
       information, see In-Place Archiving in Exchange Server.

       Address book policy: ABPs define a global address list (GAL), an offline address
       book (OAB), a room list, and a set of address lists. An ABP gives the user access to a
       customized GAL in Outlook and Outlook on the web. For more information, see
       Address book policies in Exchange Server.
