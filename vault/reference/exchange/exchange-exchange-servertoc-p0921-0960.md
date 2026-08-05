---
title: "Exchange Server — pages 921-960"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0921-0960
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0921-0960
family: exchange
documentKind: "doc"
abstract: "1. In the EAC, navigate to Permissions > Admin Roles. 2. Select the role group you want to copy and then click Copy . 3. In the New role group window, provide a name for the new role group. 4. Review the roles that have been copied to the new role group. Add or remove roles as n"
---

# Exchange Server — pages 921-960

<!-- p.921 -->

 1. In the EAC, navigate to Permissions > Admin Roles.

 2. Select the role group you want to copy and then click Copy     .

 3. In the New role group window, provide a name for the new role group.

 4. Review the roles that have been copied to the new role group. Add or remove roles as
   necessary.

 5. Review the write scope, and change it as necessary.

 6. Review the members that have been copied to the new role group. Add or remove
   members as necessary.

 7. Click Save to create the role group.

Use the Exchange Management Shell to copy a role group
with no scope
 1. Store the role group that you want to copy in a variable using the following syntax.

     PowerShell

      $RoleGroup = Get-RoleGroup <name of role group to copy>

 2. Create the new role group, and also add members to the role group and specify who can
   delegate the new role group to other users, using the following syntax.

     PowerShell

      New-RoleGroup <name of new role group> -Roles $RoleGroup.Roles -Members
      <member1, member2, member3...> -ManagedBy <user1, user2, user3...>

   For example, the following commands copy the Organization Management role group,
   and name the new role group "Limited Organization Management". It adds the members
   Isabelle, Carter, and Lukas and can be delegated by Jenny and Katie.

     PowerShell

      $RoleGroup = Get-RoleGroup "Organization Management"
      New-RoleGroup "Limited Organization Management" -Roles $RoleGroup.Roles -
      Members Isabelle, Carter, Lukas -ManagedBy Jenny, Katie

<!-- p.922 -->

After the new role group is created, you can add or remove roles, change the scope of role
assignments on the role, and more.

For detailed syntax and parameter information, see Get-RoleGroup and New-RoleGroup.

Use the Exchange Management Shell to copy a role group
with a custom scope
   1. Store the role group that you want to copy in a variable using the following syntax.

        PowerShell

        $RoleGroup = Get-RoleGroup <name of role group to copy>

   2. Create the new role group with a custom scope using the following syntax.

        PowerShell

        New-RoleGroup <name of new role group> -Roles $RoleGroup.Roles -
        CustomRecipientWriteScope <recipient scope name> -CustomConfigWriteScope
        <configuration scope name>

For example, the following commands copy the Organization Management role group and
create a new role group called Vancouver Organization Management with the Vancouver Users
recipient scope and Vancouver Servers configuration scope.

  PowerShell

  $RoleGroup = Get-RoleGroup "Organization Management"
  New-RoleGroup "Vancouver Organization Management" -Roles $RoleGroup.Roles -
  CustomRecipientWriteScope "Vancouver Users" -CustomConfigWriteScope "Vancouver
  Servers"

You can also add members to the role group when you create it by using the Members
parameter as shown in Use the Exchange Management Shell to create a role assignment with
no scope earlier in this topic. For more information about management scopes, see
Understanding Management Scopes.

After the new role group is created, you can add or remove roles, change the scope of role
assignments on the role, and perform other tasks.

For detailed syntax and parameter information, see Get-RoleGroup and New-RoleGroup.

<!-- p.923 -->

Use the Exchange Management Shell to copy a role group
with an OU scope
   1. Store the role group that you want to copy in a variable using the following syntax.

        PowerShell

        $RoleGroup = Get-RoleGroup <name of role group to copy>

   2. Create the new role group with a custom scope using the following syntax.

        PowerShell

        New-RoleGroup <name of new role group> -Roles $RoleGroup.Roles -
        RecipientOrganizationalUnitScope <OU name>

For example, the following commands copy the Recipient Management role group and create
a new role group called Toronto Recipient Management that allows management of only users
in the Toronto Users OU.

  PowerShell

  $RoleGroup = Get-RoleGroup "Recipient Management"
  New-RoleGroup "Toronto Recipient Management" -Roles $RoleGroup.Roles -
  RecipientOrganizationalUnitScope "contoso.com/Toronto Users"

You can also add members to the role group when you create it by using the Members
parameter as shown in Use the Exchange Management Shell to create a role assignment with
no scope earlier in this topic. For more information about management scopes, see
Understanding Management Scopes.

After the new role group is created, you can add or remove roles, change the scope of role
assignments on the role, and more.

For detailed syntax and parameter information, see Get-RoleGroup and New-RoleGroup.

How do you know this worked?
To verify that you have successfully copied a role group, do the following:

   1. In the EAC, navigate to Permissions > Admin Roles.

   2. Verify that the copied role group appears in the role group list, and then select it.

<!-- p.924 -->

   3. Verify that members, assigned roles, and scope that you specified on the copied role
     group are listed in the role group details pane.

Remove a role group
If you no longer need a role group you created, you can remove it. When you remove a role
group, the management role assignments between the role group and the management roles
are deleted. The management roles aren't deleted. If a user depended on the role group for
access to a feature, the user will no longer have access to the feature. You can't remove built-in
role groups.

Use the EAC to remove a role group
   1. In the EAC, navigate to Permissions > Admin Roles.

   2. Select the role group you want to remove and then click Delete     .

   3. Verify that you want to remove the selected role group, and if so, respond Yes to the
     warning.

Use the Exchange Management Shell to remove a role group
To remove a role group, see the Examples section in Remove-RoleGroup.

View role groups
You can view either a list of role groups or the detailed information about a specific role group
that exists in your organization.

Use the EAC to view a list of role groups and role group
details
   1. In the EAC, navigate to Permissions > Admin Roles. All of the role groups in your
     organization are listed here.

   2. Select a role group to view the members, assigned roles, and scope that are configured
     on the role group.

Use the Exchange Management Shell to view a list of role
groups and role group details

<!-- p.925 -->

To view a list of role groups, see the Examples section in Get-RoleGroup.

Add a role to a role group
Adding a management role to a role group is the best and simplest way to grant permissions
to a group of administrators or specialist users. If you want to give users that are members of a
role group the ability to manage a feature, you add the management role that manages the
feature to the role group. After the role is added, the members of the role group are granted
the permissions provided by the role.

Use the EAC to add a management role to a role group

  ） Important

  You can't use the EAC to add roles to a role group if you've used the Exchange
  Management Shell to configure multiple management role scopes or exclusive scopes on
  the role group. If you've configured multiple scopes or exclusive scopes on the role group,
  you must use the Exchange Management Shell procedures later in this topic to add roles
  to the role group. For more information about management role scopes, see
  Understanding Management Role Scopes.

   1. In the EAC, navigate to Permissions > Admin Roles.

   2. Select the role group you want to add a role to, and then click Edit   .

   3. In the Roles section, select the roles you want to add to the role group.

   4. When you've finished adding roles to the role group, click Save.

Use the Exchange Management Shell to create a role
assignment with no scope
You can create a role assignment with no scope between a role and a role group. When you do
this, the implicit read and implicit write scopes of the role apply.

Use the following syntax to assign a role without any scope to a role group. A role assignment
name is created automatically if you don't specify one.

  PowerShell

  New-ManagementRoleAssignment -SecurityGroup <role group name> -Role <role name>

<!-- p.926 -->

This example assigns the Transport Rules management role to the Seattle Compliance role
group.

  PowerShell

  New-ManagementRoleAssignment -SecurityGroup "Seattle Compliance" -Role "Transport
  Rules"

For detailed syntax and parameter information, see New-ManagementRoleAssignment.

Use the Exchange Management Shell to create a role
assignment with a predefined scope
If a predefined scope meets your business requirements, you can apply that scope to the role
assignment rather than create a new one. For a list of predefined scopes and their descriptions,
see Understanding Management Role Scopes.

For more information about role assignments, see Understanding Management Role
Assignments.

Use the following syntax to assign a role to a role group with a predefined scope. A role
assignment name is created automatically if you don't specify one.

  PowerShell

  New-ManagementRoleAssignment -SecurityGroup <role group name> -Role <role name> -
  RecipientRelativeWriteScope < MyGAL | MyDistributionGroups | Organization | Self >

This example assigns the Message Tracking role to the Enterprise Support role group and
applies the Organization predefined scope.

  PowerShell

  New-ManagementRoleAssignment -SecurityGroup "Enterprise Support" -Role "Message
  Tracking" -RecipientRelativeWriteScope Organization

For detailed syntax and parameter information, see New-ManagementRoleAssignment.

Use the Exchange Management Shell to create a role
assignment with a recipient filter-based scope
If you created a recipient filter-based scope, you need to include the scope in the command
used to assign the role to a role group by using the CustomRecipientWriteScope parameter.

<!-- p.927 -->

You can also include a configuration write scope when you create a role assignment that has a
recipient write scope.

For more information about role assignments and scopes, see the following topics:

     Understanding Management Role Assignments

     Understanding Management Role Scopes

Use the following syntax to assign a role to a role group with a recipient filter-based scope. A
role assignment name is created automatically if you don't specify one.

  PowerShell

  New-ManagementRoleAssignment -SecurityGroup <role group name> -Role <role name> -
  CustomRecipientWriteScope <role scope name>

This example assigns the Message Tracking role to the Seattle Recipient Admins role group and
applies the Seattle Recipients scope.

  PowerShell

  New-ManagementRoleAssignment -SecurityGroup "Seattle Recipient Admins" -Role
  "Message Tracking" -CustomRecipientWriteScope "Seattle Recipients"

For detailed syntax and parameter information, see New-ManagementRoleAssignment.

Use the Exchange Management Shell to create a role
assignment with a configuration scope
If you created a server or database configuration filter or list-based scope, you need to include
the scope in the command used to assign the role to a role group by using the
CustomConfigWriteScope parameter.

You can also include a recipient write scope when you create a role assignment that has a
configuration write scope.

For more information about role assignments and management scopes, see the following
topics:

     Understanding Management Role Assignments

     Understanding Management Role Scopes

<!-- p.928 -->

Use the following syntax to assign a role to a role group with a configuration scope. A role
assignment name is created automatically if you don't specify one.

  PowerShell

  New-ManagementRoleAssignment -SecurityGroup <role group name> -Role <role name> -
  CustomConfigWriteScope <role scope name>

This example assigns the Databases role to the Seattle Server Admins role group and applies
the Seattle Servers scope.

  PowerShell

  New-ManagementRoleAssignment -SecurityGroup "Seattle Server Admins" -Role
  "Databases" -CustomConfigWriteScope "Seattle Servers"

For detailed syntax and parameter information, see New-ManagementRoleAssignment.

Use the Exchange Management Shell to create a role
assignment with an OU scope
If you want to scope a role's write scope to an OU, you can specify the OU in the
RecipientOrganizationalUnitScope parameter directly.

For more information about role assignments and management scopes, see the following
topics:

     Understanding Management Role Assignments

     Understanding Management Role Scopes

Use the following command to assign a role to a role group and restrict the write scope of a
role to a specific OU. A role assignment name is created automatically if you don't specify one.

  PowerShell

  New-ManagementRoleAssignment -SecurityGroup <role group name> -Role <role name> -
  RecipientOrganizationalUnitScope <OU>

This example assigns the Mail Recipients role to the Seattle Recipient Admins role group and
scopes the assignment to the Sales\Users OU in the Contoso.com domain.

  PowerShell

<!-- p.929 -->

  New-ManagementRoleAssignment -SecurityGroup "Seattle Recipient Admins" -Role "Mail
  Recipients" -RecipientOrganizationalUnitScope contoso.com/sales/users

For detailed syntax and parameter information, see New-ManagementRoleAssignment.

How do you know this worked?
To verify that you have successfully added roles to a role group, do the following:

   1. In the EAC, navigate to Permissions > Admin Roles.

   2. Select the role group you added roles to. In the role group details pane, verify that the
     roles that you added are listed.

Remove a role from a role group
Removing a role from a management role group is the best and simplest way to revoke
permissions granted to a group of administrators or specialist users. If you don't want
administrators or specialist users to have permissions to manage a feature, you remove the
management role from the management role group that manages the permissions. After the
role is removed, the members of the role group will no longer have permissions to manage the
feature.

  ７ Note

  Some role groups, such as the Organization Management role group, restrict what roles
  can be removed from a role group. For more information, see Understanding
  Management Role Groups. > If an administrator is a member of another role group that
  contains management roles that grants permissions to manage the feature, you need to
  either remove the administrator from the other role groups, or remove the role that grants
  permissions to manage the feature from the other role groups.

Use the EAC to remove a management role from a role group

  ） Important

  You can't use the EAC to remove roles from a role group if you've used the Exchange
  Management Shell to configure multiple scopes or exclusive scopes on the role group. If
  you've configured multiple scopes or exclusive scopes on the role group, you must use

<!-- p.930 -->

  the Exchange Management Shell procedures later in this topic to remove roles from the
  role group. For more information about management role scopes, see Understanding
  Management Role Scopes.

   1. In the EAC, navigate to Permissions > Admin Roles.

   2. Select the role group you want to remove a role from, and then click Edit   .

   3. In the Roles section, select the roles you want to remove from the role group.

   4. When you've finished removing roles from the role group, click Save.

Use the Exchange Management Shell to remove a role from a
role group
You can remove roles from role groups by retrieving the associated management role
assignment using the Get-ManagementRoleAssignment cmdlet and then piping the role
assignment returned to the Remove-ManagementRoleAssignment cmdlet. Unless you want to
remove both delegating and regular role assignments at the same time, specify the Delegating
parameter to specify whether you want to remove regular or delegating role assignments.

For more information about regular and delegating role assignments, see Understanding
Management Role Assignments.

This procedure uses pipelining. For more information about pipelining, see about_Pipelines.

To remove a role from a role group, use the following syntax.

  PowerShell

  Get-ManagementRoleAssignment -RoleAssignee <role group name> -Role <role name> -
  Delegating <$true | $false> | Remove-ManagementRoleAssignment

This example removes the Distribution Groups role, which enables administrators to manage
distribution groups, from the Seattle Recipient Administrators role group. Because we want to
remove the role assignment that provides permissions to manage distribution groups, the
Delegating parameter is set to $False , which returns only regular role assignments.

  PowerShell

  Get-ManagementRoleAssignment -RoleAssignee "Seattle Recipient Administrators" -
  Role "Distribution Groups" -Delegating $false | Remove-ManagementRoleAssignment

<!-- p.931 -->

For detailed syntax and parameter information, see Remove-ManagementRoleAssignment.

How do you know this worked?
To verify that you have successfully removed roles from a role group, do the following:

   1. In the EAC, navigate to Permissions > Admin Roles.

   2. Select the role group you removed roles from. In the role group details pane, verify that
     the roles that you removed are no longer listed.

Change a role group's scope
The management role assignments between a role group and a role contain management
scopes, which determine what objects are made available to members of that role group. By
changing the write scope on a role group, you can change what objects are made available to
role group members to create, change, or remove. You can't change the read scope on a role
group.

Exchange Server includes scopes that are applied by default to role assignments when no
custom scopes are created. If you want to use a custom scope with a role assignment on a role
group, you must create one first. For more information about creating custom scopes, which is
an advanced task, see Create a Regular or Exclusive Scope.

For more information about management role scopes and assignments in Exchange Server, see
the following topics:

     Understanding Management Role Scopes

     Understanding Management Role Assignments

Use the EAC to change the scope on a role group
When you use the EAC to change the scope on a role group, you're actually changing the
scope on all the role assignments between the role group and each of the management roles
assigned to the role group. If you want to change the scope on specific role assignments, you
must use the Exchange Management Shell procedures later in this topic.

  ） Important

  You can't use the EAC to manage scopes on role assignments between roles and a role
  group if you've used the Exchange Management Shell to configure multiple scopes or

<!-- p.932 -->

  exclusive scopes on those role assignments. If you've configured multiple scopes or
  exclusive scopes on those role assignments, you must use the Exchange Management
  Shell procedures later in this topic to manage scopes. For more information about
  management role scopes, see Understanding Management Role Scopes.

   1. In the EAC, navigate to Permissions > Admin Roles.

   2. Select the role group you want to change the scope on, and then click Edit    .

   3. Select one of the two following Write scope options:

           A write scope from the drop-down box, where you can select either the default write
           scope or a custom write scope.

           Organizational unit: Select this option and provide an organizational unit (OU) if
           you want to scope this role group to an OU.

   4. Click Save to save the changes to the role group.

Use the Exchange Management Shell to change the scope of
all role assignments on a role group at the same time
Role assignments between the role group and the roles assigned to it can use the implicit
scope obtained from the roles themselves, the same custom scope, or different custom scopes.
For more information about role assignments, see Understanding Management Role
Assignments.

The scopes on the role assignments are managed using the Set-ManagementRoleAssignment
cmdlet. You can't manage scopes using the Set-RoleGroup cmdlet.

To change the scope of all the role assignments between a role group and a set of
management roles at the same time, you need to first retrieve the role assignments on the role
group, and then set the new scope on each of the assignments. You can do this by using the
Get-ManagementRoleAssignment cmdlet to retrieve the role assignments, and then pipe
them to the Set-ManagementRoleAssignment cmdlet.

This procedure uses the concepts of pipelining and the WhatIf switch. For more information,
see the following topics:

     about_Pipelines

     WhatIf, Confirm, and ValidateOnly Switches

<!-- p.933 -->

To set the scope on all of the role assignments on a role group at the same time, use the
following syntax.

  PowerShell

  Get-ManagementRoleAssignment -RoleAssignee <name of role group> | Set-
  ManagementRoleAssignment -CustomRecipientWriteScope <recipient scope name> -
  CustomConfigWriteScope <configuration scope name> -
  RecipientRelativeScopeWriteScope < MyDistributionGroups | Organization | Self> -
  ExclusiveRecipientWriteScope <exclusive recipient scope name> -
  ExclusiveConfigWriteScope <exclusive configuration scope name> -
  RecipientOrganizationalUnitScope <organizational unit>

You use only the parameters you need to configure the scope you want to use. For example, if
you want to change the recipient scope for all role assignments on the Sales Recipient
Management role group to Direct Sales Employees, use the following command.

  PowerShell

  Get-ManagementRoleAssignment -RoleAssignee "Sales Recipient Management" | Set-
  ManagementRoleAssignment -CustomRecipientWriteScope "Direct Sales Employees"

  ７ Note

  You can use the WhatIf switch to verify that only the role assignments you want to change
  are changed. Run the preceding command with the WhatIf switch to verify the results, and
  then remove the WhatIf switch to apply the changes.

For more information about changing management role assignments, see Change a Role
Assignment.

For detailed syntax and parameter information, see Get-ManagementRoleAssignment.

Use the Exchange Management Shell to change the scope of
individual role assignments on a role group
Role assignments between the role group and the roles assigned to it can use the implicit
scope obtained from the roles themselves, the same custom scope, or different custom scopes.
For more information about role assignments, see Understanding Management Role
Assignments.

The scopes on the role assignments are managed using the Set-ManagementRoleAssignment
cmdlet. You can't manage scopes using the Set-RoleGroup cmdlet.

<!-- p.934 -->

This procedure uses the concepts of pipelining and the Format-List cmdlet. For more
information, see the following topics:

     about_Pipelines

     Working with Command Output

To change the scope on a role assignment between a role group and a management role, you
first find the name of the role assignment, and then set the scope on the role assignment.

   1. To find the names of all the role assignments on a role group, use the following
     command. By piping the management role assignments to the Format-List cmdlet, you
     can view the full name of the assignment.

        PowerShell

        Get-ManagementRoleAssignment -RoleAssignee <role group name> | Format-List
        Name

   2. Find the name of the role assignment you want to change. Use the name of the role
     assignment in the next step.

   3. To set the scope on an individual assignment, use the following syntax.

        PowerShell

        Set-ManagementRoleAssignment <role assignment name> -
        CustomRecipientWriteScope <recipient scope name> -CustomConfigWriteScope
        <configuration scope name> -RecipientRelativeScopeWriteScope <
        MyDistributionGroups | Organization | Self> -ExclusiveRecipientWriteScope
        <exclusive recipient scope name> -ExclusiveConfigWriteScope <exclusive
        configuration scope name> -RecipientOrganizationalUnitScope <organizational
        unit>

You use only the parameters you need to configure the scope you want to use. For example, if
you want to change the recipient scope for the Mail Recipients_Sales Recipient Management
role assignment to All Sales Employees, use the following command.

  PowerShell

  Set-ManagementRoleAssignment "Mail Recipients_Sales Recipient Management" -
  CustomRecipientWriteScope "All Sales Employees"

For more information about changing management role assignments, see Change a Role
Assignment.

<!-- p.935 -->

For detailed syntax and parameter information, see Set-ManagementRoleAssignment.

How do you know this worked?
To verify that you have successfully changed the scope of a role assignment on a role group,
do the following:

     If you used the EAC to configure the scope on the role group, do the following:

        1. In the EAC, navigate to Permissions> Admin Roles. All the role groups in your
          organization are listed here.

        2. Select a role group to view the scope that's configured on the role group.

     If you used the Exchange Management Shell to configure the scope on the role group, do
     the following:

        1. Run the following command in the Exchange Management Shell.

             PowerShell

             Get-ManagementRoleAssignment -RoleAssignee <role group name> | Format-
             Table *WriteScope

        2. Verify that the write scope on the role assignments has been changed to the scope
          you specified.

Add or remove a role group delegate
Role group delegates are users or universal security groups (USGs) that can add or remove
members from a role group or change the properties of a role group. By adding or removing
role group delegates, you can control who is allowed to manage a role group.

  ） Important

  After you add a delegate to a role group, the role group can only be managed by the
  delegates on the role group, or by users who are assigned, either directly or indirectly, the
  Role Management management role. > If a user is assigned, either directly or indirectly,
  the Role Management role and isn't added as a delegate of the role group, the user must
  use the BypassSecurityGroupManagerCheck switch on the Add-RoleGroupMember,
  Remove-RoleGroupMember, Update-RoleGroupMember, and Set-RoleGroup cmdlets to
  manage a role group.

<!-- p.936 -->

  ７ Note

  You can't use the EAC to add a delegate to a role group.

Use the Exchange Management Shell to add a delegate to a
role group
To change the list of delegates on a role group, you use the ManagedBy parameter on the Set-
RoleGroup cmdlet. The ManagedBy parameter overwrites the entire delegate list on the role
group. If you want to add delegates to the role group rather than replace the entire list of
delegates, use the following steps:

   1. Store the role group in a variable using the following command.

         PowerShell

         $RoleGroup = Get-RoleGroup <role group name>

   2. Add the delegate to the role group stored in the variable using the following command.

         PowerShell

         $RoleGroup.ManagedBy += (Get-User <user to add>).Identity

         ７ Note

         Use the Get-Group cmdlet if you want to add a USG.

   3. Repeat Step 2 for each delegate you want to add.

   4. Apply the new list of delegates to the actual role group using the following command.

         PowerShell

         Set-RoleGroup <role group name> -ManagedBy $RoleGroup.ManagedBy

This example adds the user David Strome as a delegate on the Organization Management role
group.

  PowerShell

<!-- p.937 -->

  $RoleGroup = Get-RoleGroup "Organization Management"
  $RoleGroup.ManagedBy += (Get-User "David Strome").Identity
  Set-RoleGroup "Organization Management" -ManagedBy $RoleGroup.ManagedBy

For detailed syntax and parameter information, see Set-RoleGroup.

Use the Exchange Management Shell to remove a delegate
from a role group
To change the list of delegates on a role group, you use the ManagedBy parameter on the Set-
RoleGroup cmdlet. The ManagedBy parameter overwrites the entire delegate list on the role
group. If you want to remove delegates from the role group rather than replace the entire list
of delegates, use the following steps:

   1. Store the role group in a variable using the following command.

        PowerShell

        $RoleGroup = Get-RoleGroup <role group name>

   2. Remove the delegate from the role group stored in the variable using the following
     command.

        PowerShell

        $RoleGroup.ManagedBy -= (Get-User <user to remove>).Identity

        ７ Note

        Use the Get-Group cmdlet if you want to remove a USG.

   3. Repeat Step 2 for each delegate you want to remove.

   4. Apply the new list of delegates to the actual role group using the following command.

        PowerShell

        Set-RoleGroup <role group name> -ManagedBy $RoleGroup.ManagedBy

This example removes the user David Strome as a delegate on the Organization Management
role group.

<!-- p.938 -->

  PowerShell

  $RoleGroup = Get-RoleGroup "Organization Management"
  $RoleGroup.ManagedBy -= (Get-User "David Strome").Identity
  Set-RoleGroup "Organization Management" -ManagedBy $RoleGroup.ManagedBy

For detailed syntax and parameter information, see Set-RoleGroup.

How do you know this worked?
To verify that you have successfully changed the delegate list on a role group, do the following:

   1. In the Exchange Management Shell, run the following command.

        PowerShell

        Get-RoleGroup <role group name> | Format-List ManagedBy

   2. Verify that the delegates listed on the ManagedBy property include only the delegates
     that should be able to manage the role group.

<!-- p.939 -->

Manage role group members in Exchange
Server
07/23/2025

APPLIES TO:      2016       2019    Subscription Edition

To learn about role groups in Exchange Server, see Understanding Management Role Groups.

For additional management tasks related to role groups, see Permissions.

What do you need to know before you begin?
     Estimated time to complete each procedure: 5 minutes

     To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
     Management Shell, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Role groups" entry in the Role
     management permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Add members to a role group
To give a user the permissions that are granted by a role group, you need to add the user, or a
universal security group (USG), or another role group that the user is a member of, as a
member of the role group.

Use the EAC to add members to a role group
   1. In the Exchange admin center (EAC), navigate to Permissions > Admin Roles.

   2. Select the role group you want to add members to, and then click Edit    .

<!-- p.940 -->

   3. In the Members section, click Add    .

   4. Select the users, USGs, or other role groups you want to add to the role group, click Add,
     and then click OK.

   5. Click Save to save the changes to the role group.

Use the Exchange Management Shell to add members to a
role group
To add a role group member, see the Examples section in Add-RoleGroupMember.

To add multiple role group members or to replace the role group membership entirely, see the
Examples section in Update-RoleGroupMember.

How do you know this worked?
To verify that you have successfully added one or more members to a role group, do the
following:

   1. In the EAC, navigate to Permissions > Admin Roles.

   2. Select the role group you added members to.

   3. In the role group details pane, verify that the members you added are listed.

Remove members from a role group
To remove the permissions granted by a role group from a user, you need to remove the user,
or the universal security group (USG) the user is a member of, from the role group's
membership.

Use the EAC to remove members from a role group
   1. In the EAC, navigate to Permissions > Admin Roles.

   2. Select the role group you want to remove members from, and then click Edit       .

   3. In the Members section, select the members you want to remove, click Remove          , and
     then click Save.

<!-- p.941 -->

Use the Exchange Management Shell to remove members
from a role group
To remove a role group member, see the Examples section in Remove-RoleGroupMember.

To remove multiple role group members or to replace the role group membership entirely, see
the Examples section in Update-RoleGroupMember.

How do you know this worked?
To verify that you have successfully removed one or more members to a role group, do the
following:

   1. In the EAC, navigate to Permissions > Admin Roles.

   2. Select the role group you removed members from.

   3. In the role group details pane, verify that the members you removed are no longer listed.

View the members of a role group
The members of a role group are granted the permissions provided by the management roles
assigned to the role group. You can view the members of a role group to see which users,
universal security groups (USG), or other role groups are granted permissions by the role group
you specify.

Use the EAC to view the members of a role group
   1. In the EAC, navigate to Permissions > Admin Roles.

   2. Select the role group you want to view the members of.

   3. In the role group details pane, view the members in the role group details pane.

Use the Exchange Management Shell to view the members of
a role group
To view the members of a role group, see the "Examples" section in Get-RoleGroupMember.

<!-- p.942 -->

Manage role assignment policies in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

If you want to customize the permissions that you assign to a group of end users, create a new
custom management role assignment policy. The assignment policy you create can be
customized to suit your end user's specific requirements. For more information about
assignment policies in Exchange Server, see Understanding Management Role Assignment
Policies.

Looking for other management tasks related to managing permissions? Check out Permissions.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes

      To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
      Management Shell, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Assignment policies" entry in the
      Role management permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online        , or Exchange Online Protection .

Add an assignment policy
After you've created the new assignment policy, you assign users to it. For more information,
see Change the assignment policy on a mailbox.

Use the EAC to create a new assignment policy

<!-- p.943 -->

  ７ Note

  You can only create explicit assignment policies using the Exchange admin center (EAC). If
  you want to create a new default assignment policy, you must use the Exchange
  Management Shell. For more information, see the "Use the Exchange Management Shell
  to create a default assignment policy" section later in this topic.

   1. In the EAC, navigate to Permissions > User Roles and then click Add     .

   2. In the role assignment policy window, provide a name for the new assignment policy.

   3. Select the check box next to the role or roles you want to add to the assignment policy.
     You can select multiple roles, including end-user roles you've added. If you select a role
     that has child roles, the child roles are automatically selected.

   4. Click Save to save the changes to the assignment policy.

Use the Exchange Management Shell to create an explicit
assignment policy
To create an explicit assignment policy that can be manually assigned to mailboxes, use the
following syntax.

  PowerShell

  New-RoleAssignmentPolicy <assignment policy name> -Roles <roles to assign>

This example creates the explicit assignment policy Limited Mailbox Configuration and assigns
the MyBaseOptions , MyAddressInformation , and MyDisplayName roles to it.

  PowerShell

  New-RoleAssignmentPolicy "Limited Mailbox Configuration" -Roles MyBaseOptions,
  MyAddressInformation, MyDisplayName

For detailed syntax and parameter information, see New-RoleAssignmentPolicy.

Use the Exchange Management Shell to create a default
assignment policy
To create a default assignment policy assigned to new mailboxes, use the following syntax.

<!-- p.944 -->

  PowerShell

  New-RoleAssignmentPolicy <assignment policy name> -Roles <roles to assign> -
  IsDefault

This example creates the default assignment policy Limited Mailbox Configuration and assigns
the MyBaseOptions , MyAddressInformation , and MyDisplayName roles to it.

  PowerShell

  New-RoleAssignmentPolicy "Limited Mailbox Configuration" -Roles MyBaseOptions,
  MyAddressInformation, MyDisplayName -IsDefault

For detailed syntax and parameter information, see New-RoleAssignmentPolicy.

Remove an assignment policy
If you no longer need a management role assignment policy, you can remove it.

What do you need to know before you begin?
     All users assigned the assignment policy must be changed to another assignment policy.
     For more information about how to change an assignment policy on a mailbox, see
     Change the assignment policy on a mailbox.

     All the management role assignments between the assignment policy and the assigned
     management roles must be removed. For more information about how to remove a role
     assignment from an assignment policy, see the Remove a role from an assignment policy
     section later in this topic.

     If you want to remove a default assignment policy, it must be the last assignment policy
     in the Exchange Server organization.

Use the EAC to remove an assignment policy
   1. In the EAC, navigate to Permissions > User Roles.

   2. Select the assignment policy you want to remove, and then click Delete   .

Use the Exchange Management Shell to remove an assignment policy

To remove an assignment policy, use the following syntax.

<!-- p.945 -->

  PowerShell

  Remove-RoleAssignmentPolicy <role assignment policy>

This example removes the New York Temporary Users assignment policy.

  PowerShell

  Remove-RoleAssignmentPolicy "New York Temporary Users"

For detailed syntax and parameter information, see Remove-RoleAssignmentPolicy.

View a list of assignment policies or assignment policy details
You can view management role assignment policies in a variety of ways, depending on the
information you want and whether you're using the EAC or the Exchange Management Shell.

In the EAC, you can view the list of assignment policies and the roles assigned to them. In the
Exchange Management Shell, you can view all the assignment policies in your organization, list
the mailboxes assigned a specific policy, and more.

Use the EAC to view a list of assignment policies
   1. In the EAC, navigate to Permissions > User Roles. All of the assignment policies in the
     organization are listed here.

   2. To view the details of a specific assignment policy, select the assignment policy you want
     to view. The description and the roles assigned to the assignment policy are displayed in
     the details pane.

Use the Exchange Management Shell to view a list of assignment
policies
You can view a list of all the assignment policies in your organization by not specifying any
assignment policies when you run the Get-RoleAssignmentPolicy cmdlet.

This procedure makes use of pipelining and the Format-Table cmdlet. For more information
about these concepts, see the following topics:

     about_Pipelines

     Working with Command Output

<!-- p.946 -->

To return a list of all assignment policies in your organization, use the following command.

  PowerShell

  Get-RoleAssignmentPolicy

To return a list of specific properties for all the assignment policies in your organization, you
can pipe the results to the Format-Table cmdlet and specify the properties you want in the list
of results. Use the following syntax.

  PowerShell

  Get-RoleAssignmentPolicy | Format-Table <property 1>, <property 2...>

This example returns a list of all the assignment policies in your organization and includes the
Name and IsDefault properties.

  PowerShell

  Get-RoleAssignmentPolicy | Format-Table Name, IsDefault

For detailed syntax and parameter information, see Get-Mailbox or Get-RoleAssignmentPolicy.

Use the Exchange Management Shell to view the details of a single
assignment policy
You can view the details of a specific assignment policy by using the Get-
RoleAssignmentPolicy cmdlet and piping the output to the Format-List cmdlet.

This procedure makes use of pipelining and the Format-List cmdlet. For more information
about these concepts, see the following topics:

     about_Pipelines

     Working with Command Output

To view the details of a specific assignment policy, use the following syntax.

  PowerShell

  Get-RoleAssignmentPolicy <assignment policy name> | Format-List

<!-- p.947 -->

This example views the details about the Redmond Users - no Text Messaging assignment
policy.

  PowerShell

  Get-RoleAssignmentPolicy "Redmond Users - no Text Messaging" | Format-List

For detailed syntax and parameter information, see Get-Mailbox or Get-RoleAssignmentPolicy.

Use the Exchange Management Shell to find the default assignment
policy

You can find the default assignment policy by piping the output of the Get-
RoleAssignmentPolicy cmdlet to the Where cmdlet. With the Where cmdlet, filter the data
returned to display only the assignment policy that has its IsDefault property set to $True .

This procedure makes use of pipelining and the Where cmdlet. For more information about
these concepts, see the following topics:

     about_Pipelines

     Working with Command Output

This example returns the default assignment policy.

  PowerShell

  Get-RoleAssignmentPolicy | Where {$_.IsDefault -eq $True}

For detailed syntax and parameter information, see Get-Mailbox or Get-RoleAssignmentPolicy.

Use the Exchange Management Shell to view mailboxes that are
assigned a specific policy
You can find all the mailboxes assigned a specific assignment policy by piping the output of
the Get-Mailbox cmdlet to the Where cmdlet. With the Where cmdlet, filter the data returned
to display only the mailboxes that have their RoleAssignmentPolicy property set to the
assignment policy name you specify.

This procedure makes use of pipelining and the Where cmdlet. For more information about
these concepts, see the following topics:

     about_Pipelines

<!-- p.948 -->

     Working with Command Output

Use the following syntax.

  PowerShell

  Get-Mailbox | Where {$_.RoleAssignmentPolicy -Eq "<role assignment policy>"}

This example finds all the mailboxes assigned the policy Vancouver End Users.

  PowerShell

  Get-Mailbox | Where {$_.RoleAssignmentPolicy -Eq "Vancouver End Users"}

For detailed syntax and parameter information, see Get-Mailbox or Get-RoleAssignmentPolicy.

Change the default assignment policy
You can change the management role assignment policy assigned to new mailboxes that are
created. Changing the default role assignment policy doesn't change the assignment policy
assigned to existing mailboxes. To change the assignment policy assigned to existing
mailboxes, see Change the assignment policy on a mailbox.

  ７ Note

  You can't use the EAC to change the default assignment policy. You need to use the
  Exchange Management Shell.

Use the Exchange Management Shell to change the default assignment
policy
To change the default assignment policy, use the following syntax.

  PowerShell

  Set-RoleAssignmentPolicy <assignment policy name> -IsDefault

This example sets the Vancouver End Users assignment policy as the default assignment policy.

  PowerShell

<!-- p.949 -->

  Set-RoleAssignmentPolicy "Vancouver End Users" -IsDefault

  ） Important

  New mailboxes are assigned the default assignment policy even if the policy hasn't been
  assigned management roles. Mailboxes assigned assignment policies with no assigned
  management roles can't access any mailbox configuration features in Outlook on the web.

For detailed syntax and parameter information, see Set-RoleAssignmentPolicy.

Add a role to an assignment policy

Use the EAC to add a role to an assignment policy
   1. In the EAC, navigate to Permissions > User Roles.

   2. Select the assignment policy you want to add one or more roles to, and then click Edit      .

   3. Select the check box next to the role or roles you want to add to the assignment policy.
     You can select multiple roles, including end-user roles you've added. If you select a role
     that has child roles, the child roles are automatically selected.

   4. Click Save to save the changes to the assignment policy.

Use the Exchange Management Shell to add a role to an assignment
policy

To create a management role assignment between a role and an assignment policy, use the
following syntax.

  PowerShell

  New-ManagementRoleAssignment -Name <role assignment name> -Role <role name> -
  Policy <assignment policy name>

This example creates the role assignment Seattle Users - Voicemail between the MyVoicemail
role and the Seattle Users assignment policy.

  PowerShell

<!-- p.950 -->

  New-ManagementRoleAssignment -Name "Seattle Users - Voicemail" -Role MyVoicemail -
  Policy "Seattle Users"

For detailed syntax and parameter information, see New-ManagementRoleAssignment.

Remove a role from an assignment policy
If you don't want end users to have permissions to manage certain features of their mailbox or
distribution group, you can remove the management role that grants the permissions from the
management role assignment policy to which the user is assigned. If other users are assigned
the same assignment policy, they also lose the ability to manage that feature.

Use the EAC to remove a role from an assignment policy
   1. In the EAC, navigate to Permissions > User Roles.

   2. Select the assignment policy you want to remove one or more roles from, and then click
     Edit      .

   3. Clear the check box next to the role or roles you want to remove from the assignment
     policy. If you clear the check box for a role that has child roles, the check boxes for the
     child roles are also cleared.

   4. Click Save to save the changes to the assignment policy.

Use the Exchange Management Shell to remove a role from an
assignment policy
You can remove roles from assignment policies by retrieving the associated management role
assignment using the Get-ManagementRoleAssignment cmdlet and then piping the role
assignment returned to the Remove-ManagementRoleAssignment cmdlet.

For more information about regular and delegating role assignments, see Understanding
Management Role Assignments.

This procedure uses pipelining. For more information about pipelining, see about_Pipelines.

To remove a role from an assignment policy, use the following syntax.

  PowerShell

  Get-ManagementRoleAssignment -RoleAssignee <assignment policy name> -Role <role

<!-- p.951 -->

  name> | Remove-ManagementRoleAssignment

This example removes the MyVoicemail management role, which enables users to manage
their voice mail options, from the Seattle Users assignment policy.

  PowerShell

  Get-ManagementRoleAssignment -RoleAssignee "Seattle Users" -Role MyVoicemail |
  Remove-ManagementRoleAssignment

For detailed syntax and parameter information, see Remove-ManagementRoleAssignment.

<!-- p.952 -->

Exchange Server: Change the assignment
policy on a mailbox
07/23/2025

APPLIES TO:      2016       2019    Subscription Edition

When you change a mailbox's assignment policy, the change takes effect as soon as the user
refreshes the connection, such as the next time they log into their mailbox or open the mailbox
options page. For more information about assignment policies in Exchange Server, see
Understanding Management Role Assignment Policies.

Looking for other management tasks related to permissions? Check out Permissions.

What do you need to know before you begin?
     Estimated time to complete each procedure: 5 minutes

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Role groups" entry in the Role
     management permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the EAC to change the assignment policy on a
mailbox
   1. In the Exchange admin center (EAC), navigate to Recipients > Mailboxes.

   2. Select the user or resource mailbox you want to change the assignment policy on and
     then click Edit    .

   3. Select Mailbox Features.

<!-- p.953 -->

   4. In the Role assignment policy list, select the assignment policy you want to assign to the
     mailbox and then click Save.

Use the Exchange Management Shell to change
the assignment policy on a mailbox
To change the assignment policy that's assigned to a mailbox, use the following syntax.

  PowerShell

  Set-Mailbox <mailbox alias or name> -RoleAssignmentPolicy <assignment policy>

This example sets the assignment policy to Engineering Users on the mailbox Brian.

  PowerShell

  Set-Mailbox Brian -RoleAssignmentPolicy "Engineering Users"

Use the Exchange Management Shell to change
the assignment policy on a group of mailboxes
assigned a specific assignment policy

  ７ Note

  You can't use the EAC to change the assignment policy on a group of mailboxes all at
  once.

This procedure makes use of pipelining, the Where cmdlet, and the WhatIf parameter. For
more information about these concepts, see the following topics:

     about_Pipelines

     Working with Command Output

     WhatIf, Confirm, and ValidateOnly Switches

If you want to change the assignment policy for a group of mailboxes that are assigned a
specific policy, use the following syntax.

  PowerShell

<!-- p.954 -->

  Get-Mailbox | Where {$_.RoleAssignmentPolicy -Eq "<assignment policy to find>"} |
  Set-Mailbox -RoleAssignmentPolicy <assignment policy to set>

This example finds all the mailboxes assigned to the Redmond Users - No Voicemail
assignment policy and changes the assignment policy to Redmond Users - Voicemail Enabled.

  PowerShell

  Get-Mailbox | Where {$_.RoleAssignmentPolicy -Eq "Redmond Users - No Voicemail"} |
  Set-Mailbox -RoleAssignmentPolicy "Redmond Users - Voicemail Enabled"

This example includes the WhatIf parameter so that you can see all the mailboxes that would
be changed without committing any changes.

  PowerShell

  Get-Mailbox | Where {$_.RoleAssignmentPolicy -Eq "Redmond Users - No Voicemail"} |
  Set-Mailbox -RoleAssignmentPolicy "Redmond Users - Voicemail Enabled" -WhatIf

For detailed syntax and parameter information, see Get-Mailbox or Set-Mailbox.

<!-- p.955 -->

Feature permissions in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Permissions in Microsoft Exchange Server are managed using the Role Based Access Control
(RBAC) permissions model. The following topics identify the management role groups required
to administer the features associated with each functional area in Exchange Server.

      Role management permissions

      Messaging policy and compliance in Exchange Server

      Antispam and antimalware permissions

      Mail flow permissions

      Recipients Permissions

      Email address and address book permissions

      Sharing and collaboration permissions

      Clients and mobile devices permissions

      Unified Messaging permissions

      High availability and site resilience permissions

      Exchange infrastructure and PowerShell permissions

      Server health and performance permissions

<!-- p.956 -->

Role management permissions in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The permissions required to perform tasks to configure management roles vary depending on
the procedure being performed or the cmdlet you want to run. For more information about
management roles, see Understanding Management Roles.

To find out what permissions you need to perform the procedure or run the cmdlet, do the
following:

   1. In the table below, find the feature that is most related to the procedure you want to
      perform or the cmdlet you want to run.

   2. Next, look at the permissions required for the feature. You must be assigned one of those
      role groups, an equivalent custom role group, or an equivalent management role. You can
      also click on a role group to see its management roles. If a feature lists more than one
      role group, you only need to be assigned one of the role groups to use the feature. For
      more information about role groups and management roles, see Understanding Role
      Based Access Control.

   3. Now, run the Get-ManagementRoleAssignment cmdlet to look at the role groups or
      management roles assigned to you to see if you have the permissions that are necessary
      to manage the feature.

        ７ Note

        You must be assigned the Role Management management role to run the Get-
        ManagementRoleAssignment cmdlet. If you don't have permissions to run the Get-
        ManagementRoleAssignment cmdlet, ask your Exchange administrator to retrieve
        the role groups or management roles assigned to you.

If you want to delegate the ability to manage a feature to another user, see Delegate role
assignments.

Role management permissions
You can use the features in the following table to manage the management role groups, roles,
assignment policies, assignments, scopes that define the permissions you can apply to

<!-- p.957 -->

administrators, and end users. Users who are assigned the View-Only Management role group
can view the configuration of the features in the following table. For more information, see
View-only Organization Management.

                                                                                    ﾉ   Expand table

 Feature             Permissions required

 Management roles    Organization Management

 Unscoped            Unscoped Role Management management role
 management roles

 Role groups         Organization Management

 Assignment          Organization Management
 policies

 Role assignments    Organization Management

 Management          Organization Management
 scopes

 Management role     Organization Management
 entries

 Legacy              Organization Management
 permissions

 Active Directory    Organization Management
 split permissions   Important: To run the setup.exe command with the PrepareAD and
                     ActiveDirectorySplitPermissions parameters, the account you use must be a member
                     of the Schema Admins and Enterprise Administrators groups.

<!-- p.958 -->

Messaging policy and compliance
permissions in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The permissions required to configure messaging policy and compliance vary depending on
the procedure being performed or the cmdlet you want to run. For more information about
messaging policy and compliance, see Messaging policy and compliance in Exchange Server.

To find out what permissions you need to perform the procedure or run the cmdlet, do the
following:

   1. In the table below, find the feature that is most related to the procedure you want to
      perform or the cmdlet you want to run.

   2. Next, look at the permissions required for the feature. You must be assigned one of those
      role groups, an equivalent custom role group, or an equivalent management role. You can
      also click on a role group to see its management roles. If a feature lists more than one
      role group, you only need to be assigned one of the role groups to use the feature. For
      more information about role groups and management roles, see Understanding Role
      Based Access Control.

   3. Now, run the Get-ManagementRoleAssignment cmdlet to look at the role groups or
      management roles assigned to you to see if you have the permissions that are necessary
      to manage the feature.

        ７ Note

        You must be assigned the Role Management management role to run the Get-
        ManagementRoleAssignment cmdlet. If you don't have permissions to run the Get-
        ManagementRoleAssignment cmdlet, ask your Exchange administrator to retrieve
        the role groups or management roles assigned to you.

If you want to delegate the ability to manage a feature to another user, see Delegate role
assignments.

Messaging policy and compliance permissions
You can use the features in the following table to configure messaging policy and compliance
features. The role groups that are required to configure each feature are listed.

<!-- p.959 -->

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-Only Organization
Management.

                                                                                          ﾉ   Expand table

 Feature                   Permissions required

 Data loss prevention      Compliance Management
 (DLP)

 Delete mailbox content    Discovery Management and
 (using the Search-        Mailbox Import Export Role
 Mailbox cmdlet with the
 DeleteContent switch)     Note: By default, the Mailbox Import Export role isn't assigned to any role
                           group. You can assign a management role to a built-in or custom role group,
                           a user, or a universal security group. Assigning a role to a role group is
                           recommended. For more information, see Add a role to a role group.

 Discovery mailboxes -     Organization Management
 Create                    Recipient Management

 Information Rights        Compliance Management
 Management (IRM)          Organization Management
 configuration

 In-Place Archive          Organization Management
                           Recipient Management

 In-Place Archive - Test   Organization Management
 connectivity              Server Management

 In-Place eDiscovery       Discovery Management

                           Note: By default, the Discovery Management role group doesn't have any
                           members. No users, including administrators, have the required permissions
                           to search mailboxes. For more information, see Assign eDiscovery
                           permissions in Exchange Server.

 In-Place Hold             Discovery Management
                           Organization Management

                           Notes:

                                 To create a query-based In-Place Hold, a user requires both the
                                 Mailbox Search and Legal Hold roles to be assigned directly or via
                                 membership in a role group that has both roles assigned. To create an
                                 In-Place Hold without using a query, which places all mailbox items on
                                 hold, you must have the Legal Hold role assigned. The Discovery
                                 Management role group is assigned both roles.

<!-- p.960 -->

Feature                     Permissions required

                                 The Organization Management role group is assigned the Legal Hold
                                 role. Members of the Organization Management role group can place
                                 an In-Place Hold on all items in a mailbox, but can't create a query-
                                 based In-Place Hold.

Journaling                  Organization Management
                            Records Management

Litigation Hold             Organization Management

Mailbox audit logging       Organization Management
                            Records Management

Message classifications     Organization Management

Messaging records           Compliance Management
management                  Organization Management
                            Records Management

Retention policies -        Organization Management
Apply                       Recipient Management
                            Records Management

Retention policies -        See the entry for Messaging records management
Create

Mail flow rules (also       Organization Management
known as transport rules)   Records Management
