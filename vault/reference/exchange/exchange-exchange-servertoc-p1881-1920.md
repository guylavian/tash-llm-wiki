---
title: "Exchange Server — pages 1881-1920"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1881-1920
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1881-1920
family: exchange
documentKind: "doc"
abstract: "Default value: 1.0 This header field is the first MIME header field that appears in a MIME-formatted message. This header field appears after the other standard RFC 5322 header fields, but before any other MIME header fields. MIME-aware email clients use this header field to ide"
---

# Exchange Server — pages 1881-1920

<!-- p.1881 -->

Default value: 1.0

This header field is the first MIME header field that appears in a MIME-formatted message. This
header field appears after the other standard RFC 5322 header fields, but before any other
MIME header fields. MIME-aware email clients use this header field to identify a MIME-
encoded message. When this header field is absent, MIME-aware email clients identify the
message as plain text.

Content-Type header field
Default value: text/plain

This header field identifies the media type of the message content as described in RFC 2046. A
media type consists of:

     A type:

        Types that begin with x- aren't standard. The Internet Assigned Numbers Authority
        (IANA) maintains a list of registered media types. For more information, see MIME
        Media Types       .

        The multipart media type allows for multiple message parts in the same message by
        using sections defined by different media types. Some Content-Type field values
        include text/plain , text/html , multipart/mixed , and multipart/alternative .

     A subtype: Subtypes that begin with vnd. are vendor-specific.

     One or more optional parameters: For example, a charset= parameter that defines the
     MIME character encoding.

Content-Transfer-Encoding header field
Default value: 7bit

This header field can describe the following information about a message:

     The encoding algorithm used to transform any non-US-ASCII text or binary data that
     exists in the message body.
     An indicator that describes the current condition of the message body.

There can be multiple values of the Content-Transfer-Encoding header field in a MIME
message. When the Content-Transfer-Encoding header field appears in the message header, it
applies to the whole body of the message. When the Content-Transfer-Encoding header field
appears in one of the parts of a multipart message, it applies only to that part of the message.

<!-- p.1882 -->

When an encoding algorithm is applied to the message body data, the message body data is
transformed into plain US-ASCII text. This transformation allows the message to travel through
older messaging servers that only support messages in US-ASCII text. The Content-Transfer-
Encoding header field values that indicate an encoding algorithm was used on the message
body are:

     Quoted-printable : Uses printable US-ASCII characters to encode the message body data.

     If the original message text is mostly US-ASCII text, Quoted-printable encoding gives
     somewhat readable and compact results. All printable US-ASCII text characters except the
     equal sign (=) character can be represented without encoding.

     Base64 : Based primarily on the privacy-enhanced mail (PEM) standard defined in RFC

     4648. Base64 encoding uses the 64-character alphabet encoding algorithm and output
     padding characters defined by PEM to encode the message body data. A Base64 encoded
     message is typically 33 percent larger than the original message. Base64 encoding creates
     a predictable increase in message size and is optimal for binary data and non-US-ASCII
     text.

Typically, you won't see multiple encoding algorithms used in the same message.

When no encoding algorithm has been used on the message body, the Content-Transfer-
Encoding header field merely identifies the current condition of the message body data. The
Content-Transfer-Encoding header field values that indicate that no encoding algorithms were
used on the message body are:

     7bit : Indicates that the message body data is already in the RFC 5322 format. Specifically,
     this means that the following conditions must be true:

        All lines of text must be less than 998 characters long.

        All characters must be US-ASCII text that have character values from 1 through 127.

        The CR and LF characters can only be used together to indicate the end of a line of
        text.

        The whole message body may be 7-bit, or part of the message body in a multipart
        message may be 7-bit. If the multipart message contains other parts that have any
        binary data or non-US-ASCII text, that part of the message must be encoded using the
        Quoted-printable or Base64 encoding algorithms.

        Messages that have 7-bit bodies can travel between messaging servers by using the
        standard DATA command.

<!-- p.1883 -->

8bit : Indicates that the message body data contains non-US-ASCII characters.

Specifically, this means that the following conditions must be true:

  All lines of text must be less than 998 characters long.

  One or more characters in the message body have values larger than 127.

  The CR and LF characters can only be used together to indicate the end of a line of
  text.

  The whole message body may be 8-bit, or part of the message body in a multipart
  message may be 8-bit. If the multipart message contains other parts that have binary
  data, that part of the message must be encoded using the Quoted-printable or Base64
  encoding algorithms.

  Messages that have 8-bit bodies can only travel between messaging servers that
  support the 8BITMIME SMTP extension as defined in RFC 6152, such as Exchange 2000
  Server or later. Specifically, this means that the following conditions must be true:

  The 8BITMIME keyword must be advertised in the server's EHLO response.

  Messages are still transferred by using the SMTP standard DATA command. However,
  the BODY=8BITMIME parameter must be added to the end of the MAIL FROM command.

Binary : Indicates that the message body contains non-US-ASCII text or binary data.

Specifically, this means that the following conditions are true:

  Any sequence of characters is allowed.

  There is no line length limitation.

  Binary message elements don't require encoding.

  Messages that have binary bodies can only travel between messaging servers that
  support the BINARYMIME SMTP extension as defined in RFC 3030, such as Exchange
  2000 Server or later. Specifically, this means that the following conditions must be true:

  The BINARYMIME keyword must be advertised in the server's EHLO response.

  The BINARYMIME SMTP extension can only be used with the CHUNKING SMTP
  extension. Chunking enables large message bodies to be sent in multiple, smaller
  chunks. Chunking is also defined in RFC 3030. The CHUNKING keyword must also be
  advertised in the server's EHLO response.

  Messages are transferred using the BDAT command instead of the standard DATA
  command.

<!-- p.1884 -->

        The BODY=BINARYMIME parameter must be added to the end of the MAIL FROM
        command when the message has a message body.

The values 7bit , 8bit , and Binary never exist together in the same multipart message (the
values are mutually exclusive). The Quoted-printable or Base64 values may appear in a 7-bit or
8-bit multipart message body, but never in a binary message body. If a multipart message
body contains different parts composed of 7-bit and 8-bit content, the whole message is
classified as 8-bit. If a multipart message body contains different parts composed of 7-bit, 8-
bit, and binary content, the whole message is classified as binary.

Content-Disposition header field
Default value: Attachment

This header field instructs a MIME-enabled email client on how it should display an attached
file, and is described in RFC 2183. Valid values are:

      Inline : The attachment is displayed in the message body.

      Attachment : The attached file appears as a regular attachment separate from the message

     body. Other parameters are also with this values (for example, Filename , Creation-date ,
     and Size ).

<!-- p.1885 -->

Message encoding options in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The message encoding options in Exchange Server let you specify message characteristics such
as MIME and non-MIME character sets, binary encoding, and attachment formats. You can
specify message encoding options in the following locations:

      Remote domain settings

      Mail contact and mail user settings

      Outlook settings:

         Message format

         Internet message format

         Internet recipient message format (Outlook 2010 or earlier)

         Message character set encoding options

      Outlook on the web (formerly known as Outlook Web App) message format settings

Typically, the default settings for these message encoding options will work fine. However, you
might need to change the messaging encoding options for recipients that are using older
email clients or messaging systems. They'll likely tell you if messages from your Exchange
environment appear to have formatting issues.

For more information about content conversion in Exchange, see Content conversion. For TNEF
(also known as or Rich Text) settings, see TNEF conversion options.

Remote domain settings
Remote domains specify settings for messages sent to domains that are external to your
Exchange organization. For more information, see Remote Domains.

When you configure message encoding options for a remote domain, the settings are applied
to all messages that are sent to recipients in that domain. Some settings are available in the
Exchange admin center (EAC), but most are only available in the Exchange Management Shell.
The message encoding settings are described in this table:

<!-- p.1886 -->

                                                                                          ﾉ   Expand table

Setting                                        EAC configuration           Exchange Management Shell
                                                                           configuration

MIME character set: The specified              Mail flow > Remote          Cmdlet: Set-RemoteDomain
character set is only used for MIME            domains > Add , or          Parameters: CharacterSet and
messages that don't contain a character        select an existing remote   NonMimeCharacterSet
set. This setting won't overwrite character    domain, and then click
sets that are already specified in             Edit    > Supported
outgoing messages.                             character set section.
Non-MIME character set: This setting is
used if either of these conditions are true:

      Incoming messages from a remote
      domain are missing the value of
      the charset= setting in the MIME
      Content-Type: header field.
      Outgoing messages to a remote
      domain are missing the value of
      the MIME character set.

Content type: Valid values are:                n/a                         Cmdlet: Set-RemoteDomain
MimeHtmlText : All messages are                                            Parameter: ContentType
converted to MIME messages that use
HTML formatting, unless the original
message is a text message. If the original
message is a text message, the outgoing
message will be a MIME message that
uses text formatting. This is the default
value.
MimeText : All messages are converted to
MIME messages that use text formatting.
MimeHtml : All messages are converted to
MIME messages that use HTML
formatting.

Line wrap size: You can specify the            n/a                         Cmdlet: Set-RemoteDomain
maximum number of characters that can                                      Parameter: LineWrapSize
exist on a single line of text in the body                                 The default value is Unlimited ,
of the email message. Older email clients                                  which means the email client is
might prefer 78 characters per line.                                       responsible for setting the line
                                                                           wrap size in new messages.

Mail contact and mail user settings

<!-- p.1887 -->

Mail contacts and mail users represent users that have external email addresses in your
Exchange organization. For more information, see Recipients.

When you configure message encoding options for a mail contact or a mail user, the settings
are only applied to messages that are sent to that specific recipient. All settings are only
available in the Exchange Management Shell in these cmdlets:

     Enable-MailContact, New-MailContact, or Set-MailContact.

     Enable-MailUser, New-MailUser, or Set-MailUser.

The message encoding settings for mail contacts and mail users are described in this list:

     UsePreferMessageFormat parameter*: Specifies whether the message format settings for
     the mail contact or mail user override the corresponding settings for the remote domain.
     Valid values are:

         $true : Messages sent to the Mail contact or mail user use the message format that's

        configured for the Mail contact or mail user.

         $false : Messages sent to the Mail contact or mail user use the message format that's

        configured for the remote domain (the default remote domain or a specific remote
        domain) or configured by the message sender. This is the default value.

     MessageFormat parameter: This parameter specifies the message format for messages
     sent to the mail contact or mail user. Valid values are Text or Mime , and the default value
     is Mime .

     MessageBodyFormat parameter: This parameter specifies the message body format for
     messages sent to the mail contact or mail user. Valid values are Text , Html , or
      TextAndHtml , and the default value is TextAndHtml .

     The MessageFormat and MessageBodyFormat parameters are interdependent:

        If the MessageFormat value is Mime , the MessageBodyFormat value can be Text , Html ,
        or TextAndHtml .

        If the MessageFormat value is Text , the MessageBodyFormat value can only be Text .

     MacAttachmentFormat parameter: Specifies the message attachment format for Apple
     Macintosh operating system clients. Valid values are BinHex , UuEncode , AppleSingle , or
      AppleDouble , and the default value is BinHex .

     The MessageFormat and MacAttachmentFormat parameters are interdependent:

<!-- p.1888 -->

        If the MessageFormat value is Text , the MacAttachmentFormat value can be BinHex or
        UuEncode .

        If the MessageFormat value is Mime , the MacAttachmentFormat value can be BinHex ,
        AppleSingle , or AppleDouble .

Outlook settings
As a sender, you can specify the message encoding in Outlook by using any of these methods:

     Configure the default message format to plain text or HTML.

     Configure the message format to plain text or HTML as you're composing the message by
     using the Format area in the Format Text tab.

     Configure the message encoding options for messages sent to all external recipients.
     These options are called Internet message format options, and they only apply to remote
     recipients (not to recipients in the Exchange organization).

     Configure the message encoding options for messages sent to specific external recipients
     (Outlook 2010 or earlier). These options are called Internet recipient message format
     options, and they only apply to remote recipients in your Contacts folder (not to
     recipients in the Exchange organization).

For instructions on configuring these settings in Outlook, see Change the message format to
HTML, Rich Text Format, or plain text .

By default, Outlook uses automatic character set message encoding by scanning the whole text
of the outgoing message to determine the appropriate encoding to use for the message. This
setting applies to internal and external recipients. However, you can bypass the automatic
selection and specify a preferred encoding for outgoing messages at File > Options >
Advanced > International options.

Outlook on the web settings
As a sender, you can specify message encoding options in Outlook on the web by using either
of these methods:

     Configure the default message format as plain text or HTML in the Message format
     section at Settings > Options > Mail > Layout.

<!-- p.1889 -->

     Configure the message format to plain text or HTML as you're composing the message by
     clicking More options     , and selecting Switch to plain text (if the current format is
     HTML) or Switch to HTML (if the current format is plain text).

Order of precedence for message encoding
options
Some message encoding options are available in remote domain settings, Mail contact or mail
user settings, and Outlook or Outlook on the web settings. Message encoding options for
outgoing messages sent to external recipients are described in the following list from highest
priority to lowest priority:

   1. Mail contact or mail user settings (if the use preferred message format setting is enabled)

   2. Outlook or Outlook on the web settings

   3. Remote domain settings

A setting at a higher level overrides the corresponding setting at a lower level. For example,
Mail contact or mail user settings override the corresponding setting for a remote domain.
Unique settings are unaffected (there's no higher or lower priority setting that conflicts).

The order of precedence for message encoding options are described in the following sections.

Order of precedence for message character sets
The following table describes the order of precedence from highest priority to lowest priority
for message character set encoding options.

                                                                                  ﾉ   Expand table

<!-- p.1890 -->

 Source       Setting               Values

 Outlook      Preferred encoding    Automatically select encoding for outgoing messages enabled or
              for outgoing          disabled (enabled by default).
              messages              Preferred encoding for outgoing messages set to the specified
                                    character set. This is the encoding option that's used if you disable
                                    Automatically select encoding for outgoing messages

 Remote       MIME character set    The specified MIME and non-MIME character sets (which can be the
 domain       and non-MIME          same).
              character set

Notes:

     When you configure the non-MIME character set for a remote domain, the character set
     is assigned to incoming or outgoing messages to and from the remote domain that don't
     contain a specified character set.

     The value of the Windows ANSI code page for the Exchange server is used to assign a
     character set to these types of messages:

          Internal messages that don't contain a specified character set.

          Internal messages that contain a specified character set, but don't contain a specified
          server code page.

     If a message contains a specified but invalid character set, the Exchange server tries to
     replace the invalid character set with a valid one.

Order of precedence for plain text message encoding options
The following table describes the order of precedence from highest priority to lowest priority
for plain text message encoding options.

Note: Only plain text message settings are included here (not plain text settings for MIME
encoded messages).

                                                                                        ﾉ   Expand table

 Source        Setting                Values

 Mail          Use the preferred      If the value $true , the plain text message encoding settings for
 contact or    message format         the mail contact or mail user override the corresponding settings
 mail user                            in Outlook.
                                      If the value is $false , the plain text message encoding settings for

<!-- p.1891 -->

 Source         Setting                    Values

                                           the mail contact or mail user are ignored (the corresponding
                                           settings in Outlook are used).

 Mail           Message format             Text
 contact or
 mail user

 Mail           Message body format        Text
 contact or
 mail user

 Mail           Mac attachment             BinHex or UUEncode
 contact or     format
 mail user

 Outlook        Internet recipient         Send plain text only
 2010 or        message format             Open a contact in the Contacts folder > double-click the email
 earlier        (settings on a specific    address > click View more options for interacting with this
                contact)                   person > select Outlook properties, In the E-mail Properties
                                           dialog that opens, select Send Plain Text only in the Internet
                                           format field.

 Outlook        Internet message           Plain text options for external messages at File > Options > Mail
                format                     > Message format:
                                           Encode attachments in UUENCODE format when sending plain-
                                           text messages (not selected by default)
                                           Automatically wrap text at nn characters (the default value is 76).

 Remote         Line wrap size             132 characters or less, or the value Unlimited . The default value is
 domain                                    Unlimited .

Order of precedence for MIME message encoding options
The following table describes the order of precedence from highest priority to lowest priority
for MIME message encoding options.

                                                                                              ﾉ   Expand table

 Source            Setting                Values

 Mail contact      Use the preferred      If the value $true , the MIME message encoding settings for the
 or mail user      message format         mail contact or mail user override the corresponding settings in
                                          Outlook.
                                          If the value is $false , the MIME text message encoding settings for
                                          the mail contact or mail user are ignored (the corresponding

<!-- p.1892 -->

Source         Setting          Values

                                settings in Outlook, Outlook on the web, or remote domains are
                                used).

Mail contact   Message format   MIME
or mail user

Mail contact   Message body     Text, HTML, or TextAndHtml (the default value is TextAndHtml ).
or mail user   format

Mail contact   Mac attachment   BinHex , AppleSingle , or AppleDouble (the default value is BinHex ).
or mail user   format

Outlook or     Message format   Plain text or HTML
Outlook on
the web

Remote         Content type     MimeHtmlText (the default value), MimeText , or MimeHtml
domain

<!-- p.1893 -->

Exchange Server: TNEF conversion options
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

TNEF, also known as the Transport Neutral Encapsulation Format, Outlook Rich Text Format, or
Exchange Rich Text Format, is a Microsoft-specific format for encapsulating MAPI message
properties. All versions of Outlook fully support TNEF. Outlook on the web (formerly known as
Outlook Web App) translates TNEF into MAPI and displays the formatted messages. Other
email clients that don't support TNEF typically display TNEF formatted messages as plain text
messages with Winmail.dat or Win.dat attachments. For more information about TNEF, see
Exchange and Outlook message formats.

Administrators can specify whether TNEF should be preserved or removed from messages that
leave their Exchange organization. You can specify TNEF conversion options in the following
locations:

      Remote domain settings

      Mail contact and mail user settings

      Outlook settings:

         Message format

         Internet message format

         Internet recipient message format (Outlook 2010 or earlier)

Typically, the default TNEF conversion options will work fine (by default, TNEF messages are
converted to HTML for external recipients). However, you might need to force plain text
conversion for recipients that are using older email clients or messaging systems. They'll likely
tell you if TNEF messages from your Exchange environment appear to have formatting issues.

For more information about other content conversion in Exchange, see Content conversion.

TNEF conversion options for remote domains
Remote domains specify settings for messages sent to domains that are external to your
Exchange organization. For more information, see Remote Domains.

When you configure TNEF conversion options for a remote domain, the settings are applied to
all messages sent to recipients in that domain. You can use the Exchange admin center (EAC) or
the Exchange Management Shell to configure these options:

<!-- p.1894 -->

     In the EAC, go to Mail flow > Remote domains > Add             , or select an existing remote
     domain, and then click Edit          > Use rich-text format section.

     In the Exchange Management Shell, use the TnefEnabled parameter on the Set-
     RemoteDomain cmdlet.

The TNEF conversion options for remote domains are described in this table:

                                                                                     ﾉ    Expand table

 Setting                                                           Value in      Value in Exchange
                                                                   the EAC       Management Shell

 Use TNEF for all messages sent to the remote domain.              Always        $true

 Never use TNEF for any messages sent to the remote domain.        Never         $false

 TNEF messages aren't specifically allowed or prevented for        Follow user   $null (blank)
 recipients in the remote domain. This is the default value.       settings
 Whether TNEF messages are sent to recipients in the remote
 domain depends on the specific setting on the mail contact or
 mail user, or the setting specified by the sender in Outlook.

TNEF conversion options for mail contacts and
mail users
Mail contacts and mail users represent users in your Exchange organization that have external
email addresses For more information, see Recipients.

When you configure TNEF conversion options for a mail contact or a mail user, those options
are applied to all messages sent to that specific recipient. You use the UseMapiRichTextFormat
parameter on the Set-MailUser and Set-MailContact cmdlets in the Exchange Management
Shell. Valid values are:

      Always : TNEF is used for all messages sent to the recipient.

      Never : TNEF is never used for any messages sent to the recipient.

      UseDefaultSettings : This is the default value. TNEF messages aren't specifically allowed or

     prevented for the mail user or mail contact. Whether TNEF messages are sent to the
     recipient depends on the TNEF conversion setting for the remote domain, or the TNEF
     conversion setting that's configured by the sender in Outlook.

<!-- p.1895 -->

TNEF conversion options in Outlook
Senders can control the default conversion options for TNEF messages sent to all external
recipients. These options are called Internet message format options. The options only apply to
external recipients, and not to recipients in the Exchange organization.

Note: The following options define how Outlook rich text messages are handled when sent to
external recipients. If the messages are HTML or plain text, these settings don't apply.

The following TNEF conversion options are available in Outlook:

     Convert to HTML format: This is the default option. TNEF messages sent to external
     recipients are converted to HTML. Any formatting in the message should closely resemble
     the original message. MIME-encoded HTML messages are supported by most email
     clients.

     Convert to Plain Text format: Any TNEF messages sent to remote recipients are
     converted to plain text. Any formatting in the message is lost.

     Send using Outlook Rich Text Format: Any TNEF messages sent to remote recipients
     remain TNEF messages.

Senders in Outlook 2010 or earlier can also control the default TNEF message conversion
options for TNEF messages sent to specific external recipients. These options are called Internet
recipient message format options. The options only apply to external recipients stored in your
Contacts folder, and not to recipients in the Exchange organization. The following list describes
the TNEF conversion options for an external recipient in your Contacts folder:

     Let Outlook decide the best sending format: This is the default setting. This setting
     forces Outlook to use the TNEF conversion option that's specified by the default Internet
     format as described in the previous list (Convert to HTML format, Convert to Plain Text
     format, or Send using Outlook Rich Text Format). Therefore, the TNEF message may be
     left as TNEF, converted to HTML, or converted to plain text (the default result is converted
     to HTML). If you want to make sure that the TNEF message remains TNEF for the contact,
     you should change this setting to Send using Outlook Rich Text format.

     Send Plain Text only: Any TNEF messages sent to the recipient are converted to plain text.
     Any formatting in the message is lost.

     Send using Outlook Rich Text format: Any TNEF messages sent to remote recipients
     remain TNEF messages.

To configure the TNEF conversion settings in Outlook, see Change the message format to
HTML, Rich Text Format, or plain text .

<!-- p.1896 -->

Order of precedence for TNEF conversion options
The TNEF conversion options for messages sent to external recipients are described in the
following list from highest priority to lowest priority:

   1. Remote domain settings

   2. Mail user or mail contact settings

   3. Outlook settings

The setting at a higher level overrides the setting at a lower level. The TNEF setting on the
remote domain overrides the TNEF setting on the mail contact or mail user, or the setting in
Outlook. For example, suppose you send a Rich Text message in Outlook, but the recipient is in
a domain where the remote domain setting specifically doesn't allow TNEF messages. The
message received by the recipient will be plain text or HTML, but not TNEF.

Note: Exchange never sends Summary Transport Neutral Encoding Format (STNEF) messages
to external recipients. Only TNEF messages can be sent to recipients outside the Exchange
organization.

<!-- p.1897 -->

Message size and recipient limits in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019         Subscription Edition

You can apply limits to messages that move through your organization. You can set the
maximum size of an entire message as a whole, or the size of individual parts of a message, or
both. For example, you could restrict the maximum size of the message header or attachments,
or set a maximum number of recipients that can be added to the message. You can apply these
limits to your entire Exchange organization, to specific mail transport connectors, specific
servers, and to individual mailboxes.

This topic only talks about message and recipient size limits. If you want to know more about
how to control how many messages are sent over time, how many connections are allowed
over time, and how long Exchange will wait before closing a connection, see Message rate
limits and throttling.

As you plan the message size limits for your Exchange organization, consider the following
questions:

      What size limits should I impose on all incoming messages?

      What size limits should I impose on all outgoing messages?

      What is the mailbox quota for my organization, and how do the message size limits that I
      have chosen relate to the mailbox quota size?

      Are there users in my organization who need to send or receive messages that are larger
      than the maximum allowed size?

      Does my organization include other messaging systems or separate business units that
      require different message size limits?

This topic provides guidance to help you answer these questions and to apply the appropriate
message size limits in the appropriate locations.

Types of message size limits
The following list describes the basic types of message size limits, and the message
components that they apply to.

<!-- p.1898 -->

     Whole message size limits: Specifies the maximum size of a message, which includes the
     message header, the message body, and any attachments. Exchange uses the custom X-
     MS-Exchange-Organization-OriginalSize: message header to record the original size of
     the message as it enters the Exchange organization. Whenever the message size is
     checked, the lower value of the current message size or the original message size header
     is used. The size of the message can change because of content conversion, encoding,
     and transport agent processing.

     For any message size limit, you need to set a value that's larger than the actual size you
     want enforced. This accounts for the Base64 encoding of attachments and other binary
     data. Base64 encoding increases the size of the message by approximately 33%, so the
     value you specify should be approximately 33% larger than the actual message size you
     want enforced. For example, if you specify a maximum message size value of 64 MB, you
     can expect a realistic maximum message size of approximately 48 MB.

     Attachment size limits: Specifies the maximum size of a single attachment in a message.
     The message might contain many smaller attachments that greatly increase its overall
     size. However, the attachment size limit applies only to the size of an individual
     attachment. While you can't limit the number of attachments on a message, you can use
     the maximum message size limit to control the maximum total of attachments on the
     message.

     Recipient limits: Specifies the total number of recipients that are allowed in a message.
     This includes the total number of recipients in the To:, Cc:, and Bcc: fields. A distribution
     group counts as a single recipient.

     Message header size limits: Specifies the maximum size of all message header fields in a
     message. The size of the message body or attachments isn't considered. Because the
     header fields are plain text, the size of the header is determined by the number of
     characters in each header field and by the total number of header fields. Each text
     character consumes 1 byte.

Scope of limits
The following tables show the message limits at the Organization, Connector, Server, and
Mailbox levels, including information about how to configure the limits in the Exchange admin
center (EAC) or the Exchange Management Shell. To learn how to open the Exchange
Management Shell in your on-premises Exchange organization, see Open the Exchange
Management Shell.

Organizational limits

<!-- p.1899 -->

Organizational limits apply to all Exchange 2019 servers, Exchange 2016 servers, Exchange 2013
Mailbox servers, and Exchange 2010 Hub Transport servers that exist in your organization. On
Edge Transport servers, any organizational limits that you configure are applied to the local
server.

  ７ Note

  Organizational limits also apply to external senders and external recipients (anonymous or
  unauthenticated senders or recipients):

          For inbound messages from external senders, Exchange applies the organizational
          maximum send message size limit (the maximum receive message size limit as
          described in the Recipient limits section is applied to the internal recipient).

          For outbound messages to external recipients, Exchange applies the organization
          maximum receive message size limit (the maximum send message size limit as
          described in the Recipient limits section is applied to the internal sender).

  Therefore, a message size must be within the message size limits for both the sender and
  the recipient. This concept is also explained in the Order of precedence and placement of
  message size limits section later in this topic.

                                                                                    ﾉ     Expand table

 Size limit                  Default      EAC configuration              Exchange Management
                             value                                       Shell configuration

 Maximum size of a           10 MB        Mail flow > Receive            Cmdlet: Set-TransportConfig
 message received                         connectors > More options      Parameter: MaxReceiveSize
                                             > Organization transport
                                          settings > Limits tab >
                                          Maximum receive message
                                          size (MB)

 Maximum size of a           10 MB        Mail flow > Receive            Cmdlet: Set-TransportConfig
 message sent                             connectors > More options      Parameter: MaxSendSize
                                             > Organization transport
                                          settings > Limits > Maximum
                                          send message size (MB)

 Maximum number of           500          Mail flow > Receive            Cmdlet: Set-TransportConfig
 recipients in a message                  connectors > More options      Parameter:
                                             > Organization transport    MaxRecipientEnvelopeLimit

<!-- p.1900 -->

 Size limit                  Default      EAC configuration                  Exchange Management
                             value                                           Shell configuration

                                          settings > Limits Maximum
                                          number of recipients

 Maximum attachment          Not          Mail flow > Rules > Add       >    Cmdlets: New-
 size for a message that     configured   Create a new rule, or select an    TransportRule, Set-
 matches the conditions of                existing rule, and then click      TransportRule
 the mail flow rule (also                 Edit   .                           Parameter:
 known as a transport                     Click More options.                AttachmentSizeOver
 rule)                                    Use the condition Apply this
                                          rule if > Any attachment >
                                          size is greater than or equal
                                          to, and enter a value in
                                          kilobytes (KB).

 Maximum message size        Not          Mail flow > Rules > Add       >    Cmdlets: New-
 for a message that          configured   Create a new rule, or select an    TransportRule, Set-
 matches the conditions of                existing rule, and then click      TransportRule
 the mail flow rule                       Edit    .                          Parameter: MessageSizeOver
                                          Click More options.
                                          Use the condition Apply this
                                          rule if > The message > size is
                                          greater than or equal to, and
                                          enter a value in kilobytes (KB).

To see the values of these organizational limits, run the following commands in the Exchange
Management Shell:

  PowerShell

  Get-TransportConfig | Format-List
  MaxReceiveSize,MaxSendSize,MaxRecipientEnvelopeLimit

  PowerShell

  Get-TransportRule | where {($_.MessageSizeOver -ne $null) -or
  ($_.AttachmentSizeOver -ne $null)} | Format-Table
  Name,MessageSizeOver,AttachmentSizeOver

Connector limits
Connector limits apply to any messages that use the specified Send connector, Receive
connector, Delivery Agent connector, or Foreign connector for message delivery.

<!-- p.1901 -->

You can assign specific message size limits to the Active Directory site links in your
organization. The Transport service on Mailbox servers uses Active Directory sites, and the costs
that are assigned to the Active Directory IP site links as one of the factors to determine the
least-cost routing path between Exchange servers in the organization.

You can assign specific message size limits to the Delivery Agent connectors and Foreign
connectors that are used to send non-SMTP messages in your organization.

                                                                                        ﾉ     Expand table

 Size limit        Default value                         EAC configuration    Exchange Management
                                                                              Shell configuration

 Maximum size      36 MB                                 Mail flow >          Cmdlets: New-
 of a message                                            Receive connectors   ReceiveConnector, Set-
 sent through                                            > Edit    >          ReceiveConnector
 the Receive                                             General >            Parameter: MaxMessageSize
 connector                                               Maximum receive
                                                         message size (MB)

 Maximum size      256 KB                                Not available        Cmdlets: New-
 of all header                                                                ReceiveConnector, Set-
 fields in a                                                                  ReceiveConnector
 message sent                                                                 Parameter: MaxHeaderSize
 through the
 Receive
 connector

 Maximum           Transport service on Mailbox          Not available        Cmdlets: New-
 number of         servers                                                    ReceiveConnector, Set-
 recipients in a   Default <ServerName>: 5000                                 ReceiveConnector
 message sent      Client Proxy <ServerName>: 200                             Parameter:
 through the       Front End Transport service on                             MaxRecipientsPerMessage
 Receive           Mailbox servers
 connector         Default Frontend <ServerName>:
                   200
                   Outbound Proxy Frontend
                   <ServerName>: 200
                   Client Frontend <ServerName>:
                   200
                   If the number of recipients is
                   exceeded in a message from an
                   anonymous sender (for example,
                   an Internet sender), the message
                   is accepted for the first 200
                   recipients. Most messaging
                   servers will continue to resend the
                   message in groups of 200

<!-- p.1902 -->

 Size limit       Default value                     EAC configuration    Exchange Management
                                                                         Shell configuration

                  recipients until the message is
                  delivered to all recipients.

 Maximum size     10 MB                             Mail flow > Send     Cmdlets: New-
 of a message                                       connectors > Edit    SendConnector, Set-
 sent through                                          > General tab >   SendConnector
 the Send                                           Maximum send         Parameter: MaxMessageSize
 connector                                          message size (MB)

 Maximum size     Unlimited                         Not available        Cmdlet: Set-AdSiteLink
 of a message                                                            Parameter: MaxMessageSize
 sent through
 the Active
 Directory site
 link

 Maximum size     Unlimited                         Not available        Cmdlets: New-
 of a message                                                            DeliveryAgentConnector,
 sent through                                                            Set-
 the Delivery                                                            DeliveryAgentConnector
 Agent                                                                   Parameter: MaxMessageSize
 connector

 Maximum size     Unlimited                         Not available        Cmdlet: Set-
 of a message                                                            ForeignConnector
 sent through                                                            Parameter: MaxMessageSize
 the Foreign
 connector

To see the values of these connector limits, run the following command in the Exchange
Management Shell:

  PowerShell

  Get-ReceiveConnector | Format-Table Name,Max*Size,MaxRecipientsPerMessage; Get-
  SendConnector | Format-Table Name,MaxMessageSize; Get-AdSiteLink | Format-Table
  Name,MaxMessageSize; Get-DeliveryAgentConnector | Format-Table
  Name,MaxMessageSize; Get-ForeignConnector | Format-Table Name,MaxMessageSize

Server limits
Server limits apply to specific Mailbox servers or Edge Transport servers. You can set these
message size limits independently on each Mailbox server or Edge Transport server.

<!-- p.1903 -->

                                                                                          ﾉ   Expand table

 Size limit                 Default      EAC              Exchange Management Shell configuration
                            value        configuration

 Maximum size for a         35 MB        Not available    You configure this value in web.config XML
 message sent by                                          application configuration files on the Mailbox
 Outlook on the web                                       server. For more information, see Configure
 clients                                                  client-specific message size limits.

 Maximum size for a         10 MB        Not available    You configure this value in web.config XML
 message sent by                                          application configuration files on the Mailbox
 Exchange ActiveSync                                      server. For more information, see Configure
 clients                                                  client-specific message size limits.

 Maximum size for a         64 MB        Not available    You configure this value in web.config XML
 message sent by                                          application configuration files on the Mailbox
 Exchange Web Services                                    server. For more information, see Configure
 clients                                                  client-specific message size limits.

The pickup directory that's available on Edge Transport servers and Mailbox servers also has
messages size limits that you can configure. Typically, the pickup directory isn't used in
everyday mail flow. It's is used by administrators for mail flow testing, or by applications that
need to create and submit their own messages files. For more information, see Configure the
Pickup Directory and the Replay Directory.

     Maximum size of all header fields in a message file placed in the pickup directory: 64 KB.

     Maximum number of recipients in a message file placed in the pickup directory: 100.

Recipient limits
Recipient limits apply to a specific user object, such as a mailbox, mail contact, mail user,
distribution group, or a mail-enabled public folder.

                                                                                          ﾉ   Expand table

 Size Limit           Default value      EAC configuration                 Exchange Management Shell
                                                                           configuration

 Maximum size of      Site mailbox       For mailboxes:                    Cmdlets:
 a message that       provisioning       Recipients > Mailboxes > Edit     Set-DistributionGroup
 can be sent to       policies: 36 MB        > Mailbox features > Mail     Set-DynamicDistributionGroup
 the specific         All other          flow section > Message size       Set-Mailbox
 recipient            recipient types:   restrictions section > View       Set-MailContact
                      unlimited          details > Received messages       Set-MailUser
                                         section > Maximum message         Set-MailPublicFolder

<!-- p.1904 -->

 Size Limit        Default value   EAC configuration                     Exchange Management Shell
                                                                         configuration

                                   size (KB)                             New-
                                   For mail users:                       SiteMailboxProvisioningPolicy
                                   Recipients > Contacts > Edit          Set-
                                   > Mail flow settings > Message        SiteMailboxProvisioningPolicy
                                   size restrictions > View details      Parameter: MaxReceiveSize
                                   > Received messages section >
                                   Maximum message size (KB)
                                   This setting available in the EAC
                                   for other types of recipients.

 Maximum size of   Unlimited       For mailboxes:                        Cmdlets:
 a message that                    Recipients > Mailboxes > Edit         Set-DistributionGroup
 can be sent by                        > Mailbox features > Mail         Set-DynamicDistributionGroup
 the specific                      flow section > Message size           Set-Mailbox
 sender                            restrictions section > View           Set-MailContact
                                   details > Sent messages section       Set-MailUser
                                   > Maximum message size (KB)           Set-MailPublicFolder
                                   For mail users:                       Parameter: MaxSendSize
                                   Recipients > Contacts > Edit
                                   > Mail flow settings > Message
                                   size restrictions section > View
                                   details > Sent messages section
                                   > Maximum message size (KB)
                                   This setting available in the EAC
                                   for other types of senders.

 Maximum           Unlimited       For mailboxes:                        Cmdlets:
 number of                         Recipients > Mailboxes > Edit         Set-Mailbox, Set-MailUser
 recipients in a                       > Mailbox features > Mail         Parameter: RecipientLimits
 message that's                    flow section > View details >
 sent by the                       Recipient limit section >
 specific sender                   Maximum recipients
                                   This setting isn't available in the
                                   EAC for mail users.

To see the values of these limits, run the corresponding Get- cmdlet for the recipient type in
the Exchange Management Shell.

For example, to see the limits that are configured on a specific mailbox, run the following
command:

  PowerShell

  Get-Mailbox <MailboxIdentity> | Format-List
  MaxReceiveSize,MaxSendSize,RecipientLimits

<!-- p.1905 -->

To see the limits that are configured on all user mailboxes, run the following command:

  PowerShell

  $mb= Get-Mailbox -ResultSize unlimited; $mb | where {$_.RecipientTypeDetails -eq
  'UserMailbox'} | Format-Table Name,MaxReceiveSize,MaxSendSize,RecipientLimits

Order of precedence and placement of message
size limits
The order of precedence for message size limits is the most restrictive limit is enforced. The
only question is where that limit is enforced. The goal is to reject messages that are too large
as early in the transport pipeline as possible. For example, it's a waste of system resources for
the Internet Receive connector to accept large messages that are eventually rejected because
of a lower organizational limit. Make sure that your organization, server, and connector limits
are configured in a way that minimizes any unnecessary processing of messages. You do this
by keeping the limits the same in all locations, or by configuring more restrictive limits where
messages enter your Exchange organization.

An exception to the order is message size limits on mailboxes and messages size limits in mail
flow rules. Exchange checks the maximum message size that's allowed on mailboxes before
mail flow rules process messages. For example, your organization's message size limit is 50 MB,
you configure a 35 MB limit on a mailbox, and you configure a mail flow rule to find and reject
messages larger than 40 MB. If an external sender sends a 45 MB message to the mailbox, the
message is rejected before the mail flow rule is able to evaluate the message.

Recipient limits between authenticated senders and recipients (typically, internal message
senders and recipients) are exempt from the organizational message size restrictions.
Therefore, you can configure specific senders and recipients to exceed the default message size
limits for your organization. For example, you can allow specific mailboxes to send and receive
larger messages than the rest of the organization by configuring custom send and receive
limits for those mailboxes.

However, this exemption applies only to messages sent between authenticated senders and
recipients (typically, internal senders and recipients). For messages sent between anonymous
senders and recipients (typically, Internet senders or Internet recipients), the organizational
limits apply. For example, suppose your organizational message size limit is 10 MB, but you
configured the users in your marketing department to send and receive messages up to 50 MB.
These users will be able to exchange large messages with each other, but not with Internet
senders and recipients (unauthenticated senders and recipients).

<!-- p.1906 -->

How recipient limits work together
The recipient limit on a message is enforced in two places:

     At the protocol level during email transfer where the Receive connector
     MaxRecipientsPerMessage is enforced.

     At the Transport level during categorization where MaxRecipientEnvelopeLimit is enforced.

There is also the mailbox level RecipientLimits, which overrides the Transport level
MaxRecipientEnvelopeLimit and is also enforced during message categorization. If the mailbox
level RecipientLimits is set to unlimited (the default value), then the maximum number of
recipients per message for the mailbox is controlled by the Transport level
MaxRecipientEnvelopeLimit.

For inbound email, the Receive connector MaxRecipientsPerMessage is verified first. However, if
the number of recipients exceeds the limit, the message is not rejected; the connection receives
the error, 452 4.5.3 Too many recipients . Most mail servers understand this error and they will
continue to resend the message in another connection until the message is delivered to all
recipients.

The Receive connector MaxRecipientsPerMessage applies to authenticated and anonymous
SMTP client submissions. However, when an Exchange server relays email through another
Exchange server in the same organization, the Receive connector MaxRecipientsPerMessage is
bypassed.

When the message is accepted and email is sent to the categorizer, the mailbox level
RecipientLimits (if it is not set to unlimited ) or Transport level MaxRecipientEnvelopeLimit are
checked. If the number of recipients exceeds this limit, the message is rejected and a bounce
message is sent with the error 550 5.5.3 RESOLVER.ADR.RecipLimit; too many recipients .

Here is an example scenario:

The receive connector MaxRecipientsPerMessage is set to 100 and the Transport level
MaxRecipientEnvelopeLimit is set to 500. Now, if someone sends an inbound email to 1000

recipients, the email will typically be accepted because the Receive connector limit will force
the sending server to send email in 10 chunks with 100 recipients on each message, which is
lower than the transport categorizer setting MaxRecipientEnvelopeLimit .

Messages exempt from size limits
The following list shows the types of messages that are generated by Mailbox servers or Edge
Transport servers that are exempted from all message size limits except the organizational limit

<!-- p.1907 -->

for the maximum number of recipients that are allowed in a message:

     System messages

     Agent-generated message

     Delivery status notification (DSN) messages (also known as non-delivery reports, NDRs, or
     bounce messages). However, you can use the ExternalDsnMaxMessageAttachSize and
     InternalDsnMaxMessageAttachSize parameters on the Set-TransportConfig cmdlet to limit
     the size of original messages that are included in DSN messages (hence, the effective size
     of the DSN message itself).

     Journal report messages

     Quarantined messages

<!-- p.1908 -->

Message rate limits and throttling
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Message throttling refers to a group of limits that are set on the number of messages and
connections that can be processed by an Exchange server. These limits include message processing
rates, SMTP connection rates, and SMTP session timeout values. These limits work together to
protect an Exchange server from being overwhelmed by accepting and delivering messages.
Although a large backlog of messages and connections may be waiting to be processed, the
message throttling limits enable the Exchange server to process the messages and connections in
an orderly manner.

  ７ Note

  Back pressure is another feature that helps to avoid overwhelming the system resources of an
  Exchange server. Key resources, such as available hard disk space and memory utilization are
  monitored, and when the utilization level exceeds the specified threshold, the server gradually
  stops accepting new connections and messages. For more information, see Understanding
  back pressure. There are also static limits that are available on messages, such as the
  maximum message size, the size of individual attachments, and the number of recipients. For
  more information about message size limits, see Message size and recipient limits in
  Exchange Server.

You can set the message rate limits and throttling options in the following locations:

      Mailbox servers and Edge Transport servers. Collectively, we'll refer to these as transport
      servers.
      Send connectors
      Receive connectors
      Users

Message throttling on transport servers
The following table shows the message throttling options that are available on Mailbox servers and
Edge Transport servers.

                                                                                     ﾉ   Expand table

<!-- p.1909 -->

Rate limit      Default value                     Exchange Management Shell          EAC
                                                  configuration                      configuration

Maximum         20                                Cmdlet: Set-TransportService and   Not available
concurrent      We recommend that you don't       Set-MailboxTransportService p>
mailbox         modify this value unless you're   Parameter:
deliveries:     directed to do so by Microsoft    MaxConcurrentMailboxDeliveries
The             Customer Service and Support.
maximum
number of
delivery
threads that
the Transport
service and
the Mailbox
Transport
Delivery
service can
have open at
the same
time to
deliver
message to
mailboxes.

Maximum         20                                Cmdlet: Set-TransportService and   Not available
concurrent      We recommend that you don't       Set-MailboxTransportService
mailbox         modify this value unless you're
submissions:    directed to do so by Microsoft    Parameter:
The             Customer Service and Support.     MaxConcurrentMailboxSubmissions
maximum
number of
submission
threads that
the Transport
service and
the Mailbox
Transport
Submission
service can
have open at
the same
time to send
messages
from
mailboxes.

Maximum         1200                              Cmdlet: Set-TransportService       Not available
connection
rate per                                          Parameter:
minute: The                                       MaxConnectionRatePerMinute
maximum

<!-- p.1910 -->

 Rate limit      Default value                           Exchange Management Shell         EAC
                                                         configuration                     configuration

 rate that
 connections
 are allowed
 to be
 opened with
 the Transport
 service.

 Maximum         1000                                    Cmdlet: Set-TransportService      Servers >
 concurrent      This value must be greater than or                                        Servers >
 connections:    equal to the                            Parameter:                        Properties
 The             MaxPerDomainOutboundConnections         MaxOutboundConnections            > Transport
 maximum         value.                                                                    limits section
 number of                                                                                 > Maximum
 outbound                                                                                  concurrent
 connections                                                                               connections.
 that the
 Transport                                                                                 Note: In the
 service can                                                                               EAC, you can
 have open at                                                                              only set the
 a time.                                                                                   values 100,
                                                                                           1000, 5000, or
                                                                                           unlimited.

 Maximum         20                                      Cmdlet: Set-TransportService      Servers >
 concurrent      This value must be less than or equal                                     Servers >
 connections     to the MaxOutboundConnections           Parameter:                        Properties
 per domain:     value.                                  MaxPerDomainOutboundConnections   > Transport
 The                                                                                       limits section
 maximum                                                                                   > Maximum
 number of                                                                                 concurrent
 outbound                                                                                  connections
 connections                                                                               per domain.
 that the
 Transport                                                                                 Note: In the
 service can                                                                               EAC, you can
 have open to                                                                              only set the
 a single                                                                                  values 100,
 domain at a                                                                               1000, 5000, or
 time.                                                                                     unlimited.

To see the values of these server message throttling settings, run the following command in the
Exchange Management Shell:

  PowerShell

  Write-Host "Transport service:" -ForegroundColor yellow; Get-TransportService |
  Format-List MaxConcurrent*,MaxConnection*,Max*OutboundConnections; Write-Host "Mailbox

<!-- p.1911 -->

  Transport service:" -ForegroundColor yellow; Get-MailboxTransportService | Format-List
  MaxConcurrent*

  ７ Note

  The Pickup directory and the Replay directory that are available on Edge Transport servers and
  Mailbox servers also have messages rate limits that you can configure. Typically, the Pickup
  directory and the Replay directory aren't used in everyday mail flow. For more information, see
  Configure the Pickup Directory and the Replay Directory. The maximum number of message
  files per minute that can be processed by the Pickup directory and the Replay directory is 100.
  Each directory can independently process message files at this rate.

Message throttling on Send connectors
The following table shows the message throttling options that are available on Send connectors.
Send connectors exist in the Transport service on Mailbox servers and on Edge Transport servers.
For more information, see Send connectors.

                                                                                   ﾉ    Expand table

 Rate limit                            Default    Exchange Management Shell            EAC
                                       value      configuration                        configuration

 Connection inactivity time out: The   00:10:00   Cmdlet: New-SendConnector and        Not available
 maximum amount of time that an        (10        Set-SendConnector
 open SMTP connection with a source    minutes)
 messaging server can remain idle                 Parameter:
 before the connection is closed.                 ConnectionInactivityTimeOut

 Maximum messages per connection:      20         Cmdlet: New-SendConnector and        Not available
 The maximum number of messages                   Set-SendConnector
 that can be sent over a single
 connection                                       Parameter:
                                                  SmtpMaxMessagesPerConnection

To see the values of these Send connector throttling settings, run the following command in the
Exchange Management Shell:

  PowerShell

  Get-SendConnector | Format-List
  Name,ConnectionInactivityTimeout,SmtpMaxMessagesPerConnection

Message throttling on Receive connectors

<!-- p.1912 -->

The following table shows the message throttling options that are available on Receive connectors.
Receive connectors are available in the Front End Transport service on Mailbox servers, the
Transport service on Mailbox servers, and on Edge Transport servers. For more information, see
Receive connectors.

                                                                                            ﾉ   Expand table

 Rate limit             Default value                  Exchange Management Shell                  EAC
                                                       configuration                              configuration

 Connection time        00:10:00 (10 minutes) for      Cmdlet: New-ReceiveConnector and Set-      Not available
 out: The maximum       Receive connectors on          ReceiveConnector
 amount of time         Mailbox servers.
 that an SMTP                                          Parameter: ConnectionTimeout
 connection with a      00:05:00 (1 minute) for

 source messaging       Receive connectors on Edge
 server can remain      Transport servers.
 open, even when
                        This value must be greater
 the source
                        than the
 messaging server is
                        ConnectionInactivityTimeOut
 transmitting data.
                        value.

 Connection             00:05:00 (5 minutes) for       Cmdlet: New-ReceiveConnector and Set-      Not available
 inactivity time out:   Receive connectors on          ReceiveConnector
 The maximum            Mailbox servers.
 amount of time                                        Parameter: ConnectionInactivityTimeOut
 that an open SMTP      00:01:00 (1 minute) for

 connection with a      Receive connectors on Edge
 source messaging       Transport servers.
 server can remain
                        This value must be less than
 idle before the
                        the ConnectionTimeout
 connection is
                        value.
 closed.

 Maximum                5000                           Cmdlet: New-ReceiveConnector and Set-      Not available
 inbound                                               ReceiveConnector
 connections: The
 maximum number                                        Parameter: MaxInboundConnection
 of inbound SMTP
 connections that
 are allowed at the
 same time.

 Maximum                unlimited on the default       Cmdlet: New-ReceiveConnector and Set-      Not available
 inbound                Receive connector named        ReceiveConnector
 connections per        Default <ServerName> in
 source: The            the Transport service on       Parameter:
 maximum number         Mailbox servers.               MaxInboundConnectionPerSource
 of inbound SMTP
 connections that

<!-- p.1913 -->

Rate limit            Default value                 Exchange Management Shell                 EAC
                                                    configuration                             configuration

are allowed from a    20 on other Receive
source messaging      connectors on Mailbox
server at the same    servers and Edge Transport
time.                 servers.

Maximum               100 percent on the default    Cmdlet: New-ReceiveConnector and Set-     Not available
inbound               Receive connector named       ReceiveConnector
connection            Default <ServerName> in
percentage per        the Transport service on      Parameter:
source: The           Mailbox servers.              MaxInboundConnectionPercentagePerSource
maximum
percentage of         2 percent on other Receive
inbound SMTP          connectors on Mailbox
connections that      servers and Edge Transport
are allowed from a    servers.
source messaging
server at the same
time.

Message rate limit:   unlimited on the following    Cmdlet: New-ReceiveConnector and Set-     Not available
The maximum           default Receive connectors:   ReceiveConnector
number of
messages per                Default                 Parameter: MessageRateLimit
minute that can be          <ServerName> in the
sent by a single            Transport service on
source.                     Mailbox servers.
                            Default Frontend
                            <ServerName> in the
                            Front End Transport
                            service on Mailbox
                            servers.
                            Outbound Proxy
                            Frontend
                            <ServerName> in the
                            Front End Transport
                            service on Mailbox
                            servers.

                      5 on the following default
                      Receive connectors:

                            Client Proxy
                            <ServerName> in the
                            Transport service on
                            Mailbox servers.
                            Client Frontend
                            <ServerName> in the
                            Front End Transport
                            service on Mailbox
                            servers.

<!-- p.1914 -->

Rate limit             Default value                 Exchange Management Shell               EAC
                                                     configuration                           configuration

                       600 on the default Receive
                       connector named Default
                       internal Receive connector
                       <ServerName> on Edge
                       Transport servers.

Message rate           IPAddress on the following    Cmdlet: New-ReceiveConnector and Set-   Not available
source: This           default Receive connectors:   ReceiveConnector
indicates how the
message                      Default                 Parameter: MessageRateSource
submission rate is           <ServerName> in the
calculated. Valid            Transport service on
values are:                  Mailbox servers.
                             Default Frontend
      User : The             <ServerName> in the
      rate is                Front End Transport
      calculated             service on Mailbox
      for sending            servers.
      user (based            Outbound Proxy
      on how user            Frontend
      authenticates          <ServerName> in the
      in the SMTP            Front End Transport
      session).              service on Mailbox
       IPAddress :           servers.
      The rate is            Default internal
      calculated             Receive connector
      for sending            <ServerName> on
      hosts.                 Edge Transport
      All : The rate         servers.
      is calculated
      for both         User on the following

      sending          default Receive connectors:
      users and
                             Client Proxy
      sending
                             <ServerName> in the
      hosts.
                             Transport service on
                             Mailbox servers.
                             Client Frontend
                             <ServerName> in the
                             Front End Transport
                             service on Mailbox
                             servers

Tarpit interval: The   00:00:05 (5 seconds)          Cmdlet: New-ReceiveConnector and Set-   Not available
amount of time to                                    ReceiveConnector
artificially delay
SMTP responses to                                    Parameter: TarpitInterval
unauthenticated

<!-- p.1915 -->

 Rate limit            Default value              Exchange Management Shell                   EAC
                                                  configuration                               configuration

 remote servers that
 appear to be
 abusing the
 connection.
 Authenticated
 connections are
 never delayed in
 this manner.

To see the values of these Receive connector message throttling settings, run the following
command in the Exchange Management Shell:

  PowerShell

  Get-ReceiveConnector | Format-List
  Name,Connection*,MaxInbound*,MessageRate*,TarpitInterval

Message throttling on users
The Microsoft Exchange Throttling service tracks resource settings for specific uses and caches the
information in memory. Mail flow throttling settings are also known as a budget. Restarting the
Microsoft Exchange Throttling service resets the mail flow throttling budgets.

Each mailbox has a ThrottlingPolicy setting. The default value for this setting is blank ( $null ). You
can use the ThrottlingPolicy parameter on the Set-Mailbox cmdlet to configure a throttling policy
for a mailbox.

For more information, see the following topics:

     User workload management in Exchange Server

     Change User Throttling Settings for Specific Users

     Change User Throttling Settings for All Users in Your Organization

<!-- p.1916 -->

Understanding back pressure
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

Back pressure is a system resource monitoring feature of the Microsoft Exchange Transport service that exists
on Mailbox servers and Edge Transport servers. Back pressure detects when vital system resources, such as
hard drive space and memory, are overused, and takes action to prevent the server from becoming
completely overwhelmed and unavailable. For example, when a system resource utilization level on the
Exchange server is determined to be too high, the server delays accepting new messages. If the resource
utilization gets worse, the server stops accepting new messages to work exclusively on processing all existing
messages, and might even stop processing outgoing messages. When the system resource utilization returns
to an acceptable level, the Exchange server resumes normal operation by accepting new messages and
processing outgoing messages.

Monitored resources
The following system resources are monitored by back pressure:

      DatabaseUsedSpace[%ExchangeInstallPath%TransportRoles\data\Queue]: Hard drive utilization for
      the drive that holds the message queue database.
      PrivateBytes: The memory that's used by the EdgeTransport.exe process.
      QueueLength[SubmissionQueue]: The number of messages in the Submission queue.
      SystemMemory: The memory that's used by all other processes.
      UsedDiskSpace[%ExchangeInstallPath%TransportRoles\data\Queue]: Hard drive utilization for the
      drive that holds the message queue database transaction logs.
      UsedDiskSpace[%ExchangeInstallPath%TransportRoles\data]: Hard drive utilization for the drive that's
      used for content conversion.
      UsedVersionBuckets[%ExchangeInstallPath%TransportRoles\data\Queue\mail.que]: The number of
      uncommitted message queue database transactions that exist in memory.

For each monitored system resource on a Mailbox server or Edge Transport server, the following levels of
resource utilization or pressure are defined:

      Low or Normal: The resource isn't overused. The server accepts new connections and messages.
      Medium: The resource is slightly overused. Back pressure is applied to the server in a limited manner.
      Mail from senders in the organization's authoritative domains can flow. However, depending on the
      specific resource under pressure, the server uses tarpitting to delay server response or rejects incoming
      MAIL FROM commands from other sources.
      High: The resource is severely overused. Full back pressure is applied. All message flow stops, and the
      server rejects all new incoming MAIL FROM commands.

Transition levels define the low, medium and high resource utilization values depending on whether the
resource pressure is increasing or decreasing. Typically, a resource utilization level that's lower than the
original level is required as the resource utilization decreases. In other words, there really isn't a static value
for low, medium and high resource pressure. You need to know if the utilization is increasing or decreasing
before you can determine the next change in resource utilization level.

<!-- p.1917 -->

The following sections explain how Exchange handles the situation when a specific resource is under
pressure.

Hard drive utilization for the drive that holds the message queue
database
Resource: DatabaseUsedSpace[%ExchangeInstallPath%TransportRoles\data\Queue]

Description: Monitors the percentage of total drive space that's consumed by all files on the drive that holds
the message queue database. Note that the message queue database file contains unused space, so an
accurate description of the total drive space that's consumed by all files is drive size - free disk space - free
space in the database.

To change the default location of the message queue database, see Change the location of the queue
database.

Pressure transitions (%):

     LowToMedium: 96
     MediumToHigh: 99
     HighToMedium: 97
     MediumToLow: 94 Comments::

The default high level of hard drive utilization is calculated by using the following formula:

100 * (<hard drive size in MB> - 500 MB) / <hard drive size in MB>

This formula accounts for the fact that there's unused space in the message queue database

1 GB = 1024 MB. The result is rounded down to the nearest integer.

For example, if your message queue database is located on a 1 terabyte (TB) drive (1048576 MB), the high
level of utilization is 100*(1048576-500)/1048576) or 99%.

As you can see from the formula and the rounding down behavior, the hard drive needs to be very small
before the formula calculates a high utilization value that's less than 99%. For example, a 98% value for high
utilization requires a hard drive of approximately 25 GB or less.

Memory used by the EdgeTransport.exe process
Resource: PrivateBytes

Description: Monitors the percentage of memory that's used by the EdgeTransport.exe process that's part of
the Microsoft Exchange Transport service. This doesn't include virtual memory in the paging file, or memory
that's used by other processes.

Pressure transitions (%):

     LowToMedium: 72
     MediumToHigh: 75

<!-- p.1918 -->

     HighToMedium: 73
     MediumToLow: 71

Comments:

By default, the high level of memory utilization by the EdgeTransport.exe process is 75 percent of the total
physical memory or 1 terabyte, whichever is less. The results are always rounded down to the nearest integer.

Exchange keeps a history of the memory utilization of the EdgeTransport.exe process. If the utilization
doesn't go down to low level for a specific number of polling intervals, known as the history depth, Exchange
rejects incoming messages until the resource utilization goes back to the low level. By default, the history
depth for EdgeTransport.exe memory utilization s 30 polling intervals.

Number of messages in the Submission queue
Resource: QueueLength[SubmissionQueue]

Description: Monitors the number of messages in the Submission queue. Typically, message enter the
Submission queue from Receive connectors. For more information, see Mail flow and the transport pipeline.
A large number of messages in the Submission queue indicates the categorizer is having difficulty processing
messages.

Pressure transitions:

     LowToMedium: 9999
     MediumToHigh: 15000
     HighToMedium: 10000
     MediumToLow: 2000

Comments:

When the Submission queue is under pressure, the Exchange throttles incoming connections by delaying
acknowledgement of incoming messages. Exchange reduces the rate of incoming message flow by tarpitting,
which delays the acknowledgment of the SMTP MAIL FROM command to the sending server. If the pressure
condition continues, Exchange gradually increases the tarpitting delay. After the Submission queue utilization
returns to the low level, Exchange reduces the acknowledgment delay and eases back into normal operation.
By default, Exchange delays message acknowledgments for 10 seconds when under Submission queue
pressure. If the resource pressure continues, the delay is increased in 5-second increments up to 55 seconds.

Exchange keeps a history of Submission queue utilization. If the Submission queue utilization doesn't go
down to the low level for a specific number of polling intervals, known as the history depth, Exchange stops
the tarpitting delay and rejects incoming messages until the Submission utilization goes back to the low
level. By default, the history depth for the Submission queue is in 300 polling intervals.

Memory used by all processes
Resource: SystemMemory

<!-- p.1919 -->

Description: Monitors the percentage of memory that's used by all processes on the Exchange server. This
doesn't include virtual memory in the paging file.

Pressure transitions (%):

     LowToMedium: 88
     MediumToHigh: 94
     HighToMedium: 89
     MediumToLow: 84

Comments:

When the server reaches the high level of memory utilization, message dehydration occurs. Message
dehydration removes unnecessary elements of queued messages that are cached in memory. Typically,
complete messages are cached in memory for increased performance. Removal of the MIME content from
these cached messages reduces the amount of memory that's used at the expense of higher latency, because
the messages are now read directly from the message queue database. By default, message dehydration is
enabled.

Hard drive utilization for the drive that holds the message queue
database transaction logs
Resource: UsedDiskSpace[%ExchangeInstallPath%TransportRoles\data\Queue]

Description: Monitors the percentage of total drive space that's consumed by all files on the drive that holds
the message queue database transaction logs. To change the default location, see Change the location of the
queue database.

Pressure transitions (%):

     LowToMedium: 89
     MediumToHigh: 99
     HighToMedium: 90
     MediumToLow: 80

Comments::

The default high level of hard drive utilization is calculated by using the following formula:

100 * (<hard drive size in MB> - 1152 MB) / <hard drive size in MB>

1 GB = 1024 MB. The result is rounded down to the nearest integer.

For example, if your queue database is located on a 1 terabyte (TB) drive (1048576 MB), the high level of
utilization is 100*(1048576-1152)/1048576) or 99%.

As you can see from the formula and the rounding down behavior, the hard drive needs to be fairly small
before the formula calculates a high utilization value that's less than 99%. For example, a 98% value for high
utilization requires a hard drive of approximately 56 GB or less.

<!-- p.1920 -->

The %ExchangeInstallPath%Bin\EdgeTransport.exe.config application configuration file contains the
DatabaseCheckPointDepthMax key that has the default value 384MB . This key controls the total allowed size
of all uncommitted transaction logs that exist on the hard drive. The value of this key is used in the formula
that calculates high utilization. If you customize this value, the formula becomes:

100 * (<hard drive size in MB> - Min(5120 MB, 3* DatabaseCheckPointDepthMax)) / <hard drive size in MB>

  ７ Note

  The value of the DatabaseCheckPointDepthMax key applies to all transport-related Extensible Storage
  Engine (ESE) databases that exist on the Exchange server. On Mailbox servers, this includes the message
  queue database, and the sender reputation database. On Edge Transport servers, this includes the
  message queue database, the sender reputation database, and the IP filter database that's used by the
  Connection Filtering agent.

Hard drive utilization for the drive that's used for content
conversion
Resource: UsedDiskSpace[%ExchangeInstallPath%TransportRoles\data]

Description: Monitors the percentage of total drive space that's consumed by all files on the drive that's
used for content conversion. The default location of the folder is
%ExchangeInstallPath%TransportRoles\data\Temp and is controlled by the TemporaryStoragePath key in the
%ExchangeInstallPath%Bin\EdgeTransport.exe.config application configuration file.

Pressure transitions (%):

     LowToMedium: 89
     MediumToHigh: 99
     HighToMedium: 90
     MediumToLow: 80

Comments:

The default high level of hard drive utilization is calculated by using the following formula:

100 * (<hard drive size in MB> - 500 MB) / <hard drive size in MB>

1 GB = 1024 MB. The result is rounded down to the nearest integer.

For example, if your message queue database is located on a 1 terabyte (TB) drive (1048576 MB), the high
level of utilization is 100*(1048576-500)/1048576) or 99%.

As you can see from the formula and the rounding down behavior, the hard drive needs to be very small
before the formula calculates a high utilization value that's less than 99%. For example, a 98% value for high
utilization requires a hard drive of approximately 25 GB or less.
