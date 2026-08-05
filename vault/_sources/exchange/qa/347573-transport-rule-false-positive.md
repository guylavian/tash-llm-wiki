---
title: "Transport Rule - false positive"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/347573/transport-rule-false-positive
question_id: 347573
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Transport Rule - false positive

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/347573/transport-rule-false-positive (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have a problem where I set up a transport rule to block xlsm attachments sent to a distribution group, however at times it blocks pdf-s as well.  

I checked the message tracking log and sometimes pdf-s arrive, sometimes not. Each fail contains the transport rule rejection reason.  

Exchange version 2016 CU 19  

I couldn't find anything more specific, or a debug logging of transport rules.   

Could you help out why such a specific transport rule can result in a false positive? Is there some sort of a bug?  

Thank you in advance!  

Message tracking:  

```
RunspaceId              : e939e06b-1823-4dbe-8803-8dafea667cef
Timestamp               : 4/6/2021 2:46:03 PM
ClientIp                :
ClientHostname          : ***
ServerIp                :
ServerHostname          :
SourceContext           : Transport Rule Agent
ConnectorId             :
Source                  : AGENT
EventId                 : FAIL
InternalMessageId       : 80762565034851
MessageId               : 
NetworkMessageId        : 8e9b967e-b07a-46d7-081f-08d8f8f9f041
Recipients              : {***}
RecipientStatus         : {[{LED=550 5.7.1 TRANSPORT.RULES.RejectMessage; the message was rejected by organization policy};{MSG=};{FQDN=};{IP=};{LRT=}]}
TotalBytes              : 799707
RecipientCount          : 1
RelatedRecipientAddress :
Reference               :
MessageSubject          : ***
Sender                  : ***
ReturnPath              : ***
Directionality          : Incoming
TenantId                :
OriginalClientIp        :
MessageInfo             : 2021-04-06T12:46:03.426Z;SRV=***,TOTAL-HUB=0.453|SMR=0.209(SMRDI=0.049(SMREH=0.009(SMREH-Sender Filter
                          Agent=0.007)|SMRED=0.001)|SMRC=0.159(SMRCL=0.159|X-SMRCR=0.156))|CAT-PEN=0.251(CATOS=0.007(CATSM=0.005(CATSM-Unified Group Post Sent Item Routing
                          Agent=0.003))|CATRESL=0.002|CATORES-PEN=0.241(CATRS-PEN=0.241(CATRS-Transport Rule Agent-PEN=0.240)))
MessageLatency          :
MessageLatencyType      : None
EventData               : {[E2ELatency, 0.453], [DeliveryPriority, Normal], [AccountForest, ***]}
TransportTrafficType    : Email
SchemaVersion           : 15.01.2176.009
```

Rule configuration:  

```
SerializationData                             : {0, 1, 0, 0, 0, 255, 255, 255, 255, 1, 0, 0, 0, 0, 0, 0...}
RunspaceId                                    : e939e06b-1823-4dbe-8803-8dafea667cef
Priority                                      : 3
DlpPolicy                                     :
DlpPolicyId                                   : 00000000-0000-0000-0000-000000000000
Comments                                      :
ManuallyModified                              : False
ActivationDate                                :
ExpiryDate                                    :
Description                                   : If the message:
                                                    Is sent to a member of group 'distribution group address'
                                                    and has an attachment with a file extension that matches one of these values: 'xlsm'
                                                Take the following actions:
                                                    reject the message and include the explanation 'Delivery not authorized, message refused by Transport Rules' with the status code:
                                                '5.7.1'

RuleVersion                                   : 15.0.1.1
Conditions                                    : {Microsoft.Exchange.MessagingPolicies.Rules.Tasks.SentToMemberOfPredicate,
                                                Microsoft.Exchange.MessagingPolicies.Rules.Tasks.AttachmentExtensionMatchesWordsPredicate}
Exceptions                                    :
Actions                                       : {Microsoft.Exchange.MessagingPolicies.Rules.Tasks.RejectMessageAction}
State                                         : Enabled
Mode                                          : Enforce
RuleErrorAction                               : Ignore
SenderAddressLocation                         : Header
RuleSubType                                   : None
UseLegacyRegex                                : False
From                                          :
FromMemberOf                                  :
FromScope                                     :
SentTo                                        :
SentToMemberOf                                : {*distribution group address*}
SentToScope                                   :
BetweenMemberOf1                              :
BetweenMemberOf2                              :
ManagerAddresses                              :
ManagerForEvaluatedUser                       :
SenderManagementRelationship                  :
ADComparisonAttribute                         :
ADComparisonOperator                          :
SenderADAttributeContainsWords                :
SenderADAttributeMatchesPatterns              :
RecipientADAttributeContainsWords             :
RecipientADAttributeMatchesPatterns           :
AnyOfToHeader                                 :
AnyOfToHeaderMemberOf                         :
AnyOfCcHeader                                 :
AnyOfCcHeaderMemberOf                         :
AnyOfToCcHeader                               :
AnyOfToCcHeaderMemberOf                       :
HasClassification                             :
HasNoClassification                           : False
SubjectContainsWords                          :
SubjectOrBodyContainsWords                    :
HeaderContainsMessageHeader                   :
HeaderContainsWords                           :
FromAddressContainsWords                      :
SenderDomainIs                                :
RecipientDomainIs                             :
SubjectMatchesPatterns                        :
SubjectOrBodyMatchesPatterns                  :
HeaderMatchesMessageHeader                    :
HeaderMatchesPatterns                         :
FromAddressMatchesPatterns                    :
AttachmentNameMatchesPatterns                 :
AttachmentExtensionMatchesWords               : {xlsm}
AttachmentPropertyContainsWords               :
ContentCharacterSetContainsWords              :
HasSenderOverride                             : False
MessageContainsDataClassifications            :
MessageContainsAllDataClassifications         :
SenderIpRanges                                :
SCLOver                                       :
AttachmentSizeOver                            :
MessageSizeOver                               :
WithImportance                                :
MessageTypeMatches                            :
RecipientAddressContainsWords                 :
RecipientAddressMatchesPatterns               :
SenderInRecipientList                         :
RecipientInSenderList                         :
AttachmentContainsWords                       :
AttachmentMatchesPatterns                     :
AttachmentIsUnsupported                       : False
AttachmentProcessingLimitExceeded             : False
AttachmentHasExecutableContent                : False
AttachmentIsPasswordProtected                 : False
AnyOfRecipientAddressContainsWords            :
AnyOfRecipientAddressMatchesPatterns          :
ExceptIfFrom                                  :
ExceptIfFromMemberOf                          :
ExceptIfFromScope                             :
ExceptIfSentTo                                :
ExceptIfSentToMemberOf                        :
ExceptIfSentToScope                           :
ExceptIfBetweenMemberOf1                      :
ExceptIfBetweenMemberOf2                      :
ExceptIfManagerAddresses                      :
ExceptIfManagerForEvaluatedUser               :
ExceptIfSenderManagementRelationship          :
ExceptIfADComparisonAttribute                 :
ExceptIfADComparisonOperator                  :
ExceptIfSenderADAttributeContainsWords        :
ExceptIfSenderADAttributeMatchesPatterns      :
ExceptIfRecipientADAttributeContainsWords     :
ExceptIfRecipientADAttributeMatchesPatterns   :
ExceptIfAnyOfToHeader                         :
ExceptIfAnyOfToHeaderMemberOf                 :
ExceptIfAnyOfCcHeader                         :
ExceptIfAnyOfCcHeaderMemberOf                 :
ExceptIfAnyOfToCcHeader                       :
ExceptIfAnyOfToCcHeaderMemberOf               :
ExceptIfHasClassification                     :
ExceptIfHasNoClassification                   : False
ExceptIfSubjectContainsWords                  :
ExceptIfSubjectOrBodyContainsWords            :
ExceptIfHeaderContainsMessageHeader           :
ExceptIfHeaderContainsWords                   :
ExceptIfFromAddressContainsWords              :
ExceptIfSenderDomainIs                        :
ExceptIfRecipientDomainIs                     :
ExceptIfSubjectMatchesPatterns                :
ExceptIfSubjectOrBodyMatchesPatterns          :
ExceptIfHeaderMatchesMessageHeader            :
ExceptIfHeaderMatchesPatterns                 :
ExceptIfFromAddressMatchesPatterns            :
ExceptIfAttachmentNameMatchesPatterns         :
ExceptIfAttachmentExtensionMatchesWords       :
ExceptIfAttachmentPropertyContainsWords       :
ExceptIfContentCharacterSetContainsWords      :
ExceptIfSCLOver                               :
ExceptIfAttachmentSizeOver                    :
ExceptIfMessageSizeOver                       :
ExceptIfWithImportance                        :
ExceptIfMessageTypeMatches                    :
ExceptIfRecipientAddressContainsWords         :
ExceptIfRecipientAddressMatchesPatterns       :
ExceptIfSenderInRecipientList                 :
ExceptIfRecipientInSenderList                 :
ExceptIfAttachmentContainsWords               :
ExceptIfAttachmentMatchesPatterns             :
ExceptIfAttachmentIsUnsupported               : False
ExceptIfAttachmentProcessingLimitExceeded     : False
ExceptIfAttachmentHasExecutableContent        : False
ExceptIfAttachmentIsPasswordProtected         : False
ExceptIfAnyOfRecipientAddressContainsWords    :
ExceptIfAnyOfRecipientAddressMatchesPatterns  :
ExceptIfHasSenderOverride                     : False
ExceptIfMessageContainsDataClassifications    :
ExceptIfMessageContainsAllDataClassifications :
ExceptIfSenderIpRanges                        :
PrependSubject                                :
SetAuditSeverity                              :
ApplyClassification                           :
ApplyHtmlDisclaimerLocation                   :
ApplyHtmlDisclaimerText                       :
ApplyHtmlDisclaimerFallbackAction             :
ApplyRightsProtectionTemplate                 :
SetSCL                                        :
SetHeaderName                                 :
SetHeaderValue                                :
RemoveHeader                                  :
AddToRecipients                               :
CopyTo                                        :
BlindCopyTo                                   :
AddManagerAsRecipientType                     :
ModerateMessageByUser                         :
ModerateMessageByManager                      : False
RedirectMessageTo                             :
RejectMessageEnhancedStatusCode               : 5.7.1
RejectMessageReasonText                       : Delivery not authorized, message refused by Transport Rules
DeleteMessage                                 : False
Disconnect                                    : False
Quarantine                                    : False
SmtpRejectMessageRejectText                   :
SmtpRejectMessageRejectStatusCode             :
LogEventText                                  :
StopRuleProcessing                            : False
SenderNotificationType                        :
GenerateIncidentReport                        :
IncidentReportContent                         :
RouteMessageOutboundConnector                 :
RouteMessageOutboundRequireTls                : False
ApplyOME                                      : False
RemoveOME                                     : False
OMEExpiryDays                                 : 0
GenerateNotification                          :
Identity                                      : TO CONTAINS xlsm BLOCK
DistinguishedName                             : CN=TO  CONTAINS xlsm BLOCK,CN=TransportVersioned,CN=Rules,CN=Transport Settings,CN=...,CN=Microsoft
                                                Exchange,CN=Services,CN=Configuration,
Guid                                          : a49971d3-
ImmutableId                                   : a49971d3-
OrganizationId                                :
Name                                          : TO  CONTAINS xlsm BLOCK
IsValid                                       : True
WhenChanged                                   : 3/24/2021 10:37:11 AM
ExchangeVersion                               : 0.1 (8.0.535.0)
ObjectState                                   : Unchanged
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-08*

Hello Lucas,  

thank you for your detailed answer.  

We made some more investigations with my customer and found out that the sender was ACTUALLY sending 1 pdf and 1 xlsm.  It's annoying because they "swore" they sent 2 pdf-s and nothing else :(  

Thank you for your time! It might be that the customer will ask me to set the rule up in a way that it'd allow through pdf+xlsm combos and I'd make good use of your idea then.  

Kind regards,  

Marianna
