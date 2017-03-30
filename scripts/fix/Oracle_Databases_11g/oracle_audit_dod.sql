-- TODO need to add fine grained auditing if confidentiality is sensitive or classified
audit all by access;
audit all privileges by access;
audit alter database link by access;
audit alter java class by access;
audit alter java resource by access;
audit alter java source by access;
audit alter mining model by access;
audit alter public database link by access;
audit alter sequence by access;
audit alter table by access;
audit comment edition by access;
audit comment mining model by access;
audit comment table by access;
audit create java class by access;
audit create java resource by access;
audit create java source by access;
audit debug procedure by access;
audit drop java class by access;
audit drop java resource by access;
audit drop java source by access;
audit execute assembly;
audit exempt access policy by access;
audit exempt identity policy by access;
audit grant directory by access;
audit grant edition by access;
audit grant mining model by access;
audit grant procedure by access;
audit grant sequence by access;
audit grant table by access;
audit grant type by access;
audit sysdba by access;
audit sysoper by access;
-- the following are not included in the STIG, but show up in the checks
audit direct_path unload by access;
audit direct_path load by access;
-- The following SQL statements will disable audits set by the commands above that are not required:
noaudit execute library;
audit rename on default by access;
-- If application objects have already been created, then the audit rename on object statement
-- should be issued for all application objects.
--audit rename on [application object name] by access;