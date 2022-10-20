# VsCode Get a list of Disabled Extensions - Script: Export to text file  

# Work in progress

A list of DISABLED EXTENSIONS is saved in the VSCode SQLite database here:
C:\Users\MyUsername\AppData\Roaming\Code\User\globalStorage\state.vscdb

There is a table called "ItemTable", with two columns "key" and "value"
The key with the name "extensionsIdentifiers/disabled" contains a list of all the disabled extensions

This script will extract this list.
