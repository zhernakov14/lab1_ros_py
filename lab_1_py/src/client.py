#!/usr/bin/env python

#from __future__ import print_function

import sys
import rospy
from lab_1_py.srv import *
from random import randint
from rospy.core import loginfo

# def add_two_ints_client(color, number):
#   rospy.wait_for_service('table_py')
#   try:
#     add_two_ints = rospy.ServiceProxy('table_py', table_py)
#     resp1 = add_two_ints(color, number)
#     return resp1.sum
#   except rospy.ServiceException as e:
#     print("Service call failed: %s"%e)

#def usage():
  #return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
  rospy.init_node('casino_publisher')
  
  if len(sys.argv) == 2:
    color = sys.argv[1]
    number = 37
  elif len(sys.argv) == 3:
    color = sys.argv[1]
    number = int(sys.argv[2])
  else:
    sys.exit(1)
    
  rospy.wait_for_service('table_py') 
  #try:
  client = rospy.ServiceProxy('table_py', table_py)
  res = client(color, number)
  if res.result == 'error':
    loginfo("There are only green, red and black.")
  elif res.result == 'win':
    loginfo("OMG!!! YOU WON!!!")
  else:
    defeat_responses = ['It is just not your day.', 
                        'Try again, you will probably get lucky.', 
                        'Sorry, but the casino is not for you.']
    number_defeat_response = randint(0, 2)
    loginfo("%s"%defeat_responses[number_defeat_response])
  loginfo("You can play it again.")
  loginfo("To finish, write exit.")
  
  # new_color = input()
  # print(new_color)
  
  # if(new_color.startswith('exit')):
  #   sys.exit()
  
  # sys.argv[1] = new_color
  
  # if input() != '\n':
  #   new_number = input()
  #   sys.argv[2] = new_number

  # if len(sys.argv == 2):
  #   color = sys.argv[1]
  #   number = 37
  # elif len(sys.argv) == 3:
  #   color = sys.argv[1]
  #   number = int(sys.argv[2])
        
  # except rospy.ServiceException as e:
  #   print("Service call failed: %s"%e)
   
  # print("Requesting %s+%s"%(x, y))
  # print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))