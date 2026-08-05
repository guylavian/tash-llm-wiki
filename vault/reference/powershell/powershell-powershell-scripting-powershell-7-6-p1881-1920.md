---
title: "How to use this documentation — pages 1881-1920"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1881-1920
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1881-1920
family: powershell
documentKind: "doc"
abstract: "DatabaseTableInfo table = GetTable(tableName); if (type == PathType.Table) { // if specified path represents a table then DatabaseTableInfo // object for the same should exist if (table != null) { return true; } } else if (type == PathType.Row) { // if specified path represents"
---

# How to use this documentation — pages 1881-1920

<!-- p.1881 -->

              DatabaseTableInfo table = GetTable(tableName);

              if (type == PathType.Table)
              {
                  // if specified path represents a table then DatabaseTableInfo
                  // object for the same should exist
                  if (table != null)
                  {
                      return true;
                  }
              }
              else if (type == PathType.Row)
              {
                  // if specified path represents a row then DatabaseTableInfo should
                  // exist for the table and then specified row number must be within
                  // the maximum row count in the table
                  if (table != null && rowNumber < table.RowCount)
                  {
                      return true;
                  }
              }

              return false;

         }

Implementing IsValidPath
The System.Management.Automation.Provider.ItemCmdletProvider.IsValidPath* method checks
whether the specified path is syntactically valid for the current provider. It does not check
whether an item exists at the path.

 C#

 protected override bool IsValidPath(string path)
        {
            bool result = true;

              // check if the path is null or empty
              if (String.IsNullOrEmpty(path))
              {
                  result = false;
              }

              // convert all separators in the path to a uniform one
              path = NormalizePath(path);

              // split the path into individual chunks
              string[] pathChunks = path.Split(pathSeparator.ToCharArray());

<!-- p.1882 -->

                foreach (string pathChunk in pathChunks)
                {
                    if (pathChunk.Length == 0)
                    {
                        result = false;
                    }
                }
                return result;
           }

Next steps
A typical real-world provider is capable of supporting items that contain other items, and of
moving items from one path to another within the drive. For an example of a provider that
supports containers, see Writing a container provider. For an example of a provider that
supports moving items, see Writing a navigation provider.

See Also
Writing a container provider

Writing a navigation provider

Windows PowerShell Provider Overview

 Last updated on 05/20/2025

<!-- p.1883 -->

Writing a container provider
This topic describes how to implement the methods of a Windows PowerShell provider that
support items that contain other items, such as folders in the FileSystem provider. To be able to
support containers, a provider must derive from the
System.Management.Automation.Provider.ContainerCmdletProvider class.

The provider in the examples in this topic uses an Access database as its data store. There are
several helper methods and classes that are used to interact with the database. For the
complete sample that includes the helper methods, see AccessDBProviderSample04.

For more information about Windows PowerShell providers, see Windows PowerShell Provider
Overview.

Implementing container methods
The System.Management.Automation.Provider.ContainerCmdletProvider class implements
methods that support containers, and create, copy, and remove items. For a complete list of
these methods, see System.Management.Automation.Provider.ContainerCmdletProvider.

  ７ Note

  This topic builds on the information in Windows PowerShell Provider QuickStart. This
  topic does not cover the basics of how to set up a provider project, or how to implement
  the methods inherited from the
  System.Management.Automation.Provider.DriveCmdletProvider class that create and
  remove drives. This topic also does not cover how to implement methods exposed by the
  System.Management.Automation.Provider.ItemCmdletProvider class. For an example
  that shows how to implement item cmdlets, see Writing an item provider.

Declaring the provider class
Declare the provider to derive from the
System.Management.Automation.Provider.ContainerCmdletProvider class, and decorate it with
the System.Management.Automation.Provider.CmdletProviderAttribute.

 C#

<!-- p.1884 -->

 [CmdletProvider("AccessDB", ProviderCapabilities.None)]
    public class AccessDBProvider : ContainerCmdletProvider
    {

      }

Implementing GetChildItems
The PowerShell engine calls the
System.Management.Automation.Provider.ContainerCmdletProvider.GetChildItems* method
when a user calls the Microsoft.PowerShell.Commands.GetChildItemCommand cmdlet. This
method gets the items that are the children of the item at the specified path.

In the Access database example, the behavior of the
System.Management.Automation.Provider.ContainerCmdletProvider.GetChildItems* method
depends on the type of the specified item. If the item is the drive, then the children are tables,
and the method returns the set of tables from the database. If the specified item is a table,
then the children are the rows of that table. If the item is a row, then it has no children, and the
method returns that row only. All child items are sent back to the PowerShell engine by the
System.Management.Automation.Provider.CmdletProvider.WriteItemObject* method.

 C#

 protected override void GetChildItems(string path, bool recurse)
        {
            // If path represented is a drive then the children in the path are
            // tables. Hence all tables in the drive represented will have to be
            // returned
            if (PathIsDrive(path))
            {
                foreach (DatabaseTableInfo table in GetTables())
                {
                    WriteItemObject(table, path, true);

                       // if the specified item exists and recurse has been set then
                       // all child items within it have to be obtained as well
                       if (ItemExists(path) && recurse)
                       {
                           GetChildItems(path + pathSeparator + table.Name, recurse);
                       }
                   } // foreach (DatabaseTableInfo...
              } // if (PathIsDrive...
              else
              {
                   // Get the table name, row number and type of path from the
                   // path specified
                   string tableName;

<!-- p.1885 -->

                   int rowNumber;

                   PathType type = GetNamesFromPath(path, out tableName, out
 rowNumber);

                   if (type == PathType.Table)
                   {
                       // Obtain all the rows within the table
                       foreach (DatabaseRowInfo row in GetRows(tableName))
                       {
                           WriteItemObject(row, path + pathSeparator + row.RowNumber,
                                   false);
                       } // foreach (DatabaseRowInfo...
                   }
                   else if (type == PathType.Row)
                   {
                       // In this case the user has directly specified a row, hence
                       // just give that particular row
                       DatabaseRowInfo row = GetRow(tableName, rowNumber);
                       WriteItemObject(row, path + pathSeparator + row.RowNumber,
                                   false);
                   }
                   else
                   {
                       // In this case, the path specified is not valid
                       ThrowTerminatingInvalidPathException(path);
                   }
               } // else
         }

Implementing GetChildNames
The System.Management.Automation.Provider.ContainerCmdletProvider.GetChildNames*
method is similar to the
System.Management.Automation.Provider.ContainerCmdletProvider.GetChildItems* method,
except that it returns only the name property of the items, and not the items themselves.

 C#

 protected override void GetChildNames(string path,
                                      ReturnContainers returnContainers)
        {
            // If the path represented is a drive, then the child items are
            // tables. get the names of all the tables in the drive.
            if (PathIsDrive(path))
            {
                foreach (DatabaseTableInfo table in GetTables())
                {
                    WriteItemObject(table.Name, path, true);
                } // foreach (DatabaseTableInfo...
            } // if (PathIsDrive...

<!-- p.1886 -->

               else
               {
                      // Get type, table name and row number from path specified
                      string tableName;
                      int rowNumber;

                      PathType type = GetNamesFromPath(path, out tableName, out
 rowNumber);

                      if (type == PathType.Table)
                      {
                          // Get all the rows in the table and then write out the
                          // row numbers.
                          foreach (DatabaseRowInfo row in GetRows(tableName))
                          {
                              WriteItemObject(row.RowNumber, path, false);
                          } // foreach (DatabaseRowInfo...
                      }
                      else if (type == PathType.Row)
                      {
                          // In this case the user has directly specified a row, hence
                          // just give that particular row
                          DatabaseRowInfo row = GetRow(tableName, rowNumber);

                         WriteItemObject(row.RowNumber, path, false);
                   }
                   else
                   {
                       ThrowTerminatingInvalidPathException(path);
                   }
               } // else
         }

Implementing NewItem
The System.Management.Automation.Provider.ContainerCmdletProvider.NewItem* method
creates a new item of the specified type at the specified path. The PowerShell engine calls this
method when a user calls the Microsoft.PowerShell.Commands.NewItemCommand cmdlet.

In this example, the method implements logic to determine that the path and type match. That
is, only a table can be created directly under the drive (the database), and only a row can be
created under a table. If the specified path and item type don't match in this way, the method
throws an exception.

 C#

 protected override void NewItem(string path, string type,
                                    object newItemValue)
        {
            string tableName;

<!-- p.1887 -->

           int rowNumber;

           PathType pt = GetNamesFromPath(path, out tableName, out rowNumber);

           if (pt == PathType.Invalid)
           {
               ThrowTerminatingInvalidPathException(path);
           }

           // Check if type is either "table" or "row", if not throw an
           // exception
           if (!String.Equals(type, "table", StringComparison.OrdinalIgnoreCase)
               && !String.Equals(type, "row", StringComparison.OrdinalIgnoreCase))
           {
               WriteError(new ErrorRecord
                                 (new ArgumentException("Type must be either a
table or row"),
                                     "CannotCreateSpecifiedObject",
                                        ErrorCategory.InvalidArgument,
                                             path
                                  )
                         );

               throw new ArgumentException("This provider can only create items of
type \"table\" or \"row\"");
           }

           // Path type is the type of path of the container. So if a drive
           // is specified, then a table can be created under it and if a table
           // is specified, then a row can be created under it. For the sake of
           // completeness, if a row is specified, then if the row specified by
           // the path does not exist, a new row is created. However, the row
           // number may not match as the row numbers only get incremented based
           // on the number of rows

           if (PathIsDrive(path))
           {
               if (String.Equals(type, "table",
StringComparison.OrdinalIgnoreCase))
               {
                   // Execute command using ODBC connection to create a table
                   try
                   {
                       // create the table using an sql statement
                       string newTableName = newItemValue.ToString();

                       if (!TableNameIsValid(newTableName))
                       {
                           return;
                       }
                       string sql = "create table " + newTableName
                                            + " (ID INT)";

                       // Create the table using the Odbc connection from the
                       // drive.

<!-- p.1888 -->

                       AccessDBPSDriveInfo di = this.PSDriveInfo as
AccessDBPSDriveInfo;

                       if (di == null)
                       {
                           return;
                       }
                       OdbcConnection connection = di.Connection;

                       if (ShouldProcess(newTableName, "create"))
                       {
                           OdbcCommand cmd = new OdbcCommand(sql, connection);
                           cmd.ExecuteScalar();
                       }
                    }
                    catch (Exception ex)
                    {
                         WriteError(new ErrorRecord(ex, "CannotCreateSpecifiedTable",
                                   ErrorCategory.InvalidOperation, path)
                                   );
                    }
                } // if (String...
                else if (String.Equals(type, "row",
StringComparison.OrdinalIgnoreCase))
                {
                    throw new
                         ArgumentException("A row cannot be created under a database,
specify a path that represents a Table");
                }
           }// if (PathIsDrive...
           else
           {
                if (String.Equals(type, "table",
StringComparison.OrdinalIgnoreCase))
                {
                    if (rowNumber < 0)
                    {
                         throw new
                             ArgumentException("A table cannot be created within
another table, specify a path that represents a database");
                    }
                    else
                    {
                         throw new
                             ArgumentException("A table cannot be created inside a
row, specify a path that represents a database");
                    }
                } //if (String.Equals....
                // if path specified is a row, create a new row
                else if (String.Equals(type, "row",
StringComparison.OrdinalIgnoreCase))
                {
                    // The user is required to specify the values to be inserted
                    // into the table in a single string separated by commas
                    string value = newItemValue as string;

<!-- p.1889 -->

                   if (String.IsNullOrEmpty(value))
                   {
                       throw new
                           ArgumentException("Value argument must have comma
separated values of each column in a row");
                   }
                   string[] rowValues = value.Split(',');

                   OdbcDataAdapter da = GetAdapterForTable(tableName);

                   if (da == null)
                   {
                       return;
                   }

                   DataSet ds = GetDataSetForTable(da, tableName);
                   DataTable table = GetDataTable(ds, tableName);

                   if (rowValues.Length != table.Columns.Count)
                   {
                       string message =
                            String.Format(CultureInfo.CurrentCulture,
                                            "The table has {0} columns and the
value specified must have so many comma separated values",
                                                table.Columns.Count);

                       throw new ArgumentException(message);
                   }

                   if (!Force && (rowNumber >=0 && rowNumber < table.Rows.Count))
                   {
                       string message = String.Format(CultureInfo.CurrentCulture,
                                                        "The row {0} already
exists. To create a new row specify row number as {1}, or specify path to a table,
or use the -Force parameter",
                                                            rowNumber,
table.Rows.Count);

                       throw new ArgumentException(message);
                   }

                   if (rowNumber > table.Rows.Count)
                   {
                       string message = String.Format(CultureInfo.CurrentCulture,
                                            "To create a new row specify row number
as {0}, or specify path to a table",
                                                table.Rows.Count);

                       throw new ArgumentException(message);
                   }

                   // Create a new row and update the row with the input
                   // provided by the user
                   DataRow row = table.NewRow();

<!-- p.1890 -->

                        for (int i = 0; i < rowValues.Length; i++)
                        {
                            row[i] = rowValues[i];
                        }
                        table.Rows.Add(row);

                        if (ShouldProcess(tableName, "update rows"))
                        {
                            // Update the table from memory back to the data source
                            da.Update(ds, tableName);
                        }

                  }// else if (String...
              }// else ...

          }

Implementing CopyItem
The System.Management.Automation.Provider.ContainerCmdletProvider.CopyItem copies the
specified item to the specified path. The PowerShell engine calls this method when a user calls
the Microsoft.PowerShell.Commands.CopyItemCommand cmdlet. This method can also be
recursive, copying all of the items children in addition to the item itself.

Similarly to the System.Management.Automation.Provider.ContainerCmdletProvider.NewItem*
method, this method performs logic to make sure that the specified item is of the correct type
for the path to which it is being copied. For example, if the destination path is a table, the item
to be copied must be a row.

 C#

 protected override void CopyItem(string path, string copyPath, bool recurse)
        {
            string tableName, copyTableName;
            int rowNumber, copyRowNumber;

            PathType type = GetNamesFromPath(path, out tableName, out rowNumber);
            PathType copyType = GetNamesFromPath(copyPath, out copyTableName, out
 copyRowNumber);

              if (type == PathType.Invalid)
              {
                  ThrowTerminatingInvalidPathException(path);
              }

              if (type == PathType.Invalid)
              {
                  ThrowTerminatingInvalidPathException(copyPath);
              }

<!-- p.1891 -->

           // Get the table and the table to copy to
           OdbcDataAdapter da = GetAdapterForTable(tableName);
           if (da == null)
           {
               return;
           }

           DataSet ds = GetDataSetForTable(da, tableName);
           DataTable table = GetDataTable(ds, tableName);

           OdbcDataAdapter cda = GetAdapterForTable(copyTableName);
           if (cda == null)
           {
               return;
           }

           DataSet cds = GetDataSetForTable(cda, copyTableName);
           DataTable copyTable = GetDataTable(cds, copyTableName);

           // if source represents a table
           if (type == PathType.Table)
           {
               // if copyPath does not represent a table
               if (copyType != PathType.Table)
               {
                   ArgumentException e = new ArgumentException("Table can only be
copied on to another table location");

                   WriteError(new ErrorRecord(e, "PathNotValid",
                       ErrorCategory.InvalidArgument, copyPath));

                   throw e;
               }

               // if table already exists then Force parameter should be set
               // to force a copy
               if (!Force && GetTable(copyTableName) != null)
               {
                   throw new ArgumentException("Specified path already exists");
               }

               for (int i = 0; i < table.Rows.Count; i++)
               {
                   DataRow row = table.Rows[i];
                   DataRow copyRow = copyTable.NewRow();

                   copyRow.ItemArray = row.ItemArray;
                   copyTable.Rows.Add(copyRow);
                }
           } // if (type == ...
           // if source represents a row
           else
           {
                if (copyType == PathType.Row)

<!-- p.1892 -->

                 {
                     if (!Force && (copyRowNumber < copyTable.Rows.Count))
                     {
                         throw new ArgumentException("Specified path already
exists.");
                     }

                     DataRow row = table.Rows[rowNumber];
                     DataRow copyRow = null;

                   if (copyRowNumber < copyTable.Rows.Count)
                   {
                        // copy to an existing row
                        copyRow = copyTable.Rows[copyRowNumber];
                        copyRow.ItemArray = row.ItemArray;
                        copyRow[0] = GetNextID(copyTable);
                   }
                   else if (copyRowNumber == copyTable.Rows.Count)
                   {
                        // copy to the next row in the table that will
                        // be created
                        copyRow = copyTable.NewRow();
                        copyRow.ItemArray = row.ItemArray;
                        copyRow[0] = GetNextID(copyTable);
                        copyTable.Rows.Add(copyRow);
                   }
                   else
                   {
                        // attempting to copy to a nonexistent row or a row
                        // that cannot be created now - throw an exception
                        string message = String.Format(CultureInfo.CurrentCulture,
                                              "The item cannot be specified to the
copied row. Specify row number as {0}, or specify a path to the table.",
                                                     table.Rows.Count);

                         throw new ArgumentException(message);
                     }
                 }
                 else
                 {
                     // destination path specified represents a table,
                     // create a new row and copy the item
                     DataRow copyRow = copyTable.NewRow();
                     copyRow.ItemArray = table.Rows[rowNumber].ItemArray;
                     copyRow[0] = GetNextID(copyTable);
                     copyTable.Rows.Add(copyRow);
                 }
             }

             if (ShouldProcess(copyTableName, "CopyItems"))
             {
                 cda.Update(cds, copyTableName);
             }

       } //CopyItem

<!-- p.1893 -->

Implementing RemoveItem
The System.Management.Automation.Provider.ContainerCmdletProvider.RemoveItem* method
removes the item at the specified path. The PowerShell engine calls this method when a user
calls the Microsoft.PowerShell.Commands.RemoveItemCommand cmdlet.

 C#

 protected override void RemoveItem(string path, bool recurse)
        {
            string tableName;
            int rowNumber = 0;

             PathType type = GetNamesFromPath(path, out tableName, out rowNumber);

             if (type == PathType.Table)
             {
                 // if recurse flag has been specified, delete all the rows as well
                 if (recurse)
                 {
                     OdbcDataAdapter da = GetAdapterForTable(tableName);
                     if (da == null)
                     {
                         return;
                     }

                      DataSet ds = GetDataSetForTable(da, tableName);
                      DataTable table = GetDataTable(ds, tableName);

                      for (int i = 0; i < table.Rows.Count; i++)
                      {
                          table.Rows[i].Delete();
                      }

                     if (ShouldProcess(path, "RemoveItem"))
                     {
                         da.Update(ds, tableName);
                         RemoveTable(tableName);
                     }
                 }//if (recurse...
                 else
                 {
                     // Remove the table
                     if (ShouldProcess(path, "RemoveItem"))
                     {
                         RemoveTable(tableName);
                     }
                 }
             }
             else if (type == PathType.Row)

<!-- p.1894 -->

                {
                       OdbcDataAdapter da = GetAdapterForTable(tableName);
                       if (da == null)
                       {
                           return;
                       }

                       DataSet ds = GetDataSetForTable(da, tableName);
                       DataTable table = GetDataTable(ds, tableName);

                       table.Rows[rowNumber].Delete();

                       if (ShouldProcess(path, "RemoveItem"))
                       {
                           da.Update(ds, tableName);
                       }
                }
                else
                {
                       ThrowTerminatingInvalidPathException(path);
                }

            }

Next steps
A typical real-world provider is capable of moving items from one path to another within the
drive. For an example of a provider that supports moving items, see Writing a navigation
provider.

See Also
Writing a navigation provider

Windows PowerShell Provider Overview

 Last updated on 05/20/2025

<!-- p.1895 -->

Writing a navigation provider
This topic describes how to implement the methods of a Windows PowerShell provider that
support nested containers (multi-level data stores), moving items, and relative paths. A
navigation provider must derive from the
System.Management.Automation.Provider.NavigationCmdletProvider class.

The provider in the examples in this topic uses an Access database as its data store. There are
several helper methods and classes that are used to interact with the database. For the
complete sample that includes the helper methods, see AccessDBProviderSample05.

For more information about Windows PowerShell providers, see Windows PowerShell Provider
Overview.

Implementing navigation methods
The System.Management.Automation.Provider.NavigationCmdletProvider class implements
methods that support nested containers, relative paths, and moving items. For a complete list
of these methods, see NavigationCmdletProvider Methods.

  ７ Note

  This topic builds on the information in Windows PowerShell Provider QuickStart. This
  topic does not cover the basics of how to set up a provider project, or how to implement
  the methods inherited from the
  System.Management.Automation.Provider.DriveCmdletProvider class that create and
  remove drives. This topic also does not cover how to implement methods exposed by the
  System.Management.Automation.Provider.ItemCmdletProvider or
  System.Management.Automation.Provider.ContainerCmdletProvider classes. For an
  example that shows how to implement item cmdlets, see Writing an item provider. For an
  example that shows how to implement container cmdlets, see Writing a container
  provider.

Declaring the provider class
Declare the provider to derive from the
System.Management.Automation.Provider.NavigationCmdletProvider class, and decorate it

<!-- p.1896 -->

with the System.Management.Automation.Provider.CmdletProviderAttribute.

 [CmdletProvider("AccessDB", ProviderCapabilities.None)]
    public class AccessDBProvider : NavigationCmdletProvider
    {

      }

Implementing IsItemContainer
The System.Management.Automation.Provider.NavigationCmdletProvider.IsItemContainer*
method checks whether the item at the specified path is a container.

 C#

 protected override bool IsItemContainer(string path)
       {
          if (PathIsDrive(path))
          {
              return true;
          }

              string[] pathChunks = ChunkPath(path);
              string tableName;
              int rowNumber;

              PathType type = GetNamesFromPath(path, out tableName, out rowNumber);

          if (type == PathType.Table)
          {
             foreach (DatabaseTableInfo ti in GetTables())
             {
                 if (string.Equals(ti.Name, tableName,
 StringComparison.OrdinalIgnoreCase))
                 {
                     return true;
                 }
             } // foreach (DatabaseTableInfo...
          } // if (pathChunks...

              return false;
          }

Implementing GetChildName

<!-- p.1897 -->

The System.Management.Automation.Provider.NavigationCmdletProvider.GetChildName*
method gets the name property of the child item at the specified path. If the item at the
specified path is not a child of a container, then this method should return the path.

 C#

 protected override string GetChildName(string path)
        {
            if (PathIsDrive(path))
            {
                return path;
            }

                 string tableName;
                 int rowNumber;

                 PathType type = GetNamesFromPath(path, out tableName, out rowNumber);

                 if (type == PathType.Table)
                 {
                      return tableName;
                 }
                 else if (type == PathType.Row)
                 {
                      return rowNumber.ToString(CultureInfo.CurrentCulture);
                 }
                 else
                 {
                      ThrowTerminatingInvalidPathException(path);
                 }

                 return null;
         }

Implementing GetParentPath
The System.Management.Automation.Provider.NavigationCmdletProvider.GetParentPath*
method gets the path of the parent of the item at the specified path. If the item at the
specified path is the root of the data store (so it has no parent), then this method should return
the root path.

 C#

 protected override string GetParentPath(string path, string root)
        {
            // If root is specified then the path has to contain
            // the root. If not nothing should be returned
            if (!String.IsNullOrEmpty(root))
            {

<!-- p.1898 -->

                  if (!path.Contains(root))
                  {
                      return null;
                  }
              }

            return path.Substring(0, path.LastIndexOf(pathSeparator,
 StringComparison.OrdinalIgnoreCase));
        }

Implementing MakePath
The System.Management.Automation.Provider.NavigationCmdletProvider.MakePath* method
joins a specified parent path and a specified child path to create a provider-internal path (for
information about path types that providers can support, see Windows PowerShell Provider
Overview. The PowerShell engine calls this method when a user calls the
Microsoft.PowerShell.Commands.JoinPathCommand cmdlet.

 C#

 protected override string MakePath(string parent, string child)
        {
            string result;

              string normalParent = NormalizePath(parent);
              normalParent = RemoveDriveFromPath(normalParent);
              string normalChild = NormalizePath(child);
              normalChild = RemoveDriveFromPath(normalChild);

            if (String.IsNullOrEmpty(normalParent) &&
 String.IsNullOrEmpty(normalChild))
            {
                result = String.Empty;
            }
            else if (String.IsNullOrEmpty(normalParent) &&
 !String.IsNullOrEmpty(normalChild))
            {
                result = normalChild;
            }
            else if (!String.IsNullOrEmpty(normalParent) &&
 String.IsNullOrEmpty(normalChild))
            {
                if (normalParent.EndsWith(pathSeparator,
 StringComparison.OrdinalIgnoreCase))
                {
                    result = normalParent;
                }
                else
                {
                    result = normalParent + pathSeparator;

<!-- p.1899 -->

                 }
            } // else if (!String...
            else
            {
                 if (!normalParent.Equals(String.Empty) &&
                     !normalParent.EndsWith(pathSeparator,
 StringComparison.OrdinalIgnoreCase))
                 {
                     result = normalParent + pathSeparator;
                 }
                 else
                 {
                     result = normalParent;
                 }

                if (normalChild.StartsWith(pathSeparator,
 StringComparison.OrdinalIgnoreCase))
                {
                    result += normalChild.Substring(1);
                }
                else
                {
                    result += normalChild;
                }
            } // else

             return result;
         }

Implementing NormalizeRelativePath
The
System.Management.Automation.Provider.NavigationCmdletProvider.NormalizeRelativePath*
method takes path and basepath parameters, and returns a normalized path that is equivalent
to the path parameter and relative to the basepath parameter.

 C#

 protected override string NormalizeRelativePath(string path,
                                                             string basepath)
        {
            // Normalize the paths first
            string normalPath = NormalizePath(path);
            normalPath = RemoveDriveFromPath(normalPath);
            string normalBasePath = NormalizePath(basepath);
            normalBasePath = RemoveDriveFromPath(normalBasePath);

             if (String.IsNullOrEmpty(normalBasePath))
             {
                 return normalPath;
             }

<!-- p.1900 -->

             else
             {
                    if (!normalPath.Contains(normalBasePath))
                    {
                        return null;
                    }

                return normalPath.Substring(normalBasePath.Length +
 pathSeparator.Length);
            }
        }

Implementing MoveItem
The System.Management.Automation.Provider.NavigationCmdletProvider.MoveItem* method
moves an item from the specified path to the specified destination path. The PowerShell
engine calls this method when a user calls the
Microsoft.PowerShell.Commands.MoveItemCommand cmdlet.

 C#

 protected override void MoveItem(string path, string destination)
        {
            // Get type, table name and rowNumber from the path
            string tableName, destTableName;
            int rowNumber, destRowNumber;

             PathType type = GetNamesFromPath(path, out tableName, out rowNumber);

             PathType destType = GetNamesFromPath(destination, out destTableName,
                                      out destRowNumber);

             if (type == PathType.Invalid)
             {
                 ThrowTerminatingInvalidPathException(path);
             }

             if (destType == PathType.Invalid)
             {
                 ThrowTerminatingInvalidPathException(destination);
             }

             if (type == PathType.Table)
             {
                 ArgumentException e = new ArgumentException("Move not supported for
 tables");

                    WriteError(new ErrorRecord(e, "MoveNotSupported",
                        ErrorCategory.InvalidArgument, path));

                    throw e;

<!-- p.1901 -->

             }
             else
             {
                    OdbcDataAdapter da = GetAdapterForTable(tableName);
                    if (da == null)
                    {
                        return;
                    }

                    DataSet ds = GetDataSetForTable(da, tableName);
                    DataTable table = GetDataTable(ds, tableName);

                    OdbcDataAdapter dda = GetAdapterForTable(destTableName);
                    if (dda == null)
                    {
                        return;
                    }

                    DataSet dds = GetDataSetForTable(dda, destTableName);
                    DataTable destTable = GetDataTable(dds, destTableName);
                    DataRow row = table.Rows[rowNumber];

                    if (destType == PathType.Table)
                    {
                        DataRow destRow = destTable.NewRow();

                        destRow.ItemArray = row.ItemArray;
                    }
                    else
                    {
                        DataRow destRow = destTable.Rows[destRowNumber];

                        destRow.ItemArray = row.ItemArray;
                    }

                    // Update the changes
                    if (ShouldProcess(path, "MoveItem"))
                    {
                        WriteItemObject(row, path, false);
                        dda.Update(dds, destTableName);
                    }
             }
         }

See Also
Writing a container provider

Windows PowerShell Provider Overview

<!-- p.1902 -->

Last updated on 05/20/2025

<!-- p.1903 -->

Provider Samples
This section includes samples of providers that access a Microsoft Access database. These
samples include provider classes that derive from all the base provider classes.

In This Section
This section includes the following topics:

AccessDBProviderSample01 Sample This sample shows how to declare the provider class that
derives directly from the System.Management.Automation.Provider.CmdletProvider class. It is
included here only for completeness.

AccessDBProviderSample02 This sample shows how to overwrite the
System.Management.Automation.Provider.DriveCmdletProvider.NewDrive* and
System.Management.Automation.Provider.DriveCmdletProvider.RemoveDrive* methods to
support calls to the New-PSDrive and Remove-PSDrive cmdlets. The provider class in this sample
derives from the System.Management.Automation.Provider.DriveCmdletProvider class.

AccessDBProviderSample03 This sample shows how to overwrite the
System.Management.Automation.Provider.ItemCmdletProvider.GetItem* and
System.Management.Automation.Provider.ItemCmdletProvider.SetItem* methods to support
calls to the Get-Item and Set-Item cmdlets. The provider class in this sample derives from the
System.Management.Automation.Provider.ItemCmdletProvider class.

AccessDBProviderSample04 This sample shows how to overwrite container methods to support
calls to the Copy-Item , Get-ChildItem , New-Item , and Remove-Item cmdlets. These methods
should be implemented when the data store contains items that are containers. A container is a
group of child items under a common parent item. The provider class in this sample derives
from the System.Management.Automation.Provider.ContainerCmdletProvider class.

AccessDBProviderSample05 This sample shows how to overwrite container methods to support
calls to the Move-Item and Join-Path cmdlets. These methods should be implemented when
the user needs to move items within a container and if the data store contains nested
containers. The provider class in this sample derives from the
System.Management.Automation.Provider.NavigationCmdletProvider class.

<!-- p.1904 -->

AccessDBProviderSample06 This sample shows how to overwrite content methods to support
calls to the Clear-Content , Get-Content , and Set-Content cmdlets. These methods should be
implemented when the user needs to manage the content of the items in the data store. The
provider class in this sample derives from the
System.Management.Automation.Provider.NavigationCmdletProvider class, and it implements
the System.Management.Automation.Provider.IContentCmdletProvider interface.

See Also
Writing a Windows PowerShell Provider

 Last updated on 05/20/2025

<!-- p.1905 -->

AccessDBProviderSample01
This sample shows how to declare a provider class that derives directly from the
System.Management.Automation.Provider.CmdletProvider class. It is included here only for
completeness.

Demonstrates

  ） Important

  Your provider class will most likely derive from one of the following classes and possibly
  implement other provider interfaces:

         System.Management.Automation.Provider.ItemCmdletProvider class. See
         AccessDBProviderSample03.
         System.Management.Automation.Provider.ContainerCmdletProvider class. See
         AccessDBProviderSample04.
         System.Management.Automation.Provider.NavigationCmdletProvider class. See
         AccessDBProviderSample05.

  For more information about choosing which provider class to derive from based on
  provider features, see Designing Your Windows PowerShell Provider.

This sample demonstrates the following:

       Declaring the CmdletProvider attribute.

       Defining a provider class that derives directly from the
       System.Management.Automation.Provider.CmdletProvider class.

Example
This sample shows how to define a provider class and how to declare the CmdletProvider
attribute.

  C#

<!-- p.1906 -->

 using System.Management.Automation;
 using System.Management.Automation.Provider;
 using System.ComponentModel;

 namespace Microsoft.Samples.PowerShell.Providers
 {
    #region AccessDBProvider

       /// <summary>
     /// Simple provider.
     /// </summary>
     [CmdletProvider("AccessDB", ProviderCapabilities.None)]
     public class AccessDBProvider : CmdletProvider
     {

     }

     #endregion AccessDBProvider
 }

See Also
System.Management.Automation.Provider.ItemCmdletProvider

System.Management.Automation.Provider.ContainerCmdletProvider

System.Management.Automation.Provider.NavigationCmdletProvider

Designing Your Windows PowerShell Provider

Last updated on 05/20/2025

<!-- p.1907 -->

AccessDBProviderSample02
This sample shows how to overwrite the
System.Management.Automation.Provider.DriveCmdletProvider.NewDrive* and
System.Management.Automation.Provider.DriveCmdletProvider.RemoveDrive* methods to
support calls to the New-PSDrive and Remove-PSDrive cmdlets. The provider class in this sample
derives from the System.Management.Automation.Provider.DriveCmdletProvider class.

Demonstrates

  ） Important

  Your provider class will most likely derive from one of the following classes and possibly
  implement other provider interfaces:

       System.Management.Automation.Provider.ItemCmdletProvider class. See
       AccessDBProviderSample03.
       System.Management.Automation.Provider.ContainerCmdletProvider class. See
       AccessDBProviderSample04.
       System.Management.Automation.Provider.NavigationCmdletProvider class. See
       AccessDBProviderSample05.

  For more information about choosing which provider class to derive from based on
  provider features, see Designing Your Windows PowerShell Provider.

This sample demonstrates the following:

     Declaring the CmdletProvider attribute.

     Defining a provider class that drives from the
     System.Management.Automation.Provider.DriveCmdletProvider class.

     Overwriting the
     System.Management.Automation.Provider.DriveCmdletProvider.NewDrive* method to
     support creating new drives. (This sample does not show how to add dynamic parameters
     to the New-PSDrive cmdlet.)

<!-- p.1908 -->

      Overwriting the
      System.Management.Automation.Provider.DriveCmdletProvider.RemoveDrive* method to
      support removing existing drives.

Example
This sample shows how to overwrite the
System.Management.Automation.Provider.DriveCmdletProvider.NewDrive* and
System.Management.Automation.Provider.DriveCmdletProvider.RemoveDrive* methods. For
this sample provider, when a drive is created its connection information is stored in an
AccessDBPsDriveInfo object.

 C#

 using System;
 using System.IO;
 using System.Data;
 using System.Data.Odbc;
 using System.Management.Automation;
 using System.Management.Automation.Provider;
 using System.ComponentModel;

 namespace Microsoft.Samples.PowerShell.Providers
 {
    #region AccessDBProvider

        /// <summary>
      /// A PowerShell Provider which acts upon a access data store.
      /// </summary>
      /// <remarks>
      /// This example only demonstrates the drive overrides
      /// </remarks>
      [CmdletProvider("AccessDB", ProviderCapabilities.None)]
      public class AccessDBProvider : DriveCmdletProvider
      {
           #region Drive Manipulation

          /// <summary>
          /// Create a new drive. Create a connection to the database file and set
          /// the Connection property in the PSDriveInfo.
          /// </summary>
          /// <param name="drive">
          /// Information describing the drive to add.
          /// </param>
          /// <returns>The added drive.</returns>
          protected override PSDriveInfo NewDrive(PSDriveInfo drive)
          {
              // check if drive object is null
              if (drive == null)

<!-- p.1909 -->

           {
               WriteError(new ErrorRecord(
                   new ArgumentNullException("drive"),
                   "NullDrive",
                   ErrorCategory.InvalidArgument,
                   null)
               );

               return null;
           }

           // check if drive root is not null or empty
           // and if its an existing file
           if (String.IsNullOrEmpty(drive.Root) || (File.Exists(drive.Root) ==
false))
           {
               WriteError(new ErrorRecord(
                   new ArgumentException("drive.Root"),
                   "NoRoot",
                   ErrorCategory.InvalidArgument,
                   drive)
               );

               return null;
           }

           // create a new drive and create an ODBC connection to the new drive
           AccessDBPSDriveInfo accessDBPSDriveInfo = new
AccessDBPSDriveInfo(drive);

           OdbcConnectionStringBuilder builder = new OdbcConnectionStringBuilder();

           builder.Driver = "Microsoft Access Driver (*.mdb)";
           builder.Add("DBQ", drive.Root);

           OdbcConnection conn = new OdbcConnection(builder.ConnectionString);
           conn.Open();
           accessDBPSDriveInfo.Connection = conn;

           return accessDBPSDriveInfo;
       } // NewDrive

       /// <summary>
       /// Removes a drive from the provider.
       /// </summary>
       /// <param name="drive">The drive to remove.</param>
       /// <returns>The drive removed.</returns>
       protected override PSDriveInfo RemoveDrive(PSDriveInfo drive)
       {
           // check if drive object is null
           if (drive == null)
           {
               WriteError(new ErrorRecord(
                   new ArgumentNullException("drive"),
                   "NullDrive",

<!-- p.1910 -->

                 ErrorCategory.InvalidArgument,
                 drive)
            );

           return null;
       }

       // close ODBC connection to the drive
       AccessDBPSDriveInfo accessDBPSDriveInfo = drive as AccessDBPSDriveInfo;

       if (accessDBPSDriveInfo == null)
       {
           return null;
       }
       accessDBPSDriveInfo.Connection.Close();

        return accessDBPSDriveInfo;
    } // RemoveDrive

    #endregion Drive Manipulation

} // AccessDBProvider

#endregion AccessDBProvider

#region AccessDBPSDriveInfo

/// <summary>
/// Any state associated with the drive should be held here.
/// In this case, it's the connection to the database.
/// </summary>
internal class AccessDBPSDriveInfo : PSDriveInfo
{
    private OdbcConnection connection;

    /// <summary>
    /// ODBC connection information.
    /// </summary>
    public OdbcConnection Connection
    {
        get { return connection; }
        set { connection = value; }
    }

    /// <summary>
    /// Constructor that takes one argument
    /// </summary>
    /// <param name="driveInfo">Drive provided by this provider</param>
    public AccessDBPSDriveInfo(PSDriveInfo driveInfo)
        : base(driveInfo)
    { }

} // class AccessDBPSDriveInfo

<!-- p.1911 -->

     #endregion AccessDBPSDriveInfo
 }

See Also
System.Management.Automation.Provider.ItemCmdletProvider

System.Management.Automation.Provider.ContainerCmdletProvider

System.Management.Automation.Provider.NavigationCmdletProvider

Designing Your Windows PowerShell Provider

Last updated on 05/20/2025

<!-- p.1912 -->

AccessDBProviderSample03
This sample shows how to overwrite the
System.Management.Automation.Provider.ItemCmdletProvider.GetItem* and
System.Management.Automation.Provider.ItemCmdletProvider.SetItem* methods to support
calls to the Get-Item and Set-Item cmdlets. The provider class in this sample derives from the
System.Management.Automation.Provider.ItemCmdletProvider class.

Demonstrates

  ） Important

  Your provider class will most likely derive from one of the following classes and possibly
  implement other provider interfaces:

       System.Management.Automation.Provider.ItemCmdletProvider class.
       System.Management.Automation.Provider.ContainerCmdletProvider class. See
       AccessDBProviderSample04.
       System.Management.Automation.Provider.NavigationCmdletProvider class. See
       AccessDBProviderSample05.

  For more information about choosing which provider class to derive from based on
  provider features, see Designing Your Windows PowerShell Provider.

This sample demonstrates the following:

     Declaring the CmdletProvider attribute.
     Defining a provider class that derives from the
     System.Management.Automation.Provider.ItemCmdletProvider class.
     Overwriting the
     System.Management.Automation.Provider.DriveCmdletProvider.NewDrive* method to
     change the behavior of the New-PSDrive cmdlet, allowing the user to create new drives.
     (This sample does not show how to add dynamic parameters to the New-PSDrive cmdlet.)
     Overwriting the
     System.Management.Automation.Provider.DriveCmdletProvider.RemoveDrive* method to
     support removing existing drives.

<!-- p.1913 -->

      Overwriting the System.Management.Automation.Provider.ItemCmdletProvider.GetItem*
      method to change the behavior of the Get-Item cmdlet, allowing the user to retrieve
      items from the data store. (This sample does not show how to add dynamic parameters
      to the Get-Item cmdlet.)
      Overwriting the System.Management.Automation.Provider.ItemCmdletProvider.SetItem*
      method to change the behavior of the Set-Item cmdlet, allowing the user to update the
      items in the data store. (This sample does not show how to add dynamic parameters to
      the Get-Item cmdlet.)
      Overwriting the
      System.Management.Automation.Provider.ItemCmdletProvider.ItemExists* method to
      change the behavior of the Test-Path cmdlet. (This sample does not show how to add
      dynamic parameters to the Test-Path cmdlet.)
      Overwriting the
      System.Management.Automation.Provider.ItemCmdletProvider.IsValidPath* method to
      determine if the provided path is valid.

Example
This sample shows how to overwrite the methods needed to get and set items in a Microsoft
Access data base.

 C#

 using System;
 using System.IO;
 using System.Data;
 using System.Data.Odbc;
 using System.Collections.ObjectModel;
 using System.Text;
 using System.Diagnostics;
 using System.Text.RegularExpressions;
 using System.Management.Automation;
 using System.Management.Automation.Provider;
 using System.ComponentModel;
 using System.Globalization;

 namespace Microsoft.Samples.PowerShell.Providers
 {
    #region AccessDBProvider

      /// <summary>
      /// A PowerShell Provider which acts upon a access database.
      /// </summary>
      /// <remarks>
      /// This example implements the item overloads.

<!-- p.1914 -->

    /// </remarks>
   [CmdletProvider("AccessDB", ProviderCapabilities.None)]

   public class AccessDBProvider : ItemCmdletProvider
   {
      #region Drive Manipulation

       /// <summary>
       /// Create a new drive. Create a connection to the database file and set
       /// the Connection property in the PSDriveInfo.
       /// </summary>
       /// <param name="drive">
       /// Information describing the drive to add.
       /// </param>
       /// <returns>The added drive.</returns>
       protected override PSDriveInfo NewDrive(PSDriveInfo drive)
       {
           // check if drive object is null
           if (drive == null)
           {
               WriteError(new ErrorRecord(
                   new ArgumentNullException("drive"),
                   "NullDrive",
                   ErrorCategory.InvalidArgument,
                   null)
               );

               return null;
           }

           // check if drive root is not null or empty
           // and if its an existing file
           if (String.IsNullOrEmpty(drive.Root) || (File.Exists(drive.Root) ==
false))
           {
               WriteError(new ErrorRecord(
                   new ArgumentException("drive.Root"),
                   "NoRoot",
                   ErrorCategory.InvalidArgument,
                   drive)
               );

               return null;
           }

           // create a new drive and create an ODBC connection to the new drive
           AccessDBPSDriveInfo accessDBPSDriveInfo = new
AccessDBPSDriveInfo(drive);

           OdbcConnectionStringBuilder builder = new OdbcConnectionStringBuilder();

           builder.Driver = "Microsoft Access Driver (*.mdb)";
           builder.Add("DBQ", drive.Root);

           OdbcConnection conn = new OdbcConnection(builder.ConnectionString);

<!-- p.1915 -->

    conn.Open();
    accessDBPSDriveInfo.Connection = conn;

     return accessDBPSDriveInfo;
 } // NewDrive

 /// <summary>
 /// Removes a drive from the provider.
 /// </summary>
 /// <param name="drive">The drive to remove.</param>
 /// <returns>The drive removed.</returns>
 protected override PSDriveInfo RemoveDrive(PSDriveInfo drive)
 {
     // check if drive object is null
     if (drive == null)
     {
         WriteError(new ErrorRecord(
             new ArgumentNullException("drive"),
             "NullDrive",
             ErrorCategory.InvalidArgument,
             drive)
         );

         return null;
    }

    // close ODBC connection to the drive
    AccessDBPSDriveInfo accessDBPSDriveInfo = drive as AccessDBPSDriveInfo;

    if (accessDBPSDriveInfo == null)
    {
        return null;
    }
    accessDBPSDriveInfo.Connection.Close();

     return accessDBPSDriveInfo;
 } // RemoveDrive

 #endregion Drive Manipulation

 #region Item Methods

/// <summary>
/// Retrieves an item using the specified path.
/// </summary>
/// <param name="path">The path to the item to return.</param>
protected override void GetItem(string path)
{
    // check if the path represented is a drive
    if (PathIsDrive(path))
    {
        WriteItemObject(this.PSDriveInfo, path, true);
        return;
    }// if (PathIsDrive...

<!-- p.1916 -->

   // Get table name and row information from the path and do
   // necessary actions
   string tableName;
   int rowNumber;

   PathType type = GetNamesFromPath(path, out tableName, out rowNumber);

   if (type == PathType.Table)
   {
        DatabaseTableInfo table = GetTable(tableName);
        WriteItemObject(table, path, true);
   }
   else if (type == PathType.Row)
   {
        DatabaseRowInfo row = GetRow(tableName, rowNumber);
        WriteItemObject(row, path, false);
   }
   else
   {
        ThrowTerminatingInvalidPathException(path);
   }

} // GetItem

/// <summary>
/// Set the content of a row of data specified by the supplied path
/// parameter.
/// </summary>
/// <param name="path">Specifies the path to the row whose columns
/// will be updated.</param>
/// <param name="values">Comma separated string of values</param>
protected override void SetItem(string path, object values)
{
    // Get type, table name and row number from the path specified
    string tableName;
    int rowNumber;

   PathType type = GetNamesFromPath(path, out tableName, out rowNumber);

   if (type != PathType.Row)
   {
       WriteError(new ErrorRecord(new NotSupportedException(
             "SetNotSupported"), "",
          ErrorCategory.InvalidOperation, path));

       return;
   }

   // Get in-memory representation of table
   OdbcDataAdapter da = GetAdapterForTable(tableName);

   if (da == null)
   {
       return;
   }

<!-- p.1917 -->

   DataSet ds = GetDataSetForTable(da, tableName);
   DataTable table = GetDataTable(ds, tableName);

   if (rowNumber >= table.Rows.Count)
   {
       // The specified row number has to be available. If not
       // NewItem has to be used to add a new row
       throw new ArgumentException("Row specified is not available");
   } // if (rowNum...

   string[] colValues = (values as string).Split(',');

   // set the specified row
   DataRow row = table.Rows[rowNumber];

   for (int i = 0; i < colValues.Length; i++)
   {
       row[i] = colValues[i];
   }

   // Update the table
   if (ShouldProcess(path, "SetItem"))
   {
       da.Update(ds, tableName);
   }

} // SetItem

/// <summary>
/// Test to see if the specified item exists.
/// </summary>
/// <param name="path">The path to the item to verify.</param>
/// <returns>True if the item is found.</returns>
protected override bool ItemExists(string path)
{
    // check if the path represented is a drive
    if (PathIsDrive(path))
    {
        return true;
    }

   // Obtain type, table name and row number from path
   string tableName;
   int rowNumber;

   PathType type = GetNamesFromPath(path, out tableName, out rowNumber);

   DatabaseTableInfo table = GetTable(tableName);

   if (type == PathType.Table)
   {
       // if specified path represents a table then DatabaseTableInfo
       // object for the same should exist
       if (table != null)
       {

<!-- p.1918 -->

             return true;
         }
    }
    else if (type == PathType.Row)
    {
        // if specified path represents a row then DatabaseTableInfo should
        // exist for the table and then specified row number must be within
        // the maximum row count in the table
        if (table != null && rowNumber < table.RowCount)
        {
            return true;
        }
    }

    return false;

 } // ItemExists

 /// <summary>
 /// Test to see if the specified path is syntactically valid.
 /// </summary>
 /// <param name="path">The path to validate.</param>
 /// <returns>True if the specified path is valid.</returns>
 protected override bool IsValidPath(string path)
 {
     bool result = true;

    // check if the path is null or empty
    if (String.IsNullOrEmpty(path))
    {
        result = false;
    }

    // convert all separators in the path to a uniform one
    path = NormalizePath(path);

    // split the path into individual chunks
    string[] pathChunks = path.Split(pathSeparator.ToCharArray());

     foreach (string pathChunk in pathChunks)
     {
         if (pathChunk.Length == 0)
         {
             result = false;
         }
     }
     return result;
 } // IsValidPath

 #endregion Item Overloads

#region Helper Methods

/// <summary>
/// Checks if a given path is actually a drive name.

<!-- p.1919 -->

/// </summary>
/// <param name="path">The path to check.</param>
/// <returns>
/// True if the path given represents a drive, false otherwise.
/// </returns>
private bool PathIsDrive(string path)
{
    // Remove the drive name and first path separator. If the
    // path is reduced to nothing, it is a drive. Also if its
    // just a drive then there wont be any path separators
    if (String.IsNullOrEmpty(
                path.Replace(this.PSDriveInfo.Root, "")) ||
        String.IsNullOrEmpty(
                path.Replace(this.PSDriveInfo.Root + pathSeparator, ""))

        )
    {
        return true;
    }
    else
    {
        return false;
    }
} // PathIsDrive

/// <summary>
/// Breaks up the path into individual elements.
/// </summary>
/// <param name="path">The path to split.</param>
/// <returns>An array of path segments.</returns>
private string[] ChunkPath(string path)
{
    // Normalize the path before splitting
    string normalPath = NormalizePath(path);

    // Return the path with the drive name and first path
    // separator character removed, split by the path separator.
    string pathNoDrive = normalPath.Replace(this.PSDriveInfo.Root
                                   + pathSeparator, "");

    return pathNoDrive.Split(pathSeparator.ToCharArray());
} // ChunkPath

/// <summary>
/// Adapts the path, making sure the correct path separator
/// character is used.
/// </summary>
/// <param name="path"></param>
/// <returns></returns>
private string NormalizePath(string path)
{
    string result = path;

    if (!String.IsNullOrEmpty(path))
    {

<!-- p.1920 -->

              result = path.Replace("/", pathSeparator);
          }

         return result;
     } // NormalizePath

      /// <summary>
      /// Chunks the path and returns the table name and the row number
      /// from the path
      /// </summary>
      /// <param name="path">Path to chunk and obtain information</param>
      /// <param name="tableName">Name of the table as represented in the
      /// path</param>
      /// <param name="rowNumber">Row number obtained from the path</param>
      /// <returns>what the path represents</returns>
      private PathType GetNamesFromPath(string path, out string tableName, out int
rowNumber)
      {
           PathType retVal = PathType.Invalid;
           rowNumber = -1;
           tableName = null;

          // Check if the path specified is a drive
          if (PathIsDrive(path))
          {
              return PathType.Database;
          }

          // chunk the path into parts
          string[] pathChunks = ChunkPath(path);

          switch (pathChunks.Length)
          {
              case 1:
                  {
                      string name = pathChunks[0];

                        if (TableNameIsValid(name))
                        {
                            tableName = name;
                            retVal = PathType.Table;
                        }
                  }
                  break;

              case 2:
                  {
                        string name = pathChunks[0];

                        if (TableNameIsValid(name))
                        {
                            tableName = name;
                        }

                        int number = SafeConvertRowNumber(pathChunks[1]);
