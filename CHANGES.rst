Changelog
=========

1.3.3v3API (unreleased)
-----------------------
 - Introduce folder_id field in campaing.py to handle local settings
   [lucabel]

1.3.2v3API (unreleased)
-----------------------
- fixed some API calls to get template folder id and fixed portlet to subscribe new users.
  [daniele]
- [BreakingChange]: change the wrapper we use to communicate with mailchimp
  from PostMonkey to mailchimp3 due to old unsupported API version.
  Adapt the code to work with v3 API
  Need to refactor and made some changes again.
  [lucabel]


1.3.1 (2018-12-10)
------------------

- Updated "wizard/confirm" in "edit" [fdelia]


1.3.0 (2017-03-27)
------------------

- Added possibility to move items in the table during
  the first step of the wizard [pnicolli]


1.2.1 (2014-08-04)
------------------

- fixed translation issues [keul]
- added script for compile translations [keul]
- fixed issue that was showing empty site when surfing
  "Campaign's items" settings [keul]


1.2 (2013-03-26)
----------------

- subscribe portlet now supports multi campaigns [amleczko]


1.1 (2013-03-12)
----------------

- translation fixes [amleczko]
- portlet hidden for anonymous [amleczko]
- make sure only published content is used [amleczko]


1.0 (2013-03-05)
----------------

- Initial release
