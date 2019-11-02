import subprocess
import xbmc

xbmc.executebuiltin( "XBMC.Action(Stop)")
xbmc.executebuiltin('Lirc.Stop')
subprocess.call(['chromium-browser', '--start-maximized', '--force-device-scale-factor=1.8'])
xbmc.executebuiltin('Lirc.Start')
