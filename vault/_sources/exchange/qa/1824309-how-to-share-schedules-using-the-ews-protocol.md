---
title: "How to share schedules using the ews protocol"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1824309/how-to-share-schedules-using-the-ews-protocol
question_id: 1824309
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to share schedules using the ews protocol

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1824309/how-to-share-schedules-using-the-ews-protocol (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How to share schedules using the ews protocol

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-19*

Hi,Welcome to the Microsoft Q&A forum.

Here’s a  overview of how you can do that:1. Set up EWS Managed API: First, you need to install and set up the EWS Managed API. You can download it from the Microsoft website or use NuGet to install it into your project.

-  Authenticate: Establish a connection to the Exchange server using proper authentication credentials.

-  Create and Send Sharing Invitation:

-  Create a Calendar Folder: If you don't already have a calendar folder to share, you can create one.

-  Create Sharing Invitation: Use the `CreateSharingInvitation` method to generate a sharing invitation for the calendar.

-  Send Sharing Invitation: Send the sharing invitation to the intended recipient.

Here is a basic example in C#:

```
using Microsoft.Exchange.WebServices.Data;

class Program

{

    static void Main(string[] args)

    {

        ExchangeService service = new ExchangeService(ExchangeVersion.Exchange2013);

        service.Credentials = new WebCredentials("your_username", "your_password", "your_domain");

        service.Url = new Uri("https://your_exchange_server/EWS/Exchange.asmx");

        // Create a calendar folder

        Folder calendarFolder = new Folder(service);

        calendarFolder.DisplayName = "Shared Calendar";

        calendarFolder.FolderClass = "IPF.Appointment";

        calendarFolder.Save(WellKnownFolderName.Calendar);

        // Create a sharing invitation

        FolderPermission permission = new FolderPermission("recipient_email@example.com", FolderPermissionLevel.Reviewer);

        calendarFolder.PermissionSet.Permissions.Add(permission);

        // Send sharing invitation

        CalendarFolder calendar = CalendarFolder.Bind(service, WellKnownFolderName.Calendar);

        calendar.Save();

        Console.WriteLine("Sharing invitation sent.");

    }

}
```

Replace placeholders like `"your_username"`, `"your_password"`, `"your_domain"`, and `"your_exchange_server"` with your actual Exchange server details and credentials.

Please feel free to contact me for any updates.And if this helps,don't forget to mark it as an answer.
