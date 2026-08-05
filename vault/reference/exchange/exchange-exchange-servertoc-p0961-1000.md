---
title: "Exchange Server — pages 961-1000"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0961-1000
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0961-1000
family: exchange
documentKind: "doc"
abstract: "Antispam and antimalware permissions Article • 04/30/2025 APPLIES TO: 2016 2019 Subscription Edition The permissions required to perform tasks related to antispam and antimalware vary depending on the procedure being performed or the cmdlet you want to run. For more information"
---

# Exchange Server — pages 961-1000

<!-- p.961 -->

Antispam and antimalware permissions
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The permissions required to perform tasks related to antispam and antimalware vary
depending on the procedure being performed or the cmdlet you want to run. For more
information about transport features, see Mail flow and the transport pipeline.

This topic lists the permissions required to manage the mail flow features in Microsoft
Exchange Server.

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

  ７ Note

  Some features that you want to manage might exist on Edge Transport servers. To manage
  features on Edge Transport servers, you need to become a member of the Local

<!-- p.962 -->

  Administrators group on the Edge Transport server you want to manage. Edge Transport
  servers don't use Role Based Access Control (RBAC). Features that can be managed on
  Edge Transport servers have Edge Transport Local Administrator in the "Permissions
  required" column in the table below.

  ７ Note

  Some features may require that you have local administrator permissions on the server
  you want to manage. To manage these features, you must be a member of the Local
  Administrators group on that server.

Antispam and Anti-Malware Permissions
You can use the features in the following tables to configure antispam and antimalware
settings in your organization. The permissions that are required to configure each feature are
listed.

Users who are assigned the View Only Management role group can view the configuration of
the features shown in the following table. For more information, see View Only Organization
Management.

                                                                                   ﾉ      Expand table

 Feature                                      Permissions required

 Anti-malware                                 Organization Management
                                              Hygiene Management

 Antispam features                            Organization Management
                                              Hygiene Management

 Antispam features - Edge Transport           Edge Transport server local administrator

<!-- p.963 -->

Mail flow permissions in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

The permissions required to perform tasks related to mail flow vary depending on the
procedure being performed or the cmdlet you want to run. For more information about
transport features, see Mail flow and the transport pipeline.

This topic lists the permissions required to manage the mail flow features in Exchange Server
2016 and Exchange Server 2019. For information about how Microsoft 365 or Office 365
permissions relate to Exchange permissions, see About admin roles.

To find out what permissions you need to perform the procedure or run the cmdlet, do the
following:

   1. In the table below, find the feature that is most related to the procedure you want to
      perform or the cmdlet you want to run.

   2. Next, look at the permissions required for the feature. You must be assigned one of those
      role groups, an equivalent custom role group, or an equivalent management role. You can
      also click a role group to see its management roles. If a feature lists more than one role
      group, you need to be assigned to only one of the role groups to use the feature. For
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

  ７ Note

<!-- p.964 -->

  Some features that you want to manage might exist on Edge Transport servers. To manage
  features on Edge Transport servers, you need to become a member of the Local
  Administrators group on the Edge Transport server you want to manage. Edge Transport
  servers don't use Role Based Access Control (RBAC). Features that can be managed on
  Edge Transport servers have Edge Transport Local Administrator in the "Permissions
  required" column in the table below.

  ７ Note

  Some features may require that you have local administrator permissions on the server
  you want to manage. To manage these features, you must be a member of the Local
  Administrators group on that server.

Mail flow permissions
You can use the features in the following tables to configure mail flow settings in the Front End
Transport, Mailbox Transport, and Transport services on Mailbox servers, and on Edge Transport
servers. The permissions that are required to configure each feature are listed.

Users who are assigned the View Only Management role group can view the configuration of
the features shown in the following table. For more information, see View Only Organization
Management.

Mailbox servers

                                                                                   ﾉ   Expand table

 Feature                                                            Permissions required

 Accepted domains                                                   Organization Management

 Active Directory site and site link management                     Organization Management

 Antispam features                                                  Organization Management
                                                                    Hygiene Management

 Antispam updates                                                   Organization Management
                                                                    Hygiene Management

 Certificate management                                             Organization Management

 Delivery Agent connectors                                          Organization Management
                                                                    Server Management

<!-- p.965 -->

Feature                            Permissions required

DSNs                               Organization Management

EdgeSync                           Organization Management

Foreign connectors                 Organization Management

Front End Transport service        Organization Management
                                   Server Management
                                   Hygiene Management

Journaling                         Organization Management
                                   Records Management

Mailbox access                     Organization Management

Mailbox junk email configuration   Organization Management
                                   Records Management
                                   Recipient Management
                                   Help Desk

Mailbox Transport service          Organization Management
                                   Server Management
                                   Hygiene Management

MailTips                           Organization Management

Message classifications            Organization Management
                                   Records Management

Message tracking                   Organization Management
                                   Records Management
                                   Recipient Management

Moderated transport                Organization Management
                                   Recipient Management

Queues                             Organization Management
                                   Server Management

Receive connectors                 Organization Management
                                   Server Management
                                   Hygiene Management

Remote domains                     Organization Management

SafeList aggregation               Organization Management
                                   Records Management

Send connectors                    Organization Management

<!-- p.966 -->

 Feature                                                                     Permissions required

 Shadow redundancy                                                           Organization Management

 Testing mail flow                                                           Organization Management
                                                                             Server Management

 Testing mail flow rule (also known as transport rule) processing            Organization Management

 Transport agents                                                            Organization Management
                                                                             Records Management

 Transport configuration                                                     Organization Management

 Transport logs                                                              Organization Management
                                                                             Server Management

 Mail flow rules (also known as transport rules)                             Organization Management
                                                                             Records Management

 Transport service                                                           Organization Management
                                                                             Server Management
                                                                             Hygiene Management

 X.400 domains                                                               Organization Management

Edge Transport servers

                                                                                           ﾉ      Expand table

 Feature                                                            Permissions required

 Accepted domains - Edge Transport                                  Edge Transport server local
                                                                    administrator

 Address Rewriting - Edge Transport                                 Edge Transport server local
                                                                    administrator

 Edge Transport server                                              Edge Transport server local
                                                                    administrator

 EdgeSync - Edge Transport                                          Edge Transport server local
                                                                    administrator

 Queues - Edge Transport                                            Edge Transport server local
                                                                    administrator

 Receive connectors - Edge Transport                                Edge Transport server local
                                                                    administrator

<!-- p.967 -->

Feature                                                  Permissions required

Send connectors - Edge Transport                         Edge Transport server local
                                                         administrator

Transport configuration - Edge Transport                 Edge Transport server local
                                                         administrator

Transport logs - Edge Transport                          Edge Transport server local
                                                         administrator

Mail flow rules (also known as transport rules) - Edge   Edge Transport server local
Transport                                                administrator

<!-- p.968 -->

Recipients permissions in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The permissions required to perform tasks to manage recipients vary depending on the
procedure being performed or the cmdlet you want to run.

To find out what permissions you need to perform the procedure or run the cmdlet, do the
following:

   1. In the table below, find the feature that is most related to the procedure you want to
      perform or the cmdlet you want to run.

   2. Next, look at the permissions required for the feature. You must be assigned one of those
      role groups, an equivalent custom role group, or an equivalent management role. You can
      also click on a role group to see its management roles. If a feature lists more than one
      role group, you need to be assigned to only one of the role groups to use the feature. For
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

Mailbox server permissions
Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

<!-- p.969 -->

                                                                                         ﾉ      Expand table

Feature                                 Permissions required

Calendar repair, server configuration   Organization Management
                                        Server Management

Delegating Mailbox servers              Organization Management

Email address policies                  Organization Management
                                        Server Management

Exchange Search                         Organization Management
                                        View-Only Organization Management
                                        Server Management

Exchange Search - diagnostics           Organization Management
                                        View-Only Organization Management
                                        Support Diagnostics role
                                        Note:: The Support Diagnostics role isn't assigned to a role group.
                                        For more information, see Add a role to a role group.

Group metrics                           Organization Management
                                        Server Management

Import Export                           Mailbox Import Export role
                                        Note:: The Mailbox Import Export role isn't assigned to a role
                                        group. For more information, see Mailbox Import Export Role.

Mailbox Assistants                      Organization Management
                                        Server Management

Mailbox moves                           Organization Management
                                        Recipient Management

Mailbox recovery                        Organization Management

Mailbox repair request                  Organization Management
                                        Server Management
                                        Recipient Management

Mailbox restore request                 Organization Management

Mailbox server configuration            Organization Management
                                        Server Management

Manage Exchange Search Indexer          Local Administrator on the Mailbox server
service on a Mailbox server

MAPI connectivity                       Organization Management
                                        Server Management

<!-- p.970 -->

 Feature                           Permissions required

 OAB virtual directories           Organization Management
                                   Server Management

 Remove store mailbox              Organization Management
                                   Server Management

Calendar and sharing permissions
Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                              ﾉ   Expand table

 Feature                                        Permissions required

 Calendar configuration                         Organization Management
                                                Recipient Management
                                                Help Desk

 Calendar diagnostics                           Organization Management
                                                Records Management
                                                Hygiene Management
                                                Compliance Management
                                                Help Desk

 Calendar processing                            Organization Management
                                                Recipient Management
                                                Help Desk

 Notifications                                  Organization Management
                                                Recipient Management

 Organization relationships                     Organization Management

 Sharing policies                               Organization Management

Resource mailbox configuration permissions
Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

<!-- p.971 -->

                                                                                ﾉ      Expand table

 Feature                                                 Permissions required

 Booking policies                                        Organization Management
                                                         Recipient Management
                                                         Help Desk

 Delegation                                              Organization Management
                                                         Recipient Management

 Resource mailbox schema configuration                   Organization Management

Mailbox database permissions
Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                ﾉ      Expand table

 Feature                                 Permissions required

 Mailbox databases                       Organization Management
                                         Server Management

Recipient provisioning permissions
This table contains the various permissions that are required to manage recipients.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                ﾉ      Expand table

 Feature                                                        Permissions required

 Address list, GAL                                              Organization Management

 Antispam                                                       Organization Management
                                                                Recipient Management

 Apps for Outlook                                               Organization Management
                                                                View-Only Organization

<!-- p.972 -->

Feature                           Permissions required

                                  Management
                                  Help Desk

Applying sharing policies         Organization Management
                                  Recipient Management

Arbitration                       Organization Management

Archive connectivity              Organization Management
                                  View-Only Organization
                                  Management
                                  Server Management

Assigning offline address books   Organization Management
                                  Recipient Management

Automatic replies                 Organization Management
                                  Recipient Management
                                  Help Desk

Calendar configuration            Organization Management
                                  Recipient Management

Calendar repair                   Organization Management
                                  Recipient Management

Contact aggregation settings      Organization Management
                                  Recipient Management
                                  View-Only Organization
                                  Management

Convert mailboxes                 Organization Management
                                  Recipient Management

Disconnected mailboxes            Organization Management
                                  Recipient Management
                                  Help Desk

Distribution groups               Organization Management
                                  Recipient Management

Dynamic distribution groups       Organization Management
                                  Recipient Management

Email addresses                   Organization Management
                                  Recipient Management
                                  UM Management

Inbox rules                       Organization Management
                                  Recipient Management

<!-- p.973 -->

Feature                      Permissions required

                             Help Desk

Mail contacts                Organization Management
                             Recipient Management

Mail tips                    Organization Management
                             Recipient Management

Mail user                    Organization Management
                             Recipient Management

Mailbox folder permissions   Organization Management
                             Recipient Management
                             Help Desk

Mailbox folders              Organization Management
                             Recipient Management

MAPI connectivity            Organization Management

Message configuration        Organization Management
                             Recipient Management
                             Help Desk

Message quotas               Organization Management
                             Recipient Management

Moderation                   Organization Management
                             Recipient Management

Permissions and delegation   Organization Management

Archive mailboxes            Organization Management
                             Recipient Management

Recipient data properties    Organization Management
                             Recipient Management

Remote mailboxes             Organization Management
                             Recipient Management

Retention and legal holds    Organization Management
                             Recipient Management
                             Records Management

Send As                      Organization Management
                             Recipient Management

Spelling configuration       Organization Management
                             Recipient Management

<!-- p.974 -->

 Feature                                                          Permissions required

                                                                  Help Desk

 Unified Messaging (in Exchange 2016; not available in Exchange   Organization Management
 2019)                                                            UM Management

 User mailboxes                                                   Organization Management
                                                                  Recipient Management

 User photos                                                      Organization Management
                                                                  Recipient Management
                                                                  Help Desk

Mailbox move and migration permissions
The table contains the permissions that are required to move on-premises mailboxes to
different domains or forests and to migrate on-premises mailboxes to and from your cloud-
based organization.

                                                                                  ﾉ      Expand table

 Feature                                                             Permissions required

 Mailbox moves (local or cross-forest)                               Organization Management
                                                                     Recipient Management

 Mailbox moves (hybrid deployment)                                   Organization Management
                                                                     Recipient Management

 Migration (on-boarding and off-boarding from the cloud)             Organization Management
                                                                     Recipient Management

<!-- p.975 -->

Email address and address book
permissions in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The permissions required to configure email address and address book features vary
depending on the procedure being performed or the cmdlet you want to run. For more
information about email addresses and address books, see Email addresses and address books
in Exchange Server.

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

Email address and address book permissions

<!-- p.976 -->

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                               ﾉ   Expand table

 Feature                                             Permissions required

 Address book policies                               Organization Management

 Address lists                                       Organization Management

 Email address policies                              Organization Management

 Details templates                                   Organization Management

 Global address lists                                Organization Management

 Offline address books                               Organization Management

 Offline address book connectivity                   Organization Management

<!-- p.977 -->

Sharing and collaboration permissions in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The permissions required to configure sharing and collaboration features vary depending on
the procedure being performed or the cmdlet you want to run. For more information about
sharing and collaboration, see Collaboration and Sharing.

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

Sharing and collaboration feature permissions
You can use the features in the following table to configure sharing and collaboration features.
The role groups that are required to configure each feature are listed.

<!-- p.978 -->

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                               ﾉ   Expand table

 Feature                                            Permissions required

 Partner applications - configure                   Organization Management

 Public folders, mail-enabled                       Organization Management
                                                    Recipient Management

 Public folders                                     Organization Management
                                                    Public Folder Management

 Site mailboxes                                     Organization Management
                                                    Recipient Management

 Site mailbox provisioning policy                   Organization Management
                                                    Recipient Management

<!-- p.979 -->

Clients and mobile devices permissions in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The permissions required to perform tasks for clients and mobile devices vary depending on
the procedure being performed or the cmdlet you want to run. For more information about
client and mobile device features, see Clients and mobile.

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

  ７ Note

<!-- p.980 -->

  Some features may require that you have local administrator permissions on the server
  you want to manage. To manage these features, you must be a member of the Local
  Administrators group on that server.

Client Access service permissions
You can configure any of the following features for the Client Access service.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                 ﾉ   Expand table

 Feature                                             Permissions required

 Client Access service array settings                Organization Management
                                                     Server Management

 Client Access service settings                      Server Management

 Client Access service email channel settings        Organization Management
                                                     Server Management

 Client Access user settings                         Server Management

 Client Access virtual directory settings            Organization Management
                                                     Server Management

 RPC Client Access settings                          Organization Management
                                                     Server Management
                                                     View-Only Organization Management

 Push notification proxy settings                    Organization Management
                                                     Recipient Management

 OAuth authentication redirection settings           Organization Management

Exchange ActiveSync permissions
You can configure any of the following for Exchange ActiveSync.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

<!-- p.981 -->

                                                                                ﾉ   Expand table

 Feature                                                    Permissions required

 Exchange ActiveSync Autoblock settings                     Organization Management

 Exchange ActiveSync mailbox policy settings                Organization Management
                                                            Server Management

 Exchange ActiveSync server settings                        Organization Management
                                                            Server Management

 Exchange ActiveSync settings                               Organization Management
                                                            Server Management

 Exchange ActiveSync user settings                          Recipient Management

 Exchange ActiveSync virtual directory settings             Organization Management
                                                            Server Management

 Mobile device mailbox policy settings                      Organization Management
                                                            Server Management

 Mobile device user settings                                Organization Management
                                                            Server Management
                                                            Recipient Management

Autodiscover permissions
You can configure the following for the Autodiscover service.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                ﾉ   Expand table

 Feature                                           Permissions required

 Autodiscover service configuration settings       Organization Management
                                                   Server Management
                                                   View-Only Organization Management
                                                   Delegated Setup
                                                   Hygiene Management

 Autodiscover virtual directory settings           Organization Management
                                                   Server Management

<!-- p.982 -->

Availability service permissions
You can configure the following for the Availability service.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                     ﾉ   Expand table

 Feature                                                  Permissions required

 Availability service address space settings              Organization Management
                                                          View-Only Organization Management

 Availability service configuration settings              Organization Management
                                                          Server Management
                                                          View-Only Organization Management

Client throttling permissions
You can configure the following for client throttling.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                     ﾉ   Expand table

 Feature                                       Permissions required

 Client throttling settings                    Organization Management
                                               View-Only Organization Management

Exchange Web Services permissions
You can configure the following for Web Services virtual directories.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                     ﾉ   Expand table

<!-- p.983 -->

 Feature                                                           Permissions required

 Exchange Web Services virtual directory settings                  Organization Management
                                                                   Server Management

 Test Exchange Web Services                                        Organization Management
                                                                   Server Management

 Test Outlook Web Services                                         Organization Management

Outlook Anywhere permissions
You can configure and manage the following settings for Outlook Anywhere.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                      ﾉ   Expand table

 Feature                                                          Permissions required

 Outlook Anywhere configuration (enable, disable, change, view)   Organization Management
                                                                  Server Management
                                                                  View-Only Organization Management
                                                                  Delegated Setup
                                                                  Hygiene Management

 RPC over HTTP Proxy component                                    Local Server Administrator

 Test Outlook Anywhere connectivity                               Organization Management
                                                                  View-Only Organization Management
                                                                  Server Management

Outlook on the web permissions
You can use the following features to view Outlook on the web settings, control security and
user access to Outlook on the web, and test Outlook on the web connectivity.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                      ﾉ   Expand table

<!-- p.984 -->

 Feature                                                  Permissions required

 Graphics editor                                          Local Server Administrator

 IIS Manager                                              Local Server Administrator

 ISA Server 2006                                          ISA Server Enterprise Administrator

 Outlook on the web mailbox policies                      Organization Management
                                                          Recipient Management

 Outlook on the web virtual directories                   Organization Management
                                                          Server Management

 Registry Editor                                          Local Server Administrator

 S/MIME configuration                                     Organization Management

 Text editor                                              Local Server Administrator

 View Outlook on the web mailbox policies                 Organization Management
                                                          Recipient Management
                                                          View-Only Organization Management
                                                          Delegated Setup
                                                          Hygiene Management

POP3 and IMAP4 permissions
You can configure the following for POP3 and IMAP4.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                         ﾉ      Expand table

 Feature                                  Permissions required

 IMAP4 settings                           Organization Management
                                          Server Management
                                          View-Only Organization Management

 POP3 settings                            Organization Management
                                          Server Management
                                          View-Only Organization Management

 Test IMAP4 settings                      Organization Management
                                          Server Management

<!-- p.985 -->

 Feature                                Permissions required

                                        View-Only Organization Management

 Test POP3 settings                     Organization Management
                                        Server Management
                                        View-Only Organization Management

Windows PowerShell virtual directory permissions
You can configure the following for Windows PowerShell.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                      ﾉ   Expand table

 Feature                                                Permissions required

 Test Windows PowerShell                                Organization Management

 Windows PowerShell settings                            Organization Management

Text Messaging permissions
You can configure the following for text messaging.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                      ﾉ   Expand table

 Feature                                                       Permissions required

 Text messaging notification settings                          Recipient Management

 Text messaging settings                                       Recipient Management

 Text messaging user settings                                  Recipient Management

<!-- p.986 -->

Unified Messaging permissions in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The permissions required to manage Unified Messaging services and features on Exchange
2016 Mailbox servers vary depending on the procedure being performed or the cmdlet you
want to run.

  ７ Note

  Unified Messaging is not available in Exchange 2019.

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

<!-- p.987 -->

UM component permissions
You can configure settings for the UM components and features in the following table.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                              ﾉ   Expand table

 Feature                                          Permissions required

 UM auto attendants                               Organization Management
                                                  Unified Messaging Management

 UM call answering rules                          Organization Management
                                                  Unified Messaging Management

 UM call data and summary reports                 Organization Management
                                                  Unified Messaging Management

 UM Call Router service (front-end)               Organization Management
                                                  Unified Messaging Management

 UM dial plans                                    Organization Management
                                                  Unified Messaging Management

 UM hunt groups                                   Organization Management
                                                  Unified Messaging Management

 UM IP gateways                                   Organization Management
                                                  Unified Messaging Management

 UM mailbox policies                              Organization Management
                                                  Unified Messaging Management

 UM mailboxes                                     Organization Management
                                                  Unified Messaging Management

 UM prompts                                       Organization Management
                                                  Unified Messaging Management

 UM service (back-end)                            Organization Management
                                                  Server Management

<!-- p.988 -->

High availability and site resilience
permissions in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019        Subscription Edition

The permissions required to configure high availability vary depending on the procedure being
performed or the cmdlet you want to run. For more information about high availability, see
High availability and site resilience.

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

Database availability group permissions
You can use the features in the following table to add, remove, and configure settings for
database availability groups (DAGs).

<!-- p.989 -->

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                ﾉ      Expand table

 Feature                                                Permissions required

 Database availability group membership                 Organization Management
                                                        Database Availability Groups

 Database availability group properties                 Organization Management
                                                        Database Availability Groups

 Database availability groups                           Organization Management
                                                        Database Availability Groups

 Database availability networks                         Organization Management
                                                        Database Availability Groups

Mailbox database copy permissions
You can use the features in the following table to add, remove, update, and activate mailbox
database copies.

                                                                                ﾉ      Expand table

 Feature                                             Permissions required

 Database switchover                                 Organization Management
                                                     Database Copies

 Mailbox database copies                             Organization Management
                                                     Database Copies

 Server switchover                                   Organization Management
                                                     Database Copies

 Update a mailbox database copy                      Organization Management
                                                     Database Copies

<!-- p.990 -->

Exchange infrastructure and PowerShell
permissions
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The permissions required to perform tasks to configure various components of Exchange
Server depend on the procedure being performed or the cmdlet you want to run. See each of
the sections in this topic for more information about their respective features.

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

  ７ Note

<!-- p.991 -->

  Some features may require that you have local administrator permissions on the server
  you want to manage. To manage these features, you must be a member of the Local
  Administrators group on that server.

Exchange infrastructure permissions
The following table lists the permissions required to perform tasks that configure general
Exchange settings.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                 ﾉ   Expand table

 Feature                   Permissions required

 Administrator audit       Organization Management
 logging                   Records Management

 Exchange admin center     View-Only Organization Management
 configuration settings

 Exchange admin center     Organization Management
 connectivity              Server Management

 Exchange server           Organization Management
 configuration settings    Server Management

 Exchange Help settings    Organization Management

 Message categories        Organization Management
                           Hygiene Management
                           Recipient Management
                           Help Desk

 Product key               Organization Management

 Test system health        Organization Management
                           Server Management

 View-only administrator   Organization Management
 audit logging             Records Management
                           Note: You can also manually assign the View-Only Audit Logs management
                           role to a management role group. For more information, see View-Only
                           Audit Logs.

<!-- p.992 -->

 Feature                          Permissions required

 Write to audit log               Users that are members of any role group or assigned any management
                                  role can write to the administrator audit log.

Exchange PowerShell infrastructure permissions
The following table lists the permissions required to perform tasks that configure features that
control how the Exchange Management Shell runs.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                             ﾉ   Expand table

 Feature                                                                  Permissions required

 Active Directory Domain Services server settings                         Organization Management
                                                                          Server Management
                                                                          Recipient Management
                                                                          UM Management

 Cmdlet extension agents                                                  Organization Management

 PowerShell virtual directories                                           Organization Management
                                                                          Server Management

 PowerShell and WinRM installation                                        Local Server Administrator

 Remote PowerShell                                                        Organization Management

Federation and certificates permissions
The following table lists permissions required for performing tasks related to federation trusts,
OAuth configuration, certificate management, and hybrid deployment configuration.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                                             ﾉ   Expand table

<!-- p.993 -->

Feature                           Permissions required

Certificate management            Organization Management
                                  Server Management

Federation trusts, OAuth          Organization Management

Test federation trusts, OAuth     Organization Management
                                  View-Only Organization Management
                                  Server Management

Hybrid deployment configuration   Organization Management

Intra-Organization connectors     Organization Management
                                  Recipient Management
                                  Records Management

<!-- p.994 -->

Server health and performance permissions
in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The permissions required to perform tasks to configure various components of Exchange
Server depend on the procedure being performed or the cmdlet you want to run. See each of
the sections in this topic for more information about their respective features.

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

  ７ Note

<!-- p.995 -->

  Some features may require that you have local administrator permissions on the server
  you want to manage. To manage these features, you must be a member of the Local
  Administrators group on that server.

Exchange workload management permissions
The following table lists the permissions required to perform tasks that manage the health and
performance of your Exchange Server organization. For more information, see User workload
management in Exchange Server.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                               ﾉ   Expand table

 Feature                                   Permissions required

 User throttling                           Organization Management
                                           Recipient Management
                                           View-Only Organization Management

 Exchange workload throttling              Organization Management
                                           View-Only Organization Management

Exchange event log permissions
The following table lists the permissions required to perform tasks that manage Exchange
event log settings.

Users who are assigned the View-Only Management role group can view the configuration of
the features in the following table. For more information, see View-only Organization
Management.

                                                                               ﾉ   Expand table

 Feature                                      Permissions required

 Exchange event log management                Organization Management
                                              Server Management
                                              View-Only Organization Management
                                              UM Management

<!-- p.996 -->

Split permissions in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Organizations that separate the management of Exchange Server 2016 and Exchange Server
2019 objects and Active Directory objects use what's called a split permissions model. Split
permissions enable organizations to assign specific permissions and related tasks to specific
groups within the organization. This separation of work helps to maintain standards and
workflows, and helps to control change in the organization.

The highest level of split permissions is the separation of Exchange management and Active
Directory management. Many organizations have two groups: administrators that manage the
organization's Exchange infrastructure, including servers and recipients, and administrators that
manage the Active Directory infrastructure. This is an important separation for many
organizations because the Active Directory infrastructure often spans many locations, domains,
services, applications, and even Active Directory forests. Active Directory administrators must
ensure that changes made to Active Directory don't negatively impact any other services. As a
result, typically only a small group of administrators is allowed to manage that infrastructure.

At the same time, the infrastructure for Exchange, including servers and recipients, can also be
complex and require specialized knowledge. Additionally, Exchange stores extremely
confidential information about the business of the organization. Exchange administrators can
potentially access this information. By limiting the number of Exchange administrators, the
organization limits who can make changes to Exchange configuration and who can access
sensitive information.

Split permissions typically make a distinction between the creation of security principals in
Active Directory, such as users and security groups, and the subsequent configuration of those
objects. This helps to reduce the chance of unauthorized access to the network by controlling
who can create objects that grant access to it. Most often only Active Directory administrators
can create security principals while other administrators, such as Exchange administrators, can
manage specific attributes on existing Active Directory objects.

To support the varying needs to separate the management of Exchange and Active Directory,
Exchange lets you choose whether you want a shared permissions model or a split permissions
model. Exchange offers two types of split permissions models: RBAC and Active Directory.
Exchange defaults to a shared permissions model.

Explanation of Role Based Access Control and
Active Directory

<!-- p.997 -->

To understand split permissions, you need to understand how the Role Based Access Control
(RBAC) permissions model in Exchange works with Active Directory. The RBAC model controls
who can perform what actions, and on which objects those actions can be performed. For more
information about the various components of RBAC that are discussed in this topic, see
Exchange Server permissions.

All tasks that are performed on Exchange objects must be done through the Exchange
Management Shell or the Exchange admin center (EAC) interface. Both of these management
tools use RBAC to authorize all tasks that are performed.

RBAC is a component that exists on every Exchange server. RBAC checks whether the user
performing an action is authorized to do so:

     If the user isn't authorized to perform the action, RBAC doesn't allow the action to
     proceed.

     If the user is authorized to perform the action, RBAC checks whether the user is
     authorized to perform the action against the specific object being requested:

     If the user is authorized, RBAC allows the action to proceed.

     If the user isn't authorized, RBAC doesn't allow the action to proceed.

If RBAC allows an action to proceed, the action is performed in the context of the Exchange
Trusted Subsystem and not the user's context. The Exchange Trusted Subsystem is a highly
privileged universal security group (USG) that has read/write access to every Exchange-related
object in the Exchange organization. It's also a member of the Administrators local security
group and the Exchange Windows Permissions USG, which enables Exchange to create and
manage Active Directory objects.

  ２ Warning

  Don't make any manual changes to the membership of the Exchange Trusted Subsystem
  security group. Also, don't add it to or remove it from object access control lists (ACLs). By
  making changes to the Exchange Trusted Subsystem USG yourself, you could cause
  irreparable damage to your Exchange organization.

It's important to understand that it doesn't matter what Active Directory permissions a user has
when using the Exchange management tools. If the user is authorized, via RBAC, to perform an
action in the Exchange management tools, the user can perform the action regardless of his or
her Active Directory permissions. Conversely, if a user is an Enterprise Admin in Active Directory
but isn't authorized to perform an action, such as creating a mailbox, in the Exchange

<!-- p.998 -->

management tools, the action won't succeed because the user doesn't have the required
permissions according to RBAC.

  ） Important

  Although the RBAC permissions model doesn't apply to the Active Directory Users and
  Computers management tool, Active Directory Users and Computers can't manage the
  Exchange configuration. S, although a user may have access to modify some attributes on
  Active Directory objects, such as the display name of a user, the user must use the
  Exchange management tools, and therefore must be authorized by RBAC, to manage
  Exchange attributes.

Shared permissions
The shared permissions model is the default model for Exchange. You don't need to change
anything if this is the permissions model you want to use. This model doesn't separate the
management of Exchange and Active Directory objects from within the Exchange management
tools. It allows administrators using the Exchange management tools to create security
principals in Active Directory.

The following table shows the roles that enable the creation of security principals in Exchange
and the management role groups they're assigned to by default.

                                                                               ﾉ    Expand table

 Management role                                             Role group

 Mail Recipient Creation role                                Organization Management

                                                             Recipient Management

 Security Group Creation and Membership role                 Organization Management

Only role groups, users, or USGs that are assigned the Mail Recipient Creation role can create
security principals such as Active Directory users. By default, the Organization Management
and Recipient Management role groups are assigned this role. Therefore members of these
role groups can create security principals.

Only role groups, users, or USGs that are assigned the Security Group Creation and
Membership role can create security groups or manage their memberships. By default, only the
Organization Management role group is assigned this role. Therefore only members of the

<!-- p.999 -->

Organization Management role group can create or manage the membership of security
groups.

You can assign the Mail Recipient Creation role and the Security Group Creation and
Membership role to other role groups, users, or USGs if you want other users to be able to
create security principals.

To enable the management of existing security principals in Exchange, the Mail Recipients role
is assigned to the Organization Management and Recipient Management role groups by
default. Only role groups, users, or USGs that are assigned the Mail Recipients role can manage
existing security principals. If you want other role groups, users, or USGs to be able to manage
existing security principals, you must assign the Mail Recipients role to them.

For more information about how to add roles to role groups, users, or USGs, see the following
topics:

     Manage role groups

     Add a role to a user or USG

If you switched to a split permissions model and want to change back to a shared permissions
model, see Configure Exchange Server for shared permissions.

Split permissions
If your organization separates Exchange management and Active Directory management, you
need to configure Exchange to support the split permissions model. When configured
correctly, only the administrators who you want to create security principals, such as Active
Directory administrators, will be able to do so and only Exchange administrators will be able to
modify the Exchange attributes on existing security principals. This splitting of permissions also
falls roughly along the lines of the domain and configuration partitions in Active Directory.
Partitions are also called naming contexts. The domain partition stores the users, groups, and
other objects for a specific domain. The configuration partition stores the forest-wide
configuration information for the services that used Active Directory, such as Exchange. Data
that's stored in the domain partition is typically managed by Active Directory administrators,
although objects may contain Exchange-specific attributes that can be managed by Exchange
administrators. Data that's stored in the configuration partition is managed by the
administrators for each respective service that stores data in this partition. For Exchange, this is
typically Exchange administrators.

Exchange supports the two following types of split permissions:

<!-- p.1000 -->

     RBAC split permissions: Permissions to create security principals in the Active Directory
     domain partition are controlled by RBAC. Only Exchange servers, services, and those who
     are members of the appropriate role groups can create security principals.

     Active Directory split permissions: Permissions to create security principals in the Active
     Directory domain partition are completely removed from any Exchange user, service, or
     server. No option is provided in RBAC to create security principals. Creation of security
     principals in Active Directory must be performed using Active Directory management
     tools.

        ） Important

        In coexistence scenarios, Active Directory split permissions configuration also applies
        to any Exchange 2010 or later servers in the organization.

If your organization chooses to use a split permissions model instead of shared permissions,
we recommend that you use the RBAC split permissions model. The RBAC split permissions
model provides significantly more flexibility while providing the nearly same administration
separation as Active Directory split permissions, with the exception that Exchange servers and
services can create security principals in the RBAC split permissions model.

You're asked whether you want to enable Active Directory split permissions during Setup. If you
choose to enable Active Directory split permissions, you can only change to shared permissions
or RBAC split permissions by rerunning Setup and disabling Active Directory split permissions.
This choice applies to all Exchange 2010 or later servers in the organization.

The following sections describe RBAC and Active Directory split permissions in more detail.

RBAC split permissions
The RBAC security model modifies the default management role assignments to separate who
can create security principals in the Active Directory domain partition from those who
administer the Exchange organization data in the Active Directory configuration partition.
Security principals, such as users with mailboxes and distribution groups, can be created by
administrators who are members of the Mail Recipient Creation and Security Group Creation
and Membership roles. These permissions remain separate from the permissions required to
create security principals outside of the Exchange management tools. Exchange administrators
who aren't assigned the Mail Recipient Creation or Security Group Creation and Membership
roles can still modify Exchange-related attributes on security principals. Active Directory
administrators also have the option of using the Exchange management tools to create Active
Directory security principals.
