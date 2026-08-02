---
title: "Exchange Server — pages 2241-2280"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2241-2280
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2241-2280
family: exchange
documentKind: "doc"
abstract: "Auditing of RBAC role changes, which is enabled by default, makes sure that adequate records are kept to track assignment of the Discovery Management role group. You can use the administrator role group report to search for changes made to administrator role groups. For more inf"
---

# Exchange Server — pages 2241-2280

<!-- p.2241 -->

Auditing of RBAC role changes, which is enabled by default, makes sure that adequate records
are kept to track assignment of the Discovery Management role group. You can use the
administrator role group report to search for changes made to administrator role groups. For
more information, see Search the role group changes or administrator audit logs.

Using In-Place eDiscovery
Users who have been added to the Discovery Management role group can perform In-Place
eDiscovery searches. You can perform a search using the web-based interface in the EAC. This
makes it easier for non-technical users such as records managers, compliance officers, or legal
and HR professionals to use In-Place eDiscovery. You can also use the Exchange Management
Shell to perform a search. For more information, see Create an In-Place eDiscovery search in
Exchange Server

The In-Place eDiscovery & Hold wizard in the EAC allows you to create an In-Place eDiscovery
search and also use In-Place Hold to place search results on hold. When you create an In-Place
eDiscovery search, a search object is created in the In-Place eDiscovery system mailbox. This
object can be manipulated to start, stop, modify, and remove the search. After you create the
search, you can choose to get an estimate of search results, which includes keyword statistics
that help you determine query effectiveness. You can also do a live preview of items returned in
the search, allowing you to view message content, the number of messages returned from
each source mailbox and the total number of messages. You can use this information to further
fine-tune your query if required.

When satisfied with the search results, you can copy them to a discovery mailbox. You can also
use the EAC or Outlook to export a discovery mailbox or some of its content to a PST file.

When creating an In-Place eDiscovery search, you must specify the following parameters:

     Name - The search name is used to identify the search. When you copy search results to a
     discovery mailbox, a folder is created in the discovery mailbox using the search name and
     the timestamp to uniquely identify search results in a discovery mailbox.

     Sources - You can choose to search all mailboxes in your Exchange Server organization or
     specify the mailboxes to search. You can also choose to search all public folders. If you
     also want to use the same search to place items on hold, you must specify the mailboxes.
     You can also place all public folders on In-Place Hold. You can specify a distribution group
     to include mailbox users who are members of that group. Membership of the group is
     calculated once when creating the search and subsequent changes to group membership
     aren't automatically reflected in the search. A user's primary and archive mailboxes are
     included in the search.

<!-- p.2242 -->

Search query - You can either include all mailbox content from the specified mailboxes or
use a search query to return items that are more relevant to the case or investigation. You
can specify the following parameters in a search query:

  Keywords - You can specify keywords and phrases to search message content. You can
  also use the logical operators AND, OR, and NOT. Additionally, Exchange Server also
  supports the NEAR operator, allowing you to search for a word or phrase that's in
  proximity to another word or phrase.

  To search for an exact match of a multiple word phrase, you must enclose the phrase in
  quotation marks. For example, searching for the phrase "plan and competition" returns
  messages that contain an exact match of the phrase, whereas specifying plan AND
  competition returns messages that contain the words plan and competition anywhere
  in the message.

  Exchange Server also supports the Keyword Query Language (KQL) syntax for In-Place
  eDiscovery searches. For more information about KQL, see Keyword Query Language
  syntax reference.

     ７ Note

     In-Place eDiscovery does not support regular expressions.

  You must capitalize logical operators such as AND and OR for them to be treated as
  operators instead of keywords. We recommend that you use explicit parenthesis for
  any query that mixes multiple logical operators to avoid mistakes or
  misinterpretations. For example, if you want to search for messages that contain either
  WordA or WordB AND either WordC or WordD, you must use (WordA OR WordB)
  AND (WordC OR WordD).

  Start and End dates - By default, In-Place eDiscovery doesn't limit searches by a date
  range. To search messages sent during a specific date range, you can narrow the
  search by specifying the start and end dates. If you don't specify an end date, the
  search will return the latest results every time you restart it.

  Senders and recipients - To narrow down the search, you can specify the senders or
  recipients of messages. You can use email addresses, display names, or the name of a
  domain to search for items sent to or from everyone in the domain. For example, to
  find email sent by or sent to anyone at Contoso, Ltd, specify @contoso.com in the
  From or the To/cc field in the EAC. You can also specify @contoso.com in the Senders
  or Recipients parameters in the Exchange Management Shell

<!-- p.2243 -->

        Message types - By default, all message types are searched. You can restrict the search
        by selecting specific message types such as email, contacts, documents, journal,
        meetings, notes and Lync content.

The following screenshot shows an example of a search query in the EAC.

When using In-Place eDiscovery, also consider the following:

     Attachments - In-Place eDiscovery searches attachments supported by Exchange Search.
     For details, see Default Filters for Exchange Search. In on-premises deployments, you can
     add support for additional file types by installing search filters (also known as an iFilter)
     for the file type on Mailbox servers.

     Unsearchable items - Unsearchable items are mailbox items that can't be indexed by
     Exchange Search. Reasons they can't be indexed include the lack of an installed search
     filter for an attached file, a filter error, and encrypted messages. For a successful
     eDiscovery search, your organization may be required to include such items for review.
     When copying search results to a discovery mailbox or exporting them to a PST file, you
     can include unsearchable items. For more information, see Unsearchable Items in
     Exchange eDiscovery.

     Encrypted items - Because messages encrypted using S/MIME aren't indexed by
     Exchange Search, In-Place eDiscovery doesn't search these messages. If you select the

<!-- p.2244 -->

option to include unsearchable items in search results, these S/MIME encrypted messages
are copied to the discovery mailbox.

De-duplication - When copying search results to a discovery mailbox or exporting search
results to a PST file, you can enable de-duplication of search results to copy only one
instance of a unique message to the discovery mailbox. De-duplication has the following
benefits:

   Lower storage requirement and smaller discovery mailbox size due to reduced number
   of messages copied.

   Reduced workload for discovery managers, legal counsel, or others involved in
   reviewing search results.

   Reduced cost of eDiscovery, depending on the number of duplicate items excluded
   from search results.

IRM-protected items - Messages protected using Information Rights Management (IRM)
are indexed by Exchange Search and therefore included in the search results if they match
query parameters. Messages must be protected by using an Active Directory Rights
Management Services (AD RMS) cluster in the same Active Directory forest as the Mailbox
server. For more information, see Information Rights Management in Exchange Server.

Important:

   When Exchange Search fails to index an IRM-protected message, either due to a
   decryption failure or because IRM is disabled, the protected message isn't added to
   the list of failed items. If you select the option to include unsearchable items in search
   results, the results may not include IRM-protected messages that could not be
   decrypted.

   To include IRM-protected messages in a search, you can create another search to
   include messages with .rpmsg attachments. You can use the query string
   attachment:rpmsg to search all IRM-protected messages in the specified mailboxes,

   whether successfully indexed or not. This may result in some duplication of search
   results in scenarios where one search returns messages that match the search criteria,
   including IRM-protected messages that have been indexed successfully. The search
   doesn't return IRM-protected messages that couldn't be indexed.

   Performing a second search for all IRM-protected messages also includes the IRM-
   protected messages that were successfully indexed and returned in the first search.
   Additionally, the IRM-protected messages returned by the second search may not
   match the search criteria such as keywords used for the first search.

<!-- p.2245 -->

Estimate, preview, and copy search results
After an In-Place eDiscovery search is completed, you can view search result estimates in the
Details pane in the EAC. The estimate includes number of items returned and total size of those
items. You can also view keyword statistics, which returns details about number of items
returned for each keyword used in the search query. This information is helpful in determining
query effectiveness. If the query is too broad, it may return a much bigger data set, which could
require more resources to review and raise eDiscovery costs. If the query is too narrow, it may
significantly reduce the number of records returned or return no records at all. You can use the
estimates and keyword statistics to fine-tune the query to meet your requirements.

  ７ Note

  In Exchange Server, keyword statistics also include statistics for non-keyword properties
  such as dates, message types, and senders/recipients specified in a search query.

You can also preview the search results to further ensure that messages returned contain the
content you're searching for and further fine-tune the query if required. eDiscovery Search
Preview displays the number of messages returned from each mailbox searched and the total
number of messages returned by the search. The preview is generated quickly without
requiring you to copy messages to a discovery mailbox.

After you're satisfied with the quantity and quality of search results, you can copy them to a
discovery mailbox. When copying messages, you have the following options:

     Include unsearchable items - For details about the types of items that are considered
     unsearchable, see the eDiscovery search considerations in the previous section.

     Enable de-duplication - De-duplication reduces the dataset by only including a single
     instance of a unique record if multiple instances are found in one or more mailboxes
     searched.

     Enable full logging - By default, only basic logging is enabled when copying items. You
     can select full logging to include information about all records returned by the search.

     Send me mail when the copy is completed - An In-Place eDiscovery search can
     potentially return a large number of records. Copying the messages returned to a
     discovery mailbox can take a long time. Use this option to get an email notification when
     the copying process is completed. For easier access using Outlook on the web, the
     notification includes a link to the location in a discovery mailbox where the messages are
     copied.

<!-- p.2246 -->

For more information, see Copy eDiscovery search results to a discovery mailbox.

Export search results to a PST file
After search results are copied to a discovery mailbox, you can export the search results to a
PST file.

After search results are exported to a PST file, you or other users can open them in Outlook to
review or print messages returned in the search results. For more information, see Export
eDiscovery search results to a PST file.

Logging for In-Place eDiscovery searches
There are two types of logging available for In-Place eDiscovery searches.

      Basic logging - Basic logging is enabled by default for all In-Place eDiscovery searches. It
      includes information about the search and who performed it. Information captured about
      basic logging appears in the body of the email message sent to the mailbox where the
      search results are stored. The message is located in the folder created to store search
      results.

      Full logging - Full logging includes information about all messages returned by the
      search. This information is provided in a comma-separated value (.csv) file attached to the
      email message that contains the basic logging information. The name of the search is
      used for the .csv file name. This information may be required for compliance or record-
      keeping purposes. To enable full logging, you must select the Enable full logging option
      when copying search results to a discovery mailbox in the EAC. If you're using the
      Exchange Management Shell, specify the full logging option using the LogLevel
      parameter.

  ７ Note

<!-- p.2247 -->

  When using the Exchange Management Shell to create or modify an In-Place eDiscovery
  search, you can also disable logging.

Besides the search log included when copying search results to a discovery mailbox, Exchange
also logs cmdlets used by the EAC or the Exchange Management Shell to create, modify or
remove In-Place eDiscovery searches. This information is logged in the admin audit log entries.
For details, see Administrator audit logging in Exchange Server.

Discovery mailboxes
After you create an In-Place eDiscovery search, you can copy the search results to a target
mailbox. The EAC allows you to select a discovery mailbox as the target mailbox. A discovery
mailbox is a special type of mailbox that provides the following functionality:

     Easier and secure target mailbox selection - When you use the EAC to copy In-Place
     eDiscovery search results, only discovery mailboxes are made available as a repository in
     which to store search results. This eliminates the possibility of a discovery manager
     accidentally selecting another user's mailbox or an unsecured mailbox in which to store
     potentially sensitive messages.

     Large mailbox storage quota - The target mailbox should be able to store a large
     amount of message data that may be returned by an In-Place eDiscovery search. By
     default, discovery mailboxes have a mailbox storage quota of 50 GB. This storage quota
     can't be increased.

     More secure by default - Like all mailbox types, a discovery mailbox has an associated
     Active Directory user account. However, this account is disabled by default. Only users
     explicitly authorized to access a discovery mailbox have access to it. Members of the
     Discovery Management role group are assigned Full Access permissions to the default
     discovery mailbox. Any additional discovery mailboxes you create don't have mailbox
     access permissions assigned to any user.

     Email delivery disabled - Users can't send email to a discovery mailbox. Email delivery to
     discovery mailboxes is prohibited by using delivery restrictions. This preserves the
     integrity of search results copied to a discovery mailbox. By default, discovery mailboxes
     aren't displayed in your organization's global address list.

Exchange Server Setup creates one discovery mailbox with the display name Discovery Search
Mailbox. You can use the Exchange Management Shell to create additional discovery
mailboxes. By default, the discovery mailboxes you create won't have any mailbox access
permissions assigned. You can assign Full Access permissions for a discovery manager to
access messages copied to a discovery mailbox. For details, see Create a Discovery Mailbox .

<!-- p.2248 -->

In-Place eDiscovery also uses a system mailbox with the display name
SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9} to hold In-Place eDiscovery
metadata. System mailboxes aren't visible in the EAC or in Exchange address lists. Before
removing a mailbox database where the In-Place eDiscovery system mailbox is located, you
must move the mailbox to another mailbox database. If the mailbox is removed or corrupted,
your discovery managers are unable to perform eDiscovery searches until you re-create the
mailbox. For details, see Re-Create the Discovery System Mailbox.

In-Place eDiscovery and In-Place Hold
As part of eDiscovery requests, you may be required to preserve mailbox content until a lawsuit
or investigation is disposed. Messages deleted or altered by the mailbox user or any processes
must also be preserved. In Exchange Server, this is accomplished by using In-Place Hold. For
details, see In-Place Hold and Litigation Hold in Exchange Server.

You can use the In-Place eDiscovery & Hold wizard to search items and preserve them for as
long as they're required for eDiscovery or to meet other business requirements. When using
the same search for both In-Place eDiscovery and In-Place Hold, be aware of the following:

     You can't use the option to place a hold on all mailboxes in your organization. You must
     select the mailboxes or distribution groups. However, you can place all public fol ders in
     your organization on hold.

     You can't remove an In-Place eDiscovery search if the search is also used for In-Place
     Hold. You must first disable the In-Place Hold option in a search and then remove the
     search.

Preserving mailboxes for In-Place eDiscovery
When an employee leaves an organization, it's a common practice to disable or remove the
mailbox. After you disable a mailbox, it is disconnected from the user account but remains in
the mailbox for a certain period, 30 days by default. The Managed Folder Assistant does not
process disconnected mailboxes and any retention policies are not applied during this period.
You can't search content of a disconnected mailbox. Upon reaching the deleted mailbox
retention period configured for the mailbox database, the mailbox is purged from the mailbox
database.

If your organization requires that retention settings be applied to messages of employees who
are no longer in the organization or if you may need to retain an ex-employee's mailbox for an
ongoing or future eDiscovery search, do not disable or remove the mailbox. You can take the

<!-- p.2249 -->

following steps to ensure the mailbox can't be accessed and no new messages are delivered to
it.

      1. Disable the Active Directory user account using Active Directory Users & Computers or
        other Active Directory or account provisioning tools or scripts. This prevents mailbox
        logon using the associated user account.

           ） Important

           Users with Full Access mailbox permission will still be able to access the mailbox. To
           prevent access by others, you must remove their Full Access permission from the
           mailbox. For information about how to remove Full Access mailbox permissions on a
           mailbox, see Manage permissions for recipients.

      2. Set the message size limit for messages that can be sent from or received by the mailbox
        user to a very low value, 1 KB for example. This prevents delivery of new mail to and from
        the mailbox. For details, see Configure message size limits for a mailbox.

      3. Configure delivery restrictions for the mailbox so nobody can send messages to it. For
        details, see Configure message delivery restrictions for a mailbox.

      ） Important

      You must take the above steps along with any other account management processes
      required by your organization, but without disabling or removing the mailbox or removing
      the associated user account.

When planning to implement mailbox retention for messaging retention management (MRM)
or In-Place eDiscovery, you must take employee turnover into consideration. Long-term
retention of ex-employee mailboxes will require additional storage on Mailbox servers and also
result in an increase in Active Directory database because it requires that the associated user
account be retained for the same duration. Additionally, it may also require changes to your
organization's account provisioning and management processes.

Different search results
Because In-Place eDiscovery performs searches on live data, it's possible that two searches of
the same content sources and that use the same search query can return different results.
Estimated search results can also be different from the actual search results that are copied to a
discovery mailbox. This can happen even when rerunning the same search within a short
amount of time. There are several factors that can affect the consistency of search results.

<!-- p.2250 -->

     The continual indexing of incoming email because Exchange Search continuously crawls
     and indexes your organization's mailbox databases and transport pipeline.

     Deletion of email by users or automated processes.

     Bulk importing large amounts of email, which takes time to index.

If you do experience dissimilar results for the same search, consider placing mailboxes on hold
to preserve content, running searches during off-peak hours, and allowing time for indexing
after importing large amounts of email.

Custom management scopes for In-Place
eDiscovery
You can use a custom management scope to let specific people or groups use In-Place
eDiscovery to search a subset of mailboxes in your Exchange Server organization. For example,
you might want to let a discovery manager search only the mailboxes of users in a specific
location or department. You do this by creating a custom management scope that uses a
custom recipient filter to control which mailboxes can be searched. Recipient filter scopes use
filters to target specific recipients based on recipient type or other recipient properties.

For In-Place eDiscovery, the only property on a user mailbox that you can use to create a
recipient filter for a custom scope is distribution group membership. If you use other
properties, such as CustomAttributeN, Department, or PostalCode, the search fails when it's run
by a member of the role group that's assigned the custom scope. For more information, see
Create a custom management scope for In-Place eDiscovery searches.

In-Place eDiscovery and Exchange Search
In-Place eDiscovery uses the content indexes created by Exchange Search. Exchange Search has
been retooled to use Microsoft Search Foundation, a rich search platform that comes with
significantly improved indexing and querying performance and improved search functionality.
Because the Microsoft Search Foundation is also used by other Office products, including
SharePoint Server, it offers greater interoperability and similar query syntax across these
products.

With a single content indexing engine, no additional resources are used to crawl and index
mailbox databases for In-Place eDiscovery when eDiscovery requests are received by IT
departments.

For more information about the file formats indexed by Exchange Search, see File Formats
Indexed By Exchange Search.

<!-- p.2251 -->

eDiscovery in an Exchange hybrid deployment
In an Exchange Server Hybrid Deployments - a configuration where some user mailboxes
reside on on-premises Exchange servers while others are hosted in Exchange Online - you can
use the Exchange Admin Center (EAC) in your on-premises environment to perform In-Place
eDiscovery searches. However, this functionality is limited to on-premises mailboxes only. If
you need to search cloud-based mailboxes hosted in Exchange Online, you must use the
Microsoft Purview eDiscovery solution, which is designed to handle compliance searches across
Microsoft 365 services.

Previously, it was possible to perform cross-premises eDiscovery - searching both on-premises
and cloud mailboxes in a single query - by configuring OAuth authentication between the two
environments. However, this capability is no longer supported in current Exchange hybrid
deployments. As a result, organizations must now conduct separate searches for on-premises
and cloud mailboxes.

Integration with SharePoint Server
Exchange Server offers integration with SharePoint Server, allowing a discovery manager to use
the eDiscovery Center in SharePoint Server to perform the following tasks:

     Search and preserve content from a single location - An authorized discovery manager
     can search and preserve content across SharePoint and Exchange, including Lync content
     such as instant messaging conversations and shared meeting documents archived in
     Exchange mailboxes.

     Case management - eDiscovery Center uses a case management approach to eDiscovery,
     allowing you to create cases and search and preserve content across different content
     repositories for each case.

     Export search results - A discovery manager can use eDiscovery Center to export search
     results. Mailbox content included in search results is exported to a PST file.

SharePoint Server also uses Microsoft Search Foundation for content indexing and querying.
Regardless of whether a discovery manager uses the EAC or the eDiscovery Center to search
Exchange content, the same mailbox content is returned.

Before you can use eDiscovery Center in SharePoint Server to search Exchange mailboxes, you
must establish trust between the two applications. In Exchange and SharePoint, this is done
using OAuth authentication. For details, see Configure Exchange for SharePoint eDiscovery
Center. eDiscovery searches performed from SharePoint are authorized by Exchange using
RBAC. For a SharePoint user to be able to perform an eDiscovery search of Exchange

<!-- p.2252 -->

mailboxes, they must be assigned delegated Discovery Management permission in Exchange.
To be able to preview mailbox content returned in an eDiscovery search performed using
SharePoint eDiscovery Center, the discovery manager must have a mailbox in the same
Exchange organization.

In-Place eDiscovery limits and throttling policies
In Exchange Server, the resources In-Place eDiscovery uses are controlled with throttling
policies.

The default throttling policy contains the following parameters. You can change the default
values to meet your organization's requirements by creating a new throttling policy with an
Organization scope and name it as "DiscoveryThrottlingPolicy" only.

                                                                                    ﾉ    Expand table

 Parameter                            Description                 Default value

 DiscoveryMaxConcurrency              The maximum number of       2
                                      In-Place eDiscovery
                                      searches a user can
                                      perform concurrently.

 DiscoveryMaxMailboxes                The maximum number of       10,0001
                                      mailboxes that can be
                                      searched in a single In-
                                      Place eDiscovery search.
                                      Public folder mailboxes
                                      are also counted against
                                      the source mailbox limit.

 DiscoveryMaxStatsSearchMailboxes     The maximum number of       100
                                      mailboxes that can be       Note: After you run an eDiscovery
                                      searched in a single In-    search estimate, you can view
                                      Place eDiscovery search     keyword statistics. These statistics
                                      that still allows you to    show details about the number of
                                      view keyword statistics.    items returned for each keyword
                                                                  used in the search query. If more
                                                                  than 100 source mailboxes are
                                                                  included in the search, an error will
                                                                  be returned if you try to view
                                                                  keyword statistics.

 DiscoveryMaxKeywords                 The maximum number of       500
                                      keywords that can be
                                      specified in a single In-
                                      Place eDiscovery search.

<!-- p.2253 -->

    Parameter                                Description                  Default value

    DiscoveryPreviewSearchResultsPageSize    The maximum number of        200
                                             items displayed on a
                                             single page when
                                             previewing In-Place
                                             eDiscovery search results.

    DiscoverySearchTimeoutPeriod             The number of minutes        10 minutes
                                             that an In-Place
                                             eDiscovery search will
                                             run before it times out.

1
    Archive mailboxes are counted against the source mailbox limit. That means you can search a
maximum of 5,000 mailboxes if the corresponding archive mailbox is enabled for all 5,000
mailboxes.

In-Place eDiscovery documentation
The following table contains links to Exchange Server topics that will help you learn about and
manage In-Place eDiscovery.

                                                                                           ﾉ   Expand table

    Topic                      Description

    Assign eDiscovery          Learn how to give a user access to use In-Place eDiscovery in the EAC (and
    permissions in Exchange    by using the corresponding cmdlets) to search Exchange mailboxes.
    Server

    Create an In-Place         Learn how to create an In-Place eDiscovery search, and how to estimate and
    eDiscovery search in       preview eDiscovery search results.
    Exchange Server

    Copy eDiscovery search     Learn how to copy the results of an eDiscovery search to a discovery
    results to a discovery     mailbox.
    mailbox

    Export eDiscovery search   Learn how to export the results of an eDiscovery search to a PST file.
    results to a PST file

    Message properties and     Learn which email message properties can be searched using In-Place
    search operators for In-   eDiscovery. The topic provides syntax examples for each property,
    Place eDiscovery in        information about search operators such as AND and OR, and information
    Exchange Server            about other search query techniques such as using double quotation marks
                               (" ") and prefix wildcards.

<!-- p.2254 -->

Topic                         Description

Search and place a hold       Learn how to use In-Place eDiscovery to search and place a hold on all
on public folders using In-   public folders in your organization.
Place eDiscovery

<!-- p.2255 -->

Assign eDiscovery permissions in Exchange
Server
Article • 04/30/2025

APPLIES TO:         2016   2019      Subscription Edition

If you want users to be able to use Exchange Server In-Place eDiscovery, you first need to add
them to the Discovery Management role group. Members of the Discovery Management role
group have Full Access mailbox permissions to the default discovery mailbox, which is called
Discovery Search Mailbox.

  Ｕ Caution

  Members of the Discovery Management role group can access sensitive message content.
  Specifically, these members can use In-Place eDiscovery to search all mailboxes in your
  Exchange organization, preview the search results (and other mailbox items), copy them to
  a discovery mailbox, and export the search results to a .pst file. In most organizations, this
  permission is assigned to legal, compliance, or Human Resources personnel.

What do you need to know before you begin?
      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Role groups" entry in the Role
      management permissions topic.

      By default, the Discovery Management role group doesn't contain any members.
      Therefore, administrators that have the Organization Management role assigned can't
      create or manage discovery searches without being added to the Discovery Management
      role group.

      In Exchange Server, members of the Organization Management role group can create an
      In-Place Hold to place all mailbox content on hold. However, to create a query-based In-
      Place Hold, the user must be a member of the Discovery Management role group or have
      the Mailbox Search role assigned.

      You can only add security principals to the Discovery Management role group (users or
      groups that can be assigned permissions). For example:

         User mailboxes

         Mail users

<!-- p.2256 -->

        Security groups

        Other role groups

     To learn how to open the Exchange Management Shell in your on-premises Exchange
     organization, see Open the Exchange Management Shell.

Use the EAC to add a user to the Discovery
Management role group
  1. In the EAC, go to Permissions > Admin roles, select the Discovery Management role
     group, and then click Edit   .

  2. On the resulting Role Group page, in the Members section, click Add      .

  3. In the resulting Select Members dialog, select an available user or group, and then click
     Add. Repeat this step as many times as necessary. When you're finished, click OK.

  4. Back on the Role Group page, click Save.

Use the Exchange Management Shell to add a user
to the Discovery Management role group
To add a user to the Discovery Management role group, use the following syntax:

  PowerShell

  Add-RoleGroupMember -Identity "Discovery Management" -Member <Identity>

This example adds the user Bsuneja to the Discovery Management role group.

  PowerShell

  Add-RoleGroupMember -Identity "Discovery Management" -Member Bsuneja

This example add the members of the mail-enabled security group named Contoso
Compliance Management.

  PowerShell

  Add-RoleGroupMember -Identity "Discovery Management" -Member "Contoso Compliance
  Management"

<!-- p.2257 -->

For more information, see Add-RoleGroupMember.

How do you know this worked?
To verify that you've added the user to the Discovery Management role group, use either of the
following procedures:

     In the EAC, go to Permissions > Admin roles, and select the Discovery Management role
     group. In the details pane, verify that the user is listed in the Members section.

     In the Exchange Management Shell, run the following command to view the members of
     the Discovery Management role group.

       PowerShell

       Get-RoleGroupMember -Identity "Discovery Management"

<!-- p.2258 -->

Create an In-Place eDiscovery search in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

Use an In-Place eDiscovery search to search for content across all mailboxes and public folders
in your Exchange Server organization. This includes searching permanently deleted items and
original versions of modified items (in the Recoverable Items folder) for users placed on
Litigation Hold or In-Place Hold. For more information about these searches, see In-Place
eDiscovery in Exchange Server.

Before you begin
      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "In-Place eDiscovery" entry in the
      Messaging policy and compliance permissions in Exchange Server topic.

      To create eDiscovery searches, you have to have an SMTP address in the organization that
      you're creating the searches in. In an Exchange hybrid organization, your on-premises
      Exchange mailbox must have a corresponding mail user account in your Microsoft 365 or
      Office 365 organization, such as the tenant administrator account, that account must be
      assigned an Exchange Online license. For more information about the Microsoft 365 or
      Office 365 licensing requirements for in-place eDiscovery searches, see Exchange Online
      Service Description.

      Exchange Server Setup creates a Discovery mailbox called Discovery Search Mailbox to
      copy search results. You can create additional Discovery mailboxes. For details, see Create
      a discovery mailbox.

      When you create a search, messages returned in search results aren't copied
      automatically to a discovery mailbox. After you create the search, you can use the
      Exchange admin center (EAC) to estimate and preview search results or copy them to a
      discovery mailbox. You can also export the search results to a .pst file. For details, see:

         Use the EAC to estimate or preview search results (later in this topic)

         Copy eDiscovery search results to a discovery mailbox

         Export eDiscovery search results to a PST file

<!-- p.2259 -->

     To learn how to open the Exchange Management Shell in your on-premises Exchange
     organization, see Open the Exchange Management Shell.

Use the EAC to create a search
As previously explained, to create eDiscovery searches, you have to sign in to a user account
that has an SMTP address in your organization.

   1. Go to Compliance management > In-place eDiscovery & Hold, and then click New                 .

   2. In the New In-Place eDiscovery & Hold window, on the Name and description page,
     type a name for the search, add an optional description, and then click Next.

   3. On the Mailboxes and Public folders page, select the content sources to search:

          To include all mailboxes in the search, click Search all mailboxes. If you select this
          option, you won't be able to enable an In-Place Hold for the search.

          To exclude mailboxes from the search (and search only public folders), click Don't
          search any mailboxes.

          To include specific mailboxes in the search, click Specify mailboxes to search, and
          then add that mailboxes that you want to search.

          To include public folders in the search (or to place public folders on hold), click
          Search all public folders. For more information about searching public folders, see
          Search and place a hold on public folders using In-Place eDiscovery.

<!-- p.2260 -->

4. On the Search query page, complete the following fields:

       Include all content: Select this option to include all content in the search results. If
       you select this option, you can't specify additional search criteria.

       Filter based on criteria: Select this option to specify search criteria, including
       keywords, start and end dates, sender and recipient addresses, and message types.
       For more information about search queries, see Message properties and search
       operators for In-Place eDiscovery in Exchange Server.

<!-- p.2261 -->

         ７ Note

         The From: and To/Cc/Bcc: fields are connected by an OR operator in the search
         query that's created when you run the search. That means any message sent or
         received by any of the specified users (and matches the other search criteria) is
         included in the search results. The dates are connected by an AND operator.

5. On the In-Place Hold settings page, you can select the Place content matching the
  search query in selected sources on hold check box, and then select one of the following
  options to place items on In-Place Hold:

       Hold indefinitely: Select this option to place the returned items on an indefinite
       hold. Items on hold will be preserved until you remove the content source from the
       search or if you delete the search.

       Specify number of days to hold items relative to their received date Use this
       option to hold items for a specific period. For example, you can use this option if
       your organization requires that all messages be retained for at least seven years. You
       can use a time-based In-Place Hold along with a retention policy to make sure items
       are deleted in seven years.

         ） Important

         When placing content sources or specific items on In-Place Hold for legal
         purposes, it's generally recommended to hold items indefinitely and remove

<!-- p.2262 -->

               the hold when the case or investigation is completed.

   6. Click Finish to save the search and return an estimate of the total size and number of
     items that will be returned by the search based on the criteria you specified. Estimates are
     displayed in the details pane. Click Refresh    to update the information displayed in the
     details pane.

Use the Exchange Management Shell to create a
search
Here are four examples of using the Exchange Management Shell to search and place a hold
on content in mailboxes and public folders. For detailed syntax and parameter information
about using the Exchange Management Shell to create eDiscovery searches, see New-
MailboxSearch

Example 1
This example creates the search Discovery-CaseId012 for items containing the keywords
Contoso and ProjectA. The search results are place on In-Place hold, with an unlimited hold
duration. The search also includes the following criteria:

     Start date: 1/1/2013

     End date: 12/31/2015

     Source mailbox: DG-Finance

     Target mailbox: Discovery Search Mailbox

     Message types: Email

     Log level: Full

  ） Important

  If you don't specify a search query, a date range, or a message type, all items in the source
  mailboxes or public folders are returned in the results. The results would be similar to
  selecting Include all content on the Search query page in the EAC.

  PowerShell

<!-- p.2263 -->

  New-MailboxSearch "Discovery-CaseId012" -StartDate "01/01/2013" -EndDate
  "12/31/2015" -SourceMailboxes "DG-Finance" -TargetMailbox "Discovery Search
  Mailbox" -SearchQuery '"Contoso" AND "Project A"' -MessageTypes Email -
  IncludeUnsearchableItems -LogLevel Full -InPlaceHoldEnabled $true

  PowerShell

  Start-MailboxSearch "Discovery-CaseId012"

After using the Exchange Management Shell to create an In-Place eDiscovery search, you have
to start the search by using the Start-MailboxSearch cmdlet to copy messages to the discovery
mailbox specified in the TargetMailbox parameter. For details, see Copy eDiscovery search
results to a discovery mailbox.

  ７ Note

  When using the StartDate and EndDate parameters, you have to use the date format of
  MM/dd/yyyy, even if your local machine settings are configured to use a different date
  format, such as dd/MM/yyyy. For example, to search for messages sent between April 1,
  2015 and July 1, 2015, you would use 04/01/2015 and 07/01/2015 for the start and end
  dates.

Example 2
This example creates an In-Place eDiscovery search named HRCase090116 that searches for
email messages sent by Alex Darrow to Sara Davis in 2015.

  PowerShell

  New-MailboxSearch "HRCase090116" -StartDate "01/01/2015" -EndDate "12/31/2015" -
  SourceMailboxes alexd,sarad -SearchQuery 'From:alexd@contoso.com AND
  To:sarad@contoso.com' -MessageTypes Email -TargetMailbox "Discovery Search
  Mailbox" -IncludeUnsearchableItems -LogLevel Full

  PowerShell

  Start-MailboxSearch "HRCase090116"

Example 3

<!-- p.2264 -->

This example creates an estimate-only search that searches all public folders in the
organization for items sent between January 1, 2015 and June 30, 2015, and that contain the
phrase "patent infringement". The search doesn't include any mailboxes. The Start-
MailboxSearch cmdlet is used to start the estimate-only search.

  PowerShell

  New-MailboxSearch -Name "Northwind Subpoena-All PFs" -AllPublicFolderSources $true
  -AllSourceMailboxes $false -SearchQuery "patent infringement" -StartDate
  "01/01/2015" -EndDate "06/30/2015" -TargetMailbox "Discovery Search Mailbox" -
  EstimateOnly

  PowerShell

  Start-MailboxSearch "Northwind Subpoena-All PFs"

Example 4
This example searches all mailboxes and public folders for any content that contains the words
"price list" and "Contoso" and that was sent after January 1, 2015. The Start-MailboxSearch
cmdlet is use to run the search and copy the search results to the discovery mailbox.

  PowerShell

  New-MailboxSearch -Name "Contoso Litigation" -AllSourceMailboxes $true -
  AllPublicFolderSources $true -SearchQuery '"price list" AND "contoso"' -StartDate
  "01/01/2015" -TargetMailbox "Discovery Search Mailbox"

  PowerShell

  Start-MailboxSearch "Contoso Litigation"

Use the EAC to estimate or preview search results
After you create an eDiscovery search, you can use the EAC to get an estimate and preview of
the search results. If you created a new search using the New-MailboxSearch cmdlet, you can
use the Exchange Management Shell to start the search to get an estimate of the search
results.

   1. Go to Compliance management > In-Place eDiscovery & Hold.

   2. In the list view, select the search, and then do one of the following:

<!-- p.2265 -->

Click Search    > Estimate search results to return an estimate of the total size and
number of items that will be returned by the search based on the criteria you
specified. Selecting this option restarts the search and performs an estimate.

Search estimates are displayed in the details pane. Click Refresh    to update the
information displayed in the details pane.

Click Preview search results in the details pane to preview the results after the
search estimate is completed. Selecting this option opens the eDiscovery search
preview window. All messages returned from the mailboxes or public folders that
were searched are displayed.

  ７ Note

  The mailboxes or public folders that were searched are listed in the right pane
  in the eDiscovery search preview window. For each source, the number of
  items returned and the total size of these items is also displayed. All items
  returned by the search are listed in the right pane, and can be sorted by newest
  or oldest date. Items from each mailbox or public folder can't be displayed in
  the right pane by clicking a source in the left pane. To view the items returned
  from a specific mailbox or public folder, you can copy the search results and
  view the items in the discovery mailbox.

<!-- p.2266 -->

Use the Exchange Management Shell to estimate
search results
You can use the EstimateOnly switch to get an estimate of the search results and not copy the
results to a discovery mailbox. You have to start an estimate-only search with the Start-
MailboxSearch cmdlet. Then you can retrieve the estimated search results by using the Get-
MailboxSearch cmdlet. You can't use the Exchange Management Shell to preview messages
returned in search results.

For example, you would run the following commands to create a new search and then display
an estimate of the search results:

  PowerShell

  New-MailboxSearch "FY15 Q2 Financial Results" -StartDate "04/01/2015" -EndDate
  "06/30/2015" -SourceMailboxes "DG-Finance" -SearchQuery '"Financial" AND
  "Fabrikam"' -EstimateOnly -IncludeKeywordStatistics

  PowerShell

  Start-MailboxSearch "FY15 Q2 Financial Results"

  PowerShell

  Get-MailboxSearch "FY15 Q2 Financial Results"

To display specific information about the estimated search results from the previous example,
you could run the following command:

  PowerShell

  Get-MailboxSearch "FY15 Q2 Financial Results" | Format-List
  Name,Status,LastRunBy,LastStartTime,LastEndTime,Sources,SearchQuery,ResultSizeEsti
  mate,ResultNumberEstimate,Errors,KeywordHits

More information
     After you create a new eDiscovery search, you can copy search results to the discovery
     mailbox and export those search results to a PST file. For more information, see:

        Copy eDiscovery search results to a discovery mailbox

<!-- p.2267 -->

   Export eDiscovery search results to a PST file

After you run an eDiscovery search estimate (that includes keywords in the search
criteria), you can view keyword statistics by clicking View keyword statistics in the details
pane for the selected search. These statistics show details about the number of items
returned for each keyword used in the search query. However, if more than 100 source
mailboxes are included in the search, an error will be returned if you try to view keyword
statistics. To view keyword statistics, no more than 100 source mailboxes can be included
in the search.

If you use Get-MailboxSearch in Exchange Online to retrieve information about an
eDiscovery search, you have to specify the name of a search to return a complete list of
the search properties; for example, Get-MailboxSearch "Contoso Legal Case" . If you run
the Get-MailboxSearch cmdlet without using any parameters, the following properties
aren't returned:

   SourceMailboxes

   Sources

   PublicFolderSources

   SearchQuery

   ResultsLink

   PreviewResultsLink

   Errors

   The reason is that it requires a lot of resources to return these properties for all
   eDiscovery searches in your organization.

<!-- p.2268 -->

Copy eDiscovery search results to a
discovery mailbox in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

After you create an In-Place eDiscovery search in Exchange Server, you can use the Exchange
admin center (EAC) to copy the results to a discovery mailbox. You can also use the Exchange
Management Shell to start an eDiscovery search that was created using the New-
MailboxSearch cmdlet, which will copy the results to the discovery mailbox that was specified
when you created the search.

What do you need to know before you begin?
      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "In-Place eDiscovery" entry in the
      Messaging policy and compliance permissions in Exchange Server topic.

      An eDiscovery search has to be created, by using the EAC or the Exchange Management
      Shell, before you can copy the search results. For details, see Create an In-Place
      eDiscovery search in Exchange Server.

      Exchange Server Setup creates a discovery mailbox called Discovery Search Mailbox to
      copy search results. You can create additional discovery mailboxes. For details, see Create
      a Discovery Mailbox.

      It might take 5 minutes or longer to copy search results to a discovery mailbox,
      depending on the number of mailbox items returned in the results.

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

Use the EAC to copy search results
   1. In the EAC, go to Compliance management > In-Place eDiscovery & Hold.

   2. In the list view, select an eDiscovery search.

   3. Click Search     , and then click Copy search results from the drop-down list.

   4. In Copy Search Results, select from the following options:

<!-- p.2269 -->

         Include unsearchable items: Select this check box to include mailbox items that
         couldn't be searched (for example, messages with attachments of file types that
         couldn't be indexed by Exchange Search). For more information, see Unsearchable
         Items in Exchange eDiscovery.

         Enable de-duplication: Select this check box to exclude duplicate messages. Only a
         single instance of a message will be copied to the discovery mailbox.

         Enable full logging: Select this check box to include a full log in search results.

         Send me mail when the copy is completed: Select this check box to get an email
         notification when the search is completed.

         Copy results to this discovery mailbox: Click Browse to select the discovery mailbox
         where you want the search results copied to.

 5. Click Copy to start the process to copy the search results to the specified discovery
   mailbox.

 6. Click Refresh      to update the information about the copying status that is displayed in
   the details pane.

 7. When copying is complete, click Open to open the discovery mailbox to view the search
   results.

Use the Exchange Management Shell to copy
search results

<!-- p.2270 -->

After using the New-MailboxSearch cmdlet to create an In-Place eDiscovery search, you need
to start the search to copy messages to the discovery mailbox you specified in the
TargetMailbox parameter. For information about creating eDiscovery searches by using the
Exchange Management Shell, see:

     Create an In-Place eDiscovery search in Exchange Server

     New-MailboxSearch

In the following example, you would run the following command to start an eDiscovery search
named Fabrikam Investigation to copy the search results to the discovery mailbox that was
specified by the TargetMailbox parameter when the search was created.

  PowerShell

  Start-MailboxSearch "Fabrikam Investigation"

If you used the EstimateOnly switch to get an estimate of the search results, you have to
remove the switch before you can copy the search results. You also have to specify a discovery
mailbox to copy to search results to. For example, say you created an estimate-only search by
using the following command:

  PowerShell

  New-MailboxSearch "FY15 Q2 Financial Results" -StartDate "04/01/2015" -EndDate
  "06/30/2015" -SourceMailboxes "DG-Finance" -SearchQuery '"Financial" AND
  "Fabrikam"' -EstimateOnly -IncludeUnsearchableItems

To copy the results of this search to a discovery mailbox, you would run the following
commands:

  PowerShell

  Set-MailboxSearch "FY15 Q2 Financial Results" -EstimateOnly $false -TargetMailbox
  "Discovery Search Mailbox"

  PowerShell

  Start-MailboxSearch "FY15 Q2 Financial Results"

For more information about these cmdlets, see the following topics:

     Set-Mailboxsearch

<!-- p.2271 -->

  Start-MailboxSearch

More information
  After you copy search results to the discovery mailbox, you can also export those search
  results to a PST file. For more information, see Export eDiscovery search results to a PST
  file. Note that you can export search results without having to copy them to a discovery
  mailbox. You can create an estimate-only search, start it, and then export the search
  results.

  For more information about unsearchable items, see Unsearchable Items in Exchange
  eDiscovery.

  If you're copying all mailbox content within a specific date range (by not specifying any
  keywords in the search criteria), then all unsearchable items within that date range will be
  automatically included in the search results. Therefore, don't select the Include
  unsearchable items checkbox when copying search results. Otherwise, a duplicate copy
  of all unsearchable items will be copied to the discovery mailbox.

  In addition to copying the search results to a discovery mailbox, you can also estimate or
  preview the search results for a selected search.

     Estimate search results: This option returns an estimate of the total size and number
     of items that will be returned by the search based on the criteria you specified.
     Estimates are displayed in the details pane in the EAC.

     Preview search results: This option lets you preview the search results returned by the
     search instead of having to copy them to a discovery mailbox to view. This lets you
     quickly determine whether the search results are relevant. After you preview the
     results, you can revise your search query to narrow the search results and rerun the
     search. Items in the preview page are read-only versions of the actual search results, so
     you can't move, edit, delete or forward on the preview page.

     For more information, see Use the EAC to estimate or preview search results.

<!-- p.2272 -->

Export eDiscovery search results to a PST
file
Article • 04/30/2025

APPLIES TO:        2016      2019     Subscription Edition

You can use the eDiscovery Export tool in the Exchange admin center (EAC) to export the
results of an In-Place eDiscovery search to an Outlook Data File, which is also called a PST file.
Search results will contain items from mailboxes and public folders, depending on the content
sources from the eDiscovery search. This lets you distribute search results to other people
within your organization, such as a human resources manager or records manager, or to
opposing counsel in a legal case. After search results are exported to a PST file, you or other
users can open them in Outlook to review or print messages returned in the search results. PST
files can also be opened in third-party eDiscovery and reporting applications.

What do you need to know before you begin?
      The amount of time it takes to export search results will vary based on the amount and
      size of the search results that will be exported.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "In-Place eDiscovery" entry in the
      Messaging policy and compliance permissions in Exchange Server topic.

      You'll need an active mail account attached to the account you wish to export.

      The computer you use to export search results to a PST file needs to meet the following
      system requirements:

         32- and 64-bit versions of Windows 7 and later versions

         Microsoft .NET Framework 4.7

         A supported browser:

         Internet Explorer 8 and later versions

         OR

         Mozilla Firefox or Google Chrome, with the ClickOnce add-in installed

<!-- p.2273 -->

Use the EAC to export In-Place eDiscovery search
results to a PST file
 1. In the EAC, go to Compliance management > In-Place eDiscovery & Hold.

 2. In the list view, select the eDiscovery search you want to export the results of, and then
   click Export to a PST file.

 3. In the eDiscovery PST Export Tool window, do the following:

         Click Browse to specify the location where you want to download the PST file.

         Click the Enable deduplication checkbox to exclude duplicate messages. Only a
         single instance of a message will be included in the PST file.

         Click the Include unsearchable items checkbox to include items that couldn't be
         searched (for example, messages with attachments of file types that couldn't be
         indexed by Exchange Search). Unsearchable items are exported to a separate PST
         file.

   Note: Including unsearchable items when you export eDiscovery search results takes
   longer when mailboxes or public folders contain a lot of unsearchable items. To reduce
   the time it takes to export search results and prevent large PST export files, consider the
   following recommendations:

         Create multiple eDiscovery searches that each search a fewer number of source
         mailboxes.

         Create an eDiscovery search that only includes public folders.

         If you're exporting all mailbox or public folder content within a specific date range
         (by not specifying any keywords in the search criteria), then all unsearchable items
         within that date range will be automatically included in the search results. Therefore,
         don't select the Include unsearchable items checkbox.

<!-- p.2274 -->

 4. Click Start to export the search results to a PST file.

   A window is displayed that contains status information about the export process.

More information
   Another way to reduce the size of PST export files is to export only the unsearchable
   items for an eDiscovery search. To do this, create or edit a search, specify a start date in
   the future, and then remove any keywords from the Keywords box. This will result in no
   search results being returned. When you copy or export the search results and select the
   Include unsearchable items checkbox, only the unsearchable items will be copied to the
   discovery mailbox or exported to a PST file.

   If you enable deduplication, all search results are exported in a single PST file. If you don't
   enable deduplication, a separate PST file is exported for each mailbox (including public
   folder mailboxes if the search includes public folders) that contains search results. And as
   previously stated, unsearchable items are exported to a separate PST file.

   In addition to the PST files that contain the search results, two other files are also
   exported:

      A configuration file (.txt file format) that contains information about the PST export
      request, such as the name of the eDiscovery search that was exported, the date and
      time of the export, whether de-duplication and unsearchable items were enabled, the
      search query, and the content sources that were searched.

      A search results log (.csv file format) that contains an entry for each message returned
      in the search results. Each entry identifies the content source where the message is
      located. If you've enabled de-duplication, this helps you identify all mailboxes or public
      folders that contain a duplicate message.

   The name of the search is the first part of the filename for each file that is exported. Also,
   the date and time of the export request is appended to the filename of each PST file and
   the results log.

   You can't use the PST export tool with accounts that require mult-factor authentication
   (MFA). Instead, you need to create an app password for the PST export tool. For
   instructions, see Create an app password for Microsoft 365      .

<!-- p.2275 -->

Message properties and search operators
for In-Place eDiscovery in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016       2019          Subscription Edition

This topic describes the properties of Exchange email messages that you can search by using
In-Place eDiscovery & Hold in Exchange Server 2016 or Exchange Server 2019. The topic also
describes Boolean search operators and other search query techniques that you can use to
refine eDiscovery search results.

In-Place eDiscovery uses Keyword Query Language (KQL). For more information, see Keyword
Query Language syntax reference.

Searchable properties in Exchange
The following table lists email message properties that can be searched using an In-Place
eDiscovery search or by using the New-MailboxSearch or the Set-MailboxSearch cmdlet. The
table includes an example of the property:value syntax for each property and a description of
the search results returned by the examples.

                                                                                          ﾉ   Expand table

 Property       Property description           Examples                  Search results returned by
                                                                         the examples

 Attachment     The names of files             attachment:               Messages that have an
                attached to an email           annualreport.ppt          attached file with a name
                message.                                                 matching annualreport.ppt, for
                                               attachment: annual*       example, "annualreport.ppt" or
                                                                         "2017 annualreport.ppt".

                                                                         In the second example, using
                                                                         the wildcard returns messages
                                                                         with the word "annual" in the
                                                                         file name of an attachment.

 Bcc2           The BCC field of an email      bcc: pilarp@contoso.com   All examples return messages
                message.1                                                with Pilar Pinilla included in
                                               bcc:pilarp                the Bcc field.

                                               bcc:"Pilar Pinilla"

 Category       The categories to search.      category:"Red Category"   Messages that have been
                Categories can be defined                                assigned the red category in

<!-- p.2276 -->

Property        Property description          Examples                    Search results returned by
                                                                          the examples

                by users by using Outlook                                 the source mailboxes.
                or Outlook on the web
                (formerly known as
                Outlook Web App). Valid
                values are:
                      blue
                      green
                      orange
                      purple
                      red
                      yellow

Cc              The CC field of an email      cc:pilarp@contoso.com       In both examples, messages
                message.1                                                 with Pilar Pinilla specified in
                                              cc:"Pilar Pinilla"          the CC field.

From            The sender of an email        from:pilarp@contoso.com     Messages sent by the specified
                           1
                message.                                                  user or sent from a specified
                                              from: contoso.com           domain.

Importance      The importance of an          importance: high            Messages that are marked as
                email message, which a                                    high importance, medium
                sender can specify when       importance: medium          importance, or low
                sending a message. By                                     importance.
                default, messages are sent    importance: low
                with normal importance,
                unless the sender sets the
                importance as high or low.

Kind            The message type to           kind: email                 Email messages that meet the
                search. Valid values are:                                 search criteria. The second
                      contacts                kind: email OR kind:im OR   example returns email
                      docs                    kind:voicemail              messages, instant messaging
                      email                                               conversations, and voice
                      faxes                                               messages that meet the search
                      im                                                  criteria.
                      journals
                      meetings
                      notes
                      posts
                      rssfeeds
                      tasks
                      voicemail

Participants2   All the people fields in an   participants:               Messages sent by or sent to
                email message; these          garthf@contoso.com          garthf@contoso.com.

<!-- p.2277 -->

Property      Property description           Examples                    Search results returned by
                                                                         the examples

              fields are From, To, CC, and
              BCC.1                          participants: contoso.com   The second example returns all
                                                                         messages sent by or sent to a
                                                                         user in the contoso.com
                                                                         domain.

Received      The date that an email         received: 04/15/2015        Messages that were received
              message was received by a                                  on April 15, 2014. The second
              recipient.                     received>=01/01/2015        example returns all messages
                                             AND                         received between January 1,
                                             received<=03/31/2015        2014 and March 31, 2014.

Recipients2   All recipient fields in an     recipients:                 Messages sent to
              email message; these           garthf@contoso.com          garthf@contoso.com.
              fields are To, CC, and BCC.1
                                             recipients: contoso.com     The second example returns
                                                                         messages sent to any recipient
                                                                         in the contoso.com domain.

Sent          The date that an email         sent: 07/01/2015            Messages that were sent on
              message was sent by the                                    the specified date or sent
              sender.                        sent>=06/01/2015 AND        within the specified date
                                             sent<=07/01/2015            range.

Size          The size of an item, in        size>26214400               Messages larger than 25 MB.
              bytes.
                                             size:1..1048576             The second example returns
                                                                         messages from 1 through
                                                                         1,048,576 bytes (1 MB) in size.

Subject       The text in the subject line   subject:"Quarterly          Messages that contain the
              of an email message.           Financials"                 exact phrase "Quarterly
                                                                         Financials" anywhere in the
                                             subject: northwind          text of the subject line.

                                                                         The second example returns all
                                                                         messages that contain the
                                                                         word northwind in the subject
                                                                         line.

To            The To field of an email       to: annb@contoso.com        All examples return messages
                           1
              message.                                                   where Ann Beebe is specified
                                             to:annb                     in the To: line.

                                             to:"Ann Beebe"

<!-- p.2278 -->

1
    For the value of a recipient property, you can use the SMTP address, display name, or alias to
specify a user. For example, you can use annb@contoso.com, annb, or "Ann Beebe" to specify
the user Ann Beebe.

2
    While using BCC, Participants, or Recipients properties, ensure you are focused on the
Sender's mailbox for proper search results.

Supported search operators
Boolean search operators, such as AND, OR, and NOT, help you define more-precise mailbox
searches by including or excluding specific words in the search query. Other techniques, such
as using property operators (such as >= or ..), quotation marks, parentheses, and wildcards,
help you refine eDiscovery search queries. The following table lists the operators that you can
use to narrow or broaden search results.

                                                                                        ﾉ   Expand table

    Operator   Usage               Description

    AND        keyword1 AND        Returns messages that include all of the specified keywords or
               keyword2            property: value expressions.

    +          keyword1            Returns items that contain either keyword2 or keyword3 and that also
               +keyword2           contain keyword1 . Therefore, this example is equivalent to the query
               +keyword3           (keyword2 OR keyword3) AND keyword1 .

                                   The query keyword1 + keyword2 (with a space after the + symbol) isn't
                                   the same as using the AND operator. This query would be equivalent
                                   to "keyword1 + keyword2" and return items with the exact phase
                                   "keyword1 + keyword2" .

    OR         keyword1 OR         Returns messages that include one or more of the specified keywords
               keyword2            or property: value expressions.

    NOT        keyword1 NOT        Excludes messages specified by a keyword or a property: value
               keyword2            expression. For example, NOT from:"Ann Beebe" excludes messages
                                   sent by Ann Beebe.
               NOT from:"Ann
               Beebe"

    -          keyword1 -          The same as the NOT operator. This query returns items that contain
               keyword2            keyword1 and excludes items that contain keyword2 .

    NEAR       keyword1 NEAR(n)    Returns messages with words that are near each other, where n equals
               keyword2            the number of words apart. For example, best NEAR(5) worst returns

<!-- p.2279 -->

    Operator   Usage                    Description

                                        messages where the word "worst" is within five words of "best". If no
                                        number is specified, the default distance is eight words.

    :          property:value           The colon (:) in the property:value syntax specifies that the property
                                        value being searched for equals the specified value. For example,
                                        recipients:garthf@contoso.com returns any message sent to
                                        garthf@contoso.com.

    <          property<value           Denotes that the property being searched is less than the specified
                                        value. 1

    >          property>value           Denotes that the property being searched is greater than the specified
                                        value.1

    <=         property<=value          Denotes that the property being searched is less than or equal to a
                                        specific value.1

    >=         property>=value          Denotes that the property being searched is greater than or equal to a
                                        specific value.1

    ..         property:                Denotes that the property being searched is greater than or equal to
               value1..value2           value1 and less than or equal to value2.1

    ""         "fair value"             Use double quotation marks (" ") to search for an exact phrase or term
                                        in keyword and property: value search queries.
               subject:"Quarterly
               Financials"

    *          cat*                     Prefix wildcard searches (where the asterisk is placed at the end of a
                                        word) match for zero or more characters in keywords or property:
               subject:set*             value queries. For example, subject:set* returns messages that
                                        contain the word set, setup, and setting (and other words that start
                                        with "set") in the subject line.

    ()         (fair OR free) AND       Parentheses group together Boolean phrases, property: value items,
               from: contoso.com        and keywords. For example, (quarterly financials) returns items
                                        that contain the words quarterly and financials.
               (IPO OR initial) AND
               (stock OR shares)

               (quarterly financials)

1
    Use this operator for properties that have date or numeric values.

2
    Boolean search operators must be uppercase; for example, AND. Using lowercase operators
in search queries will return an error.

<!-- p.2280 -->

Unsupported characters in search queries
Unsupported characters in a search query typically cause a search error or return unintended
results. Unsupported characters are often hidden and they're typically added to a query when
you copy the query or parts of the query from other applications (such as Microsoft Word or
Microsoft Excel) and copy them to the keyword box on the query page of In-Place eDiscovery
search.

Here's a list of the unsupported characters for an In-Place eDiscovery search query.

     Smart quotation marks: Smart single and double quotation marks (also called curly
     quotes) aren't supported. Only straight quotation marks can be used in a search query.

     Non-printable and control characters: Non-printable and control characters don't
     represent a written symbol, such as a alpha-numeric character. Examples of non-printable
     and control characters include characters that format text or separate lines of text.

     Left-to-right and right-to-left marks: These characters are control characters used to
     indicate text direction for left-to-right languages (such as English and Spanish) and right-
     to-left languages (such as Arabic and Hebrew).

     Lowercase Boolean operators: As previous explained, you have to use uppercase Boolean
     operators, such as AND and OR, in a search query. The query syntax will often indicate
     that a Boolean operator is being used even though lowercase operators might be used;
     for example, (WordA or WordB) and (WordC or WordD) .

How to prevent unsupported characters in your search queries? The best way to prevent
unsupported characters is to just type the query in the keyword box. Alternatively, you can
copy a query from Word or Excel and then paste it to file in a plain text editor, such as
Microsoft Notepad. Then save the text file and select ANSI in the Encoding drop-down list.
This selection will remove any formatting and unsupported characters. Then you can copy and
paste the query from the text file to the keyword query box.

Search tips and tricks
     Keyword searches are not case sensitive. For example, cat and CAT return the same
     results.

     A space between two keywords or two property: value expressions is the same as using
     AND. For example, from:"Sara Davis" subject:reorganization returns all messages sent
     by Sara Davis that contain the word reorganization in the subject line.
