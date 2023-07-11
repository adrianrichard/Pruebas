"""
================================================================================
fixfrozenpaths.py:
  setup path/cwd context for all frozen scripts (part of the frigcal system)

For frozen apps/exes, fix module+resource visibility.  This configures
sys.path and the CWD as needed for the freeze tool used, to grant importers
access to these items.  This module is imported by most scripts frozen in
the frigcal package; it updates the global sys.path and CWD in-place.

In the frozen package, all command-line scripts are frozen executables without 
a ".py" extension, but otherwise work the same, and require no separate Python
install.  In the Mac app, running the app itself launches the frigcal GUI; 
on Windows an Linux, the launcher-GUI executable must be started directly.

The logic here was originally hashed out in PyEdit's file of the same name;
see that system's more-complex version for additional background details.

FORMER CAVEAT: an os.chdir(exedir) for PyInstaller apps was used to make the
empty __file__ dir portably map to the install dir in sys.argv[0] (instead of the
_MEIPASS temp unzip folder), but precluded using any relative paths in command
lines.  This isn't an issue in PyEdit or PyMailGUI (they have no or rare args),
but utilities in both frigcal and mergeall process file paths.  Omitting the
chdir almost works, but the launcher then couldn't find its icons, help, and
script if run from elsewhere via a command line (instead of clicked directly).

   FIXED: the chdir is no longer run; instead, clients call fetchMyInstallDir()
   to select the install path explicitly per deployment mode -- from __file __
   for source and Mac apps, and sys.argv[0] for PyInstaller exes.  The cwd is
   unchanged, so relative paths work in all frozen executables' command lines.

   Exception: both frigcal-launcher.pyw and frigcal.py manually os.chdir() to
   the install dir returned from fetchMyInstallDir() early, so they can access 
   their data relative to "." easily; neither has any command-line arguments.
   Ditto for searchcals.py and makenewcaledar.py: both chdir to the install
   dir to make relative calendar paths map to it, and have no pathname args. 
================================================================================
"""

import sys, os
RunningOnMac     = sys.platform.startswith('darwin')
RunningOnWindows = sys.platform.startswith('win')
RunningOnLinux   = sys.platform.startswith('linux')

DEBUG = False
if DEBUG:
    print('file', __file__)           # this in _MEI* (parent's = 'frigcal.py')
    print('argv', sys.argv[0])        # 'frigcal.exe' (+path if not in cwd)
    print('exec', sys.executable)     # 'C:\...\frigcal.exe' (abs of argv[0])
    print('path', sys.path)           # just 2 _MEI* temp unzip folder paths
    print('cwd ', os.getcwd())        # 'C:\...' frigcal.exe dir (iff clicked!)

#===============================================================================

# Set global import-path context
    
if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
    #
    # 1) Mac py2app app-bundle folder distribution
    # Frozen importer's bootloader is in Frigcal.app's Content/MacOS dir.
    # Add '.' for importing config module in app's Content/Resources dir.
    # dirname(__file__) and cwd work for icons, UserGuide.html, scripts,
    # and imports: code is source files, run by the app's bundled Python.
    # Ok to use cwd here: py2app cds to the data dir by default anyhow. 
    #
    sys.path.append(os.getcwd())    # for configs .py

elif hasattr(sys, 'frozen') and (RunningOnWindows or RunningOnLinux):
    #
    # 2) Windows and Linux PyInstaller single-file executable distribution
    # Use exe's path (not temp _MEI*) for config module and all data items.
    # The config module cannot be in PyInstaller's auto-unzip Temp dir.
    # DROPPED os.chdir(): this made empty __file__ dir map to install dir,
    # but precluded any relative paths in cmdline args to frozen exes; see
    # fetchMyInstallDir() below for the later explicit-install-dir scheme.
    #
    exepath = sys.argv[0]
    exedir  = os.path.dirname(os.path.abspath(exepath))
    sys.path.append(exedir)         # for configs .py import
    ##os.chdir(exedir)              # for extras => now call fetchMyInstallDir!
    
else:
    #
    # 3) Portable Source code distributions - no tweaking required
    # The src dir is on sys.path: no action required for imports.
    # Data will be located by dirname(__file__) and/or cwd.
    pass

#===============================================================================

def fetchMyInstallDir(__file__):     # not global __file__
    """
    --------------------------------------------------------
    call this to fetch folder where extra items reside;
    use to access installed icons, help, readme, scripts;
    replaces former os.chdir() which precluded rel paths;
    the return value is always an absolute pathname;
    
    pass importer's __file__ to __file__ arg: for frozen
    Mac apps, this module's dir(__file__) is in a zipfile,
    and differs from the importer's dir(__file__); they're
    the same for source code, and unused for Win/Lin exes;
    --------------------------------------------------------
    """
    
    if hasattr(sys, 'frozen') and (RunningOnWindows or RunningOnLinux):
        #
        # PyInstaller executable: from sys.argv[0] = exe's dir;
        # __file__ dir is empty and cwd may be any user folder
        # if the importer is run from a command line elsewhere;
        #
        exepath = sys.argv[0]
        exedir  = os.path.dirname(os.path.abspath(exepath))
        return exedir

    else:
        #
        # Mac app bundle or source-code: from __file__ as usual;
        # cwd is anywhere: return importing file's install folder;
        # this mod's __file__ is *not* ok to use here for frozen
        # Mac apps: it's in a zipfile, not importer's Resources/;
        #
        srcpath = __file__
        srcdir  = os.path.dirname(os.path.abspath(srcpath))
        return srcdir
