---
title: "EWS 2.0 - Initial Synchronization with MS Exchange Server 2019 and 2010 - Past Data Sync Problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/212088/ews-2-0-initial-synchronization-with-ms-exchange-s
question_id: 212088
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# EWS 2.0 - Initial Synchronization with MS Exchange Server 2019 and 2010 - Past Data Sync Problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/212088/ews-2-0-initial-synchronization-with-ms-exchange-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I'm using EWS API 2.0 version with Microsoft Exchange Server 2019 and 2010 SP2 (on-premise setup).  

I have an application which subscribe 'WellKnownFolderName.Calendar' folder of email boxes using Streaming Notification. In the initial call, I send SyncState value to empty to get all the appointments from calendar for below event types.  

```
EventType.Created, EventType.Modified, EventType.Moved, EventType.Deleted
```

With this setup, when I first time subscribe for a mailbox, it does not retrieve all the old data. That is, if I start my subscription today, it generally retrieves data onwards this month or last month (there is no exact range).  

I need all the appointments available in mailbox, I’m not considering the archived one. At least the appointments those are currently present in mailbox need to be sync.  

My questions:   

-  How much past data will come-up in the initial call ?  

-  Is there any range or limit ?  

-  Can I get past appointments, say after X date or from X to Y date?  

I did lot of research on web, gone through MS documents, blogs and what not. I did not find a clue how much past data it will retrieve. Usually MS doc says it retrieves all appointment and suggest to use code like below, but it does not retrieve all appointment, and recommended code is already in place.  

Here is my sample code:  

```
private void SampleCode()
{
    var moreChangesAvailable = true;
    var syncState = string.Empty;

    while (moreChangesAvailable)
    {
        var changeCollection = exchangeService.SyncFolderItems(
            WellKnownFolderName.Calendar,
            PropertySet.IdOnly,
            null,
            10,
            SyncFolderItemsScope.NormalItems,
            syncState);

        // Internal method to process items retrieved from exchange
        ProcessCollection(changeCollection);

        syncState = changeCollection.SyncState;
        moreChangesAvailable = changeCollection.MoreChangesAvailable;
    }
}
```

Can someone please help with this ?  

Please do the needful.  

Thanks in advance.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-07-07*

SyncFolderItems doesn't do a Calendar Expansion query so if you have recurring appointments these won't be expanded, you can use it to track when the Masters are modified for your 1,3 questions it not going to return a full list of appointments like a FindItems with a CalendarView would.  It makes Calendar Sync logic unfortunately pretty complicated (they did some work in the Graph https://learn.microsoft.com/en-us/graph/delta-query-events?tabs=http to make thing easier but it seems your using OnPrem).     

The easiest sync logic is to use FindItem with a CalendarView for the time windows you want to sync and then use Streaming notifications to trigger a query anytime it detects a change in the Calendar (not the most efficient though but it reliable).   Other things you can do is read the recurrence blob and do your own expansion logic
