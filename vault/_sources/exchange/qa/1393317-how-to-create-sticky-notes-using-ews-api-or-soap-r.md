---
title: "How to create sticky notes using EWS API or Soap Request"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1393317/how-to-create-sticky-notes-using-ews-api-or-soap-r
question_id: 1393317
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to create sticky notes using EWS API or Soap Request

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1393317/how-to-create-sticky-notes-using-ews-api-or-soap-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an soap request below when I call the POST request(https://outlook.office365.com/EWS/Exchange.asmx) using postman, the item is getting created in the designation folder but it created as email message instead of an sticky note.

```
        	                          newo365@example.com                                                                             IPM. StickyNote          U3ViamVjdDogTmV3IE5vdGUNClRocmVhZC1Ub3BpYzogTmV3IE5vdGUNClRocmVhZC1JbmRleDogQWRuZjhjMGIrMXJMR3BFVVN1K3JJTXRxeGhXcC9BPT0NCkRhdGU6IFR1ZSwgNSBTZXAgMjAyMyAxMjowOToyMCArMDAwMA0KTWVzc2FnZS1JRDoNCgk8UE4wUDI4N01CMDE2NkYwOTFGRkUxM0U3NzZCRUM4QzJDRTlFOEFAUE4wUDI4N01CMDE2Ni5JTkRQMjg3LlBST0QuT1VUTE9PSy5DT00+DQpDb250ZW50LUxhbmd1YWdlOiBlbi1JTg0KWC1NUy1IYXMtQXR0YWNoOg0KWC1NUy1UTkVGLUNvcnJlbGF0b3I6DQpYLU1TLUV4Y2hhbmdlLU9yZ2FuaXphdGlvbi1SZWNvcmRSZXZpZXdDZm1UeXBlOiAwDQpDb250ZW50LVR5cGU6IG11bHRpcGFydC9hbHRlcm5hdGl2ZTsNCglib3VuZGFyeT0iXzAwMF9QTjBQMjg3TUIwMTY2RjA5MUZGRTEzRTc3NkJFQzhDMkNFOUU4QVBOMFAyODdNQjAxNjZJTkRQXyINCk1JTUUtVmVyc2lvbjogMS4wDQoNCi0tXzAwMF9QTjBQMjg3TUIwMTY2RjA5MUZGRTEzRTc3NkJFQzhDMkNFOUU4QVBOMFAyODdNQjAxNjZJTkRQXw0KQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluOyBjaGFyc2V0PSJ1cy1hc2NpaSINCg0KTmV3IE5vdGUNCg0KQ2hlY2sgLSAxNnRoIE9jdCAyMDIzDQoNCg0KLS1fMDAwX1BOMFAyODdNQjAxNjZGMDkxRkZFMTNFNzc2QkVDOEMyQ0U5RThBUE4wUDI4N01CMDE2NklORFBfDQpDb250ZW50LVR5cGU6IHRleHQvaHRtbDsgY2hhcnNldD0idXMtYXNjaWkiDQoNCjxodG1sPg0KPGhlYWQ+DQo8bWV0YSBodHRwLWVxdWl2PSJDb250ZW50LVR5cGUiIGNvbnRlbnQ9InRleHQvaHRtbDsgY2hhcnNldD11cy1hc2NpaSI+DQo8bWV0YSBuYW1lPSJHZW5lcmF0b3IiIGNvbnRlbnQ9Ik1pY3Jvc29mdCBFeGNoYW5nZSBTZXJ2ZXIiPg0KPCEtLSBjb252ZXJ0ZWQgZnJvbSBydGYgLS0+DQo8c3R5bGU+PCEtLSAuRW1haWxRdW90ZSB7IG1hcmdpbi1sZWZ0OiAxcHQ7IHBhZGRpbmctbGVmdDogNHB0OyBib3JkZXItbGVmdDogIzgwMDAwMCAycHggc29saWQ7IH0gLS0+PC9zdHlsZT4NCjwvaGVhZD4NCjxib2R5Pg0KPGZvbnQgZmFjZT0iQ2FsaWJyaSIgc2l6ZT0iMiI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMXB0OyI+DQo8ZGl2Pk5ldyBOb3RlPC9kaXY+DQo8ZGl2PiZuYnNwOzwvZGl2Pg0KPGRpdj5DaGVjayAtIDE2dGggT2N0IDIwMjM8L2Rpdj4NCjxkaXY+Jm5ic3A7PC9kaXY+DQo8L3NwYW4+PC9mb250Pg0KPC9ib2R5Pg0KPC9odG1sPg0KDQotLV8wMDBfUE4wUDI4N01CMDE2NkYwOTFGRkUxM0U3NzZCRUM4QzJDRTlFOEFQTjBQMjg3TUIwMTY2SU5EUF8tLQ0K 		  1 -->                         
```

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-10-19*

Hi @Santhosh ,

The issue resolved after adding the extended property to the soap request.
<t:ExtendedProperty><t:ExtendedFieldURI PropertyTag="0x001A" PropertyType="String"/><t:Value>IPM.StickyNote</t:Value></t:ExtendedProperty>

Great to know that the issue has already been resolved and thanks for sharing the solution so that others experiencing the same thing can easily reference this! Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "Accept" the answer : )    

[How to create sticky notes using EWS API or Soap Request]

Issue Symptom:

"I have an soap request below when I call the POST request(https://outlook.office365.com/EWS/Exchange.asmx) using postman, the item is getting created in the designation folder but it created as email message instead of an sticky note."

```
        	                          newo365@example.com                                                                             IPM. StickyNote          U3ViamVjdDogTmV3IE5vdGUNClRocmVhZC1Ub3BpYzogTmV3IE5vdGUNClRocmVhZC1JbmRleDogQWRuZjhjMGIrMXJMR3BFVVN1K3JJTXRxeGhXcC9BPT0NCkRhdGU6IFR1ZSwgNSBTZXAgMjAyMyAxMjowOToyMCArMDAwMA0KTWVzc2FnZS1JRDoNCgk8UE4wUDI4N01CMDE2NkYwOTFGRkUxM0U3NzZCRUM4QzJDRTlFOEFAUE4wUDI4N01CMDE2Ni5JTkRQMjg3LlBST0QuT1VUTE9PSy5DT00+DQpDb250ZW50LUxhbmd1YWdlOiBlbi1JTg0KWC1NUy1IYXMtQXR0YWNoOg0KWC1NUy1UTkVGLUNvcnJlbGF0b3I6DQpYLU1TLUV4Y2hhbmdlLU9yZ2FuaXphdGlvbi1SZWNvcmRSZXZpZXdDZm1UeXBlOiAwDQpDb250ZW50LVR5cGU6IG11bHRpcGFydC9hbHRlcm5hdGl2ZTsNCglib3VuZGFyeT0iXzAwMF9QTjBQMjg3TUIwMTY2RjA5MUZGRTEzRTc3NkJFQzhDMkNFOUU4QVBOMFAyODdNQjAxNjZJTkRQXyINCk1JTUUtVmVyc2lvbjogMS4wDQoNCi0tXzAwMF9QTjBQMjg3TUIwMTY2RjA5MUZGRTEzRTc3NkJFQzhDMkNFOUU4QVBOMFAyODdNQjAxNjZJTkRQXw0KQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluOyBjaGFyc2V0PSJ1cy1hc2NpaSINCg0KTmV3IE5vdGUNCg0KQ2hlY2sgLSAxNnRoIE9jdCAyMDIzDQoNCg0KLS1fMDAwX1BOMFAyODdNQjAxNjZGMDkxRkZFMTNFNzc2QkVDOEMyQ0U5RThBUE4wUDI4N01CMDE2NklORFBfDQpDb250ZW50LVR5cGU6IHRleHQvaHRtbDsgY2hhcnNldD0idXMtYXNjaWkiDQoNCjxodG1sPg0KPGhlYWQ+DQo8bWV0YSBodHRwLWVxdWl2PSJDb250ZW50LVR5cGUiIGNvbnRlbnQ9InRleHQvaHRtbDsgY2hhcnNldD11cy1hc2NpaSI+DQo8bWV0YSBuYW1lPSJHZW5lcmF0b3IiIGNvbnRlbnQ9Ik1pY3Jvc29mdCBFeGNoYW5nZSBTZXJ2ZXIiPg0KPCEtLSBjb252ZXJ0ZWQgZnJvbSBydGYgLS0+DQo8c3R5bGU+PCEtLSAuRW1haWxRdW90ZSB7IG1hcmdpbi1sZWZ0OiAxcHQ7IHBhZGRpbmctbGVmdDogNHB0OyBib3JkZXItbGVmdDogIzgwMDAwMCAycHggc29saWQ7IH0gLS0+PC9zdHlsZT4NCjwvaGVhZD4NCjxib2R5Pg0KPGZvbnQgZmFjZT0iQ2FsaWJyaSIgc2l6ZT0iMiI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMXB0OyI+DQo8ZGl2Pk5ldyBOb3RlPC9kaXY+DQo8ZGl2PiZuYnNwOzwvZGl2Pg0KPGRpdj5DaGVjayAtIDE2dGggT2N0IDIwMjM8L2Rpdj4NCjxkaXY+Jm5ic3A7PC9kaXY+DQo8L3NwYW4+PC9mb250Pg0KPC9ib2R5Pg0KPC9odG1sPg0KDQotLV8wMDBfUE4wUDI4N01CMDE2NkYwOTFGRkUxM0U3NzZCRUM4QzJDRTlFOEFQTjBQMjg3TUIwMTY2SU5EUF8tLQ0K 		  1 -->                         
```

Resolution:

The issue resolved after adding the extended property to the soap request.

```
IPM.StickyNote
```
