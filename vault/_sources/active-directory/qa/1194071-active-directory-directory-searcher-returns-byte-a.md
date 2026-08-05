---
title: "Active Directory: Directory Searcher returns byte array instead of long (extrememly rare occurances)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1194071/active-directory-directory-searcher-returns-byte-a
question_id: 1194071
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-csharp", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory: Directory Searcher returns byte array instead of long (extrememly rare occurances)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1194071/active-directory-directory-searcher-returns-byte-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I'm dealing with importing records from Active Directory and I've had an issue come up a couple of times but as such it's not reproducable.   

With using the `DirectorySearcher` class, in some occurances attribute values are being returned as a byte array instead of a long (the searcher handles the translation from `IADsLargeInteger`). It may affect other attribute types too but is most certainly happening for longs.

Once it starts happening, it keeps happening until the program is restarted. And then it might be working ok for many months after, so since it's very uncommon, I don't have a lot of information to go on and cannot reproduce it but would like to work around it.

Just wondering if anyone has come across something like this before?  

Rough code being used is:

```
using var searchAttributes = new DirectorySearcher
{
	SearchRoot = directoryEntry,
	Filter = filter,
	PageSize = 1000,
	CacheResults = false,
};

searchAttributes.PropertiesToLoad.AddRange(...); // Various properties here
searchAttributes.PropertiesToLoad.Add("uSNChanged");

using SearchResultCollection src = searchAttributes.FindAll();

foreach (SearchResult sr in src)
{
	// This works like 99% of the time, but sometimes it fails as it's returning a byte[] not a long
	long usnChanged = (long)sr.Properties["uSNChanged"][0]
		
	...
}
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-29*

```
Hello there,

AD is using LDAPv3 encoding the values using UTF8, the solution mentioned in the link above might work for you:

if (result.Properties["sAMAccountName"][0].GetType().IsArray)
{
    name = System.Text.Encoding.UTF8.GetString((byte[])result.Properties["sAMAccountName"][0]);
}
else
{
    name = result.Properties["sAMAccountName"][0].ToString();

Similar discussion here https://social.msdn.microsoft.com/Forums/en-US/78cf7ef0-5bd3-452f-bf39-6507ba0a9bf3/ldap-directoryentry-searchresult-returns-data-differently-in-windows-8-than-win7?forum=aspactivedirectory

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer--
```
