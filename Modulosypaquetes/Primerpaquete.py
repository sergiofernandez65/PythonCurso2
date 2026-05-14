#! /usr/bin/env python3

""" module: alpha """"

def funA():
  return "Alpha"

if __name__ == "__main__":
  print("Prefiero ser un módulo.")



from sys import path
path.append('..∖∖packages')

import extra.iota
print(extra.iota.funI())


from sys import path

path.append('..∖∖packages')

import extra.good.best.sigma
from extra.good.best.tau import funT

print(extra.good.best.sigma.funS())
print(funT())


from sys import path

path.append('..∖∖packages∖∖extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())

