import subprocess
import xbmc

xbmc.executebuiltin( "XBMC.Action(Stop)")
xbmc.executebuiltin('Lirc.Stop')
subprocess.call(['chromium-browser', '--start-maximized'])
xbmc.executebuiltin('Lirc.Start')
