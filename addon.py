import subprocess
import xbmc

xbmc.executebuiltin( "XBMC.Action(Stop)")
xbmc.executebuiltin('Lirc.Stop')
subprocess.call(['chromium-browser', '--start-fullscreen'])
xbmc.executebuiltin('Lirc.Start')
