from zinolib.ritz import ritz, notifier, parse_tcl_config, Maintenance
from pprint import pprint
from time import sleep
import re
import argparse
import sys
from datetime import datetime, timedelta
import logging

def main():
  parser = argparse.ArgumentParser(description='Process some integers.')

  parser.add_argument('--prod', action='store_true')
  parser.add_argument('--remove-all-pms', action='store_true')

  args = parser.parse_args()
  conf = parse_tcl_config("~/.ritz.tcl")
  pprint(conf)

  if args.prod:
    c_server = conf["default"]["Server"]
    c_user   = conf["default"]["User"]
    c_secret = conf["default"]["Secret"]
  else:
    c_server = conf["UNINETT-backup"]["Server"]
    c_user   = conf["UNINETT-backup"]["User"]
    c_secret = conf["UNINETT-backup"]["Secret"]

  logging.basicConfig()
  logging.getLogger().setLevel(logging.DEBUG)
  requests_log = logging.getLogger("socket")
  requests_log.setLevel(logging.DEBUG)
  requests_log.propagate = True






  sess = ritz(c_server)
  sess.connect()
  sess.authenticate(c_user, c_secret)
  maintenance = Maintenance(sess)

  print("List all PMs:")
  pm = maintenance.list()
  print(pm)
  #for i in pm:
  #  print("canceling %d" % i)
  #  maintenance.cancel(i)

  print("Schedule test pm:")
  pm = maintenance.add_device(datetime.now()+timedelta(minutes=1),
                          datetime.now()+timedelta(minutes=2),
                          "teknobyen-gw*", m_type='str')
  print("Scheduled")

  print("List all PMs:")
  pms = maintenance.list()
  print(pm)

  print("get_details:")
  print(maintenance.get_details(pm))

  print("get_log:")
  print(maintenance.get_log(pm))

  print("add_log:")
  maintenance.add_log(pm, "This is a test log :)")

  print("get_details:")
  print(maintenance.get_details(pm))

  print("get_log:")
  print(maintenance.get_log(pm))

  print("get_matching:")
  print(maintenance.get_matching(pm))

  print("cancel:")
  print(maintenance.cancel(pm))


  return






if __name__ == "__main__":
  main()
