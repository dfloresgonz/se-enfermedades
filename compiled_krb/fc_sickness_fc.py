# fc_sickness_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def exact_sinthome(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('sickness', 'sinthome_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('sickness', 'sickness_sinthome',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def causes(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('sickness', 'cause_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('sickness', 'sickness_cause',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_sickness')
  
  fc_rule.fc_rule('exact_sinthome', This_rule_base, exact_sinthome,
    (('sickness', 'sinthome_of',
      (contexts.variable('sinthome'),
       contexts.variable('sickness'),),
      False),),
    (contexts.variable('sickness'),
     contexts.variable('sinthome'),))
  
  fc_rule.fc_rule('causes', This_rule_base, causes,
    (('sickness', 'cause_of',
      (contexts.variable('cause'),
       contexts.variable('sickness'),),
      False),),
    (contexts.variable('sickness'),
     contexts.variable('cause'),))


Krb_filename = '../fc_sickness.krb'
Krb_lineno_map = (
    ((12, 16), (3, 3)),
    ((17, 19), (5, 5)),
    ((28, 32), (9, 9)),
    ((33, 35), (11, 11)),
)
