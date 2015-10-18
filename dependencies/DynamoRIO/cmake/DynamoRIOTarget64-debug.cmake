#----------------------------------------------------------------
# Generated CMake target import file for configuration "Debug".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ntdll_imports" for configuration "Debug"
set_property(TARGET ntdll_imports APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(ntdll_imports PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/lib64/ntdll_imports.lib"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib64/ntdll_imports.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS ntdll_imports )
list(APPEND _IMPORT_CHECK_FILES_FOR_ntdll_imports "${_IMPORT_PREFIX}/lib64/ntdll_imports.lib" "${_IMPORT_PREFIX}/lib64/ntdll_imports.dll" )

# Import target "dynamorio" for configuration "Debug"
set_property(TARGET dynamorio APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(dynamorio PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/lib64/debug/dynamorio.lib"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG ""
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib64/debug/dynamorio.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS dynamorio )
list(APPEND _IMPORT_CHECK_FILES_FOR_dynamorio "${_IMPORT_PREFIX}/lib64/debug/dynamorio.lib" "${_IMPORT_PREFIX}/lib64/debug/dynamorio.dll" )

# Import target "drinjectlib" for configuration "Debug"
set_property(TARGET drinjectlib APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drinjectlib PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/lib64/drinjectlib.lib"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "drdecode;drhelper;drdecode;libcmtd.lib;ntdll_imports;kernel32;advapi32;imagehlp"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib64/drinjectlib.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS drinjectlib )
list(APPEND _IMPORT_CHECK_FILES_FOR_drinjectlib "${_IMPORT_PREFIX}/lib64/drinjectlib.lib" "${_IMPORT_PREFIX}/lib64/drinjectlib.dll" )

# Import target "drdecode" for configuration "Debug"
set_property(TARGET drdecode APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drdecode PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "drhelper"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib64/debug/drdecode.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS drdecode )
list(APPEND _IMPORT_CHECK_FILES_FOR_drdecode "${_IMPORT_PREFIX}/lib64/debug/drdecode.lib" )

# Import target "drhelper" for configuration "Debug"
set_property(TARGET drhelper APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drhelper PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "ASM;C"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib64/drhelper.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS drhelper )
list(APPEND _IMPORT_CHECK_FILES_FOR_drhelper "${_IMPORT_PREFIX}/lib64/drhelper.lib" )

# Import target "drconfiglib" for configuration "Debug"
set_property(TARGET drconfiglib APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drconfiglib PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/lib64/drconfiglib.lib"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "drfrontendlib"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib64/drconfiglib.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS drconfiglib )
list(APPEND _IMPORT_CHECK_FILES_FOR_drconfiglib "${_IMPORT_PREFIX}/lib64/drconfiglib.lib" "${_IMPORT_PREFIX}/lib64/drconfiglib.dll" )

# Import target "drfrontendlib" for configuration "Debug"
set_property(TARGET drfrontendlib APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drfrontendlib PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "drdecode;drhelper"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/bin64/drfrontendlib.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS drfrontendlib )
list(APPEND _IMPORT_CHECK_FILES_FOR_drfrontendlib "${_IMPORT_PREFIX}/bin64/drfrontendlib.lib" )

# Import target "drcontainers" for configuration "Debug"
set_property(TARGET drcontainers APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drcontainers PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "dynamorio;dynamorio"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drcontainers.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS drcontainers )
list(APPEND _IMPORT_CHECK_FILES_FOR_drcontainers "${_IMPORT_PREFIX}/ext/lib64/debug/drcontainers.lib" )

# Import target "drmgr" for configuration "Debug"
set_property(TARGET drmgr APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drmgr PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drmgr.lib"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "dynamorio"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drmgr.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS drmgr )
list(APPEND _IMPORT_CHECK_FILES_FOR_drmgr "${_IMPORT_PREFIX}/ext/lib64/debug/drmgr.lib" "${_IMPORT_PREFIX}/ext/lib64/debug/drmgr.dll" )

# Import target "drmgr_static" for configuration "Debug"
set_property(TARGET drmgr_static APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drmgr_static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "dynamorio"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drmgr_static.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS drmgr_static )
list(APPEND _IMPORT_CHECK_FILES_FOR_drmgr_static "${_IMPORT_PREFIX}/ext/lib64/debug/drmgr_static.lib" )

# Import target "drx" for configuration "Debug"
set_property(TARGET drx APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drx PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drx.lib"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "dynamorio;drcontainers;drmgr;ntdll_imports"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drx.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS drx )
list(APPEND _IMPORT_CHECK_FILES_FOR_drx "${_IMPORT_PREFIX}/ext/lib64/debug/drx.lib" "${_IMPORT_PREFIX}/ext/lib64/debug/drx.dll" )

# Import target "drx_static" for configuration "Debug"
set_property(TARGET drx_static APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drx_static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "dynamorio;drcontainers;drmgr_static;ntdll_imports"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drx_static.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS drx_static )
list(APPEND _IMPORT_CHECK_FILES_FOR_drx_static "${_IMPORT_PREFIX}/ext/lib64/debug/drx_static.lib" )

# Import target "drwrap" for configuration "Debug"
set_property(TARGET drwrap APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drwrap PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drwrap.lib"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "dynamorio;drmgr;drcontainers"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drwrap.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS drwrap )
list(APPEND _IMPORT_CHECK_FILES_FOR_drwrap "${_IMPORT_PREFIX}/ext/lib64/debug/drwrap.lib" "${_IMPORT_PREFIX}/ext/lib64/debug/drwrap.dll" )

# Import target "drwrap_static" for configuration "Debug"
set_property(TARGET drwrap_static APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drwrap_static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "ASM;C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "dynamorio;drmgr_static;drcontainers"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drwrap_static.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS drwrap_static )
list(APPEND _IMPORT_CHECK_FILES_FOR_drwrap_static "${_IMPORT_PREFIX}/ext/lib64/debug/drwrap_static.lib" )

# Import target "drreg" for configuration "Debug"
set_property(TARGET drreg APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drreg PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drreg.lib"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "dynamorio;drcontainers;drmgr"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drreg.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS drreg )
list(APPEND _IMPORT_CHECK_FILES_FOR_drreg "${_IMPORT_PREFIX}/ext/lib64/debug/drreg.lib" "${_IMPORT_PREFIX}/ext/lib64/debug/drreg.dll" )

# Import target "drreg_static" for configuration "Debug"
set_property(TARGET drreg_static APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drreg_static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "dynamorio;drcontainers;drmgr_static"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drreg_static.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS drreg_static )
list(APPEND _IMPORT_CHECK_FILES_FOR_drreg_static "${_IMPORT_PREFIX}/ext/lib64/debug/drreg_static.lib" )

# Import target "drsyms" for configuration "Debug"
set_property(TARGET drsyms APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drsyms PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drsyms.lib"
  IMPORTED_LINK_DEPENDENT_LIBRARIES_DEBUG "dynamorio"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG ""
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drsyms.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS drsyms )
list(APPEND _IMPORT_CHECK_FILES_FOR_drsyms "${_IMPORT_PREFIX}/ext/lib64/debug/drsyms.lib" "${_IMPORT_PREFIX}/ext/lib64/debug/drsyms.dll" )

# Import target "drsyms_static" for configuration "Debug"
set_property(TARGET drsyms_static APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drsyms_static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "C;CXX"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "libcpmtd;libcmtd;dynamorio;dbghelp;D:/derek/dr/build_package/build_debug-64/ext/drsyms/dbghelp_imports.lib;drcontainers;dwarf;elftc"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drsyms_static.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS drsyms_static )
list(APPEND _IMPORT_CHECK_FILES_FOR_drsyms_static "${_IMPORT_PREFIX}/ext/lib64/debug/drsyms_static.lib" )

# Import target "drutil" for configuration "Debug"
set_property(TARGET drutil APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drutil PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drutil.lib"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "dynamorio;drmgr"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drutil.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS drutil )
list(APPEND _IMPORT_CHECK_FILES_FOR_drutil "${_IMPORT_PREFIX}/ext/lib64/debug/drutil.lib" "${_IMPORT_PREFIX}/ext/lib64/debug/drutil.dll" )

# Import target "drutil_static" for configuration "Debug"
set_property(TARGET drutil_static APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(drutil_static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_DEBUG "dynamorio;drmgr_static"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/ext/lib64/debug/drutil_static.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS drutil_static )
list(APPEND _IMPORT_CHECK_FILES_FOR_drutil_static "${_IMPORT_PREFIX}/ext/lib64/debug/drutil_static.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
