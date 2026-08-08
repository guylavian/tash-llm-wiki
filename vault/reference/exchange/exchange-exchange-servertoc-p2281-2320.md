---
title: "Exchange Server — pages 2281-2320"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2281-2320
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2281-2320
family: exchange
documentKind: "doc"
abstract: "Use syntax that matches the property: value format. Values are not case-sensitive, and they can't have a space after the operator. If there is a space, your intended value will just be full-text searched. For example, to: pilarp searches for \"pilarp\" as a keyword, rather than fo"
---

# Exchange Server — pages 2281-2320

<!-- p.2281 -->

Use syntax that matches the property: value format. Values are not case-sensitive, and
they can't have a space after the operator. If there is a space, your intended value will just
be full-text searched. For example, to: pilarp searches for "pilarp" as a keyword, rather
than for messages that were sent to pilarp.

When searching a recipient property, such as To, From, Cc, or Recipients, you can use an
SMTP address, alias, or display name to denote a recipient. For example, you can use
pilarp@contoso.com, pilarp, or "Pilar Pinilla".

You can use only suffix wildcard searches (for example, cat* or set*). Prefix wildcard
searches (*cat) or substring wildcard searches (*cat*) aren't supported.

When searching a property, use double quotation marks (" ") if the search value consists
of multiple words. For example, subject:budget Q1 returns messages that contain budget
in the subject line and that contain Q1 anywhere in the message or in any of the message
properties. Using subject:"budget Q1" returns all messages that contain budget Q1
anywhere in the subject line.

To exclude content marked with a certain property value from your search results, place a
minus sign (-) before the name of the property. For example, -from:"Sara Davis" will
exclude any messages sent by Sara Davis.

<!-- p.2282 -->

Search and place a hold on public folders
using In-Place eDiscovery
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

You can use In-Place eDiscovery to search for content in public folders and place content in
public folders on In-Place Hold. Like content in user mailboxes, content in public folders might
be relevant if your organization has to respond to legal requests such as lawsuits or regulatory
investigations.

Before you begin
      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "In-Place eDiscovery" entry in the
      Messaging policy and compliance permissions in Exchange Server topic.

      You can include mailboxes and public folders in the same eDiscovery search.

      You can use an In-Place Hold to place content in public folders on hold. But if you select
      the option to search all mailboxes in your organization, you can't use the search to place
      a hold on any of the content sources of the search.

Use the EAC to search and place a hold on public
folders
   1. Go to Compliance management > In-place eDiscovery & hold.

   2. Click New        .

   3. On the Name and description page, type a name for the search, add an optional
      description, and then click Next.

   4. On the Mailboxes and Public folders page, under Public folders, click Search all public
      folders. Additionally, you can configure whether to include mailboxes in the search:

            To exclude mailboxes from the search, click Don't search any mailboxes.

            To include specific mailboxes in the search, click Specify mailboxes to search, and
            then add that mailboxes that you want to search.

<!-- p.2283 -->

          ７ Note

          As previously explained, if you select the Search all mailboxesoption, you won't
          be able to enable an In-Place Hold for the search.

5. On the Search query page, complete the following fields:

       Include all content: Select this option to include all content in the selected sources
       in the search results. If you select this option, you can't specify additional search
       criteria.

       Filter based on criteria: Select this option to specify search criteria, including
       keywords, start and end dates, sender and recipient addresses, and message types.

6. On the In-Place Hold settings page, you can select the Place content matching the
  search query in selected mailboxes on hold to place an In-Place Hold on all public
  folders in your organization. Leave the check box unselected to not place content on
  hold. If you place content on hold, select one of the following options for the hold
  duration:

       Hold indefinitely: Click this button to place items returned by the search on an
       indefinite hold. Items on hold will be preserved until you remove public folders from

<!-- p.2284 -->

           the search or remove the search.

           Specify number of days to hold items relative to their received date: Click this
           button to hold items in public folders for a specific period. For example, you can use
           this option if your organization requires that public folder content be retained for at
           least seven years.

   7. Click Finish to save the search and return an estimate of the total size and number of
     items that will be returned by the search or placed on hold based on the criteria you
     specified.

     Estimates are displayed in the details pane on the In-Place eDiscovery & Hold page.
     Select a search and then click Refresh     to update the information about the search
     that's displayed in the details pane.

Use the Exchange Management Shell to search and
place a hold on public folders
Here are three examples of using the Exchange Management Shell to search and place a hold
on public folders.

Example 1
This example creates an estimate-only search that searches all public folders in the
organization for items sent between January 1, 2015 and June 30, 2015 and that contain the
phrase "patent infringement". The search doesn't include any mailboxes. The Start-
MailboxSearch cmdlet is used to start the estimate-only search.

  PowerShell

  New-MailboxSearch -Name "Northwind Subpoena-All PFs" -AllPublicFolderSources $true
  -AllSourceMailboxes $false -SearchQuery "patent infringement" -StartDate
  "01/01/2015" -EndDate "06/30/2015" -TargetMailbox "Discovery Search Mailbox" -
  EstimateOnly

  PowerShell

  Start-MailboxSearch "Northwind Subpoena-All PFs"

Example 2

<!-- p.2285 -->

This example places all content in all public folders on In-Place hold, with an unlimited hold
duration. The Start-MailboxSearch cmdlet is use to run the search and place the content on
hold.

  PowerShell

  New-MailboxSearch -Name "Hold for all PFs" -AllPublicFolderSources $true -
  AllSourceMailboxes $false -EstimateOnly -InPlaceHoldEnabled $true

  PowerShell

  Start-MailboxSearch "Hold for all PFs"

Example 3
This example searches all mailboxes and public folders for any content that contains the words
"price list" and "Contoso" and that was sent after January 1, 2015. The Start-MailboxSearch
cmdlet is use to run the search and copy the search results to the discovery mailbox.

  PowerShell

  New-MailboxSearch -Name "Contoso Litigation" -AllSourceMailboxes $true -
  AllPublicFolderSources $true -SearchQuery '"price list" AND "contoso"' -StartDate
  "01/01/2015" -TargetMailbox "Discovery Search Mailbox"

  PowerShell

  Start-MailboxSearch "Contoso Litigation"

More information
        You can only search or place holds on all public folders in your organization. You can't
        select specific public folders to search.

        Moving public folders to a different public folder mailbox doesn't affect searching or
        placing holds on public folders that have been moved.

        Public folder mailboxes are counted against the source mailbox limit for the eDiscovery
        search.

        You can't delete public folders that are on In-Place Hold. You will have to remove the hold
        before you can delete any public folder.

<!-- p.2286 -->

Mail-enabling a public folder doesn't impact using In-Place eDiscovery to search or place
holds on public folders. Mail-enabled and non-mail enabled public folders can be
searched and placed on hold.

<!-- p.2287 -->

Use Compliance Search to search all
mailboxes in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

The Compliance Search feature in Exchange Server allows you to search all mailboxes in your
organization. Unlike In-Place eDiscovery where you can search up to 10,000 mailboxes, there
are no limits for the number of target mailboxes in a single search. For scenarios that require
you to perform organization-wide searches, you can use the New-ComplianceSearch cmdlet
to search all mailboxes. Then you can use the workflow features of In-Place eDiscovery to
perform other eDiscovery-related tasks, such as placing mailboxes on hold and exporting
search results. For example, let's say you have to search all mailboxes to identify specific
custodians that are responsive to a legal case. You can use the New-ComplianceSearch cmdlet
to search all mailboxes in your organization to identify those that are responsive to the case.
Then you can use that list of custodian mailboxes as the source mailboxes for an In-Place
eDiscovery. Using In-Place eDiscovery also allows you to put a hold on those source mailboxes,
copy search results to a discovery mailbox, and export the search results.

This topic includes a script that you can run to create an In-Place eDiscovery search by using
the list of source mailboxes and search query from a compliance search that is created by
running the New-ComplianceSearch cmdlet.

Step 1: Run the New-ComplianceSearch cmdlet to
search all mailboxes
The first step is to use the Exchange Management Shell to create a compliance search that
searches all mailboxes in your organization. There's no limit for the number of mailboxes for a
single compliance search. Specify an appropriate keyword query (or a query for sensitive
information types) so that the search returns only those source mailboxes that are relevant to
your investigation. If necessary, refine the search query to narrow the scope of search results
and source mailboxes that are returned.

  ７ Note

  If the source compliance search doesn't return any results, an In-Place eDiscovery won't be
  created when you run the script in Step 3. You may have to revise the search query and
  then rerun the compliance search to return search results.

<!-- p.2288 -->

Here's an example of using the New-ComplianceSearch cmdlet to search all mailboxes in your
organization. The search query returns all messages sent between October 1, 2015 and
October 31, 2015 and that contain the phrase "financial report" in the subject line. The first
command creates the search, and the second command runs the search.

  PowerShell

  New-ComplianceSearch -Name "Search All-Financial Report" -ExchangeLocation all -
  ContentMatchQuery 'sent>=01/01/2015 AND sent<=06/30/2015 AND subject:"financial
  report"'

  PowerShell

  Start-ComplianceSearch -Identity "Search All-Financial Report"

For more information, see New-ComplianceSearch.

  ） Important

  When you create a compliance search by using the New-ComplianceSearch cmdlet, a
  shadow In-Place eDiscovery search is created (but not started) and displayed on the In-
  Place eDiscovery & Hold page in the Exchange admin center (EAC). It's also returned by
  using the Get-MailboxSearch cmdlet. This mailbox search is named
  ComplianceSearchName -shadow. We recommend that you delete the shadow In-Place
  eDiscovery search, and use the script in Step 3 to create the In-Place eDiscovery search.
  The functionality of creating a shadow search will be removed in a cumulative update for
  Exchange 2016.

(Optional) Step 2: Verify the number of source
mailboxes in the compliance search
A compliance search will return a maximum of 500 source mailboxes that contain search
results. If there are more than 500 mailboxes that contain content that matches the search
query, only the top 500 mailboxes with the most search results are included in the compliance
search that you created in the previous step. So if more than 500 mailboxes contain search
results, some of those mailboxes won't be included in the list of source mailboxes copied to
the new In-Place eDiscovery search created in Step 3.

To help you create a compliance search with no more than 500 source mailboxes, follow these
steps to run a script that displays the number of source mailboxes (that contain search results)

<!-- p.2289 -->

returned by the compliance search you created in Step 1.

   1. Save the following text to a Windows PowerShell script file by using a filename suffix of
     .ps1. For example, you could save it to a file named SourceMailboxes.ps1.

       PowerShell

        [CmdletBinding()]
        Param(
              [Parameter(Mandatory=$True,Position=1)]
              [string]$SearchName
        )
        $search = Get-ComplianceSearch $SearchName
        if ($search.Status -ne "Completed")
        {
                         "Please wait until the search finishes.";
                         break;
        }
        $results = $search.SuccessResults;
        if (($search.Items -le 0) -or ([string]::IsNullOrWhiteSpace($results)))
        {
                         "The compliance search " + $SearchName + " didn't return any
        useful results.";
                         break;
        }
        $mailboxes = @();
        $lines = $results -split '[\r\n]+';
        foreach ($line in $lines)
        {
            if ($line -match 'Location: (\S+),.+Item count: (\d+)' -and $matches[2] -
        gt 0)
            {
                 $mailboxes += $matches[1];
            }
        }
        "Number of mailboxes that have search hits: " + $mailboxes.Count

   2. In the Exchange Management Shell, go to the folder where the script you created in the
     previous step is located, and then run the script; for example:

       PowerShell

        .\SourceMailboxes.ps1

   3. When prompted by the script, type the name of the compliance search that you created
     in Step 1.

     The script displays the number of source mailboxes that contain search results.

<!-- p.2290 -->

If there are more than 500 source mailboxes, try creating two (or more) compliance searches.
For example, search half of your organization's mailboxes in one compliance search and the
other half in another compliance search. You could also change the search criteria to reduce
the number of mailboxes that contain search results. For example, you could specify a date
range or refine the keyword query.

Step 3: Run the script to create an In-Place
eDiscovery search from the Compliance Search
The next step is to run a script that will convert an existing compliance search to an In-Place
eDiscovery search. Here's what the script does:

     Prompts you for the name of the compliance search to convert.

     Verifies that the compliance search has completed running. If the compliance search
     doesn't return any results, and In-Place eDiscovery won't be created.

     Saves a list of the source mailboxes from the compliance search that contain search
     results to a variable.

     Creates a new In-Place eDiscovery search, with the following properties. Note that the
     new search isn't started. You'll start it in step 4.

        Name: The name of the new search uses this format: <Name of compliance
        search>_MBSearch1. If you run the script again and use the same source compliance
        search, the search will be named <Name of compliance search>_MBSearch2.

        Source mailboxes: All mailboxes from the compliance search that contain search
        results.

        Search query: The new search uses the search query from the compliance search. If the
        compliance search includes all content (where the search query is blank) the new
        search will also have a blank search query and will include all content found in the
        source mailboxes.

        Estimate only search: The new search is marked as an estimate-only search. It won't
        copy search results to a discovery mailbox after you start it.

   1. Save the following text to a Windows PowerShell script file by using a filename suffix of
     ps1. For example, you could save it to a file named MBSearchFromComplianceSearch.ps1.

        PowerShell

<!-- p.2291 -->

[CmdletBinding()]
Param(
    [Parameter(Mandatory=$True,Position=1)]
    [string]$SearchName,
    [switch]$original,
    [switch]$restoreOriginal
)
$search = Get-ComplianceSearch $SearchName
if ($search.Status -ne "Completed")
{
   "Please wait until the search finishes";
   break;
}
$results = $search.SuccessResults;
if (($search.Items -le 0) -or ([string]::IsNullOrWhiteSpace($results)))
{
   "The compliance search " + $SearchName + " didn't return any useful
results";
   "A mailbox search object wasn't created";
   break;
}
$mailboxes = @();
$lines = $results -split '[\r\n]+';
foreach ($line in $lines)
{
    if ($line -match 'Location: (\S+),.+Item count: (\d+)' -and $matches[2] -
gt 0)
    {
        $mailboxes += $matches[1];
    }
}
$msPrefix = $SearchName + "_MBSearch";
$I = 1;
$mbSearches = Get-MailboxSearch;
while ($true)
{
    $found = $false;
    $mbsName = "$msPrefix$I";
    foreach ($mbs in $mbSearches)
    {
        if ($mbs.Name -eq $mbsName)
        {
            $found = $true;
            break;
        }
    }
    if (!$found)
    {
        break;
    }
    $I++;
}
$query = $search.KeywordQuery;
if ([string]::IsNullOrWhiteSpace($query))

<!-- p.2292 -->

        {
             $query = $search.ContentMatchQuery;
        }
        if ([string]::IsNullOrWhiteSpace($query))
        {
           New-MailboxSearch "$msPrefix$i" -SourceMailboxes $mailboxes -EstimateOnly;
        }
        else
        {
           New-MailboxSearch "$msPrefix$i" -SourceMailboxes $mailboxes -SearchQuery
        $query -EstimateOnly;
        }

   2. In the Exchange Management Shell, go to the folder where the script that you created in
     the previous step is located, and then run the script; for example:

        PowerShell

        .\MBSearchFromComplianceSearch.ps1

   3. When prompted by the script, type the name of the compliance search that you want to
     covert to an In-Place eDiscovery search (for example, the search that you created in Step
     1) , and then press Enter.

     If the script is successful, a new In-Place eDiscovery search is created with a status of
     NotStarted. Run the command Get-MailboxSearch <Name of compliance
     search>_MBSearch1 | FL to display the properties of the new search.

Step 4: Start the In-Place eDiscovery search
The script that you run in Step 3 creates a new In-Place eDiscovery search, but doesn't start it.
The next step is to start the search so you can get an estimate of the search results.

   1. In the Exchange admin center (EAC), go to Compliance management > In-Place
     eDiscovery & Hold.

   2. In the list view, select the In-Place eDiscovery search that you created in Step 3.

   3. Click Search (   ) > Estimate search results to start the search and return an estimate of
     the total size and number of items returned by the search.

     The estimates are displayed in the details pane. Click Refresh (    ) to update the
     information displayed in the details pane.

<!-- p.2293 -->

   4. To preview the results after the search is completed, click Preview search results in the
     details pane.

   Tip

  Alternatively, you can use the Exchange Management Shell to start the In-Place eDiscovery
  search; for example Start-MailboxSearch -Identity <Name of compliance
  search>_MBSearch1 .

Next steps after creating and running the In-Place
eDiscovery search
After you create and start the In-Place eDiscovery search that was created by the script in Step
3, you can use the normal In-Place eDiscovery workflow to perform different eDiscovery
actions on the search results.

Create an In-Place Hold
   1. In the EAC, go to Compliance management > In-Place eDiscovery & Hold.

   2. In the list view, select the In-Place eDiscovery search that you created in Step 3, and then
     click Edit (    ).

   3. On the In-Place Hold page, select the Place content matching the search query in
     selected mailboxes on hold check box and then select one of the following options:

           Hold indefinitely: Choose this option to place items returned by the search on an
           indefinite hold. Items on hold will be preserved until you remove the mailbox from
           the search or remove the search.

           Specify number of days to hold items relative to their received date: Choose this
           option to hold items for a specific period. The duration is calculated from the date a
           mailbox item is received or created.

   4. Click Save to create the In-Place Hold and restart the search.

Copy the search results
   1. In the EAC, go to Compliance management > In-Place eDiscovery & Hold.

   2. In the list view, select the In-Place eDiscovery search that you created in Step 3.

<!-- p.2294 -->

  3. Click Search (    ), and then click Copy search results from the drop-down list.

  4. In Copy Search Results, select from the following options:

          Include unsearchable items: Select this check box to include mailbox items that
          couldn't be searched (for example, messages with attachments of file types that
          couldn't be indexed by Exchange Search).

          Enable de-duplication: Select this check box to exclude duplicate messages. Only a
          single instance of a message will be copied to the discovery mailbox.

          Enable full logging: Select this check box to include a full log in search results.

          Send me mail when the copy is completed: Select this check box to get an email
          notification when the search is completed.

          Copy results to this discovery mailbox: Click Browse to select the discovery mailbox
          where you want the search results copied to.

  5. Click Copy to start the process to copy the search results to the specified discovery
    mailbox.

  6. Click Refresh (    ) to update the information about the copying status that is displayed in
    the details pane.

  7. When copying is complete, click Open to open the discovery mailbox to view the search
    results.

Export the search results
  1. In the EAC, go to Compliance management > In-Place eDiscovery & Hold.

  2. In the list view, select the In-Place eDiscovery search that you created in Step 3, and then
    click Export to a PST file.

  3. In the list view, select the In-Place eDiscovery search you want to export the results of,
    and then click Export to a PST file.

  4. In the eDiscovery PST Export Tool window, do the following:

          Click Browse to specify the location where you want to download the PST file.

          Click the Enable deduplication checkbox to exclude duplicate messages. Only a
          single instance of a message will be included in the PST file.

<!-- p.2295 -->

        Click the Include unsearchable items checkbox to include mailbox items that
        couldn't be searched (for example, messages with attachments of file types that
        couldn't be indexed by Exchange Search). Unsearchable items are exported to a
        separate PST file.

5. Click Start to export the search results to a PST file.

  A window is displayed that contains status information about the export process.

<!-- p.2296 -->

Search for and delete messages in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019     Subscription Edition

You can use the New-ComplianceSearch and New-ComplianceSearchAction cmdlets to search
for and delete an email message from all mailboxes in your organization. This can help you find
and remove potentially harmful or high-risk email, such as:

      Messages that contain dangerous attachment or virus

      Phishing messages

      Messages that contain sensitive data

Why use the New-ComplianceSearch and New-ComplianceSearchAction cmdlets instead of
using the Search-Mailbox cmdlet to delete messages? In previous versions of Exchange, you
could run the Search-Mailbox -DeleteContent command to search for and delete email
messages. You can still do that in Exchange Server, but you can only search a maximum of
10,000 mailboxes in a single search by using the Search-Mailbox cmdlet. For New-
ComplianceSearch, there are no limits for the number of mailboxes in a single search. This lets
large organizations perform organization-wide search and delete operations.

Here's the workflow for the search and delete process:

Step 1: Create and run a Compliance Search to find the message to delete

Step 2: Delete the message

See the More information section for description of what happens to deleted messages and
how to get the status of a search and delete operation.

  Ｕ Caution

  Search and delete is a powerful feature that allows anyone that is assigned the necessary
  permissions to delete email messages from mailboxes in your organization.

Before you begin
      To use the New-ComplianceSearch and Start-ComplianceSearchAction cmdlets to create
      and run a Compliance Search, and to use the New-ComplianceSearchAction cmdlet to

<!-- p.2297 -->

     delete messages, you have to be assigned the Mailbox Search management role.
     Administrators aren't assigned this role by default. To assign yourself this role so that you
     can search mailboxes and delete messages, add yourself as a member of the Discovery
     Management role group. See Assign eDiscovery permissions in Exchange Server.

     A maximum of 10 items per mailbox can be removed at once. Because the capability to
     search for and remove messages is intended to be an incident-response tool, this limit
     helps ensure that messages are quickly removed from mailboxes. This feature isn't
     intended to clean up user mailboxes.

Step 1: Create and run a Compliance Search to find
the message to delete
The first step is to create and run a Compliance Search to find the message that you want to
remove from mailboxes in your organization. You can create the search by running the New-
ComplianceSearch and Start-ComplianceSearch cmdlets. The messages that match the query
for this search will be deleted by running the New-ComplianceSearchAction cmdlet in Step 2.

In this example, the commands will create and start a search of all mailboxes in the
organization for a message that contains the words "Update your account information" in the
subject line.

   1. Open the Exchange Management Shell.

   2. Run the following commands.

        PowerShell

        New-ComplianceSearch -Name "Remove Phishing Message" -ExchangeLocation all -
        ContentMatchQuery 'subject:"Update your account information"'

        PowerShell

        Start-ComplianceSearch -Identity "Remove Phishing Message"

For information about creating a Compliance Search and configuring search queries, see the
following topics:

     New-ComplianceSearch

     Start-ComplianceSearch

     Message properties and search operators for In-Place eDiscovery in Exchange Server

<!-- p.2298 -->

Tips for finding messages to remove
The goal of the search query is to narrow the results of the search to only the message or
messages that you want to remove. Here are some tips:

     If you know the exact text or phrase used in the subject line of the message, use the
     Subject property in the search query.

     If you know that exact date (or date range) of the message, include the Received property
     in the search query.

     If you know who sent the message, include the From property in the search query.

     Preview the search results to verify that the search returned only the message (or
     messages) that you want to delete.

     Use the search estimate statistics (by running the Get-ComplianceSearch cmdlet) to get a
     count of the total number of search results.

Here are two examples of queries to find suspicious email messages.

     This query returns messages that were received by users between April 13, 2016 and April
     14, 2016 and that contain the words "action" and "required" in the subject line.

       PowerShell

        (Received:4/13/2016..4/14/2016) AND (Subject:'Action required')

     This query returns messages that were sent by chatsuwloginsset12345@outlook.com and
     that contain the exact phrase "Update your account information" in the subject line.

       PowerShell

        (From:chatsuwloginsset12345@outlook.com) AND (Subject:"Update your account
        information")

Step 2: Delete the message
After you've created and refined a Compliance Search to return the message that you want to
remove, the final step is to run the New-ComplianceSearchAction cmdlet to delete the
message. Deleted messages are moved to a user's Recoverable Items folder.

In this example, the command will delete the search results returned by a Compliance Search
named "Remove Phishing Message".

<!-- p.2299 -->

 1. Open the Exchange Management Shell.

 2. Run the following command.

     PowerShell

     New-ComplianceSearchAction -SearchName "Remove Phishing Message" -Purge -
     PurgeType SoftDelete

More information
   What happens after you delete a message?: A message that is deleted by using the New-
   ComplianceSearchAction -Purge -PurgeType SoftDelete command is moved to the

   Deletions folder in the user's Recoverable Items folder. It isn't immediately purged from
   the Exchange database. The user can recover messages in the Deleted Items folder for the
   duration based on the deleted item retention period configured for the mailbox. After this
   retention period expires (or if user purges the message before it expires), the message is
   moved to the Purges folder and can no longer be accessed by the user. Once in the
   Purges folder, the message is again retained for the duration based on the deleted item
   retention period configured for the mailbox if single items recovery is enabled for the
   mailbox. (In Exchange, single item recovery is enabled by default when a new mailbox is
   created. ) After the deleted item retention period expires, the message is marked from
   permanent deletion and will be purged from the Exchange database the next time that
   the mailbox is processed by the Managed Folder assistant.

   How do you know that messages are deleted and moved to the users' Recoverable
   Items folder?: If you run the same Compliance Search after you delete a message, you will
   still see the same number of search results (and might assume that the message wasn't
   deleted from user mailboxes). This is because a Compliance Search searches the
   Recoverable Items folder, which is where the deleted message is moved to after you run
   the New-ComplianceSearchAction -Purge -PurgeType SoftDelete command. To verify that
   messages where moved to the Recoverable Items folder, you can run an In-Place
   eDiscovery search (using the same source mailboxes and search criteria as the
   Compliance Search created in Step 1) and the copy the search results to discovery
   mailbox. Then you can view the search results in the discovery mailbox and verify that the
   messages was moved to the Recoverable Items folder. See Use Compliance Search to
   search all mailboxes in Exchange Server for details about creating an In-Place eDiscovery
   search that uses the list of source mailboxes and search query from a Compliance Search.

   What happens if a message is deleted from a mailbox that has been placed on In-Place
   Hold or Litigation Hold?: After the message is purged (either by the user or after the

<!-- p.2300 -->

deleted item retention period expires), the message is retained until the hold duration
expires. If the hold duration is unlimited, then items are retained until the hold is removed
or the hold duration is changed.

How to get status on the search and delete operation? Run the Get-
ComplianceSearchAction: to get the status on the delete operation. Note that the object
that is created when you run the New-ComplianceSearchAction cmdlet is named by
using this format: <name of Compliance Search>_Purge .

<!-- p.2301 -->

Messaging records management in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016       2019   Subscription Edition

Users send and receive email every day. If left unmanaged, the volume of email generated and
received each day can inundate users, impact user productivity, and expose your organization
to risks. As a result, email lifecycle management is a critical component for most organizations.

Messaging records management (MRM) is the records management technology in Exchange
Server that helps organizations manage email lifecycle and reduce the legal risks associated
with email. Deploying MRM can help your organization in several ways:

      Meet business requirements: Depending on your organization's messaging policies, you
      may need to retain important email messages for a certain period. For example, a user's
      mailbox may contain critical messages related to business strategy, transactions, product
      development, or customer interactions.

      Meet legal and regulatory requirements: Many organizations have a legal or regulatory
      requirement to store messages for a designated period and remove messages older than
      that period. Storing messages longer than necessary may increase your organization's
      legal or financial risks.

      Increase user productivity: If left unmanaged, the ever-increasing volume of email in your
      users' mailboxes can also impact their productivity. For example, although newsletter
      subscriptions and automated notifications may have informational value when they're
      received, users may not remove them after reading (often they're never read). Many of
      these types of messages don't have a retention value beyond a few days. Using MRM to
      remove such messages can help reduce information clutter in users' mailboxes, thereby
      increasing productivity.

      Improve storage management: Due to expectations driven by free consumer email
      services, many users keep old messages for a long period or never remove them.
      Maintaining large mailboxes is increasingly becoming a standard practice, and users
      shouldn't be forced to change their work habits based on restrictive mailbox quotas.
      However, retaining messages beyond the period that's necessary for business, legal, or
      regulatory reasons also increases storage costs.

MRM provides the flexibility to implement the records management policy that best meets
your organization's requirements. With a good understanding of MRM, In-Place Archiving, and

<!-- p.2302 -->

In-Place Hold, you can help meet your goals of managing mailbox storage and meeting
regulatory retention requirements.

MRM in Exchange Server
In Exchange Server, MRM is accomplished through the use of retention tags and retention
policies. Retention tags are used to apply retention settings to an entire mailbox and default
mailbox folders such as Inbox and Deleted Items. You can also create and deploy retention tags
that Outlook 2010 and later and Outlook on the web users can use to apply to folders or
individual messages. After they're created, you add retention tags to a retention policy and
then apply the policy to users. The Managed Folder Assistant processes mailboxes and applies
retention settings in the user's retention policy. To learn more about retention policies, see
Retention tags and retention policies in Exchange Server.

When a message reaches its retention age specified in the applicable retention tag, the
Managed Folder Assistant takes the retention action specified by the tag. Messages can then
be deleted permanently or deleted with the ability to recover them. If an archive has been
provisioned for the user, you can also use retention tags to move items to the user's In-Place
Archive.

MRM strategies
You can use retention policies to enforce basic message retention for an entire mailbox or for
specific default folders. Although there are several strategies for deploying MRM, here are
some of the most common:

Remove all messages after a specified period: In this strategy, you implement a single MRM
policy that removes all messages after a certain period. In this strategy, there's no classification
of messages. You can implement this policy by creating a single default policy tag (DPT) for the
mailbox. However, this doesn't ensure that messages are retained for the specified period.
Users can still delete messages before retention period is reached.

Move messages to archive mailboxes: In this strategy, you implement MRM policies that move
items to the user's archive mailbox. An archive mailbox provides additional storage for users to
maintain old and infrequently accessed content. Retention tags that move items are also
known as archive policies. Within the same retention policy, you can combine a DPT and
personal tags to move items, and a DPT, RPTs, and personal tags to delete items. To learn more
about archiving policies, see In-Place Archiving in Exchange Server.

Remove messages based on folder location: In this strategy, you implement MRM policies
based on email location. For example, you can specify that messages in the Inbox are retained

<!-- p.2303 -->

for one year and messages in the Junk Email folder are retained for 60 days. You can
implement this policy by using a combination of retention policy tags (RPTs) for each default
folder you want to configure and a DPT for the entire mailbox. The DPT applies to all custom
folders and all default folders that don't have an RPT applied.

  ７ Note

  In Exchange Server, you can create RPTs for the Calendar and Tasks folders. If you don't
  want items in these folders or other default folders to expire, you can create a disabled
  retention tag for that default folder.

Allow users to classify messages: In this strategy, you implement MRM policies that include a
baseline retention setting for all messages but allow users to classify messages based on
business or regulatory requirements. In this case, users become an important part of your
records management strategy - often they have the best understanding of a message's
retention value.

Users can apply different retention settings to messages that need to be retained for a longer
or shorter period. You can implement this policy using a combination of the following:

     A DPT for the mailbox

     Personal tags that users can apply to custom folders or individual messages

     (Optional) Additional RPTs to expire items in specific default folders

For example, you can use a retention policy with personal tags that have a shorter retention
period (such as two days, one week, or one month), as well as personal tags that have a longer
retention period (such as one, two, or five years). Users can apply personal tags with the
shorter retention periods for items such as newsletter subscriptions that may lose their value
within days of receiving them, and apply the tags with longer periods to preserve items that
have a high business value. They can also automate the process by using Inbox rules in
Outlook to apply a personal tag to messages that match rule conditions.

Retain messages for eDiscovery purposes: In this strategy, you implement MRM policies that
remove messages from mailboxes after a specified period but also retain them in the
Recoverable Items folder for In-Place eDiscovery in Exchange Server purposes, even if the
messages were deleted by the user or another process.

You can meet this requirement by using a combination of retention policies and In-Place Hold
and Litigation Hold in Exchange Server or Litigation Hold. Retention policies remove messages
from the mailbox after the specified period. A time-based In-Place Hold or Litigation Hold
preserves messages that were deleted or modified before that period. For example, to retain

<!-- p.2304 -->

messages for seven years, you can create a retention policy with a DPT that deletes messages
in seven years and Litigation Hold to hold messages for seven years. Messages that aren't
removed by users will be deleted after seven years; messages deleted by users before the
seven year period will be retained in the Recoverable Items folder for seven years. To learn
more about this folder, see Recoverable Items folder in Exchange Server.

Optionally, you can use RPTs and personal tags to allow users to clean up their mailboxes.
However, In-Place Hold and Litigation Hold continues to retain the deleted messages until the
hold period expires.

  ７ Note

  A time-based In-Place Hold or Litigation Hold is similar to what was informally referred to
  as a rolling legal hold in Exchange 2010. Rolling legal hold was implemented by
  configuring the deleted item retention period for a mailbox database or individual
  mailbox. However, deleted item retention retains deleted and modified items based on
  the date deleted. In-Place Hold and Litigation Hold preserves items based on the date
  they're received or created. This ensures that messages are preserved for at least the
  specified period.

<!-- p.2305 -->

Retention tags and retention policies in
Exchange Server
04/30/2025

APPLIES TO:      2016      2019      Subscription Edition

Messaging records management (MRM) helps organizations to manage email lifecycle and
reduce legal risks associated with email and other communications. MRM makes it easier to
keep messages needed to comply with company policy, government regulations, or legal
needs, and to remove content that has no legal or business value.

Messaging records management strategy
MRM in Exchange Server is accomplished by using retention tags and retention policies. Before
discussing the details about each of these retention features, let's learn how the features are
used in the overall MRM strategy:

     Assigning retention policy tags (RPTs) to default folders, such as the Inbox and Deleted
     Items.

     Applying default policy tags (DPTs) to mailboxes to manage the retention of all untagged
     items.

     Allowing the user to assign personal tags to custom folders and individual items.

     Separating MRM functionality from users' Inbox management and filing habits. Users
     aren't required to file messages in managed folders based on retention requirements.
     Individual messages can have a different retention tag than the one applied to the folder
     in which they're located.

The following figure illustrates the tasks involved in implementing this strategy.

<!-- p.2306 -->

<!-- p.2307 -->

Retention tags
As you can see, retention tags are used to apply retention settings to folders and individual
items such as email messages and voice mail. These settings specify how long a message
remains in a mailbox and the action to take when the message reaches the specified retention
age. When a message reaches its retention age, it's moved to the user's In-Place Archive or
deleted.

Retention tags allow users to tag their own mailbox folders and individual items for retention.
Users no longer have to file items in managed folders provisioned by an administrator based
on message retention requirements.

<!-- p.2308 -->

Types of retention tags
Retention tags are classified into the following three types based on who can apply them and
where in a mailbox they can be applied.

                                                                                        ﾉ   Expand table

 Type of      Applied...                    Applied by...   Available     Details
 retention                                                  actions...
 tag

 Default      Automatically to entire       Administrator   Move to       Users can't change DPTs
 policy tag   mailbox                                       archive       applied to a mailbox.
 (DPT)        A DPT applies to                              Delete and
              untagged items, which are                     allow
              mailbox items that don't                      recovery
              have a retention tag
              applied directly or by                        Permanently
              inheritance from the                          delete
              folder.

 Retention    Automatically to a default    Administrator   Delete and    Users can't change the RPT
 policy tag   folder                                        allow         applied to a default folder.
 (RPT)        Default folders are folders                   recovery
              created automatically in                      Permanently
              all mailboxes, for example:                   delete
              Inbox, Deleted Items, and
              Sent Items. See the list of
              supported default folders
              in Default folders that
              support Retention Policy
              Tags.

 Personal     Manually to items and         Users           Move to       Personal tags allow your users
 tag          folders                                       archive       to determine how long an item
              Users can automate                            Delete and    should be retained. For
              tagging by using Inbox                        allow         example, the mailbox can have
              rules to either move a                        recovery      a DPT to delete items in seven
              message to a folder that                                    years, but a user can create an
              has a particular tag or to                    Permanently   exception for items such as
              apply a personal tag to                       delete        newsletters and automated
              the message.                                                notifications by applying a
                                                                          personal tag to delete them in
                                                                          three days.

More about personal tags

<!-- p.2309 -->

Personal tags are available to Outlook and Outlook on the web users as part of their retention
policy. In Outlook and Outlook on the web, personal tags with the Move to Archive action
appear as Archive Policy, and personal tags with the Delete and Allow Recovery or
Permanently Delete actions appear as Retention Policy, as shown here:

Users can apply personal tags to folders they create or to individual items. Messages that have
a personal tag applied are always processed based on the personal tag's settings. Users can
apply a personal tag to a message so that it's moved or deleted sooner or later than the
settings specified in the DPT or RPTs applied to that user's mailbox. You can also create
personal tags with retention disabled. This allows users to tag items so they're never moved to
an archive or never expire.

  ７ Note

  Users can apply archive policies to default folders, user-created folders or subfolders, and
  individual items. Users can apply a retention policy to user-created folders or subfolders

<!-- p.2310 -->

  and individual items (including subfolders and items in a default folder), but not to default
  folders.

Users can also use the Exchange admin center (EAC) to select additional personal tags that
aren't linked to their retention policy. The selected tags then become available in Outlook and
Outlook on the web. To enable users to select additional tags from the EAC, you must add the
MyRetentionPolicies Role to the user's role assignment policy. To learn more about role
assignment policies for users, see Understanding Management Role Assignment Policies. If you
allow users to select additional personal tags, all personal tags in your Exchange organization
become available to them.

  ７ Note

  Personal tags are a premium feature. Mailboxes with policies that contain these tags (or as
  a result of users adding the tags to their mailbox) require an Exchange Enterprise client
  access license (CAL).

Retention age
When you enable a retention tag, you must specify a retention age for the tag. This age
indicates the number of days to retain a message after it arrives in the user's mailbox.

The retention age for non-recurring items (such as email messages) is calculated differently
than items that have an end date or recurring items (such as meetings and tasks). To learn how
retention age is calculated for different types of items, see How retention age is calculated in
Exchange Server.

You can also create retention tags with retention disabled or disable tags after they're created.
Because messages that have a disabled tag applied aren't processed, no retention action is
taken. As a result, users can use a disabled personal tag as a Never Move tag or a Never
Delete tag to override a DPT or RPT that would otherwise apply to the message.

Retention actions
When creating or configuring a retention tag, you can select one of the following retention
actions to be taken when an item reaches its retention age:

                                                                                 ﾉ   Expand table

<!-- p.2311 -->

 Retention         Action taken...                          Except...
 action

 Move to           Moves the message to the user's          If the user doesn't have an archive mailbox, no
 archive           archive mailbox                          action is taken.
                   Only available for DPTs and personal
                   tags

                   For details about archiving, see In-
                   Place Archiving in Exchange Server.

 Delete and        Emulates the behavior when the user      If you've set the deleted item retention period
 allow             empties the Deleted Items folder.        to zero days, items are permanently deleted. For
 recovery:         Items are moved to the Recoverable       details, see Configure Deleted Item retention
                   Items folder in Exchange Server in       and Recoverable Items quotas.
                   the mailbox and preserved until the
                   deleted item retention period.

                   Provides the user a second chance to
                   recover the item using the Recover
                   Deleted Items dialog box in Outlook
                   or Outlook on the web

 Permanently       Permanently deletes messages.            If mailbox is placed on In-Place Hold and
 delete            You can't recover messages after         Litigation Hold in Exchange Server or Litigation
                   they're permanently deleted.             Hold, items are preserved in the Recoverable
                                                            Items folder based on hold parameters. In-Place
                                                            eDiscovery in Exchange Server will still return
                                                            these items in search results.

 Mark as past      Marks a message as expired. In           N. A.
 retention limit   Outlook, and Outlook on the web,
                   expired items are displayed with the
                   notification stating 'This item has
                   expired' and 'This item will expire in
                   0 days'.

  ７ Note

  Default Policy tag (DPT) with Move to Archive action always overwrites the Retention
  Policy tag (RPT) or the Personal tag (PT), when the age limit for retention of DPT is lower
  than RPT or PT.

For details about how to create retention tags, see Create a retention policy in Exchange
Server.

<!-- p.2312 -->

Retention policies
To apply one or more retention tags to a mailbox, you need to add them to a retention policy
and then apply the policy to mailboxes. A mailbox can't have more than one retention policy.
Retention tags can be linked to or unlinked from a retention policy at any time, and the
changes automatically take effect for all mailboxes that have the policy applied.

A retention policy can have the following retention tags:

                                                                                        ﾉ   Expand table

 Retention tag type   Tags in a policy

 Default policy tag   One DPT with the Move to archive action
 (DPT)
                      One DPT with the Delete and allow Recovery or Permanently delete actions

                      One DPT for voice mail messages with the Delete and allow recovery or
                      Permanently delete action

 Retention policy     One RPT for each supported default folder
 tags (RPTs)          Note: You can't link more than one RPT for a particular default folder (such as
                      Deleted Items) to the same retention policy.

 Personal tags        Any number of personal tags
                      Note: Many personal tags in a policy can confuse users. We recommend adding no
                      more than 10 personal tags to a retention policy.

  ７ Note

  Although a retention policy doesn't need to have any retention tags linked to it, we don't
  recommend using this scenario. If mailboxes with retention policies don't have retention
  tags linked to them, this may cause mailbox items to never expire.

A retention policy can contain both archive tags (tags that move items to the personal archive
mailbox) and deletion tags (tags that delete items). A mailbox item can also have both types of
tags applied. Archive mailboxes don't have a separate retention policy. The same retention
policy is applied to the primary and archive mailbox.

When planning to create retention policies, you must consider whether they'll include both
archive and deletion tags. As mentioned earlier, a retention policy can have one DPT that uses
the Move to archive action and one DPT that uses either the Delete and allow recovery or
Permanently delete action. The DPT with the Move to archive action must have a lower
retention age than the DPT with a deletion action. For example, you can use a DPT with the
Move to archive action to move items to the archive mailbox in two years, and a DPT with a

<!-- p.2313 -->

deletion action to remove items from the mailbox in seven years. Items in both primary and
archive mailboxes will be deleted after seven years.

Default retention policy
Exchange Setup creates the retention policy Default MRM Policy. The policy is applied
automatically if you create an archive for the new user and don't specify a retention policy

You can modify tags included in the Default MRM Policy, for example by changing the
retention age or retention action, disable a tag or modify the policy by adding or removing
tags from it. The updated policy is applied to mailboxes the next time they're processed by the
Managed Folder Assistant (MFA).

For more details, including a list of retention tags linked to the policy, see Default Retention
Policy.

Managed Folder Assistant
The Managed Folder Assistant, a mailbox assistant that runs on Mailbox servers, processes
mailboxes that have a retention policy applied.

The Managed Folder Assistant applies the retention policy by inspecting items in the mailbox
and determining whether they're subject to retention. It then stamps items subject to retention
with the appropriate retention tags and takes the specified retention action on items past their
retention age.

The Managed Folder Assistant is a throttle-based assistant. Throttle-based assistants are always
running and don't need to be scheduled. The system resources they can consume are throttled.
You can configure the Managed Folder Assistant to process all mailboxes on a Mailbox server
within a certain period (known as a work cycle). Additionally, at a specified interval (known as
the work cycle checkpoint), the assistant refreshes the list of mailboxes to be processed. During
the refresh, the assistant adds newly created or moved mailboxes to the queue. It also
reprioritizes existing mailboxes that haven't been processed successfully due to failures and
moves them higher in the queue so they can be processed during the same work cycle.

You can also use the Start-ManagedFolderAssistant cmdlet to manually trigger the assistant to
process a specified mailbox. To learn more, see Configure and run the Managed Folder
Assistant in Exchange Server.

  ７ Note

<!-- p.2314 -->

  The Managed Folder Assistant doesn't take any action on messages that aren't subject to
  retention, specified by disabling the retention tag. You can also disable a retention tag to
  temporarily suspend items with that tag from being processed.

Moving items between folders
A mailbox item moved from one folder to another inherits any tags applied to the folder to
which it's moved. If an item is moved to a folder that doesn't have a tag assigned, the DPT is
applied to it. If the item has a tag explicitly assigned to it, the tag always takes precedence over
any folder-level tags or the default tag.

Applying a retention tag to a folder in the archive
When the user applies a personal tag to a folder in the archive, if a folder with the same name
exists in the primary mailbox and has a different tag, the tag on that folder in the archive
changes to match the one in the primary mailbox. This is by design to avoid any confusion
about items in a folder in the archive having a different expiry behavior than the same folder in
the user's primary mailbox. For example, the user has a folder named Project Contoso in the
primary mailbox with a Delete - 3 years tag and a Project Contoso folder also exists in the
archive mailbox. If the user applies a Delete - 1 year personal tag to delete items in the folder
after 1 year. When the mailbox is processed again, the folder reverts to the Delete - 3 Years tag.

Removing or deleting a retention tag from a retention policy
When a retention tag is removed from the retention policy applied to a mailbox, the tag is no
longer available to the user and can't be applied to items in the mailbox.

Existing items that have been stamped with that tag continue to be processed by the Managed
Folder Assistant based on those settings and any retention action specified in the tag is applied
to those messages.

However, if you delete the tag, the tag definition stored in Active Directory is removed. This
causes the Managed Folder Assistant to process all items in a mailbox and restamp the ones
that have the removed tag applied. Depending on the number of mailboxes and messages, this
process may significantly consume resources on all Mailbox servers that contain mailboxes with
retention policies that include the removed tag.

  ） Important

<!-- p.2315 -->

  If a retention tag is removed from a retention policy, any existing mailbox items with the
  tag applied will continue to expire based on the tag's settings. To prevent the tag's
  settings from being applied to any items, you should delete the tag. Deleting a tag
  removes it from any retention policies where it's included.

Disabling a retention tag
If you disable a retention tag, the Managed Folder Assistant ignores items that have that tag
applied. Items that have a retention tag for which retention is disabled are either never moved
or never deleted, depending on the specified retention action. Because these items are still
considered tagged items, the DPT doesn't apply to them. For example, if you want to
troubleshoot retention tag settings, you can temporarily disable a retention tag to stop the
Managed Folder Assistant from processing messages with that tag.

  ７ Note

  The retention period for a disabled retention tag is displayed to the user as Never. If a
  user tags an item believing it will never be deleted, enabling the tag later may result in
  unintentional deletion of items the user didn't want to delete. The same is true for tags
  with the Move to archive action.

Retention hold
When users are temporarily away from work and don't have access to their email, retention
settings can be applied to new messages before they return to work or access their email.
Depending on the retention policy, messages may be deleted or moved to the user's personal
archive. You can temporarily suspend retention policies from processing a mailbox for a
specified period by placing the mailbox on retention hold. When you place a mailbox on
retention hold, you can also specify a retention comment that informs the mailbox user (or
another user authorized to access the mailbox) about the retention hold, including when the
hold is scheduled to begin and end. Retention comments are displayed in supported Outlook
clients. You can also localize the retention hold comment in the user's preferred language.

  ７ Note

  Placing a mailbox on retention hold doesn't affect how mailbox storage quotas are
  processed. Depending on the mailbox usage and applicable mailbox quotas, consider
  temporarily increasing the mailbox storage quota for users when they're on vacation or

<!-- p.2316 -->

  don't have access to email for an extended period. For more information about mailbox
  storage quotas, see Configure storage quotas for a mailbox.

During long absences from work, users may accrue a large amount of email. Depending on the
volume of email and the length of absence, it may take these users several weeks to sort
through their messages. In these cases, consider the additional time it may take the users to
catch up on their mail before removing them from retention hold.

If your organization has never implemented MRM, and your users aren't familiar with its
features, you can also use retention holds during the initial warm-up and training phase of your
MRM deployment. You can create and deploy retention policies and educate users about the
policies without the risk of having items moved or deleted before users can tag them. A few
days before the warm-up and training period ends, you should remind users of the warm-up
deadline. After the deadline, you can remove the retention hold from user mailboxes, allowing
the Managed Folder Assistant to process mailbox items and take the specified retention action.

If you are using Exchange hybrid, note the following behavior: When a retention hold is
configured in Microsoft 365, the GUID for this hold is written to the msExchUserHoldPolicies
attribute of the user object to which the hold applies. This attribute is then synchronized back
to the on-premises Active Directory. When MFA processes the mailbox for elements that can
be purged, it encounters the msExchUserHoldPolicies attribute. However, it cannot retrieve the
details of the configured hold because they are not available within the Exchange Server on-
premises organization. To prevent the deletion of data that might need to be preserved, MFA
skips purging these items from the DiscoveryHolds folder in the mailbox. Over time, this folder
becomes full and causes the Recoverable Items folder to reach its quota. You can find steps to
resolve this behavior and configuration recommendations in Recoverable Items folder not
emptied for mailbox on litigation or retention hold support article.

<!-- p.2317 -->

How retention age is calculated in
Exchange Server
Article • 04/30/2025

APPLIES TO:         2016            2019    Subscription Edition

The Managed Folder Assistant (MFA) is one of many mailbox assistant processes that runs on
mailbox servers. Its job is to process mailboxes that have a Retention Policy applied, add the
Retention Tags included in the policy to the mailbox, and process items in the mailbox. If the
items have a retention tag, the assistant tests the age of those items. If an item has exceeded
its retention age, it takes the specified retention action. Retention actions include moving an
item to the user's archive, deleting the item and allowing recovery, or deleting the item
permanently.

See Retention tags and retention policies in Exchange Server for more information.

Determining the age of different types of items
The retention age of mailbox items is calculated from the date of delivery or the date of
creation for items such as drafts that aren't delivered but created by the user. When the
Managed Folder Assistant processes items in a mailbox, it stamps a start date and an expiration
date for all items that have retention tags with the Delete and Allow Recovery or Permanently
Delete retention action. Items that have an archive tag are also stamped with a move date.

Items in the Deleted Items folder and items, which may have a start and end date, such as
calendar items (meetings and appointments) and tasks, are handled differently as shown in this
table.

                                                                                     ﾉ   Expand table

 If the item type      And the         The retention age is calculated based on...
 is...                 item is...

 Email message         Not in the      Delivery date or date of creation
                       Deleted
 Document              Items
                       folder
 Fax

 Journal item

 Meeting request,
 response, or

<!-- p.2318 -->

If the item type   And the      The retention age is calculated based on...
is...              item is...

cancellation

Missed call

Notes

Email message      In the       Date of delivery or creation unless the item was deleted from a folder
                   Deleted      that doesn't have an inherited or implicit retention tag.
Document           Items
                   folder       If an item is in a folder that doesn't have an inherited or implicit
Fax                             retention tag applied, the item isn't processed by the MFA and
                                therefore doesn't have a start date stamped by it. When the user
Journal item                    deletes such an item, and the MFA processes it for the first time in the
                                Deleted Items folder, it stamps the current date as the start date.
Meeting request,
response, or
cancellation

Missed call

Notes

Calendar           Not in the   Non-recurring calendar items expire according to their end date.
                   Deleted
                   Items        Recurring calendar items expire according to the end date of their last
                   folder       occurrence. Recurring calendar items with no end date don't expire.

Calendar           In the       A calendar item expires according to its message-received date , if one
                   Deleted      exists.
                   Items
                   folder       If a calendar item doesn't have a message-received date , it expires
                                according to its message-creation date .

                                If a calendar item has neither a message-received date nor a message-
                                creation date , it doesn't expire.

Task               Not in the   Non-recurring tasks:
                   Deleted           A non-recurring task expires according to its message-received
                   Items              date , if one exists.
                   folder             If a non-recurring task doesn't have a message-received date , it
                                      expires according to its message-creation date .
                                      If a non-recurring task has neither a message-received date nor a
                                      message-creation date , it doesn't expire.

                                A recurring task expires according to the end date of its last

<!-- p.2319 -->

If the item type     And the         The retention age is calculated based on...
is...                item is...

                                     occurrence. If a recurring task doesn't have an end date , it doesn't
                                     expire.

                                     A regenerating task (which is a recurring task that regenerates a
                                     specified time after the preceding instance of the task is completed)
                                     doesn't expire.

Task                 In the          A task expires according to its message-received date , if one exists.
                     Deleted
                     Items           If a task doesn't have a message-received date , it expires according to
                     folder          its message-creation date .

                                     If a task has neither a message-received date nor a message-creation
                                     date , it doesn't expire.

Contact              In any          Contacts aren't stamped with a start date or an expiration date, so
                     folder          they're skipped by the Managed Folder Assistant and don't expire.

Corrupted            In any          Corrupted items are skipped by the Managed Folder Assistant and
                     folder          don't expire.

Examples
                                                                                             ﾉ   Expand table

If the user..            The retention        The Managed Folder Assistant...
                         tags on
                         folder...

Receives a message       Inbox: Delete in     Processes the message in the Inbox on 1/26/2016, stamps it
in the Inbox on          365 days             with a start date of 01/26/2016 and an expiration date of
01/26/2016.                                   01/26/2017.
                         Deleted Items:
Deletes the message      Delete in 30         Processes the message again in the Deleted Items folder on
on 2/27/2016.            days                 2/27/2016. It recalculates the expiration date based on the
                                              same start date (01/26/2016).

                                              Because the item is older than 30 days, it's expired
                                              immediately.

Receives a message       Inbox: None          Processes the message in the Deleted Items folder on
in the Inbox on          (inherited or        02/27/2016 and determines the item doesn't have a start date.
01/26/2016.              implicit)            It stamps the current date as the start date, and 03/27/2016 as
                                              the expiration date.
                         Deleted Items:

<!-- p.2320 -->

 If the user..         The retention   The Managed Folder Assistant...
                       tags on
                       folder...

 Deletes the message   Delete in 30    The item is expired on 3/27/2016, which is 30 days after the
 on 2/27/2016.         days            user deleted or moved it to the Deleted Items folder.

More information
Items in mailboxes placed on Retention Hold aren't removed until the hold is removed.

If a mailbox is placed on In-Place Hold or Litigation Hold, expiring items are removed from the
Inbox but preserved in the Recoverable Items folder until the mailbox is removed from In-Place
Hold and Litigation Hold in Exchange Server.

In hybrid deployments, the same retention tags and retention policies must exist in your on-
premises and Exchange Online organizations in order to consistently move and expire items
across both organizations. See Export and import retention tags for more information.
