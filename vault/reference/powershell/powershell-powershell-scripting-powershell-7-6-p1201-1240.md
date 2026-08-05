---
title: "How to use this documentation — pages 1201-1240"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1201-1240
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1201-1240
family: powershell
documentKind: "doc"
abstract: "Element Description * Matches zero of more occurrences of the preceding element. + Matches one of more occurrences of the preceding element. ? Matches zero of one occurrences of the preceding element. ^ Matches at the start of the string. To match a ^ character, use \\^. $ Matche"
---

# How to use this documentation — pages 1201-1240

<!-- p.1201 -->

 Element            Description

 *                  Matches zero of more occurrences of the preceding element.

 +                  Matches one of more occurrences of the preceding element.

 ?                  Matches zero of one occurrences of the preceding element.

 ^                  Matches at the start of the string. To match a ^ character, use \^.

 $                  Matches at the end of the string. To match a $ character, use $.

 \c                 Escapes character c, so it isn't recognized as a regular expression element.

     ７ Note

     More information can be found in, The Open Group Base Specifications: Regular
     Expressions, IEEE Std 1003.1, 2004 Edition.       .

Windows PowerShell: Character classes available in Microsoft .NET Framework regular
expressions are supported, as follows:

                                                                                            ﾉ      Expand table

 Element      Description

 \p{name}     Matches any character in the named character class specified by name. Supported names are
              Unicode groups and block ranges such as Ll, Nd, Z, IsGreek, and IsBoxDrawing.

 \P{name}     Matches text not included in the groups and block ranges specified in name.

 \w           Matches any word character. Equivalent to the Unicode character categories
              [\p{Ll}\p{Lu}\p{Lt}\p{Lo}\p{Nd}\p{Pc}] . If ECMAScript-compliant behavior is specified with
              the ECMAScript option, \w is equivalent to [a-zA-Z_0-9] .

 \W           Matches any non-word character. Equivalent to the Unicode categories
              [\^\p{Ll}\p{Lu}\p{Lt}\p{Lo}\p{Nd}\p{Pc}] .

 \s           Matches any white space character. Equivalent to the Unicode character categories
              [\f\n\r\t\v\x85\p{Z}] .

 \S           Matches any non-white-space character. Equivalent to the Unicode character categories
              [\^\f\n\r\t\v\x85\p{Z}] .

 \d           Matches any decimal digit. Equivalent to \p{Nd} for Unicode and [0-9] for non-Unicode
              behavior.

<!-- p.1202 -->

 Element     Description

 \D          Matches any non-digit. Equivalent to \P{Nd} for Unicode and [\^0-9] for non-Unicode
             behavior.

Quantifiers available in Microsoft .NET Framework regular expressions are supported, as
follows:

                                                                                          ﾉ   Expand table

 Element      Description

 *            Specifies zero or more matches; for example, \w* or (abc)*. Equivalent to {0,} .

 +            Matches repeating instances of the preceding characters.

 ?            Specifies zero or one matches; for example, \w? or (abc)? . Equivalent to {0,1} .

 {n}          Specifies exactly n matches; for example, (pizza){2} .

 {n,}         Specifies at least n matches; for example, (abc){2,} .

 {n,m}        Specifies at least n, but no more than m, matches.

 Last updated on 09/15/2023

<!-- p.1203 -->

4. Types

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

In PowerShell, each value has a type, and types fall into one of two main categories: value
types and reference types. Consider the type int , which is typical of value types. A value of
type int is completely self-contained; all the bits needed to represent that value are stored in
that value, and every bit pattern in that value represents a valid value for its type. Now,
consider the array type int[] , which is typical of reference types. A so-called value of an array
type can hold either a reference to an object that actually contains the array elements, or the
null reference whose value is $null . The important distinction between the two type
categories is best demonstrated by the differences in their semantics during assignment. For
example,

 PowerShell

 $i = 100 # $i designates an int value 100
 $j = $i # $j designates an int value 100, which is a copy

 $a = 10,20,30 # $a designates an object[], Length 3, value 10,20,30
 $b = $a # $b designates exactly the same array as does $a, not a copy
 $a[1] = 50 # element 1 (which has a value type) is changed from 20 to 50
 $b[1] # $b refers to the same array as $a, so $b[1] is 50

<!-- p.1204 -->

As we can see, the assignment of a reference type value involves a shallow copy; that is, a copy
of the reference to the object rather than its actual value. In contrast, a deep copy requires
making a copy of the object as well.

A numeric type is one that allows representation of integer or fractional values, and that
supports arithmetic operations on those values. The set of numerical types includes the integer
(§4.2.3) and real number (§4.2.4) types, but does not include bool (§4.2.1) or char (§4.2.2). An
implementation may provide other numeric types (such as signed byte, unsigned integer, and
integers of other sizes).

A collection is a group of one or more related items, which need not have the same type.
Examples of collection types are arrays, stacks, queues, lists, and hash tables. A program can
enumerate (or iterate) over the elements in a collection, getting access to each element one at
a time. Common ways to do this are with the foreach statement (§8.4.4) and the ForEach-
Object cmdlet. The type of an object that represents an enumerator is described in §4.5.16.

In this chapter, there are tables that list the accessible members for a given type. For methods,
the Type is written with the following form: returnType/argumentTypeList. If the argument type
list is too long to fit in that column, it is shown in the Purpose column instead.

Other integer types are SByte , Int16 , UInt16 , UInt32 , and UInt64 , all in the namespace
System.

Many collection classes are defined as part of the System.Collections or
System.Collections.Generic namespaces. Most collection classes implement the interfaces
ICollection , IComparer , IEnumerable , IList , IDictionary , and IDictionaryEnumerator and

their generic equivalents.

You can also use shorthand names for some types. For more information, see
about_Type_Accelerators.

4.1 Special types
4.1.1 The void type
This type cannot be instantiated. It provides a means to discard a value explicitly using the cast
operator (§7.2.9).

4.1.2 The null type

<!-- p.1205 -->

The null type has one instance, the automatic variable $null (§2.3.2.2), also known as the null
value. This value provides a means for expressing "nothingness" in reference contexts. The
characteristics of this type are unspecified.

4.1.3 The object type
Every type in PowerShell except the null type (§4.1.2) is derived directly or indirectly from the
type object, so object is the ultimate base type of all non-null types. A variable constrained
(§5.3) to type object is really not constrained at all, as it can contain a value of any type.

4.2 Value types
4.2.1 Boolean
The Boolean type is bool . There are only two values of this type, False and True, represented
by the automatic variables $false and $true , respectively (§2.3.2.2).

In PowerShell, bool maps to System.Boolean .

4.2.2 Character
A character value has type char, which is capable of storing any UTF-16-encoded 16-bit
Unicode code point.

The type char has the following accessible members:

                                                                                          ﾉ   Expand table

 Member            Member Kind              Type        Purpose

 MaxValue          Static property (read-   char        The largest possible value of type char
                   only)

 MinValue          Static property (read-   char        The smallest possible value of type char
                   only)

 IsControl         Static method            bool/char   Tests if the character is a control character

 IsDigit           Static method            bool/char   Tests if the character is a decimal digit

 IsLetter          Static method            bool/char   Tests if the character is an alphabetic letter

 IsLetterOrDigit   Static method            bool/char   Tests if the character is a decimal digit or
                                                        alphabetic letter

<!-- p.1206 -->

 Member            Member Kind                 Type          Purpose

 IsLower           Static method               bool/char     Tests if the character is a lowercase alphabetic
                                                             letter

 IsPunctuation     Static method               bool/char     Tests if the character is a punctuation mark

 IsUpper           Static method               bool/char     Tests if the character is an uppercase alphabetic
                                                             letter

 IsWhiteSpace      Static method               bool/char     Tests if the character is a white space character.

 ToLower           Static method               char/string   Converts the character to lowercase

 ToUpper           Static method               char/string   Converts the character to uppercase

Windows PowerShell: char maps to System.Char.

4.2.3 Integer
There are two signed integer types, both of use two's-complement representation for negative
values:

     Type int , which uses 32 bits giving it a range of -2147483648 to +2147483647, inclusive.
     Type long , which uses 64 bits giving it a range of -9223372036854775808 to
     +9223372036854775807, inclusive.

Type int has the following accessible members:

                                                                                              ﾉ    Expand table

 Member          Member Kind                          Type      Purpose

 MaxValue        Static property (read-only)          int       The largest possible value of type int

 MinValue        Static property (read-only)          int       The smallest possible value of type int

Type long has the following accessible members:

                                                                                              ﾉ    Expand table

 Member          Member Kind                          Type    Purpose

 MaxValue        Static property (read-only)          long    The largest possible value of type long

 MinValue        Static property (read-only)          long    The smallest possible value of type long

<!-- p.1207 -->

There is one unsigned integer type:

       Type byte , which uses 8 bits giving it a range of 0 to 255, inclusive.

Type byte has the following accessible members:

                                                                                               ﾉ   Expand table

 Member          Member Kind                         Type       Purpose

 MaxValue        Static property (read-only)         byte       The largest possible value of type byte

 MinValue        Static property (read-only)         byte       The smallest possible value of type byte

In PowerShell, byte , int , and long map to System.Byte , System.Int32 , and System.Int64 ,
respectively.

4.2.4 Real number
4.2.4.1 float and double

There are two real (or floating-point) types:

       Type float uses the 32-bit IEEE single-precision representation.
       Type double uses the 64-bit IEEE double-precision representation.

A third type name, single , is a synonym for type float ; float is used throughout this
specification.

Although the size and representation of the types float and double are defined by this
specification, an implementation may use extended precision for intermediate results.

Type float has the following accessible members:

                                                                                               ﾉ   Expand table

 Member                Member Kind                      Type       Purpose

 MaxValue              Static property (read-only)      float      The largest possible value of type float

 MinValue              Static property (read-only)      float      The smallest possible value of type float

 NaN                   Static property (read-only)      float      The constant value Not-a-Number

 NegativeInfinity      Static property (read-only)      float      The constant value negative infinity

<!-- p.1208 -->

 Member                Member Kind                         Type       Purpose

 PositiveInfinity      Static property (read-only)         float      The constant value positive infinity

Type double has the following accessible members:

                                                                                                  ﾉ   Expand table

 Member               Member Kind                       Type          Purpose

 MaxValue             Static property (read-only)       double        The largest possible value of type double

 MinValue             Static property (read-only)       double        The smallest possible value of type double

 NaN                  Static property (read-only)       double        The constant value Not-a-Number

 NegativeInfinity     Static property (read-only)       double        The constant value negative infinity

 PositiveInfinity     Static property (read-only)       double        The constant value positive infinity

In PowerShell, float and double map to System.Single and System.Double , respectively.

4.2.4.2 decimal

Type decimal uses a 128-bit representation. At a minimum it must support a scale s such that 0
<= s <= at least 28, and a value range -79228162514264337593543950335 to
79228162514264337593543950335. The actual representation of decimal is implementation
defined.

Type decimal has the following accessible members:

                                                                                                  ﾉ   Expand table

 Member         Member Kind                         Type           Purpose

 MaxValue       Static property (read-only)         decimal        The largest possible value of type decimal

 MinValue       Static property (read-only)         decimal        The smallest possible value of type decimal

  ７ Note

  Decimal real numbers have a characteristic called scale, which represents the number of
  digits to the right of the decimal point. For example, the value 2.340 has a scale of 3 where
  trailing zeros are significant. When two decimal real numbers are added or subtracted, the
  scale of the result is the larger of the two scales. For example, 1.0 + 2.000 is 3.000, while

<!-- p.1209 -->

  5.0 - 2.00 is 3.00. When two decimal real numbers are multiplied, the scale of the result is
  the sum of the two scales. For example, 1.0 * 2.000 is 2.0000. When two decimal real
  numbers are divided, the scale of the result is the scale of the first less the scale of the
  second. For example, 4.00000/2.000 is 2.00. However, a scale cannot be less than that
  needed to preserve the correct result. For example, 3.000/2.000, 3.00/2.000, 3.0/2.000, and
  3/2 are all 1.5.

In PowerShell, decimal maps to System.Decimal . The representation of decimal is as follows:

     When considered as an array of four int values it contains the following elements:
        Index 0 (bits 0‑31) contains the low-order 32 bits of the decimal's coefficient.
        Index 1 (bits 32‑63) contains the middle 32 bits of the decimal's coefficient.
        Index 2 (bits 64‑95) contains the high-order 32 bits of the decimal's coefficient.
        Index 3 (bits 96‑127) contains the sign bit and scale, as follows:
            bits 0--15 are zero
            bits 16‑23 contains the scale as a value 0--28
            bits 24‑30 are zero
            bit 31 is the sign (0 for positive, 1 for negative)

4.2.5 The switch type
This type is used to constrain the type of a parameter in a command (§8.10.5). If an argument
having the corresponding parameter name is present the parameter tests $true; otherwise, it
tests $false .

In PowerShell, switch maps to System.Management.Automation.SwitchParameter .

4.2.6 Enumeration types
An enumeration type is one that defines a set of named constants representing all the possible
values that can be assigned to an object of that enumeration type. In some cases, the set of
values are such that only one value can be represented at a time. In other cases, the set of
values are distinct powers of two, and by using the -bor operator (§7.8.5), multiple values can
be encoded in the same object.

The PowerShell environment provides a number of enumeration types, as described in the
following sections.

4.2.6.1 Action-Preference type

<!-- p.1210 -->

This implementation-defined type has the following mutually exclusive-valued accessible
members:

                                                                                        ﾉ   Expand table

 Member             Member Kind        Purpose

 Continue           Enumeration        The PowerShell runtime will continue processing and notify the
                    constant           user that an action has occurred.

 Inquire            Enumeration        The PowerShell runtime will stop processing and ask the user how
                    constant           it should proceed.

 SilentlyContinue   Enumeration        The PowerShell runtime will continue processing without notifying
                    constant           the user that an action has occurred.

 Stop               Enumeration        The PowerShell runtime will stop processing when an action
                    constant           occurs.

In PowerShell, this type is System.Management.Automation.ActionPreference .

4.2.6.2 Confirm-Impact type

This implementation-defined type has the following mutually exclusive-valued accessible
members:

                                                                                        ﾉ   Expand table

 Member     Member Kind           Purpose

 High       Enumeration           The action performed has a high risk of losing data, such as
            constant              reformatting a hard disk.

 Low        Enumeration           The action performed has a low risk of losing data.
            constant

 Medium     Enumeration           The action performed has a medium risk of losing data.
            constant

 None       Enumeration           Do not confirm any actions (suppress all requests for confirmation).
            constant

In PowerShell, this type is System.Management.Automation.ConfirmImpact .

4.2.6.3 File-Attributes type

<!-- p.1211 -->

This implementation-defined type has the following accessible members, which can be
combined:

                                                                                        ﾉ    Expand table

 Member              Member Kind   Purpose

 Archive             Enumeration   The file's archive status. Applications use this attribute to mark
                     constant      files for backup or removal.

 Compressed          Enumeration   The file is compressed.
                     constant

 Device                            Reserved for future use.

 Directory           Enumeration   The file is a directory.
                     constant

 Encrypted           Enumeration   The file or directory is encrypted. For a file, this means that all
                     constant      data in the file is encrypted. For a directory, this means that
                                   encryption is the default for newly created files and directories.

 Hidden              Enumeration   The file is hidden, and thus is not included in an ordinary
                     constant      directory listing.

 Normal              Enumeration   The file is normal and has no other attributes set. This attribute is
                     constant      valid only if used alone.

 NotContentIndexed   Enumeration   The file will not be indexed by the operating system's content
                     constant      indexing service.

 Offline             Enumeration   The file is offline. The data of the file is not immediately available.
                     constant

 ReadOnly            Enumeration   The file is read-only.
                     constant

 ReparsePoint        Enumeration   The file contains a reparse point, which is a block of user-defined
                     constant      data associated with a file or a directory.

 SparseFile          Enumeration   The file is a sparse file. Sparse files are typically large files whose
                     constant      data are mostly zeros.

 System              Enumeration   The file is a system file. The file is part of the operating system or
                     constant      is used exclusively by the operating system.

 Temporary           Enumeration   The file is temporary. File systems attempt to keep all of the data
                     constant      in memory for quicker access rather than flushing the data back
                                   to mass storage. A temporary file should be deleted by the
                                   application as soon as it is no longer needed.

<!-- p.1212 -->

In PowerShell, this type is System.IO.FileAttributes with attribute FlagsAttribute.

4.2.6.4 Regular-Expression-Option type

This implementation-defined type has the following accessible members, which can be
combined:

                                                                                       ﾉ   Expand table

 Member            Member Kind               Purpose

 IgnoreCase        Enumeration constant      Specifies that the matching is case-insensitive.

 None              Enumeration constant      Specifies that no options are set.

An implementation may provide other values.

In PowerShell, this type is System.Text.RegularExpressions.RegexOptions with attribute
FlagsAttribute . The following extra values are defined: Compiled , CultureInvariant ,

ECMAScript , ExplicitCapture , IgnorePatternWhitespace , Multiline , RightToLeft , Singleline .

4.3 Reference types
4.3.1 Strings
A string value has type string and is an immutable sequence of zero or more characters of type
char each containing a UTF-16-encoded 16-bit Unicode code point.

Type string has the following accessible members:

                                                                                       ﾉ   Expand table

 Member       Member Kind       Type         Purpose

 Length       Instance          int (read-   Gets the number of characters in the string
              Property          only)

 ToLower      Instance Method   string       Creates a new string that contains the lowercase
                                             equivalent

 ToUpper      Instance Method   string       Creates a new string that contains the uppercase
                                             equivalent

In PowerShell, string maps to System.String .

<!-- p.1213 -->

4.3.2 Arrays
All array types are derived from the type array . This type has the following accessible
members:

                                                                                       ﾉ   Expand table

 Member      Member        Type        Purpose
             Kind

 Length      Instance      int         Number of elements in the array
             Property
             (read-only)

 Rank        Instance      int         Number of dimensions in the array
             Property
             (read-only)

 Copy        Static        void/see    Copies a range of elements from one array to another. There
             Method        Purpose     are four versions, where source is the source array, destination is
                           column      the destination array, count is the number of elements to copy,
                                       and sourceIndex and destinationIndex are the starting locations
                                       in their respective arrays:

                                       Copy(source, destination, int count)
                                       Copy(source, destination, long count)
                                       Copy(source, sourceIndex, destination, destinationIndex, int
                                       count)
                                       Copy(source, sourceIndex, destination, destinationIndex, long
                                       count)

 GetLength   Instance      int/none    Number of elements in a given dimension
             Method
             (read-only)               GetLength(int dimension)

For more details on arrays, see §9.

In PowerShell, array maps to System.Array .

4.3.3 Hashtables
Type Hashtable has the following accessible members:

                                                                                       ﾉ   Expand table

<!-- p.1214 -->

 Member      Member Kind    Type                    Purpose

 Count       Instance       int                     Gets the number of key/value pairs in the
             Property                               Hashtable

 Keys        Instance       Implementation-         Gets a collection of all the keys
             Property       defined

 Values      Instance       Implementation-         Gets a collection of all the values
             Property       defined

 Remove      Instance       void/none               Removes the designated key/value
             Method

For more details on Hashtables, see §10.

In PowerShell, Hashtable maps to System.Collections.Hashtable . Hashtable elements are
stored in an object of type DictionaryEntry , and the collections returned by Keys and Values
have type ICollection .

4.3.4 The xml type
Type xml implements the W3C Document Object Model (DOM) Level 1 Core and the Core
DOM Level 2. The DOM is an in-memory (cache) tree representation of an XML document and
enables the navigation and editing of this document. This type supports the subscript operator
[] (§7.1.4.4).

In PowerShell, xml maps to System.Xml.XmlDocument .

4.3.5 The regex type
Type regex provides machinery for supporting regular expression processing. It is used to
constrain the type of a parameter (§5.3) whose corresponding argument might contain a
regular expression.

In PowerShell, regex maps to System.Text.RegularExpressions.Regex .

4.3.6 The ref type
Ordinarily, arguments are passed to commands by value. In the case of an argument having
some value type a copy of the value is passed. In the case of an argument having some
reference type a copy of the reference is passed.

<!-- p.1215 -->

Type ref provides machinery to allow arguments to be passed to commands by reference, so
the commands can modify the argument's value. Type ref has the following accessible
members:

                                                                                  ﾉ   Expand table

 Member    Member Kind                Type                          Purpose

 Value     Instance property (read-   The type of the value being   Gets/sets the value being
           write)                     referenced.                   referenced.

Consider the following function definition and call:

 PowerShell

 function Doubler {
     param ([ref]$x) # parameter received by reference
     $x.Value *= 2.0 # note that 2.0 has type double
 }

 $number = 8 # designates a value of type int, value 8
 Doubler([ref]$number) # argument received by reference
 $number # designates a value of type double, value 8.0

Consider the case in which $number is type-constrained:

 PowerShell

 [int]$number = 8 # designates a value of type int, value 8
 Doubler([ref]$number) # argument received by reference
 $number # designates a value of type int, value 8

As shown, both the argument and its corresponding parameter must be declared ref .

In PowerShell, ref maps to System.Management.Automation.PSReference .

4.3.7 The scriptblock type
Type scriptblock represents a precompiled block of script text (§7.1.8) that can be used as a
single unit. It has the following accessible members:

                                                                                  ﾉ   Expand table

<!-- p.1216 -->

 Member               Member Kind       Type                     Purpose

 Attributes           Instance          Collection of            Gets the attributes of the script block.
                      property          attributes
                      (read-only)

 File                 Instance          string                   Gets the name of the file in which the script
                      property                                   block is defined.
                      (read-only)

 Module               Instance          implementation           Gets information about the module in
                      property          defined ([§4.5.12]       which the script block is defined.
                      (read-only)       [§4.5.12])

 GetNewClosure        Instance          scriptblock              Retrieves a script block that is bound to a
                      method            /none                    module. Any local variables that are in the
                                                                 context of the caller will be copied into the
                                                                 module.

 Invoke               Instance          Collection of            Invokes the script block with the specified
                      method            object/object[]          arguments and returns the results.

 InvokeReturnAsIs     Instance          object/object[]          Invokes the script block with the specified
                      method                                     arguments and returns any objects
                                                                 generated.

 Create               Static method     scriptblock              Creates a new scriptblock object that
                                        /string                  contains the specified script.

In PowerShell, scriptblock maps to System.Management.Automation.ScriptBlock . Invoke
returns a collection of PSObject .

4.3.8 The math type
Type math provides access to some constants and methods useful in mathematical
computations. It has the following accessible members:

                                                                                             ﾉ    Expand table

 Member       Member Kind        Type                        Purpose

 E            Static property    double                      Natural logarithmic base
              (read-only)

 PI           Static property    double                      Ratio of the circumference of a circle to its
              (read-only)                                    diameter

 Abs          Static method      numeric/numeric             Absolute value (the return type is the same as

<!-- p.1217 -->

Member    Member Kind     Type                      Purpose

                                                    the type of the argument passed in)

Acos      Static method   double / double           Angle whose cosine is the specified number

Asin      Static method   double / double           Angle whose sine is the specified number

Atan      Static method   double / double           Angle whose tangent is the specified number

Atan2     Static method   double / double y,        Angle whose tangent is the quotient of two
                          double x                  specified numbers x and y

Ceiling   Static method   decimal / decimal         smallest integer greater than or equal to the
                                                    specified number
                          double / double

Cos       Static method   double / double           Cosine of the specified angle

Cosh      Static method   double / double           Hyperbolic cosine of the specified angle

Exp       Static method   double / double           e raised to the specified power

Floor     Static method   decimal / decimal         Largest integer less than or equal to the
                                                    specified number
                          double / double

Log       Static method   double / double number    Logarithm of number using base e or base base

                          double / double number,
                          double base

Log10     Static method   double / double           Base-10 logarithm of a specified number

Max       Static method   numeric/numeric           Larger of two specified numbers (the return
                                                    type is the same as the type of the arguments
                                                    passed in)

Min       Static method   numeric/numeric,          Smaller of two specified numbers (the return
                          numeric                   type is the same as the type of the arguments
                                                    passed in)

Pow       Static method   double / double x,        A specified number x raised to the specified
                          double y                  power y

Sin       Static method   double / double           Sine of the specified angle

Sinh      Static method   double / double           Hyperbolic sine of the specified angle

Sqrt      Static method   double / double           Square root of a specified number

Tan       Static method   double / double           Tangent of the specified angle

Tanh      Static method   double / double           Hyperbolic tangent of the specified angle

<!-- p.1218 -->

In PowerShell, Math maps to System.Math .

4.3.9 The ordered type
Type ordered is a pseudo type used only for conversions.

4.3.10 The pscustomobject type
Type pscustomobject is a pseudo type used only for conversions.

4.4 Generic types
A number of programming languages and environments provide types that can be specialized.
Many of these types are referred to as container types, as instances of them are able to contain
objects of some other type. Consider a type called Stack that can represent a stack of values,
which can be pushed on and popped off. Typically, the user of a stack wants to store only one
kind of object on that stack. However, if the language or environment does not support type
specialization, multiple distinct variants of the type Stack must be implemented even though
they all perform the same task, just with different type elements.

Type specialization allows a generic type to be implemented such that it can be constrained to
handling some subset of types when it is used. For example,

     A generic stack type that is specialized to hold strings might be written as Stack[string] .
     A generic dictionary type that is specialized to hold int keys with associated string values
     might be written as Dictionary[int,string] .
     A stack of stack of strings might be written as Stack[Stack[string]] .

Although PowerShell does not define any built-in generic types, it can use such types if they
are provided by the host environment. See the syntax in §7.1.10.

The complete name for the type Stack[string] suggested above is
System.Collections.Generic.Stack[string] . The complete name for the type

Dictionary[int,string] suggested above is

System.Collections.Generic.Dictionary[int,string] .

4.5 Anonymous types
In some circumstances, an implementation of PowerShell creates objects of some type, and
those objects have members accessible to script. However, the actual name of those types

<!-- p.1219 -->

need not be specified, so long as the accessible members are specified sufficiently for them to
be used. That is, scripts can save objects of those types and access their members without
actually knowing those types' names. The following subsections specify these types.

4.5.1 Provider description type
This type encapsulates the state of a provider. It has the following accessible members:

                                                                                           ﾉ   Expand table

 Member    Member Kind                 Type                             Purpose

 Drives    Instance property (read-    Implementation defined           A collection of drive description
           only)                       (§4.5.2)                         objects

 Name      Instance property (read-    string                           The name of the provider
           only)

In PowerShell, this type is System.Management.Automation.ProviderInfo .

4.5.2 Drive description type
This type encapsulates the state of a drive. It has the following accessible members:

                                                                                           ﾉ   Expand table

 Member            Member Kind                     Type     Purpose

 CurrentLocation   Instance property (read-        string   The current working location (§3.1.4) of the
                   write)                                   drive

 Description       Instance property (read-        string   The description of the drive
                   write)

 Name              Instance property (read-only)   string   The name of the drive

 Root              Instance property (read-only)   string   The name of the drive

In PowerShell, this type is System.Management.Automation.PSDriveInfo .

4.5.3 Variable description type
This type encapsulates the state of a variable. It has the following accessible members:

                                                                                           ﾉ   Expand table

<!-- p.1220 -->

 Member        Member Kind        Type                   Purpose

 Attributes    Instance           Implementation         A collection of attributes
               property           defined
               (read-only)

 Description   Instance           string                 The description assigned to the variable via the
               property                                  New-Variable or Set-Variable cmdlets.
               (read-write)

 Module        Instance           Implementation         The module from which this variable was
               property           defined (§4.5.12)      exported
               (read-only)

 ModuleName    Instance           string                 The module in which this variable was defined
               property
               (read-only)

 Name          Instance           string                 The name assigned to the variable when it was
               property                                  created in the PowerShell language or via the
               (read-only)                               New-Variable and Set-Variable cmdlets.

 Options       Instance           string                 The options assigned to the variable via the
               property                                  New-Variable and Set-Variable cmdlets.
               (read-write)

 Value         Instance           object                 The value assigned to the variable when it was
               property                                  assigned in the PowerShell language or via the
               (read-write)                              New-Variable and Set-Variable cmdlets.

In PowerShell, this type is System.Management.Automation.PSVariable .

Windows PowerShell: The type of the attribute collection is
System.Management.Automation.PSVariableAttributeCollection.

4.5.4 Alias description type
This type encapsulates the state of an alias. It has the following accessible members:

                                                                                        ﾉ   Expand table

 Member                Member Kind          Type                   Purpose

 CommandType           Instance             Implementation         Should compare equal with "Alias".
                       property (read-      defined
                       only)

 Definition            Instance             string                 The command or alias to which the
                       property (read-                             alias was assigned via the New-Alias or

<!-- p.1221 -->

 Member               Member Kind       Type                 Purpose

                      only)                                  Set-Alias cmdlets.

 Description          Instance          string               The description assigned to the alias
                      property (read-                        via the New-Alias or Set-Alias
                      write)                                 cmdlets.

 Module               Instance          Implementation       The module from which this alias was
                      property (read-   defined (§4.5.12)    exported
                      only)

 ModuleName           Instance          string               The module in which this alias was
                      property (read-                        defined
                      only)

 Name                 Instance          string               The name assigned to the alias when it
                      property (read-                        was created via the New-Alias or Set-
                      only)                                  Alias cmdlets.

 Options              Instance          string               The options assigned to the alias via
                      property (read-                        the New-Alias New-Alias or Set-Alias
                      write)                                 cmdlets.

 OutputType           Instance          Implementation       Specifies the types of the values
                      property (read-   defined collection   output by the command to which the
                      only)                                  alias refers.

 Parameters           Instance          Implementation       The parameters of the command.
                      property (read-   defined collection
                      only)

 ParameterSets        Instance          Implementation       Information about the parameter sets
                      property (read-   defined collection   associated with the command.
                      only)

 ReferencedCommand    Instance          Implementation       Information about the command that
                      property (read-   defined              is immediately referenced by this alias.
                      only)

 ResolvedCommand      Instance          Implementation       Information about the command to
                      property (read-   defined              which the alias eventually resolves.
                      only)

In PowerShell, this type is System.Management.Automation.AliasInfo .

4.5.5 Working location description type
This type encapsulates the state of a working location. It has the following accessible members:

<!-- p.1222 -->

                                                                                             ﾉ   Expand table

 Member           Member Kind                    Type                             Purpose

 Drive            Instance property (read-       Implementation defined           A drive description object
                  only)                          (§4.5.2)

 Path             Instance property (read-       string                           The working location
                  only)

 Provider         Instance property (read-       Implementation defined           The provider
                  only)                          (§4.5.1)

 ProviderPath     Instance property (read-       string                           The current path of the
                  only)                                                           provider

A stack of working locations is a collection of working location objects, as described above.

In PowerShell, a current working location is represented by an object of type
System.Management.Automation.PathInfo . A stack of working locations is represented by an

object of type System.Management.Automation.PathInfoStack , which is a collection of PathInfo
objects.

4.5.6 Environment variable description type
This type encapsulates the state of an environment variable. It has the following accessible
members:

                                                                                             ﾉ   Expand table

 Member         Member Kind                               Type     Purpose

 Name           Instance property (read-write)            string   The name of the environment variable

 Value          Instance property (read-write)            string   The value of the environment variable

In PowerShell, this type is System.Collections.DictionaryEntry . The name of the variable is the
dictionary key. The value of the environment variable is the dictionary value. Name is an
AliasProperty that equates to Key.

4.5.7 Application description type
This type encapsulates the state of an application. It has the following accessible members:

<!-- p.1223 -->

                                                                                       ﾉ   Expand table

 Member          Member Kind         Type                       Purpose

 CommandType     Instance property   Implementation defined     Should compare equal with
                 (read-only)                                    "Application".

 Definition      Instance property   string                     A description of the application.
                 (read-only)

 Extension       Instance property   string                     The extension of the application file.
                 (read-write)

 Module          Instance property   Implementation defined     The module that defines this
                 (read-only)         (§4.5.12)                  command.

 ModuleName      Instance property   string                     The name of the module that defines
                 (read-only)                                    the command.

 Name            Instance property   string                     The name of the command.
                 (read-only)

 OutputType      Instance property   Implementation defined     Specifies the types of the values output
                 (read-only)         collection                 by the command.

 Parameters      Instance property   Implementation defined     The parameters of the command.
                 (read-only)         collection

 ParameterSets   Instance property   Implementation defined     Information about the parameter sets
                 (read-only)         collection                 associated with the command.

 Path            Instance property   string                     Gets the path of the application file.
                 (read-only)

In PowerShell, this type is System.Management.Automation.ApplicationInfo .

4.5.8 Cmdlet description type
This type encapsulates the state of a cmdlet. It has the following accessible members:

                                                                                       ﾉ   Expand table

 Member               Member Kind    Type                     Purpose

 CommandType          Instance       Implementation           Should compare equal with "Cmdlet".
                      property       defined
                      (read-only)

<!-- p.1224 -->

Member                Member Kind    Type                 Purpose

DefaultParameterSet   Instance       Implementation       The default parameter set that is used if
                      property       defined              PowerShell cannot determine which
                      (read-only)                         parameter set to use based on the
                                                          supplied arguments.

Definition            Instance       string               A description of the cmdlet.
                      property
                      (read-only)

HelpFile              Instance       string               The path to the Help file for the cmdlet.
                      property
                      (read-write)

ImplementingType      Instance       Implementation       The type that implements the cmdlet.
                      property       defined
                      (read-write)

Module                Instance       Implementation       The module that defines this cmdlet.
                      property       defined (§4.5.12)
                      (read-only)

ModuleName            Instance       string               The name of the module that defines the
                      property                            cmdlet.
                      (read-only)

Name                  Instance       string               The name of the cmdlet.
                      property
                      (read-only)

Noun                  Instance       string               The noun name of the cmdlet.
                      property
                      (read-only)

OutputType            Instance       Implementation       Specifies the types of the values output by
                      property       defined collection   the cmdlet.
                      (read-only)

Parameters            Instance       Implementation       The parameters of the cmdlet.
                      property       defined collection
                      (read-only)

ParameterSets         Instance       Implementation       Information about the parameter sets
                      property       defined collection   associated with the cmdlet.
                      (read-only)

Verb                  Instance       string               The verb name of the cmdlet.
                      property
                      (read-only)

<!-- p.1225 -->

 Member                Member Kind    Type                 Purpose

 PSSnapIn              Instance       Implementation       Windows PowerShell: Information about
                       property       defined              the Windows PowerShell snap-in that is
                       (read-only)                         used to register the cmdlet.

In PowerShell, this type is System.Management.Automation.CmdletInfo .

4.5.9 External script description type
This type encapsulates the state of an external script (one that is directly executable by
PowerShell, but is not built-in). It has the following accessible members:

                                                                                     ﾉ     Expand table

 Member             Member Kind       Type                   Purpose

 CommandType        Instance          Implementation         Should compare equal with
                    property (read-   defined                "ExternalScript".
                    only)

 Definition         Instance          string                 A definition of the script.
                    property (read-
                    only)

 Module             Instance          Implementation         The module that defines this script.
                    property (read-   defined (§4.5.12)
                    only)

 ModuleName         Instance          string                 The name of the module that defines
                    property (read-                          the script.
                    only)

 Name               Instance          string                 The name of the script.
                    property (read-
                    only)

 OriginalEncoding   Instance          Implementation         The original encoding used to convert
                    property (read-   defined                the characters of the script to bytes.
                    only)

 OutputType         Instance          Implementation         Specifies the types of the values output
                    property (read-   defined collection     by the script.
                    only)

 Parameters         Instance          Implementation         The parameters of the script.
                    property (read-   defined collection
                    only)

<!-- p.1226 -->

 Member            Member Kind          Type                       Purpose

 ParameterSets     Instance             Implementation             Information about the parameter sets
                   property (read-      defined collection         associated with the script.
                   only)

 Path              Instance             string                     The path to the script file.
                   property (read-
                   only)

 ScriptBlock       Instance             scriptblock                The external script.
                   property (read-
                   only)

 ScriptContents    Instance             string                     The original contents of the script.
                   property (read-
                   only)

In PowerShell, this type is System.Management.Automation.ExternalScriptInfo .

4.5.10 Function description type
This type encapsulates the state of a function. It has the following accessible members:

                                                                                           ﾉ      Expand table

 Member                Member        Type                Purpose
                       Kind

 CmdletBinding         Instance      bool                Indicates whether the function uses the same
                       property                          parameter binding that compiled cmdlets use
                       (read-                            (see §12.3.5).
                       only)

 CommandType           Instance      Implementation      Can be compared for equality with "Function" or
                       property      defined             "Filter" to see which of those this object
                       (read-                            represents.
                       only)

 DefaultParameterSet   Instance      string              Specifies the parameter set to use if that cannot
                       property                          be determined from the arguments (see §12.3.5).
                       (read-
                       only)

 Definition            Instance      string              A string version of ScriptBlock
                       property
                       (read-
                       only)

<!-- p.1227 -->

Member          Member     Type                Purpose
                Kind

Description     Instance   string              The description of the function.
                property
                (read-
                write)

Module          Instance   Implementation      The module from which this function was
                property   defined (§4.5.12)   exported
                (read-
                only)

ModuleName      Instance   string              The module in which this function was defined
                property
                (read-
                only)

Name            Instance   string              The name of the function
                property
                (read-
                only)

Options         Instance   Implementation      The scope options for the function (§3.5.4).
                property   defined
                (read-
                write)

OutputType      Instance   Implementation      Specifies the types of the values output, in order
                property   defined             (see §12.3.6).
                (read-     collection
                only)

Parameters      Instance   Implementation      Specifies the parameter names, in order. If the
                property   defined             function acts like a cmdlet (see CmdletBinding
                (read-     collection          above) the common parameters are included at
                only)                          the end of the collection.

ParameterSets   Instance   Implementation      Information about the parameter sets associated
                property   defined             with the command. For each parameter, the
                (read-     collection          result shows the parameter name and type, and
                only)                          indicates if the parameter is mandatory, by
                                               position or a [switch] parameter. If the function
                                               acts like a cmdlet (see CmdletBinding above) the
                                               common parameters are included at the end of
                                               the collection.

ScriptBlock     Instance   scriptblock         The body of the function
                property   (§4.3.6)

<!-- p.1228 -->

 Member               Member       Type                Purpose
                      Kind

                      (read-
                      only)

In PowerShell, this type is System.Management.Automation.FunctionInfo .

      CommandType has type System.Management.Automation.CommandTypes .

      Options has type System.Management.Automation.ScopedItemOptions .

      OutputType has type

      System.Collections.ObjectModel.ReadOnlyCollection``1[[System.Management.Automation.P

     STypeName,System.Management.Automation]] .

      Parameters has type

      System.Collections.Generic.Dictionary``2[[System.String,mscorlib],

     [System.Management.Automation.ParameterMetadata,System.Management.Automation]] .

      ParameterSets has type

      System.Collections.ObjectModel.ReadOnlyCollection``1[[System.Management.Automation.C

     ommandParameterSetInfo,System.Management.Automation]] .

     Visibility has type System.Management.Automation.SessionStateEntryVisibility .
     PowerShell also has a property called Visibility.

4.5.11 Filter description type
This type encapsulates the state of a filter. It has the same set of accessible members as the
function description type (§4.5.10).

In PowerShell, this type is System.Management.Automation.FilterInfo . It has the same set of
properties as System.Management.Automation.FunctionInfo (§4.5.11).

4.5.12 Module description type
This type encapsulates the state of a module. It has the following accessible members:

                                                                                      ﾉ   Expand table

 Member        Member Kind                Type                   Purpose

 Description   Instance property          string                 The description of the module (set by
               (read-write)                                      the manifest)

 ModuleType    Instance property          Implementation         The type of the module (Manifest,

<!-- p.1229 -->

 Member          Member Kind               Type                  Purpose

                 (read-only)               defined               Script, or Binary)

 Name            Instance property         string                The name of the module
                 (read-only)

 Path            Instance property         string                The module's path
                 (read-only)

In PowerShell, this type is System.Management.Automation.PSModuleInfo . The type of ModuleType
is System.Management.Automation.ModuleType .

4.5.13 Custom object description type
This type encapsulates the state of a custom object. It has no accessible members.

In PowerShell, this type is System.Management.Automation.PSCustomObject . The cmdlets Import-
Module and New-Object can generate an object of this type.

4.5.14 Command description type
The automatic variable $PSCmdlet is an object that represents the cmdlet or function being
executed. The type of this object is implementation defined; it has the following accessible
members:

                                                                                      ﾉ   Expand table

 Member                Member Kind           Type         Purpose

 ParameterSetName      Instance property     string       Name of the current parameter set (see
                       (read-only)                        ParameterSetName)

 ShouldContinue        Instance method       Overloaded   Requests confirmation of an operation from
                                                          the user.
                                             /bool

 ShouldProcess         Instance method       Overloaded   Requests confirmation from the user before an
                                                          operation is performed.
                                             /bool

In PowerShell, this type is System.Management.Automation.PSScriptCmdlet.

4.5.15 Error record description type

<!-- p.1230 -->

The automatic variable $Error contains a collection of error records that represent recent
errors (§3.12). Although the type of this collection is unspecified, it does support subscripting
to get access to individual error records.

In PowerShell, the collection type is System.Collections.ArrayList . The type of an individual
error record in the collection is System.Management.Automation.ErrorRecord . This type has the
following public properties:

     CategoryInfo - Gets information about the category of the error.
     ErrorDetails - Gets and sets more detailed error information, such as a replacement error
     message.
     Exception - Gets the exception that is associated with this error record.
     FullyQualifiedErrorId - Gets the fully qualified error identifier for this error record.
     InvocationInfo - Gets information about the command that was invoked when the error
     occurred.
     PipelineIterationInfo - Gets the status of the pipeline when this error record was created
     TargetObject - Gets the object that was being processed when the error occurred.

4.5.16 Enumerator description type
A number of variables are enumerators for collections (§4). The automatic variable $foreach is
the enumerator created for any foreach statement. The automatic variable $input is the
enumerator for a collection delivered to a function from the pipeline. The automatic variable
$switch is the enumerator created for any switch statement.

The type of an enumerator is implementation defined; it has the following accessible members:

                                                                                       ﾉ   Expand table

 Member      Member         Type         Purpose
             Kind

 Current     Instance       object       Gets the current element in the collection. If the enumerator is
             property                    not currently positioned at an element of the collection, the
             (read-only)                 behavior is implementation defined.

 MoveNext    Instance       None/bool    Advances the enumerator to the next element of the
             method                      collection. Returns $true if the enumerator was successfully
                                         advanced to the next element; $false if the enumerator has
                                         passed the end of the collection.

<!-- p.1231 -->

In PowerShell, these members are defined in the interface System.IEnumerator , which is
implemented by the types identified below. If the enumerator is not currently positioned at an
element of the collection, an exception of type InvalidOperationException is raised. For
$foreach , this type is System.Array+SZArrayEnumerator . For $input , this type is

System.Collections.ArrayList+ArrayListEnumeratorSimple . For $switch , this type is

System.Array+SZArrayEnumerator .

4.5.17 Directory description type
The cmdlet New-Item can create items of various kinds including FileSystem directories. The
type of a directory description object is implementation defined; it has the following accessible
members:

                                                                                     ﾉ   Expand table

 Member          Member Kind         Type                     Purpose

 Attributes      Instance property   Implementation defined   Gets or sets one or more of the
                 (read-write)        (§4.2.6.3)               attributes of the directory object.

 CreationTime    Instance property   Implementation defined   Gets and sets the creation time of the
                 (read-write)        (§4.5.19)                directory object.

 Extension       Instance property   string                   Gets the extension part of the
                 (read- only)                                 directory name.

 FullName        Instance property   string                   Gets the full path of the directory.
                 (read-only)

 LastWriteTime   Instance property   Implementation defined   Gets and sets the time when the
                 (read-write)        (§4.5.19)                directory was last written to.

 Name            Instance property   string                   Gets the name of the directory.
                 (read- only)

In PowerShell, this type is System.IO.DirectoryInfo . The type of the Attributes property is
System.IO.FileAttributes .

4.5.18 File description type
The cmdlet New-Item can create items of various kinds including FileSystem files. The type of a
file description object is implementation defined; it has the following accessible members:

                                                                                     ﾉ   Expand table

<!-- p.1232 -->

 Member          Member         Type                 Purpose
                 Kind

 Attributes      Instance       Implementation       Gets or sets one or more of the attributes of the
                 property       defined (§4.2.6.3)   file object.
                 (read-write)

 BaseName        Instance       string               Gets the name of the file excluding the extension.
                 property
                 (read- only)

 CreationTime    Instance       Implementation       Gets and sets the creation time of the file object.
                 property       defined (§4.5.19)
                 (read-write)

 Extension       Instance       string               Gets the extension part of the file name.
                 property
                 (read- only)

 FullName        Instance       string               Gets the full path of the file.
                 property
                 (read-only)

 LastWriteTime   Instance       Implementation       Gets and sets the time when the file was last
                 property       defined (§4.5.19)    written to.
                 (read-write)

 Length          Instance       long                 Gets the size of the file, in bytes.
                 property
                 (read- only)

 Name            Instance       string               Gets the name of the file.
                 property
                 (read- only)

 VersionInfo     Instance       Implementation       Windows PowerShell: This ScriptProperty returns
                 property       defined              a System.Diagnostics.FileVersionInfo for the file.
                 (read- only)

In PowerShell, this type is System.IO.FileInfo .

4.5.19 Date-Time description type
The type of a date-time description object is implementation defined; it has the following
accessible members:

                                                                                        ﾉ   Expand table

<!-- p.1233 -->

 Member    Member Kind                 Type    Purpose

 Day       Instance property (read-    int     Gets the day component of the month represented by this
           only)                               instance.

 Hour      Instance property (read-    int     Gets the hour component of the date represented by this
           only)                               instance.

 Minute    Instance property (read-    int     Gets the minute component of the date represented by
           only)                               this instance.

 Month     Instance property (read-    int     Gets the month component of the date represented by this
           only)                               instance.

 Second    Instance property (read-    int     Gets the seconds component of the date represented by
           only)                               this instance.

 Year      Instance property (read-    int     Gets the year component of the date represented by this
           only)                               instance.

An object of this type can be created by cmdlet Get-Date.

In PowerShell, this type is System.DateTime .

4.5.20 Group-Info description type
The type of a group-info description object is implementation defined; it has the following
accessible members:

                                                                                       ﾉ   Expand table

 Member    Member Kind                Type                            Purpose

 Count     Instance property          int                             Gets the number of elements in the
           (read-only)                                                group.

 Group     Instance property          Implementation-defined          Gets the elements of the group.
           (read-only)                collection

 Name      Instance property          string                          Gets the name of the group.
           (read-only)

 Values    Instance property          Implementation-defined          Gets the values of the elements of
           (read-only)                collection                      the group.

An object of this type can be created by cmdlet Group-Object.

In PowerShell, this type is Microsoft.PowerShell.Commands.GroupInfo .

<!-- p.1234 -->

4.5.21 Generic-Measure-Info description type
The type of a generic-measure-info description object is implementation defined; it has the
following accessible members:

                                                                                             ﾉ   Expand table

 Member       Member Kind                Type         Purpose

 Average      Instance property (read-   double       Gets the average of the values of the properties that are
              only)                                   measured.

 Count        Instance property (read-   int          Gets the number of objects with the specified
              only)                                   properties.

 Maximum      Instance property (read-   double       Gets the maximum value of the specified properties.
              only)

 Minimum      Instance property (read-   double       Gets the minimum value of the specified properties.
              only)

 Property     Instance property (read-   string       Gets the property to be measured.
              only)

 Sum          Instance property (read-   double       Gets the sum of the values of the specified properties.
              only)

An object of this type can be created by cmdlet Measure-Object.

In PowerShell, this type is Microsoft.PowerShell.Commands.GenericMeasureInfo .

4.5.22 Text-Measure-Info description type
The type of a text-info description object is implementation defined; it has the following
accessible members:

                                                                                             ﾉ   Expand table

 Member       Member Kind                       Type      Purpose

 Characters   Instance property (read-only)     int       Gets the number of characters in the target object.

 Lines        Instance property (read-only)     int       Gets the number of lines in the target object.

 Property     Instance property (read-only)     string    Gets the property to be measured.

 Words        Instance property (read-only)     int       Gets the number of words in the target object.

<!-- p.1235 -->

An object of this type can be created by cmdlet Measure-Object .

In PowerShell, this type is Microsoft.PowerShell.Commands.TextMeasureInfo .

4.5.23 Credential type
A credential object can then be used in various security operations. The type of a credential
object is implementation defined; it has the following accessible members:

                                                                                     ﾉ    Expand table

 Member        Member Kind                       Type                           Purpose

 Password      Instance property (read-only)     Implementation defined         Gets the password.

 UserName      Instance property (read-only)     string                         Gets the username.

An object of this type can be created by cmdlet Get-Credential.

In PowerShell, this type is System.Management.Automation.PSCredential .

4.5.24 Method designator type
The type of a method designator is implementation defined; it has the following accessible
members:

                                                                                     ﾉ    Expand table

 Member     Member       Type                  Purpose
            Kind

 Invoke     Instance     object/variable       Takes a variable number of arguments, and indirectly
            method       number and type       calls the method referred to by the parent method
                                               designator, passing in the arguments.

An object of this type can be created by an invocation-expression (§7.1.3).

In PowerShell, this type is System.Management.Automation.PSMethod.

4.5.25 Member definition type
This type encapsulates the definition of a member. It has the following accessible members:

                                                                                     ﾉ    Expand table

<!-- p.1236 -->

 Member        Member Kind                Type                  Purpose

 Definition    Instance property (read-   string                Gets the definition of the member.
               only)

 MemberType    Instance property (read-   Implementation        Gets the PowerShell type of the
               only)                      defined               member.

 Name          Instance property (read-   string                Gets the name of the member.
               only)

 TypeName      Instance property (read-   string                Gets the type name of the member.
               only)

In PowerShell, this type is Microsoft.PowerShell.Commands.MemberDefinition .

4.6 Type extension and adaptation
A PowerShell implementation includes a family of core types (which are documented in this
chapter) that each contain their own set of base members. Those members can be methods or
properties, and they can be instance or static members. For example, the base members of the
type string (§4.3.1) are the instance property Length and the instance methods ToLower and
ToUpper.

When an object is created, it contains all the instance properties of that object's type, and the
instance methods of that type can be called on that object. An object may be customized via
the addition of instance members at runtime. The result is called a custom object. Any members
added to an instance exist only for the life of that instance; other instances of the same core
type are unaffected.

The base member set of a type can be augmented by the addition of the following kinds of
members:

     adapted members, via the Extended Type System (ETS), most details of which are
     unspecified.
     extended members, via the cmdlet Add-Member.

In PowerShell, extended members can also be added via types.ps1xml files. Adapted and
extended members are collectively called synthetic members.

The ETS adds the following members to all PowerShell objects: psbase, psadapted,
psextended, and pstypenames. See the Force and View parameters in the cmdlet Get-Member
for more information on these members.

<!-- p.1237 -->

An instance member may hide an extended and/or adapted member of the same name, and
an extended member may hide an adapted member. In such cases, the member sets
psadapted and psextended can be used to access those hidden members.

If a types.ps1xml specifies a member called Supports, obj.psextended provides access to just
that member and not to a member added via Add-Member .

There are three ways create a custom object having a new member M:

   1. This approach can be used to add one or more NoteProperty members.

       PowerShell

       $x = New-Object PSObject -Property @{M = 123}

   2. This approach can be used to add NoteProperty or ScriptMethod members.

       PowerShell

       $x = New-Module -AsCustomObject {$M = 123 ; Export-ModuleMember --Variable M}

   3. This approach can be used to add any kind of member.

       PowerShell

       $x = New-Object PSObject
       Add-Member -InputObject $x -Name M -MemberType NoteProperty -Value 123

PSObject is the base type of all PowerShell types.

Last updated on 04/08/2026

<!-- p.1238 -->

5. Variables
Article • 01/08/2025

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December
  2012 and is based on Windows PowerShell 3.0. This specification does not reflect
  the current state of PowerShell. There is no plan to update this documentation to
  reflect the current state. This documentation is presented here for historical
  reference.

  The specification document is available as a Microsoft Word document from the
  Microsoft Download Center at:
  https://www.microsoft.com/download/details.aspx?id=36389             That Word
  document has been converted for presentation here on Microsoft Learn. During
  conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

A variable represents a storage location for a value, and that value has a type. Traditional
procedural programming languages are statically typed; that is, the runtime type of a
variable is that with which it was declared at compile time. Object-oriented languages
add the idea of inheritance, which allows the runtime type of a variable to be that with
which it was declared at compile time or some type derived from that type. Being a
dynamically typed language, PowerShell's variables do not have types, per se. In fact,
variables are not defined; they simply come into being when they are first assigned a
value. And while a variable may be constrained (§5.3) to holding a value of a given type,
type information in an assignment cannot always be verified statically.

At different times, a variable may be associated with values of different types either
through assignment (§7.11) or the use of the ++ and ‑‑ operators (§7.1.5, §7.2.6). When
the value associated with a variable is changed, that value's type may change. For
example,

  PowerShell

  $i = "abc"           # $i holds a value of type string
  $i = 2147483647      # $i holds a value of type int

<!-- p.1239 -->

  ++$i                 # $i now holds a value of type double because
                       # 2147483648 is too big to fit in type int

Any use of a variable that has not been created results in the value $null. To see if a
variable has been defined, use the Test-Path cmdlet.

5.1 Writable location
A writable location is an expression that designates a resource to which a command has
both read and write access. A writable location may be a variable (§5), an array element
(§9), an associated value in a Hashtable accessed via a subscript (§10), a property (§7.1.2),
or storage managed by a provider (§3.1).

5.2 Variable categories
PowerShell defines the following categories of variables: static variables, instance
variables, array elements, Hashtable key/value pairs, parameters, ordinary variables, and
variables on provider drives. The subsections that follow describe each of these
categories.

In the following example

  PowerShell

  function F ($p1, $p2) {
      $radius = 2.45
      $circumference = 2 * ([Math]::PI) * $radius

       $date = Get-Date -Date "2010-2-1 10:12:14 pm"
       $month = $date.Month

       $values = 10, 55, 93, 102
       $value = $values[2]

       $h1 = @{ FirstName = "James"; LastName = "Anderson" }
       $h1.FirstName = "Smith"

       $Alias:A = "Help"
       $Env:MyPath = "E:\Temp"
       ${E:output.txt} = 123
       $Function:F = { "Hello there" }
       $Variable:v = 10
  }

      [Math::PI] is a static variable

<!-- p.1240 -->

      $date.Month is an instance variable
      $values[2] is an array element

      $h1.FirstName is a Hashtable key whose corresponding value is $h1['FirstName']`
      $p1 and $p2 are parameters

      $radius , $circumference , $date , $month , $values , $value , and $h1 are ordinary

     variables
      $Alias:A , $Env:MyPath , ${E:output.txt} , and $Function:F are variables on the

     corresponding provider drives.
      $Variable:v is actually an ordinary variable written with its fully qualified provider

     drive.

5.2.1 Static variables
A data member of an object that belongs to the object's type rather than to that
particular instance of the type is called a static variable. See §4.2.3, §4.2.4.1, and §4.3.8
for some examples.

PowerShell provides no way to create new types that contain static variables; however,
objects of such types may be provided by the host environment.

Memory for creating and deleting objects containing static variables is managed by the
host environment and the garbage collection system.

See §7.1.2 for information about accessing a static variable.

A static data member can be a field or a property.

5.2.2 Instance variables
A data member of an object that belongs to a particular instance of the object's type
rather than to the type itself is called an instance variable. See §4.3.1, §4.3.2, and §4.3.3
for some examples.

A PowerShell host environment might provide a way to create new types that contain
instance variables or to add new instance variables to existing types.

Memory for creating and deleting objects containing static variables is managed by the
host environment and the garbage collection system.

See §7.1.2 for information about accessing an instance variable.

An instance data member can be a field or a property.
