USE master;
GO

-- Create a login for the user
CREATE LOGIN daryl WITH PASSWORD = 'daryl';
GO

-- Grant the sysadmin role to the login (TOBECHANGEDWHENIFIGUREOUTWHATSPECIFICROLESTOGIVELMFAO)
ALTER SERVER ROLE sysadmin ADD MEMBER daryl;
GO