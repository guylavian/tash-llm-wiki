---
title: "Exchange EWS FindItems from public folder xml error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1230630/exchange-ews-finditems-from-public-folder-xml-erro
question_id: 1230630
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 3
qa_tags: ["developer-technologies-csharp", "office-exchange-office-exchange-server-development"]
---
# Exchange EWS FindItems from public folder xml error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1230630/exchange-ews-finditems-from-public-folder-xml-erro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.
I've been using Microsoft.Exchange.WebServices version 2.2.0 (latest stable) for two years but yesterday, the call to retrieve messages from a public folder started to fail.  

I use a very simple code very similar to the examples I found in the docs and everything worked for two years.
It's a .net 4.6.1 console application and I connect to our corporate office365 tenant.
The error appears when I call the "FindItems" method to retrieve the message list.
The exception is caused by xml invalid characters but it must reside in the call or it must depend on the particular emails in the folder.   

In english, the exception says approximately: "unexpected XML declaration. XMl declaration must be the first node and it must not have blank spaces before. Row 1, position 19737."
I have no control and I think there is a bug in the internal xml parsing.  

Can you investigate? Is there something I can do?
I tried also to remove all items from the folder but I get the same xml error, located on a lower char so I think that the method is correctly retrieving the messages but it fails to serialize and pass the results to my code.
This is very important because we have a lot of jobs that download and parse emails from public folder.  

Can you confirm that using exchange EWS is the right way to achieve this? I've studied graph API but it doesn't support public folders.
Please help
My code is:

```
int pageSize = 100;
            var view = new ItemView(pageSize);
            view.OrderBy.Add(ItemSchema.DateTimeReceived, SortDirection.Ascending);

            PropertySet itemPropset = new PropertySet(BasePropertySet.FirstClassProperties);
            itemPropset.Add(EmailMessageSchema.Flag);
            itemPropset.Add(EmailMessageSchema.Categories);
            view.PropertySet = itemPropset;

            var searchFilterCollection = new SearchFilter.SearchFilterCollection(LogicalOperator.And);
            searchFilterCollection.Add(new SearchFilter.SearchFilterCollection(LogicalOperator.And, new SearchFilter.IsGreaterThanOrEqualTo(EmailMessageSchema.DateTimeReceived, startDate)));
            

            ExtendedPropertyDefinition PR_FLAG_STATUS = new ExtendedPropertyDefinition(0x1090, MapiPropertyType.Integer);
            searchFilterCollection.Add(new SearchFilter.IsEqualTo(PR_FLAG_STATUS,1));

            bool moreItems = true;
            var mails = new List { };
            while (moreItems)
            {
                try
                {
                    var res = _servizio.FindItems(folder, searchFilterCollection, view);
                    moreItems = res.MoreAvailable;
                    mails.AddRange(res.ToList());

                    if (moreItems)
                        view.Offset += pageSize;
                }
                catch (Exception ex)
                {
                    _log.Error("Cannot download emails!", ex);
                    return null;
                }
            }

            return mails;
        }
```

## Answers

_No answers on this thread._
