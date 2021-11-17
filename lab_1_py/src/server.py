#!/usr/bin/env python

#from __future__ import print_function

from logging import log
import rospy
from rospy.topics import Publisher

from std_msgs.msg import String
from random import randint
from lab_1_py.srv import table_py, table_pyResponse
from rospy.core import loginfo

pub = rospy.Publisher('casino_topic_py', String, queue_size = 10)

def handle_add_two_ints(req):
  player_color = req.color
  player_number = req.number
  
  
  true_color_number = randint(0, 2)
  true_number = randint(0, 36)
  is_win = False
  
  
  if true_color_number == 0:
    true_color = 'green';
  elif true_color_number == 1:
    true_color = 'red'
  else:
    true_color = 'black'
    
  
  if player_number == 37:
    is_win = true_color == player_color
    
  result = ''
  
  if player_color == 'green':
    is_win = (true_number == 0) and (true_color == 'green')
  elif player_color == 'red':
    is_win = (true_number == player_number) and (true_color == 'red')
  elif player_color == 'black':
    is_win = (true_number == player_number) and (true_color == 'black')
  else:
    result = 'error'  
   
  if result != 'error':
    if is_win:
      result = 'win'
    else:
      result = 'lose'
    loginfo("color = %s, number = %d", req.color, req.number)
  
  pub.publish(result)
  
  return table_pyResponse(result)

def casino_callback_py(data):
  if data.data == 'win':
    loginfo('win')
  elif data.data == 'lose':
    loginfo('lose')
  else:
    loginfo('error')
    
def casino_server():
  rospy.init_node('casino_server')
  rospy.Subscriber('casino_topic_py', String, casino_callback_py)
  service = rospy.Service('table_py', table_py, handle_add_two_ints)
  loginfo("READY TO PLAY")
  rospy.spin()

if __name__ == "__main__":
  casino_server()