---
title: "Does LDAP API support multi-byte UTF-8 encoding for distinguishedName"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/886138/does-ldap-api-support-multi-byte-utf-8-encoding-fo
question_id: 886138
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Does LDAP API support multi-byte UTF-8 encoding for distinguishedName

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/886138/does-ldap-api-support-multi-byte-utf-8-encoding-fo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to confirm if Microsoft LDAP API supports multi-byte UTF-8 variable-length encoding for DNs.     

RFC2251 - Section 4.1.3 Distinguished Name and Relative Distinguished Name, states that DNs use LDAPString format    

RFC2251 - Section 4.1.2 String Type, states that an LDAPString is a Octet String using UTF-8 encoded based on RFC2044 which supports variable-length encoding     

RFC2253 - Section 5 Examples provides examples of UTF-8 encoding for unicode characters     

```
Unicode Letter Description      10646 code UTF-8  Quoted  
   =============================== ========== ====== =======  
   LATIN CAPITAL LETTER L          U0000004C  0x4C   L  
   LATIN SMALL LETTER U            U00000075  0x75   u  
   LATIN SMALL LETTER C WITH CARON U0000010D  0xC48D \C4\8D  
   LATIN SMALL LETTER I            U00000069  0x69   i  
   LATIN SMALL LETTER C WITH ACUTE U00000107  0xC487 \C4\87
```

The Microsoft LDAP Protocol Distinguished Names reference page does state that UTF-8 encoding is used, and notation that should be used:    

If an attribute value contains other reserved characters, such as the equals sign (=) or non-printable characters, it must be encoded in hexadecimal by replacing the character with a backslash followed by two hex digits.    

And this works if for non-printable and printable characters, all of the following examples work with the ldap_search_s API as the base parameter as the distinguished name    

```
CN=Gary Reynolds,OU=Domain Users,DC=w2k12,DC=local  
CN=G\41ry Reynolds,OU=Domain Users,DC=w2k12,DC=local  
CN=G\41\52y Reynolds,OU=Domain Users,DC=w2k12,DC=local  
CN=Before\0DAfter,OU=Domain Users,DC=w2k12,DC=local
```

However, if you try to use multi-byte UTF-8 encoding of the DN , the object is not found.  The object has the following unicode DN    

```
CN=Gačy Reynolds,OU=test1,DC=w2k12,DC=local
```

Encoded as UTF-8 this is:    

```
CN=Ga\C4\8Dy Reynolds,OU=test1,DC=w2k12,DC=local
```

This fails, if you encode the normal char 'a' as hex \41 this works as in the example above, if you encode the same char 'a' Hex 41 using two byte encoding of \C1\81, this also fails.    

Does anyone know if multi-byte UTF-8 encoding is supported for DN and if there is an alternative format that must be used for ANSI LDAP APIs?    

Gary.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-14*

Hello Gary,    

DsQuoteRdnValue and DsUnquoteRdnValue seem to describe the functionality well. The routines used by NTDSAI.dll (QuoteRdnValue and UnquoteRdnValue) differ a little bit (they don't have the third parameter ([in, out] DWORD *pcRdnValueLength).    

I think that the codepage used in a search can be specified by providing an LDAP_SERVER_SORT_OID extended control.    

I looked very carefully at the trace extracts in your previous message and could not understand why it might behave differently. I am very happy to help in understanding this; are you directly using the wldap32.dll search APIs? If so, which one?    

Gary

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-14*

Hi Gary,    

Thanks for the info.  I found that the API in the debug dump are DsQuoteRdnValue and DsUnquoteRdnValue.    

I've done some additional testing with these functions and confirmed that the unquoting function only relates to the following actions:    

-  The leading white space is discarded.    

-  The trailing white space is kept.    

-  Escaped non-special characters return an error.    

-  Unescaped special characters return an error.    

-  RDN values beginning with # (ignoring leading white space) are handled as a BER value that has previously been converted to a string, and converted accordingly.    

-  Escaped hex digits (\89) are converted into a binary byte (0x89).    

-  Escapes are removed from escaped special characters.    

From the action list above and the testing I've completed the DsUnquoteRdnValue doesn't support any form of UTF-8 multi-byte escape encoding as covered in RFC2253, i.e. SN=Lu\C4\8Di\C4\87.  The only alternative option, as you shared, is to use #hexstring option to encode the RDN and any unicode characters as a BER encoded block.    

What I don't understand is why my code hack didn't work, as you guest, this was just a update of the DN string passed to the ldap_search_s with the UTF-8 code added directly to the string.  While the data on the network wire was identical it's still failed.  I'm still looking at this and it appears to be related to code pages and character mappings, but not sure where the codepage is specified in the LDAP connection conversation.    

Gary.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-13*

Hello Gary,    

I am mostly using a debugger connected to the DSA process to see what is happening on the server side. This is what seems to happen:    

-  The inbound BER encoded octet string in the search request is converted to "wchar_t" format with a call to MultiByteToWideChar.    

-  The wchar_t string is then scanned for various things, including hexstring (e.g. #04054761c48d79), quoted special characters and quoted hexpairs.    

-  The problem seems to be the quoted hexpairs: 3 wchar_t characters are consumed from the input string (e.g. "\C4") and one wchar_t value is added to the output string.    

This shows the "normalisation" process. First each component is unquoted and then each component is quoted. The value display is the "input" string to the routine.    

```
Child-SP          RetAddr           Call Site  
00000088`6aefe468 00007ff9`e8b30034 ntdsai!UnquoteRDNValue  
0000022b`0c0a873e  6f 00 72 00 67 00                                o.r.g.  
Child-SP          RetAddr           Call Site  
00000088`6aefe468 00007ff9`e8b30034 ntdsai!UnquoteRDNValue  
0000022b`0c0a872e  68 00 6f 00 6d 00 65 00                          h.o.m.e.  
Child-SP          RetAddr           Call Site  
00000088`6aefe468 00007ff9`e8b30034 ntdsai!UnquoteRDNValue  
0000022b`0c0a871c  55 00 73 00 65 00 72 00-73 00                    U.s.e.r.s.  
Child-SP          RetAddr           Call Site  
00000088`6aefe468 00007ff9`e8b30034 ntdsai!UnquoteRDNValue  
0000022b`0c0a86fe  47 00 5c 00 34 00 31 00-5c 00 43 00 34 00 5c 00  G.\.4.1.\.C.4.\.  
0000022b`0c0a870e  38 00 44 00 79 00                                8.D.y.  
Child-SP          RetAddr           Call Site  
00000088`6aefe498 00007ff9`e8d48339 ntdsai!QuoteRDNValue  
0000022b`0c0a8f20  47 00 41 00 c4 00 8d 00-79 00                    G.A.....y.  
Child-SP          RetAddr           Call Site  
00000088`6aefe498 00007ff9`e8d48339 ntdsai!QuoteRDNValue  
0000022b`0c0a8d10  55 00 73 00 65 00 72 00-73 00                    U.s.e.r.s.  
Child-SP          RetAddr           Call Site  
00000088`6aefe498 00007ff9`e8d48339 ntdsai!QuoteRDNValue  
0000022b`0c0a8b00  68 00 6f 00 6d 00 65 00                          h.o.m.e.  
Child-SP          RetAddr           Call Site  
00000088`6aefe498 00007ff9`e8d48339 ntdsai!QuoteRDNValue  
0000022b`0c0a88f0  6f 00 72 00 67 00                                o.r.g.
```

The input string to the QuoteRDNValue in the extract above is the output of the UnquoteRDNValue - this shows how \C4\8D ends up as the four bytes 00 C4 00 8D.    

Avoiding escaping printable Unicode characters in the DN by using a suitable API on the client side or handling the BER encoding explicitly (via a # escape) are both viable solutions.    

I could not follow your hack - it looks as though you were just changing characters in the tool that uses the LDAP API and not in the LDAP API itself (e.g. a routine like ldap_search).    

Gary

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-13*

Hi Gary,    

This is the network trace of the filter (&(objectclass=*)(name=ga\c4\8dy)), this is the same for both ANSI and Unicode version:     

    

If I use LDP which uses unicode\wide versions of the LDAP API with the unicode DN it is able to return the CN=Gačy Reynolds,OU=test1,DC=w2k12,DC=local entry.  Looking at the network traces you can see that the unicode char has been encoded as a multi-byte UTF-8 value.    

    

I did a quick hack of the code calling the ANSI API to update the DN string to directly encode the string:    

```
String Temp;  
char *ptr;  
  
if (memActivePane != NULL && memActivePane->SelText!= ""){  
    Temp = "CN=Ga??y Reynolds,OU=test1,DC=w2k12,DC=local";  
    ptr = Temp.c_str();  
    *(ptr+5) = 0xc4;  
    *(ptr+6) = 0x8d;  
    TfrmObjectProperties *Prop  = new TfrmObjectProperties(Application);  
        Prop->DisplayDetails( txtLDPServer->Text, Temp, "","","");  
   }
```

and this produces this network trace, which is identical to the LDP call, however, this still fails.    

    

This is the side by side comparison, with the hacked ANSI call on the left and LDP call on the right    

    

As you said if the DN is escaped then the escaped string is passed directly to the server, I haven't tested if the Unicode version does the same:    

    

What tracing are you using on the server side to capture the quoting and unquoting of the traffic?    

Gary.
