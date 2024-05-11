import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)
print("test")

fc_goal = goal.compile('sickness.sickness_sinthome($sickness, $sinthome)')
engine.reset()
engine.activate("fc_sickness")


def check_sinthomes(sickness):
    sinthomes = []
    with engine.prove_goal(
        'sickness.sickness_sinthome($sickness, $sinthome)',
        sickness=sickness) \
            as gen:
        for vars, plan in gen:
            sinthomes.append(vars['sinthome'])
            # print("%s is a sinthome of %s" % (vars['sinthome'], SICKNESS))
    return sinthomes


def check_causes(sickness):
    causes = []
    with engine.prove_goal(
        'sickness.sickness_cause($sickness, $cause)',
        sickness=sickness) \
            as gen:
        for vars, plan in gen:
            causes.append(vars['cause'])
    return causes
