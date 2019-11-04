#!/usr/bin/env python ///numbers of days between dates
# -*- coding: utf-8 -*-

import datetime, sys

d=sys.argv
#~ print  datetime.date.today()
#~ [datetime.date.today() if x=='-now' or x=='-today' else x for x in d]
for n, x in enumerate(d):
	if x=='-now' or x=='-today':
		e=datetime.date.today()
		#~ print e
		d[n]= e
#~ print 'd', d

if len(d)<3:
	for i in range(0, 3-len(d)):
		d.append(datetime.date.today())
		
#~ print d
try:
	a=d[1].split('-')
	aa=datetime.date(int(a[0]), int(a[1]), int(a[2]))
except AttributeError:
	aa=d[1]
try:
	b=d[2].split('-')
	bb=datetime.date(int(b[0]), int(b[1]), int(b[2]))
except AttributeError:
	bb=d[2]
#~ print a, b


cc=aa-bb
print cc
#~ print dir(datetime)
