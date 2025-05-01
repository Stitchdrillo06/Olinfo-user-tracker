# Olinfo-user-tracker
Simple collection of scripts to organize olinfo user information in an sqlite database. (Win)

# Requirements

Python 3;
Git;
sqlite3 (if not using windows)

# Usage
Python and SQL scripts work for all systems, but the batch file responsible for organizing workflow is windows only and the sqlite.exe is a windows executable.

To execute, launch updDB.bat and wait for it to finish, the first time it is gonna take a while to download all information, if run again it will check for updates and download those alone.

The Output is a .sqlite database file wich can be opened through any db visualizer.

P.S: If files inside ./data folder are accidentally deleted, delete the whole ./data folder and launch updDB.bat again.
