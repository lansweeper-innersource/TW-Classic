<!-- # Compatible SQL database servers for hosting the Lansweeper database -->
Lansweeper data, reports and settings are stored in a database. Below you can find a list of supported database servers for hosting the Lansweeper database. Key differences between the database servers are listed as well, to help you decide which one to select.

Note that SQL Compact was an old database server option, which is no longer supported. If you are still using SQL Compact as your Lansweeper database server, you should [convert your database to SQL LocalDB or SQL Server](/classic/docs/convert-a-deprecated-sql-compact-database).   
For other Lansweeper installation requirements like architecture, operating system, disk space, web browser and installed software, please review [this knowledge base article](/classic/docs/lansweeper-installation-requirements).

## List of supported database servers

The database servers below are supported for hosting the Lansweeper database. Only SQL Server versions installed on a Microsoft Windows operating system are supported.

- Microsoft SQL LocalDB
- Microsoft SQL Server 2016, any edition (Express, Standard, Enterprise...) including Cumulative Update 11 or higher
- Microsoft SQL Server 2017, any edition (Express, Standard, Enterprise...) including Cumulative Update 18 or higher
- Microsoft SQL Server 2019, any edition (Express, Standard, Enterprise...) including Cumulative Update 2 or higher
- Microsoft SQL Server 2022, any edition (Express, Standard, Enterprise...)

## Database type comparison

The table below lists some key differences between the database servers. We recommend reviewing this table to determine which database server you need when installing Lansweeper. This prevents you from having to migrate your data to a different database server at a later time.

| Database server | Packaged with Lansweeper | Max database size | Support for distributed Lansweeper components | Support for multiple scanning servers | Lansweeper support status |
| --- | --- | --- | --- | --- | --- |
| SQL Compact | ✔ | 4 GB | ✘ | ✘ | unsupported from March 2020 onward |
| SQL LocalDB | ✔ | 10 GB | ✘ | ✘ | supported database server |
| SQL Server | ✘ (manual install required prior to installing Lansweeper) | - 10 GB (free Express edition 2014 or higher) - unlimited (other editions) | ✔ | ✔ | supported database server |

2.11.0.0
