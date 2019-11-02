import subprocess
import xbmc

xbmc.executebuiltin( "XBMC.Action(Stop)")
xbmc.executebuiltin('Lirc.Stop')
subprocess.call("/usr/lib/chromium-browser/chromium-browser --start-fullscreen")
xbmc.executebuiltin('Lirc.Start')
