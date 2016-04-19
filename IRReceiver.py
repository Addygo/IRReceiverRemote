#!/usr/bin/python
 from evdev import InputDevice, list_devices
 import socket
 import os
 import threading
 import ConfigParser
 
  class IRReceiverRemote(threading.thread):
   def IR_stop(self):
      mpd_func("stop")
     
   def IR_pause(self):
      mpd_func("pause")
  
   def IR_play(self):
      mpd_func("play")
  
   def IR_next(self):
      mpd_func("next")
  
   def IR_prev(self):
      mpd_func("previous")
  
   def SYS_halt(self):
      os.system("halt") 
      
      
   def readConfig(self, configFilePath = None):
      self.config = ConfigParser.ConfigParser()
      if configFilePath == None:
        print("[ConfigReader] Kein Configfile zum Lesen gefunden!")
      else:
        try:
          self.config.read(configFilePath)
        except:
          print("[ConfigReader] Pfad zum Configfile falsch oder nicht vorhanden!")
          return None
        
    
   def ConfigSectionMap(section):
      dict1 = {}
      options = Config.options(section)
      for option in options:
          try:
              dict1[option] = Config.get(section, option)
              if dict1[option] == -1:
                  DebugPrint("skip: %s" % option)
          except:
              print("exception on %s!" % option)
              dict1[option] = None
      return dict1
      
    
   def __init__(self):
     # function to keycode binding
     self.fun_tbl = { 
       1 : IR_stop,
       2 : IR_pause,
       3 : IR_next,
       4 : IR_prev,
       15 : SYS_halt,
       223 : IR_play,
     }
    
   
  
   for dev in [ InputDevice(fn) for fn in list_devices()]:
      if dev.name == "sunxi-ir":
         for event in dev.read_loop():
            if event.value == 1:
               try:
                  fun_tbl[event.code]()
               except KeyError:
                  print "Action for %d code is not defined" % (event.code)
