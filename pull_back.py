#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 12:47:14 2017

@author: jithin

A module of functions to study the Pullback attractor.
"""
import matplotlib.pyplot as plt
import numpy as np
def fwd_tractor(v,xspace,r,dt=0.005, limy = []):
    """
        Plots the forward attractor governed by the function v 
        for the initial conditions in xspace for r steps of     
        size dt.
    """
    for x_0 in xspace:
        t=np.zeros(r)
        x=np.zeros(r+1)
        x[0]= x_0
        for i in range(r):
            t[i]=i*dt
            x[i+1]=x[i]+dt*v(x[i],t[i])
        plt.plot(t,x[:-1])
        if limy != []:
            plt.ylim(limy)
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title('Forward attractor')
    
def pull_tractor(v,tspace,xspace,r,dt=0.005, limy = []):
    """
        Plots the forward attractor governed by the function v 
        for the initial conditions in xspace for r steps of     
        size dt.
    """
    for x_0 in xspace:
        for t0 in tspace:
            t=np.zeros(r)
            x=np.zeros(r+1)
            x[0]= x_0
            for i in range(r):
                t[i]=i*dt +t0
                x[i+1]=x[i]+dt*v(x[i],t[i])
            plt.plot(t,x[:-1])
            if limy != []:
                plt.ylim(limy)
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title('Pullback attractor')