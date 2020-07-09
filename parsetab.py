
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSUREleftASIGNEQleftRPTVASIGN ASIGN EQ EQ2 ID N PR PR RE RPT RPT SU V Vresultado : s\n    |\xa0repexp : srep : RPT N V ss : RPT N V ASIGN ID EQ EQ2 s\n        | RPT ID V ASIGN ID EQ EQ2 ss : ASIGN ID EQ EQ2 ss : Ns : IDs : s SU s\n        | s RE ss : RE Ns : PR ID \n    | PR s \n    | PR N'
    
_lr_action_items = {'RPT':([0,9,10,11,22,29,38,39,43,],[4,19,19,19,19,19,19,19,19,]),'ASIGN':([0,9,10,11,22,23,29,30,38,39,43,],[6,6,6,6,26,28,6,34,6,6,6,]),'N':([0,4,8,9,10,11,19,22,29,38,39,43,],[5,12,15,18,5,5,25,5,5,5,5,5,]),'ID':([0,4,6,9,10,11,19,22,26,28,29,34,38,39,43,],[7,13,14,16,7,7,13,7,31,32,7,37,7,7,7,]),'RE':([0,2,5,7,9,10,11,15,16,17,18,20,21,22,27,29,33,38,39,41,42,43,44,],[8,11,-8,-9,8,8,8,-12,-9,11,-8,-10,-11,8,11,8,11,8,8,11,11,8,11,]),'PR':([0,9,10,11,22,29,38,39,43,],[9,9,9,9,9,9,9,9,9,]),'$end':([1,2,3,5,7,15,16,17,18,20,21,27,33,41,42,44,],[0,-1,-2,-8,-9,-12,-9,-14,-8,-10,-11,-4,-7,-5,-6,-5,]),'SU':([2,5,7,15,16,17,18,20,21,27,33,41,42,44,],[10,-8,-9,-12,-9,10,-8,-10,-11,10,10,10,10,10,]),'V':([12,13,25,],[22,23,30,]),'EQ':([14,31,32,37,],[24,35,36,40,]),'EQ2':([24,35,36,40,],[29,38,39,43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'resultado':([0,],[1,]),'s':([0,9,10,11,22,29,38,39,43,],[2,17,20,21,27,33,41,42,44,]),'rep':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> resultado","S'",1,None,None,None),
  ('resultado -> s','resultado',1,'p_resultado','Interpreter.py',64),
  ('resultado -> rep','resultado',1,'p_resultado','Interpreter.py',65),
  ('exp -> s','exp',1,'p_RPT','Interpreter.py',68),
  ('rep -> RPT N V s','rep',4,'p_repetir_mostrar','Interpreter.py',72),
  ('s -> RPT N V ASIGN ID EQ EQ2 s','s',8,'p_repetir_zeromasigual','Interpreter.py',82),
  ('s -> RPT ID V ASIGN ID EQ EQ2 s','s',8,'p_repetir_zeromasigual','Interpreter.py',83),
  ('s -> ASIGN ID EQ EQ2 s','s',5,'p_asignacion','Interpreter.py',90),
  ('s -> N','s',1,'p_expr_num','Interpreter.py',94),
  ('s -> ID','s',1,'p_expr_id','Interpreter.py',98),
  ('s -> s SU s','s',3,'p_expr_op','Interpreter.py',106),
  ('s -> s RE s','s',3,'p_expr_op','Interpreter.py',107),
  ('s -> RE N','s',2,'p_expr_num_neg','Interpreter.py',114),
  ('s -> PR ID','s',2,'p_PR','Interpreter.py',121),
  ('s -> PR s','s',2,'p_PR','Interpreter.py',122),
  ('s -> PR N','s',2,'p_PR','Interpreter.py',123),
]
