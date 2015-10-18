set dy_home=C:\fanca\dependencies\DynamoRIO
set include_dir=C:\fanca\dependencies\DynamoRIO\include
set libpath_dir=C:\fanca\dependencies\DynamoRIO\lib32\release

cl myclient10.c  /I%include_dir% /GS- /DWINDOWS /DX86_32 /link /libpath:%libpath_dir% dynamorio.lib  /dll   /out:myclient10.dll

