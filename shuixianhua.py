#!/usr/bin/env python
# -*- coding:utf-8 -*-


def shuixianhua():
	for i in range(1,10):
		for j in range(10):
			for k in range(10):
				if i*i*i+j*j*j+k*k*k==i*100+j*10+k:
					print i*100+j*10+k


if __name__=='__main__':
	shuixianhua()
