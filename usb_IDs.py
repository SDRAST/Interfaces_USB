# -*- coding: utf-8 -*-
"""
usb_IDs - identify USB vendors and instruments
"""
import urllib
import pickle

module_dir = "/usr/local/lib/python2.6/site-packages/Observatory/Instruments/"

def update_usb_ids():
  """
  Refresh the USB vendor and product IDs
  """
  url = "http://www.linux-usb.org/usb.ids"
  usb_ids = urllib.urlopen(url)
  lines = usb_ids.readlines()
  usb_ids.close()

  vendor_dict = {}
  part_dict = {}
  for line in lines:
    if line.strip() == "# List of known device classes, subclasses and protocols":
      break
    if line[0] == '#':
      continue
    if line[0] == '\t':
      # this is the current vendor's part
      parts = line.strip().split("  ")
      part_id = int(parts[0],16)
      part_name = parts[1]
      if part_dict.has_key(vendor_id) == False:
        part_dict[vendor_id] = {part_id: part_name}
      else:
        part_dict[vendor_id][part_id] = part_name
    if line[0].isspace() == False:
      parts = line.strip().split("  ")
      vendor_id = int(parts[0],16)
      vendor_name = parts[1]
      vendor_dict[vendor_id] = vendor_name
  pickle_file = open(module_dir+"usb_IDs.pkl","w")
  pickle.dump((vendor_dict,part_dict),pickle_file)
  pickle_file.close()
  return vendor_dict, part_dict

def get_usb_IDs():
  """
  Get the locally stored USB IDs
  """
  pickle_file = open(module_dir+"usb_IDs.pkl","r")
  vendor_dict,part_dict = pickle.load(pickle_file)
  pickle_file.close()
  return vendor_dict, part_dict
  
if __name__ == "__main__":
  vendor_dict, part_dict = get_usb_IDs()
  print vendor_dict