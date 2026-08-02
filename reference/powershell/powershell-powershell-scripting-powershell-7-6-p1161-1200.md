---
title: "How to use this documentation — pages 1161-1200"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1161-1200
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1161-1200
family: powershell
documentKind: "doc"
abstract: "non-double-quote-chars: non-double-quote-char non-double-quote-chars non-double-quote-char non-double-quote-char: Any Unicode character except double-quote-character Description: When a command is invoked, information may be passed to it via one or more arguments whose values ar"
---

# How to use this documentation — pages 1161-1200

<!-- p.1161 -->

 non-double-quote-chars:
     non-double-quote-char
     non-double-quote-chars non-double-quote-char

 non-double-quote-char:
     Any Unicode character except
         double-quote-character

Description:

When a command is invoked, information may be passed to it via one or more arguments
whose values are accessed from within the command through a set of corresponding
parameters. The process of matching parameters to arguments is called parameter binding.

There are three kinds of argument:

     [switch] parameter (§8.10.5) -- This has the form command-parameter where first-

     parameter-char and parameter-chars together make up the switch name, which
     corresponds to the name of a parameter (without its leading - ) in the command being
     invoked. If the trailing colon is omitted, the presence of this argument indicates that the
     corresponding parameter be set to $true . If the trailing colon is present, the argument
     immediately following must designate a value of type bool, and the corresponding
     parameter is set to that value. For example, the following invocations are equivalent:

       PowerShell

       Set-MyProcess -Strict
       Set-MyProcess -Strict: $true

     Parameter with argument (§8.10.2) -- This has the form command-parameter where first-
     parameter-char and parameter-chars together make up the parameter name, which
     corresponds to the name of a parameter (without its leading -) in the command being
     invoked. There must be no trailing colon. The argument immediately following designates
     an associated value. For example, given a command Get-Power , which has parameters
     $Base and $Exponent , the following invocations are equivalent:

       PowerShell

       Get-Power -Base 5 -Exponent 3
       Get-Power -Exponent 3 -Base 5

<!-- p.1162 -->

      Positional argument (§8.10.2) - Arguments and their corresponding parameters inside
      commands have positions with the first having position zero. The argument in position 0
      is bound to the parameter in position 0; the argument in position 1 is bound to the
      parameter in position 1; and so on. For example, given a command Get-Power , that has
      parameters $Base and $Exponent in positions 0 and 1, respectively, the following invokes
      that command:

          PowerShell

          Get-Power 5 3

See §8.2 for details of the special parameters -- and --% .

When a command is invoked, a parameter name may be abbreviated; any distinct leading part
of the full name may be used, provided that is unambiguous with respect to the names of the
other parameters accepted by the same command.

For information about parameter binding see §8.14.

2.3.5 Literals
Syntax:

  Syntax

  literal:
      integer-literal
      real-literal
      string-literal

2.3.5.1 Numeric literals

There are two kinds of numeric literals: integer (§2.3.5.1.1) and real (§2.3.5.1.2). Both can have
multiplier suffixes (§2.3.5.1.3).

2.3.5.1.1 Integer literals

Syntax:

  Syntax

  integer-literal:
      decimal-integer-literal

<!-- p.1163 -->

      hexadecimal-integer-literal

 decimal-integer-literal:
     decimal-digits numeric-type-suffix~opt~ numeric-multiplier~opt~

 decimal-digits:
     decimal-digit
     decimal-digit decimal-digits

 decimal-digit: one of
     0 1 2 3 4 5 6             7   8   9

 numeric-type-suffix:
     long-type-suffix
     decimal-type-suffix

 hexadecimal-integer-literal:
     0x hexadecimal-digits long-type-suffix~opt~
     numeric-multiplier~opt~

 hexadecimal-digits:
     hexadecimal-digit
     hexadecimal-digit hexadecimal-digits

 hexadecimal-digit: one of
     0 1 2 3 4 5 6 7               8   9   a   b   c   d   e   f

 long-type-suffix:
     l

 numeric-multiplier: one of
     kb mb gb tb pb

Description:

The type of an integer literal is determined by its value, the presence or absence of long-type-
suffix, and the presence of a numeric-multiplier (§2.3.5.1.3).

For an integer literal with no long-type-suffix

     If its value can be represented by type int (§4.2.3), that is its type;
     Otherwise, if its value can be represented by type long (§4.2.3), that is its type.
     Otherwise, if its value can be represented by type decimal (§2.3.5.1.2), that is its type.
     Otherwise, it is represented by type double (§2.3.5.1.2).

For an integer literal with long-type-suffix

     If its value can be represented by type long (§4.2.3), that is its type;
     Otherwise, that literal is ill formed.

<!-- p.1164 -->

In the twos-complement representation of integer values, there is one more negative value
than there is positive. For the int type, that extra value is ‑2147483648. For the long type, that
extra value is ‑9223372036854775808. Even though the token 2147483648 would ordinarily be
treated as a literal of type long, if it is preceded immediately by the unary - operator, that
operator and literal are treated as a literal of type int having the smallest value. Similarly, even
though the token 9223372036854775808 would ordinarily be treated as a real literal of type
decimal, if it is immediately preceded by the unary - operator, that operator and literal are
treated as a literal of type long having the smallest value.

Some examples of integer literals are 123 (int), 123L (long), and 200000000000 (long).

There is no such thing as an integer literal of type byte.

2.3.5.1.2 Real literals

Syntax:

 Syntax

 real-literal:
     decimal-digits . decimal-digits exponent-part~opt~ decimal-type-suffix~opt~
 numeric-multiplier~opt~
     . decimal-digits exponent-part~opt~ decimal-type-suffix~opt~ numeric-
 multiplier~opt~
     decimal-digits exponent-part decimal-type-suffix~opt~ numeric-multiplier~opt~

 exponent-part:
     e sign~opt~     decimal-digits

 sign: one of
     +
     dash

 decimal-type-suffix:
     d
     l

 numeric-multiplier: one of
     kb mb gb tb pb

 dash:
     - (U+002D)
     EnDash character (U+2013)
     EmDash character (U+2014)
     Horizontal bar character (U+2015)

Description:

<!-- p.1165 -->

A real literal may contain a numeric-multiplier (§2.3.5.1.3).

There are two kinds of real literal: double and decimal. These are indicated by the absence or
presence, respectively, of decimal-type-suffix. (There is no such thing as a float real literal.)

A double real literal has type double (§4.2.4.1). A decimal real literal has type decimal (§4.2.4.2).
Trailing zeros in the fraction part of a decimal real literal are significant.

If the value of exponent-part's decimal-digits in a double real literal is less than the minimum
supported, the value of that double real literal is 0. If the value of exponent-part's decimal-digits
in a decimal real literal is less than the minimum supported, that literal is ill formed. If the value
of exponent-part's decimal-digits in a double or decimal real literal is greater than the
maximum supported, that literal is ill formed.

Some examples of double real literals are 1., 1.23, .45e35, 32.e+12, and 123.456E-231.

Some examples of decimal real literals are 1d (which has scale 0), 1.20d (which has scale 2),
1.23450e1d (i.e., 12.3450, which has scale 4), 1.2345e3d (i.e., 1234.5, which has scale 1),
1.2345e-1d (i.e., 0.12345, which has scale 5), and 1.2345e-3d (i.e., 0.0012345, which has scale 7).

  ７ Note

  Because a double real literal need not have a fraction or exponent part, the grouping
  parentheses in (123).M are needed to ensure that the property or method M is being
  selected for the integer object whose value is 123. Without those parentheses, the real
  literal would be ill-formed.

  ７ Note

  Although PowerShell does not provide literals for infinities and NaNs, double real literal-
  like equivalents can be obtained from the static read-only properties PositiveInfinity,
  NegativeInfinity, and NaN of the types float and double (§4.2.4.1).

The grammar permits what starts out as a double real literal to have an l or L type suffix. Such
a token is really an integer literal whose value is represented by type long.

  ７ Note

<!-- p.1166 -->

  This feature has been retained for backwards compatibility with earlier versions of
  PowerShell. However, programmers are discouraged from using integer literals of this
  form as they can easily obscure the literal's actual value. For example, 1.2L has value 1,
  1.2345e1L has value 12, and 1.2345e-5L has value 0, none of which is immediately
  obvious.

2.3.5.1.3 Multiplier suffixes

Syntax:

 Syntax

 numeric-multiplier: *one of*
     kb mb gb tb pb

Description:

For convenience, integer and real literals can contain a numeric-multiplier, which indicates one
of a set of commonly used powers of 10. numeric-multiplier can be written in any combination
of upper- or lowercase letters.

                                                                                 ﾉ   Expand table

 Multiplier    Meaning                                        Example

 kb            kilobyte (1024)                                1kb ≡ 1024

 mb            megabyte (1024 x 1024)                         1.30Dmb ≡ 1363148.80

 gb            gigabyte (1024 x 1024 x 1024)                  0x10Gb ≡ 17179869184

 tb            terabyte (1024 x 1024 x 1024 x 1024)           1.4e23tb ≡ 1.5393162788864E+35

 pb            petabyte (1024 x 1024 x 1024 x 1024 x 1024)    0x12Lpb ≡ 20266198323167232

2.3.5.2 String literals

Syntax:

 Syntax

 string-literal:
     expandable-string-literal
     expandable-here-string-literal
     verbatim-string-literal

<!-- p.1167 -->

    verbatim-here-string-literal

expandable-string-literal:
    double-quote-character expandable-string-characters~opt~   dollars~opt~ double-
quote-character

double-quote-character:
    " (U+0022)
    Left double quotation mark (U+201C)
    Right double quotation mark (U+201D)
    Double low-9 quotation mark (U+201E)

expandable-string-characters:
      expandable-string-part
      expandable-string-characters
      expandable-string-part

expandable-string-part:
    Any Unicode character except
        $
        double-quote-character
        ` (The backtick character U+0060)
    braced-variable
    $ Any Unicode character except
        (
        {
        double-quote-character
        ` (The backtick character U+0060)*
    $ escaped-character
    escaped-character
    double-quote-character double-quote-character

dollars:
    $
    dollars $

expandable-here-string-literal:
    @ double-quote-character whitespace~opt~     new-line-character
        expandable-here-string-characters~opt~   new-line-character   double-quote-
character @

expandable-here-string-characters:
    expandable-here-string-part
    expandable-here-string-characters   expandable-here-string-part

expandable-here-string-part:
    Any Unicode character except
        $
        new-line-character
    braced-variable
    $ Any Unicode character except
        (
        new-line-character
    $ new-line-character Any Unicode character except double-quote-char
    $ new-line-character double-quote-char Any Unicode character except @

<!-- p.1168 -->

      new-line-character Any Unicode character except double-quote-char
      new-line-character double-quote-char Any Unicode character except @

  expandable-string-with-subexpr-start:
      double-quote-character expandable-string-chars~opt~       $(

  expandable-string-with-subexpr-end:
      double-quote-char

  expandable-here-string-with-subexpr-start:
      @ double-quote-character whitespace~opt~        new-line-character   expandable-
  here-string-chars~opt~ $(

  expandable-here-string-with-subexpr-end:
      new-line-character double-quote-character       @

  verbatim-string-literal:
      single-quote-character verbatim-string-characters~opt~ single-quote-char

  single-quote-character:
      ' (U+0027)
      Left single quotation mark (U+2018)
      Right single quotation mark (U+2019)
      Single low-9 quotation mark (U+201A)
      Single high-reversed-9 quotation mark (U+201B)

  verbatim-string-characters:
      verbatim-string-part
      verbatim-string-characters verbatim-string-part

  verbatim-string-part:
      *Any Unicode character except* single-quote-character
      single-quote-character single-quote-character

  verbatim-here-string-literal:
      @ single-quote-character whitespace~opt~     new-line-character
          verbatim-here-string-characters~opt~     new-line-character
              single-quote-character *@*

  verbatim-*here-string-characters:
      verbatim-here-string-part
      verbatim-here-string-characters      verbatim-here-string-part

  verbatim-here-string-part:
      Any Unicode character except* new-line-character
      new-line-character Any Unicode character except single-quote-character
      new-line-character single-quote-character Any Unicode character except @

Description:

There are four kinds of string literals:

<!-- p.1169 -->

     verbatim-string-literal (single-line single-quoted), which is a sequence of zero or more
     characters delimited by a pair of single-quote-characters. Examples are '' and 'red'.

     expandable-string-literal (single-line double-quoted), which is a sequence of zero or more
     characters delimited by a pair of double-quote-characters. Examples are "" and "red".

     verbatim-here-string-literal (multi-line single-quoted), which is a sequence of zero or
     more characters delimited by the character pairs @single-quote-character and single-
     quote-character@, respectively, all contained on two or more source lines. Examples are:

       PowerShell

       @'
       '@

       @'
       line 1
       '@

       @'
       line 1
       line 2
       '@

     expandable-here-string-literal (multi-line double-quoted), which is a sequence of zero or
     more characters delimited by the character pairs @double-quote-character and double-
     quote-character@, respectively, all contained on two or more source lines. Examples are:

       PowerShell

       @"
       "@

       @"
       line 1
       "@

       @"
       line 1
       line 2
       "@

For verbatim-here-string-literals and expandable-here-string-literals, except for white space
(which is ignored) no characters may follow on the same source line as the opening delimiter-
character pair, and no characters may precede on the same source line as the closing delimiter
character pair.

<!-- p.1170 -->

The body of a verbatim-here-string-literal or an expandable-here-string-literal begins at the
start of the first source line following the opening delimiter, and ends at the end of the last
source line preceding the closing delimiter. The body may be empty. The line terminator on the
last source line preceding the closing delimiter is not part of that literal's body.

A literal of any of these kinds has type string (§4.3.1).

The character used to delimit a verbatim-string-literal or expandable-string-literal can be
contained in such a string literal by writing that character twice, in succession. For example,
'What''s the time?' and "I said, ""Hello""." . However, a single-quote-character has no

special meaning inside an expandable-string-literal, and a double-quote-character has no
special meaning inside a verbatim-string-literal.

An expandable-string-literal and an expandable-here-string-literal may contain escaped-
characters (§2.3.7). For example, when the following string literal is written to the pipeline, the
result is as shown below:

  PowerShell

  "column1`tcolumn2`nsecond line, `"Hello`", ```Q`5`!"

  Output

  column1<horizontal-tab>column2<new-line>
  second line, "Hello", `Q5!

If an expandable-string-literal or expandable-here-string-literal contains the name of a variable,
unless that name is preceded immediately by an escape character, it is replaced by the string
representation of that variable's value (§6.7). This is known as variable substitution.

  ７ Note

  If the variable name is part of some larger expression, only the variable name is replaced.
  For example, if $a is an array containing the elements 100 and 200, ">$a.Length<" results
  in >100 200.Length< while ">$($a.Length)<" results in >2< . See sub-expression expansion
  below.

For example, the source code

  PowerShell

<!-- p.1171 -->

  $count = 10
  "The value of `$count is $count"

results in the expandable-string-literal

  Output

  The value of $count is 10.

Consider the following:

  PowerShell

  $a = "red","blue"
  "`$a[0] is $a[0], `$a[0] is $($a[0])" # second [0] is taken literally

The result is

  Output

  $a[0] is red blue[0], $a[0] is red

expandable-string-literals and expandable-here-string-literals also support a kind of
substitution called sub-expression expansion, by treating text of the form $( ... ) as a sub-
expression (§7.1.6). Such text is replaced by the string representation of that expression's value
(§6.8). Any white space used to separate tokens within sub-expression's statement-list is ignored
as far as the result string's construction is concerned.

The examples,

  PowerShell

  $count = 10
  "$count + 5 is $($count + 5)"
  "$count + 5 is `$($count + 5)"
  "$count + 5 is `$(`$count + 5)"

result in the following expandable-string-literals:

  Output

  10 + 5 is 15
  10 + 5 is $(10 + 5)

<!-- p.1172 -->

 10 + 5 is $($count + 5)

The following source,

 PowerShell

 $i = 5; $j = 10; $k = 15
 "`$i, `$j, and `$k have the values $( $i; $j; $k )"

results in the following expandable-string-literal:

 Output

 $i, $j, and $k have the values 5 10 15

These four lines could have been written more succinctly as follows:

 PowerShell

 "`$i, `$j, and `$k have the values $(($i = 5); ($j = 10); ($k = 15))"

In the following example,

 PowerShell

 "First 10 squares: $(for ($i = 1; $i -le 10; ++$i) { "$i $($i*$i) " })"

the resulting expandable-string-literal is as follows:

 Output

 First 10 squares: 1 1 2 4 3 9 4 16 5 25 6 36 7 49 8 64 9 81 10 100

As shown, a sub-expression can contain string literals having both variable substitution and
sub-expression expansion. Note also that the inner expandable-string-literal's delimiters need
not be escaped; the fact that they are inside a sub-expression means they cannot be
terminators for the outer expandable-string-literal.

An expandable-string-literal or expandable-here-string-literal containing a variable substitution
or sub-expression expansion is evaluated each time that literal is used; for example,

 PowerShell

<!-- p.1173 -->

  $a = 10
  $s1 = "`$a = $($a; ++$a)"
  "`$s1 = >$s1<"
  $s2 = "`$a = $($a; ++$a)"
  "`$s2 = >$s2<"
  $s2 = $s1
  "`$s2 = >$s2<"

which results in the following expandable-string-literals:

  Output

  $s1 = >$a = 10<
  $s2 = >$a = 11<
  $s2 = >$a = 10<

The contents of a verbatim-here-string-literal are taken verbatim, including any leading or
trailing white space within the body. As such, embedded single-quote-characters need not be
doubled-up, and there is no substitution or expansion. For example,

  PowerShell

  $lit = @'
  That's it!
  2 * 3 = $(2*3)
  '@

which results in the literal

  Output

  That's it!
  2 * 3 = $(2*3)

The contents of an expandable-here-string-literal are subject to substitution and expansion, but
any leading or trailing white space within the body but outside any sub-expressions is taken
verbatim, and embedded double-quote-characters need not be doubled-up. For example,

  PowerShell

  $lit = @"
  That's it!
  2 * 3 = $(2*3)
  "@

<!-- p.1174 -->

which results in the following literal when expanded:

 PowerShell

 That's it!
 2 * 3 = 6

For both verbatim-here-string-literals and expandable-here-string-literals, each line terminator
within the body is represented in the resulting literal in an implementation-defined manner.
For example, in

 PowerShell

 $lit = @"
 abc
 xyz
 "@

the second line of the body has two leading spaces, and the first and second lines of the body
have line terminators; however, the terminator for the second line of the body is not part of
that body. The resulting literal is equivalent to: "abc<implementation-defined character
sequence>xyz" .

  ７ Note

  To aid readability of source, long string literals can be broken across multiple source lines
  without line terminators being inserted. This is done by writing each part as a separate
  literal and concatenating the parts with the + operator (§7.7.2). This operator allows its
  operands to designate any of the four kinds of string literal.

  ７ Note

  Although there is no such thing as a character literal per se, the same effect can be
  achieved by accessing the first character in a 1-character string, as follows: [char]"A" or
  "A"[0] .

For both verbatim-here-string-literals and expandable-here-string-literals, each line terminator
within the body is represented exactly as it was provided.

2.3.5.3 Null literal

<!-- p.1175 -->

See the automatic variable $null (§2.3.2.2).

2.3.5.4 Boolean literals

See the automatic variables $false and $true (§2.3.2.2).

2.3.5.5 Array literals

PowerShell allows expressions of array type (§9) to be written using the unary comma operator
(§7.2.1), array-expression (§7.1.7), the binary comma operator (§7.3), and the range operator
(§7.4).

2.3.5.6 Hash literals

PowerShell allows expressions of type Hashtable (§10) to be written using a hash-literal-
expression (§7.1.9)

2.3.5.7 Type names

Syntax:

  Syntax

  type-name:
      type-identifier
      type-name . type-identifier

  type-identifier:
      type-characters

  type-characters:
      type-character
      type-characters type-character

  type-character:
      A Unicode character of classes Lu, Ll, Lt, Lm, Lo, or Nd
      _ (The underscore character U+005F)

  array-type-name:
      type-name [

  generic-type-name:
      type-name [

2.3.6 Operators and punctuators
Syntax:

<!-- p.1176 -->

 Syntax

 operator-or-punctuator: one of
     {   }   [    ]   (    )  @(  @{      $(   ;
     && || &      |   ,    ++ ..  ::      .
     !   *   /    %   +    -  --
     -and   -band    -bnot   -bor
     -bxor   -not    -or     -xor
     assignment-operator
     merging-redirection-operator
     file-redirection-operator
     comparison-operator
     format-operator

 assignment-operator: one of
     = -= += *= /= %=

 file-redirection-operator: one of
     > >> 2> 2>> 3> 3>> 4> 4>>
     5> 5>> 6> 6>> *> *>> <

 merging-redirection-operator: one of
     *>&1 2>&1 3>&1 4>&1 5>&1 6>&1
     *>&2 1>&2 3>&2 4>&2 5>&2 6>&2

 comparison-operator: *one of
     -as           -ccontains         -ceq
     -cge          -cgt               -cle
     -clike        -clt               -cmatch
     -cne          -cnotcontains      -cnotlike
     -cnotmatch    -contains          -creplace
     -csplit       -eq                -ge
     -gt           -icontains         -ieq
     -ige          -igt               -ile
     -ilike        -ilt               -imatch
     -in           -ine               -inotcontains
     -inotlike     -inotmatch         -ireplace
     -is           -isnot             -isplit
     -join         -le                -like
     -lt           -match             -ne
     -notcontains -notin             -notlike
     -notmatch     -replace          -shl*
     -shr          -split

 format-operator:
     -f

Description:

&& and || are reserved for future use.

  ７ Note

<!-- p.1177 -->

  Editor's Note: The pipeline chain operators && and || were introduced in PowerShell 7.
  See about_Pipeline_Chain_Operators.

The name following dash in an operator is reserved for that purpose only in an operator
context.

An operator that begins with dash must not have any white space between that dash and the
token that follows it.

2.3.7 Escaped characters
Syntax:

 Syntax

 escaped-character:
     ` (The backtick character U+0060) followed by any Unicode character

Description:

An escaped character is a way to assign a special interpretation to a character by giving it a
prefix Backtick character (U+0060). The following table shows the meaning of each escaped-
character:

                                                                                 ﾉ   Expand table

 Escaped           Meaning
 Character

 `a                Alert (U+0007)

 `b                Backspace (U+0008)

 `f                Form-feed (U+000C)

 `n                New-line (U+000A)

 `r                Carriage return (U+000D)

 `t                Horizontal tab (U+0009)

 `v                Vertical tab (U+0009)

 `'                Single quote (U+0027)

<!-- p.1178 -->

 Escaped             Meaning
 Character

 `"                  Double quote (U+0022)

 ``                  Backtick (U+0060)

 `0                  NUL (U+0000)

 `x                  If x is a character other than those characters shown above, the backtick character is
                     ignored and x is taken literally.

The implication of the final entry in the table above is that spaces that would otherwise
separate tokens can be made part of a token instead. For example, a file name containing a
space can be written as Test` Data.txt (as well as 'Test Data.txt' or "Test Data.txt" ).

 Last updated on 04/08/2026

<!-- p.1179 -->

3. Basic concepts

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December 2012 and
  is based on Windows PowerShell 3.0. This specification does not reflect the current state
  of PowerShell. There is no plan to update this documentation to reflect the current state.
  This documentation is presented here for historical reference.

  The specification document is available as a Microsoft Word document from the Microsoft
  Download Center at: https://www.microsoft.com/download/details.aspx?id=36389
  That Word document has been converted for presentation here on Microsoft Learn.
  During conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

3.1 Providers and drives
A provider allows access to data and components that would not otherwise be easily accessible
at the command line. The data is presented in a consistent format that resembles a file system
drive.

The data that a provider exposes appears on a drive, and the data is accessed via a path just
like with a disk drive. Built-in cmdlets for each provider manage the data on the provider drive.

PowerShell includes the following set of built-in providers to access the different types of data
stores:

                                                                                 ﾉ   Expand table

 Provider            Drive Name          Description                                    Ref.

 Alias               Alias:              PowerShell aliases                             §3.1.1

 Environment         Env:                Environment variables                          §3.1.2

 FileSystem          A:, B:, C:, ...     Disk drives, directories, and files            §3.1.3

 Function            Function:           PowerShell functions                           §3.1.4

 Variable            Variable:           PowerShell variables                           §3.1.5

<!-- p.1180 -->

Windows PowerShell:

                                                                                    ﾉ   Expand table

 Provider      Drive Name                                       Description

 Certificate   Cert:                                            x509 certificates for digital
                                                                signatures

 Registry      HKLM: (HKEY_LOCAL_MACHINE), HKCU:                Windows registry
               (HKEY_CURRENT_USER)

 WSMan         WSMan:                                           WS-Management configuration
                                                                information

The following cmdlets deal with providers and drives:

      Get-PSProvider: Gets information about one or more providers
      Get-PSDrive: Gets information about one or more drives

The type of an object that represents a provider is described in §4.5.1. The type of an object
that represents a drive is described in §4.5.2.

3.1.1 Aliases
An alias is an alternate name for a command. A command can have multiple aliases, and the
original name and all of its aliases can be used interchangeably. An alias can be reassigned. An
alias is an item (§3.3).

An alias can be assigned to another alias; however, the new alias is not an alias of the original
command.

The provider Alias is a flat namespace that contains only objects that represent the aliases. The
variables have no child items.

PowerShell comes with a set of built-in aliases.

The following cmdlets deal with aliases:

      New-Alias: Creates an alias
      Set-Alias: Creates or changes one or more aliases
      Get-Alias: Gets information about one or more aliases
      Export-Alias: Exports one or more aliases to a file

When an alias is created for a command using New-Alias , parameters to that command cannot
be included in that alias. However, direct assignment to a variable in the Alias: namespace does

<!-- p.1181 -->

permit parameters to be included.

  ７ Note

  It is a simple matter, however, to create a function that does nothing more than contain
  the invocation of that command with all desired parameters, and to assign an alias to that
  function.

The type of an object that represents an alias is described in §4.5.4.

Alias objects are stored on the drive Alias: (§3.1).

3.1.2 Environment variables
The PowerShell Environment provider allows operating system environment variables to be
retrieved, added, changed, cleared, and deleted.

The provider Environment is a flat namespace that contains only objects that represent the
environment variables. The variables have no child items.

An environment variable's name cannot include the equal sign ( = ).

Changes to the environment variables affect the current session only.

An environment variable is an item (§3.3).

The type of an object that represents an environment variable is described in §4.5.6.

Environment variable objects are stored on the drive Env: (§3.1).

3.1.3 File system
The PowerShell FileSystem provider allows directories and files to be created, opened, changed,
and deleted.

The FileSystem provider is a hierarchical namespace that contains objects that represent the
underlying file system.

Files are stored on drives with names like A:, B:, C:, and so on (§3.1). Directories and files are
accessed using path notation (§3.4).

A directory or file is an item (§3.3).

<!-- p.1182 -->

3.1.4 Functions
The PowerShell Function provider allows functions (§8.10) and filters (§8.10.1) to be retrieved,
added, changed, cleared, and deleted.

The provider Function is a flat namespace that contains only the function and filter objects.
Neither functions nor filters have child items.

Changes to the functions affect the current session only.

A function is an item (§3.3).

The type of an object that represents a function is described in §4.5.10. The type of an object
that represents a filter is described in §4.5.11.

Function objects are stored on drive Function: (§3.1).

3.1.5 Variables
Variables can be defined and manipulated directly in the PowerShell language.

The provider Variable is a flat namespace that contains only objects that represent the
variables. The variables have no child items.

The following cmdlets also deal with variables:

     New-Variable: Creates a variable
     Set-Variable: Creates or changes the characteristics of one or more variables
     Get-Variable: Gets information about one or more variables
     Clear-Variable: Deletes the value of one or more variables
     Remove-Variable: Deletes one or more variables

As a variable is an item (§3.3), it can be manipulated by most Item-related cmdlets.

The type of an object that represents a variable is described in §4.5.3.

Variable objects are stored on drive Variable: (§3.1).

3.2 Working locations
The current working location is the default location to which commands point. This is the
location used if an explicit path (§3.4) is not supplied when a command is invoked. This location
includes the current drive.

<!-- p.1183 -->

A PowerShell host may have multiple drives, in which case, each drive has its own current
location.

When a drive name is specified without a directory, the current location for that drive is
implied.

The current working location can be saved on a stack, and then set to a new location. Later,
that saved location can be restored from that stack and made the current working location.
There are two kinds of location stacks: the default working location stack, and zero or more
user-defined named working location stacks. When a session begins, the default working
location stack is also the current working location stack. However, any named working location
stack can be made the current working location stack.

The following cmdlets deal with locations:

      Set-Location: Establishes the current working location
      Get-Location: Determines the current working location for the specified drive(s), or the
      working locations for the specified stack(s)
      Push-Location: Saves the current working location on the top of a specified stack of
      locations
      Pop-Location: Restores the current working location from the top of a specified stack of
      locations

The object types that represents a working location and a stack of working locations are
described in §4.5.5.

3.3 Items
An item is an alias (§3.1.1), a variable (§3.1.5), a function (§3.1.4), an environment variable
(§3.1.2), or a file or directory in a file system (§3.1.3).

The following cmdlets deal with items:

      New-Item: Creates a new item
      Set-Item: Changes the value of one or more items
      Get-Item: Gets the items at the specified location
      Get-ChildItem: Gets the items and child items at the specified location
      Copy-Item: Copies one or more items from one location to another
      Move-Item: Moves one or more items from one location to another
      Rename-Item: Renames an item
      Invoke-Item: Performs the default action on one or more items
      Clear-Item: Deletes the contents of one or more items, but does not delete the items (see
      Remove-Item: Deletes the specified items

<!-- p.1184 -->

The following cmdlets deal with the content of items:

     Get-Content: Gets the content of the item
     Add-Content: Adds content to the specified items
     Set-Content: Writes or replaces the content in an item
     Clear-Content: Deletes the contents of an item

The type of an object that represents a directory is described in §4.5.17. The type of an object
that represents a file is described in §4.5.18.

3.4 Path names
All items in a data store accessible through a PowerShell provider can be identified uniquely by
their path names. A path name is a combination of the item name, the container and
subcontainers in which the item is located, and the PowerShell drive through which the
containers are accessed.

Path names are divided into one of two types: fully qualified and relative. A fully qualified path
name consists of all elements that make up a path. The following syntax shows the elements in
a fully qualified path name:

   Tip

  The ~opt~ notation in the syntax definitions indicates that the lexical entity is optional in
  the syntax.

 Syntax

 path:
     provider~opt~         drive~opt~      containers~opt~   item

 provider:
     module~opt~       provider       ::

 module:
     module-name       \

 drive:
     drive-name       :

 containers:
     container   \
     containers container         \

module-name refers to the parent module.

<!-- p.1185 -->

provider refers to the PowerShell provider through which the data store is accessed.

drive refers to the PowerShell drive that is supported by a particular PowerShell provider.

A container can contain other containers, which can contain other containers, and so on, with
the final container holding an item. Containers must be specified in the hierarchical order in
which they exist in the data store.

Here is an example of a path name:

E:\Accounting\InvoiceSystem\Production\MasterAccount\MasterFile.dat

If the final element in a path contains other elements, it is a container element; otherwise, it's a
leaf element.

In some cases, a fully qualified path name is not needed; a relative path name will suffice. A
relative path name is based on the current working location. PowerShell allows an item to be
identified based on its location relative to the current working location. A relative path name
involves the use of some special characters. The following table describes each of these
characters and provides examples of relative path names and fully qualified path names. The
examples in the table are based on the current working directory being set to C:\Windows:

                                                                                   ﾉ   Expand table

 Symbol     Description                                   Relative path        Fully qualified path

 .          Current working location                      .\System             C:\Windows\System

 ..         Parent of the current working location        ..\Program Files     C:\Program Files

 \          Drive root of the current working location    \Program Files       C:\Program Files

 none       No special characters                         System               C:\Windows\System

To use a path name in a command, enter that name as a fully qualified or relative path name.

The following cmdlets deal with paths:

      Convert-Path: Converts a path from a PowerShell path to a PowerShell provider path
      Join-Path: Combines a path and a child path into a single path
      Resolve-Path: Resolves the wildcard characters in a path
      Split-Path: Returns the specified part of a path
      Test-Path: Determines whether the elements of a path exist or if a path is well formed

Some cmdlets (such as Add-Content and Copy-Item use file filters. A file filter is a mechanism
for specifying the criteria for selecting from a set of paths.

<!-- p.1186 -->

The object type that represents a resolved path is described in §4.5.5. Paths are often
manipulated as strings.

3.5 Scopes

3.5.1 Introduction
A name can denote a variable, a function, an alias, an environment variable, or a drive. The
same name may denote different items at different places in a script. For each different item
that a name denotes, that name is visible only within the region of script text called its scope.
Different items denoted by the same name either have different scopes, or are in different
name spaces.

Scopes may nest, in which case, an outer scope is referred to as a parent scope, and any nested
scopes are child scopes of that parent. The scope of a name is the scope in which it is defined
and all child scopes, unless it is made private. Within a child scope, a name defined there hides
any items defined with the same name in parent scopes.

Unless dot source notation (§3.5.5) is used, each of the following creates a new scope:

     A script file
     A script block
     A function or filter

Consider the following example:

 PowerShell

 # Start of script
 $x = 2; $y = 3
 Get-Power $x $y

 # Function defined in script
 function Get-Power([int]$x, [int]$y) {
     if ($y -gt 0) {
         return $x * (Get-Power $x (--$y))
     } else {
         return 1
     }
 }
 # End of script

The scope of the variables $x and $y created in the script is the body of that script, including
the function defined inside it. Function Get-Power defines two parameters with those same
names. As each function has its own scope, these variables are different from those defined in

<!-- p.1187 -->

the parent scope, and they hide those from the parent scope. The function scope is nested
inside the script scope.

Note that the function calls itself recursively. Each time it does so, it creates yet another nested
scope, each with its own variables $x and $y .

Here is a more complex example, which also shows nested scopes and reuse of names:

 PowerShell

 # start of script scope
 $x = 2              # top-level script-scope $x created
                     # $x is 2
 F1                  # create nested scope with call to function F1
                     # $x is 2
 F3                  # create nested scope with call to function F3
                     # $x is 2

 function F1 {             # start of function scope
                           # $x is 2
      $x = $true           # function-scope $x created
                           # $x is $true

      & {               # create nested scope with script block
                        # $x is $true
            $x = 12.345 # scriptblock-scope $x created
                        # $x is 12.345
      }                 # end of scriptblock scope, local $x goes away

                           # $x is $true
      F2                   # create nested scope with call to function F2
                           # $x is $true
 }                         # end of function scope, local $x goes away

 function F2 {             # start of function scope
                           # $x is $true
      $x = "red"           # function-scope $x created
                           # $x is "red"
 }                         # end of function scope, local $x goes away

 function F3 {             # start of function scope
                           # $x is 2
      if ($x -gt 0) {
                     # $x is 2
         $x = "green"
                     # $x is "green"
     }               # end of block, but not end of any scope
                     # $x is still "green"
 }                   # end of function scope, local $x goes away
 # end of script scope

<!-- p.1188 -->

3.5.2 Scope names and numbers
PowerShell supports the following scopes:

     Global: This is the top-most level scope. All automatic and preference variables are
     defined in this scope. The global scope is the parent scope of all other scopes, and all
     other scopes are child scopes of the global scope.

     Local: This is the current scope at any execution point within a script, script block, or
     function. Any scope can be the local scope.

     Script: This scope exists for each script file that is executed. The script scope is the parent
     scope of all scopes created from within it. A script block does not have its own script
     scope; instead, its script scope is that of its nearest ancestor script file. Although there is
     no such thing as module scope, script scope provides the equivalent.

Names can be declared private, in which case, they are not visible outside of their parent
scope, not even to child scopes. The concept of private is not a separate scope; it's an alias for
local scope with the addition of hiding the name if used as a writable location.

Scopes can be referred to by a number, which describes the relative position of one scope to
another. Scope 0 denotes the local scope, scope 1 denotes a 1-generation ancestor scope,
scope 2 denotes a 2-generation ancestor scope, and so on. (Scope numbers are used by
cmdlets that manipulate variables.)

3.5.3 Variable name scope
As shown by the following production, a variable name can be specified with any one of six
different scopes:

 Syntax

 variable-scope:
     Global:
     Local:
     Private:
     Script:
     Using:
     Workflow:
     variable-namespace

The scope is optional. The following table shows the meaning of each in all possible contexts. It
also shows the scope when no scope is specified explicitly:

<!-- p.1189 -->

                                                                                           ﾉ   Expand table

 Scope        Within a Script File             Within a Script Block            Within a Function
 Modifier

 Global       Global scope                     Global scope                     Global scope

 Script       Nearest ancestor script file's   Nearest ancestor script file's   Nearest ancestor script file's
              scope or Global if there is no   scope or Global if there is      scope or Global if there is
              nearest ancestor script file     no nearest ancestor script       no nearest ancestor script
                                               file                             file

 Private      Global/Script/Local scope        Local scope                      Local scope

 Local        Global/Script/Local scope        Local scope                      Local scope

 Using        Implementation defined           Implementation defined           Implementation defined

 Workflow     Implementation defined           Implementation defined           Implementation defined

 None         Global/Script/Local scope        Local scope                      Local scope

Variable scope information can also be specified when using the family of cmdlets listed in
(§3.1.5). In particular, refer to the parameter Scope , and the parameters Option Private and
Option AllScope for more information.

The Using: scope modifier is used to access variables defined in another scope while running
scripts via cmdlets like Start-Job , Invoke-Command , or within an inlinescript-statement. For
example:

 PowerShell

 $a = 42
 Invoke-Command --ComputerName RemoteServer { $Using:a } # returns 42
 workflow foo
 {
     $b = "Hello"
     inlinescript { $Using:b }
 }
 foo # returns "Hello"

The scope workflow is used with a parallel-statement or sequence-statement to access a
variable defined in the workflow.

3.5.4 Function name scope

<!-- p.1190 -->

A function name may also have one of the four different scopes, and the visibility of that name
is the same as for variables (§3.5.3).

3.5.5 Dot source notation
When a script file, script block, or function is executed from within another script file, script
block, or function, the executed script file creates a new nested scope. For example,

  PowerShell

  Script1.ps1
  & "Script1.ps1"
  & { ... }
  FunctionA

However, when dot source notation is used, no new scope is created before the command is
executed, so additions/changes it would have made to its own local scope are made to the
current scope instead. For example,

  PowerShell

  . Script2.ps1
  . "Script2.ps1"
  . { ... }
  . FunctionA

3.5.6 Modules
Just like a top-level script file is at the root of a hierarchical nested scope tree, so too is each
module (§3.14). However, by default, only those names exported by a module are available by
name from within the importing context. The Global parameter of the cmdlet Import-Module
allows exported names to have increased visibility.

3.6 ReadOnly and Constant Properties
Variables and aliases are described by objects that contain a number of properties. These
properties are set and manipulated by two families of cmdlets (§3.1.5, §3.1.1). One such
property is Options, which can be set to ReadOnly or Constant (using the Option parameter). A
variable or alias marked ReadOnly can be removed, and its properties can changed provided
the Force parameter is specified. However, a variable or alias marked Constant cannot be
removed nor have its properties changed.

<!-- p.1191 -->

3.7 Method overloads and call resolution

3.7.1 Introduction
As stated in §1, an external procedure made available by the execution environment (and
written in some language other than PowerShell) is called a method.

The name of a method along with the number and types of its parameters are collectively
called that method's signature. (Note that the signature does not include the method's return
type.) The execution environment may allow a type to have multiple methods with the same
name provided each has a different signature. When multiple versions of some method are
defined, that method is said to be overloaded. For example, the type Math (§4.3.8) contains a
set of methods called Abs , which computes the absolute value of a specified number, where
the specified number can have one of a number of types. The methods in that set have the
following signatures:

  PowerShell

  Abs(decimal)
  Abs(float)
  Abs(double)
  Abs(int)
  Abs(long)
  Abs(SByte)
  Abs(Int16)

In this case, all of the methods have the same number of arguments; their signatures differ by
argument type only.

Another example involves the type Array (§4.3.2), which contains a set of methods called Copy
that copies a range of elements from one array to another, starting at the beginning of each
array (by default) or at some designated element. The methods in that set have the following
signatures:

  PowerShell

  Copy(Array, Array, int)
  Copy(Array, Array, long)
  Copy(Array, int, Array, int, int)
  Copy(Array, long, Array, long, long)

In this case, the signatures differ by argument type and, in some cases, by argument number as
well.

<!-- p.1192 -->

In most calls to overloaded methods, the number and type of the arguments passed exactly
match one of the overloads, and the method selected is obvious. However, if that is not the
case, there needs to be a way to resolve which overloaded version to call, if any. For example,

  PowerShell

  [Math]::Abs([byte]10) # no overload takes type byte
  [array]::Copy($source, 3, $dest, 5L, 4) # both int and long indexes

Other examples include the type string (i.e.; System.String), which has numerous overloaded
methods.

Although PowerShell has rules for resolving method calls that do not match an overloaded
signature exactly, PowerShell does not itself provide a way to define overloaded methods.

  ７ Note

  Editor's Note: PowerShell 5.0 added the ability to define script-based classes. These classes
  can contain overloaded methods.

3.7.2 Method overload resolution
Given a method call (§7.1.3) having a list of argument expressions, and a set of candidate
methods (i.e., those methods that could be called), the mechanism for selecting the best
method is called overload resolution.

Given the set of applicable candidate methods (§3.7.3), the best method in that set is selected.
If the set contains only one method, then that method is the best method. Otherwise, the best
method is the one method that is better than all other methods with respect to the given
argument list using the rules shown in §3.7.4. If there is not exactly one method that is better
than all other methods, then the method invocation is ambiguous and an error is reported.

The best method must be accessible in the context in which it is called. For example, a
PowerShell script cannot call a method that is private or protected.

The best method for a call to a static method must be a static method, and the best method
for a call to an instance method must be an instance method.

3.7.3 Applicable method
A method is said to be applicable with respect to an argument list A when one of the following
is true:

<!-- p.1193 -->

     The number of arguments in A is identical to the number of parameters that the method
     accepts.
     The method has M required parameters and N optional parameters, and the number of
     arguments in A is greater than or equal to M, but less than N.
     The method accepts a variable number of arguments and the number of arguments in A
     is greater than the number of parameters that the method accepts.

In addition to having an appropriate number of arguments, each argument in A must match
the parameter-passing mode of the argument, and the argument type must match the
parameter type, or there must be a conversion from the argument type to the parameter type.

If the argument type is ref (§4.3.6), the corresponding parameter must also be ref, and the
argument type for conversion purposes is the type of the property Value from the ref
argument.

If the argument type is ref , the corresponding parameter could be out instead of ref .

If the method accepts a variable number of arguments, the method may be applicable in either
normal form or expanded form. If the number of arguments in A is identical to the number of
parameters that the method accepts and the last parameter is an array, then the form depends
on the rank of one of two possible conversions:

     The rank of the conversion from the type of the last argument in A to the array type for
     the last parameter.
     The rank of the conversion from the type of the last argument in A to the element type of
     the array type for the last parameter.

If the first conversion (to the array type) is better than the second conversion (to the element
type of the array), then the method is applicable in normal form, otherwise it is applicable in
expanded form.

If there are more arguments than parameters, the method may be applicable in expanded form
only. To be applicable in expanded form, the last parameter must have array type. The method
is replaced with an equivalent method that has the last parameter replaced with sufficient
parameters to account for each unmatched argument in A. Each additional parameter type is
the element type of the array type for the last parameter in the original method. The above
rules for an applicable method are applied to this new method and argument list A.

3.7.4 Better method
Given an argument list A with a set of argument expressions { E~1~, E~2~, ..., E~N~ } and
two application methods M~P~ and M~Q~ with parameter types { P~1~, P~2~, ..., P~N~ } and

<!-- p.1194 -->

{ Q~1~, Q~2~, ..., Q~N~ } , M~P~ is defined to be a better method than M~Q~ if the cumulative

ranking of conversions for M~P~ is better than that for M~Q~ .

The cumulative ranking of conversions is calculated as follows. Each conversion is worth a
different value depending on the number of parameters, with the conversion of E~1~ worth N,
E~2~ worth N-1, down to E~N~ worth 1. If the conversion from E~X~ to P~X~ is better than that

from E~X~ to Q~X~ , the M~P~ accumulates N-X+1; otherwise, M~Q~ accumulates N-X+1. If M~P~
and M~Q~ have the same value, then the following tie breaking rules are used, applied in order:

     The cumulative ranking of conversions between parameter types (ignoring argument
     types) is computed in a manner similar to the previous ranking, so P~1~ is compared
     against Q~1~ , P~2~ against Q~2~ , ..., and P~N~ against Q~N~ . The comparison is skipped if
     the argument was $null , or if the parameter types are not numeric types. The
     comparison is also skipped if the argument conversion E~X~ loses information when
     converted to P~X~ but does not lose information when converted to Q~X~ , or vice versa. If
     the parameter conversion types are compared, then if the conversion from P~X~ to Q~X~
     is better than that from Q~X~ to P~X~ , the M~P~ accumulates N-X+1; otherwise, M~Q~
     accumulates N-X+1. This tie breaking rule is intended to prefer the most specific method
     (i.e., the method with parameters having the smallest data types) if no information is lost
     in conversions, or to prefer the most general method (i.e., the method with the parameters
     with the largest data types) if conversions result in loss of information.
     If both methods use their expanded form, the method with more parameters is the better
     method.
     If one method uses the expanded form and the other uses normal form, the method
     using normal form is the better method.

3.7.5 Better conversion
The text below marked like this is specific to Windows PowerShell.

Conversions are ranked in the following manner, from lowest to highest:

      T~1~[] to T~2~[] where no assignable conversion between T~1~ and T~2~ exists

     T to string where T is any type
      T~1~ to T~2~ where T~1~ or T~2~ define a custom conversion in an implementation-

     defined manner
      T~1~ to T~2~ where T~1~ implements IConvertible
      T~1~ to T~2~ where T~1~ or T~2~ implements the method T~2~ op_Implicit(T1)

      T~1~ to T~2~ where T~1~ or T~2~ implements the method T~2~ op_Explicit(T1)

<!-- p.1195 -->

T~1~ to T~2~ where T~2~ implements a constructor taking a single argument of type
T~1~

Either of the following conversions:
  string to T where T implements a static method T Parse(string) or T Parse(string,
  IFormatProvider)

   T~1~ to T~2~ where T~2~ is any enum and T~1~ is either string or a collection of

  objects that can be converted to string
T to PSObject where T is any type

Any of the following conversions: Language
  T to bool where T is any numeric type
  string to T where T is regex , wmisearcher , wmi , wmiclass , adsi , adsisearcher , or
   type

   T to bool

  T~1~ to Nullable[T~2~] where a conversion from T~1~ to T~2~ exists
   T to void

   T~1~[] to T~2~[] where an assignable conversion between T~1~ and T~2~ exists
   T~1~ to T~2~[] where T~1~ is a collection

   IDictionary to Hashtable
   T to ref

   T to xml

   scriptblock to delegate
   T~1~ to T~2~ where T~1~ is an integer type and T~2~ is an enum

$null to T where T is any value type
$null to T where T is any reference type

Any of the following conversions:

  byte to T where T is SByte

   UInt16 to T where T is SByte , byte , or Int16

   Int16 to T where T is SByte or byte

   UInt32 to T where T is SByte , byte , Int16 , UInt16 , or int

   int to T where T is SByte , byte , Int16 , or UInt16

   UInt64 to T where T is SByte , byte , Int16 , UInt16 , int , UInt32 , or long

   long to T where T is SByte , byte , Int16 , UInt16 , int , or UInt32

   float to T where T is any integer type or decimal

<!-- p.1196 -->

        double to T where T is any integer type or decimal

        decimal to T where T is any integer type

     Any of the following conversions:
        SByte to T where T is byte , uint6 , UInt32 , or UInt64

        Int16 to T where T is UInt16 , UInt32 , or UInt64

        int to T where T is UInt32 or UInt64
        long to UInt64

        decimal to T where T is float or double

     Any of the following conversions:
        T to string where T is any numeric type

        T to char where T is any numeric type
        string to T where T is any numeric type

     Any of the following conversions, these conversion are considered an assignable
     conversions:
        byte to T where T is Int16 , UInt16 , int , UInt32 , long , UInt64 , single , double , or

        decimal
        SByte to T where T is Int16 , UInt16 , int , UInt32 , long , UInt64 , single , double , or

        decimal
        UInt16 to T where T is int , UInt32 , long , or UInt64 , single , double , or decimal

        Int16 to T where T is int , UInt32 , long , or UInt64 , single , double , or decimal

        UInt32 to T where T is long , or UInt64 , single , double , or decimal
        int to T where T is long , UInt64 , single , double , or decimal

        single to double
     T~1~ to T~2~ where T~2~ is a base class or interface of T~1~ . This conversion is

     considered an assignable conversion.
     string to char[]

     T to T -- This conversion is considered an assignable conversion.

For each conversion of the form T~1~ to T~2~[] where T~1~ is not an array and no other
conversion applies, if there is a conversion from T~1~ to T~2~ , the rank of the conversion is
worse than the conversion from T~1~ to T~2~ , but better than any conversion ranked less than
the conversion from T~1~ to T~2~

3.8 Name lookup
It is possible to have commands of different kinds all having the same name. The order in
which name lookup is performed in such a case is alias, function, cmdlet, and external
command.

<!-- p.1197 -->

3.9 Type name lookup
§7.1.10 contains the statement, "A type-literal is represented in an implementation by some
unspecified underlying type. As a result, a type name is a synonym for its underlying type."
Example of types are int , double , long[] , and Hashtable .

Type names are matched as follows: Compare a given type name with the list of built-in type
accelerators, such as int, long, double. If a match is found, that is the type. Otherwise, presume
the type name is fully qualified and see if such a type exists on the host system. If a match is
found, that is the type. Otherwise, add the namespace prefix System. . If a match is found, that
is the type. Otherwise, the type name is in error. This algorithm is applied for each type
argument for generic types. However, there is no need to specify the arity (the number of
arguments or operands taken by a function or operator).

3.10 Automatic memory management
Various operators and cmdlets result in the allocation of memory for reference-type objects,
such as strings and arrays. The allocation and freeing of this memory is managed by the
PowerShell runtime system. That is, PowerShell provides automatic garbage collection.

3.11 Execution order
A side effect is a change in the state of a command's execution environment. A change to the
value of a variable (via the assignment operators or the pre- and post-increment and
decrement operators) is a side effect, as is a change to the contents of a file.

Unless specified otherwise, statements are executed in lexical order.

Except as specified for some operators, the order of evaluation of terms in an expression and
the order in which side effects take place are both unspecified.

An expression that invokes a command involves the expression that designates the command,
and zero or more expressions that designate the arguments whose values are to be passed to
that command. The order in which these expressions are evaluated relative to each other is
unspecified.

3.12 Error handling
When a command fails, this is considered an error, and information about that error is recorded
in an error record, whose type is unspecified (§4.5.15); however, this type supports subscripting.

<!-- p.1198 -->

An error falls into one of two categories. Either it terminates the operation (a terminating error)
or it doesn't (a non-terminating error). With a terminating error, the error is recorded and the
operation stops. With a non-terminating error, the error is recorded and the operation
continues.

Non-terminating errors are written to the error stream. Although that information can be
redirected to a file, the error objects are first converted to strings and important information in
those objects would not be captured making diagnosis difficult if not impossible. Instead, the
error text can be redirected (§7.12) and the error object saved in a variable, as in $Error1 =
command 2>&1 .

The automatic variable $Error contains a collection of error records that represent recent
errors, and the most recent error is in $Error[0] . This collection is maintained in a buffer such
that old records are discarded as new ones are added. The automatic variable
$MaximumErrorCount controls the number of records that can be stored.

$Error contains all of the errors from all commands mixed in together in one collection. To

collect the errors from a specific command, use the common parameter ErrorVariable, which
allows a user-defined variable to be specified to hold the collection.

3.13 Pipelines
A pipeline is a series of one or more commands each separated by the pipe operator |
(U+007C). Each command receives input from its predecessor and writes output to its
successor. Unless the output at the end of the pipeline is discarded or redirected to a file, it is
sent to the host environment, which may choose to write it to standard output. Commands in a
pipeline may also receive input from arguments. For example, consider the following use of
commands Get-ChildItem , Sort-Object , and Process-File , which create a list of file names in
a given file system directory, sort a set of text records, and perform some processing on a text
record, respectively:

 PowerShell

 Get-ChildItem
 Get-ChildItem E:*.txt | Sort-Object -CaseSensitive | Process-File >results.txt

In the first case, Get-ChildItem creates a collection of names of the files in the current/default
directory. That collection is sent to the host environment, which, by default, writes each
element's value to standard output.

In the second case, Get-ChildItem creates a collection of names of the files in the directory
specified, using the argument E:*.txt . That collection is written to the command Sort-Object ,

<!-- p.1199 -->

which, by default, sorts them in ascending order, sensitive to case (by virtue of the
CaseSensitive argument). The resulting collection is then written to command Process-File ,
which performs some (unknown) processing. The output from that command is then redirected
to the file results.txt .

If a command writes a single object, its successor receives that object and then terminates after
writing its own object(s) to its successor. If, however, a command writes multiple objects, they
are delivered one at a time to the successor command, which executes once per object. This
behavior is called streaming. In stream processing, objects are written along the pipeline as
soon as they become available, not when the entire collection has been produced.

When processing a collection, a command can be written such that it can do special processing
before the initial element and after the final element.

3.14 Modules
A module is a self-contained reusable unit that allows PowerShell code to be partitioned,
organized, and abstracted. A module can contain commands (such as cmdlets and functions)
and items (such as variables and aliases) that can be used as a single unit.

Once a module has been created, it must be imported into a session before the commands and
items within it can be used. Once imported, commands and items behave as if they were
defined locally. A module is imported explicitly with the Import-Module command. A module
may also be imported automatically as determined in an implementation defined manner.

The type of an object that represents a module is described in §4.5.12.

Modules are discussed in detail in §11.

3.15 Wildcard expressions
A wildcard expression may contain zero or more of the following elements:

                                                                                     ﾉ   Expand table

 Element         Description

 Character       Matches that one character
 other than *,
 ?, or [

 *               Matches zero or more characters. To match a * character, use [*].

<!-- p.1200 -->

 Element            Description

 ?                  Matches any one character. To match a ? character, use [?].

 [set]              Matches any one character from set, which cannot be empty.

                    If set begins with ], that right square bracket is considered part of set and the next right
                    square bracket terminates the set; otherwise, the first right square bracket terminates the
                    set.

                    If set begins or ends with -, that hyphen-minus is considered part of set; otherwise, it
                    indicates a range of consecutive Unicode code points with the characters either side of
                    the hyphen-minus being the inclusive range delimiters. For example, A-Z indicates the 26
                    uppercase English letters, and 0-9 indicates the 10 decimal digits.

     ７ Note

     More information can be found in, The Open Group Base Specifications: Pattern
     Matching", IEEE Std 1003.1, 2004 Edition.          . However, in PowerShell, the escape character
     is backtick, not backslash.

3.16 Regular expressions
A regular expression may contain zero or more of the following elements:

                                                                                               ﾉ   Expand table

 Element             Description

 Character           Matches that one character
 other than ., [,
 ^, *, $, or \

 .                   Matches any one character. To match a . character, use \..

 [set]               The [set] form matches any one character from set. The [^set] form matches no
 [^set]              characters from set. set cannot be empty.

                     If set begins with ] or ^], that right square bracket is considered part of set and the next
                     right square bracket terminates the set; otherwise, the first right square bracket
                     terminates the set.

                     If set begins with - or ^-, or ends with -, that hyphen-minus is considered part of set;
                     otherwise, it indicates a range of consecutive Unicode code points with the characters
                     either side of the hyphen-minus being the inclusive range delimiters. For example, A-Z
                     indicates the 26 uppercase English letters, and 0-9 indicates the 10 decimal digits.
