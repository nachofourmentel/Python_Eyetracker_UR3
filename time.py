# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:14:46 2017

@author: usuario
"""
from pygaze.py3compat import *
from pygaze import settings
if settings.DISPTYPE == u'psychopy':
	from pygaze._time.psychopytime import PsychoPyTime as Time
elif settings.DISPTYPE == u'pygame':
	from pygaze._time.pygametime import PyGameTime as Time
elif settings.DISPTYPE == u'opensesame':
	from pygaze._time.ostime import OSTime as Time
else:
	raise Exception(u'Unexpected disptype : %s' % disptype)

import pygaze

def expstart():
	
	"""Time is set to 0 upon calling this"""
	
	clock.expstart()

	
def get_time():
	
	"""Returns the current time in milliseconds
	
	arguments
	None
	
	keyword arguments
	None
	
	returns
	time		--	current time in milliseconds, as measured from
				expbegintime
	"""
	
	return clock.get_time()


def pause(pausetime):
	
	"""Pauses the experiment for the given number of milliseconds
	
	arguments
	pausetime	--	time to pause in milliseconds
	
	keyword arguments
	None
	
	returns
	pausetime	--	the actual duration of the pause in milliseconds
	"""
	
	return clock.pause(pausetime)


def expend():
	
	"""Completely ends the experiment (only call this at the very end!)
	
	arguments
	None
	
	keyword arguments
	None
	
	returns
	endtime		--	experiment ending time in milliseconds, as measured
				from expbegintime
	"""
	
	return clock.expend()

# Create a singleton clock 
clock = Time()
clock.expstart()