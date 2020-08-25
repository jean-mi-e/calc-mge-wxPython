#!/usr/bin/env python3
# coding: utf-8
import wx


class Classpaht(wx.Panel):

	"""Classe du wx.TextCtrl Prix d'achat HT"""

	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		#myfont = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		#myfont.SetPointSize(9)
		self.lab_paht = wx.StaticText(self, label="Prix d'achat H.T.")
		#self.lab_paht.SetFont(myfont)
		self.paht = wx.TextCtrl(self, value="0.00")

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.lab_paht, flag=wx.EXPAND)
		sizer.Add(self.paht, proportion=1)
		sizer.Add(-1, 10)
		self.SetSizer(sizer)

	def val_get(self):
		"""Méthode permettant de vérifier si l'entrée est numérique et de retourner
		un float"""

		try:
			float(self.paht.GetValue())
		except ValueError:
			res = wx.MessageDialog(self, "Le PA H.T. n'est pas un nombre", "ERREUR",
								   style=wx.OK | wx.ICON_ERROR | wx.CENTRE, pos=wx.DefaultPosition)
			res.ShowModal()

		if self.paht.GetValue() == '':
			self.paht.SetValue(float(0))

		return float(self.paht.GetValue())

	def lab_get(self):
		"""Méthode retournant le contenu du Label de la classe"""

		return wx.Control.GetLabel(self.lab_paht)

	def delete(self):
		"""Méthode effaçant le contenu de l'Entry de la classe"""

		return self.paht.SetValue('0')

	def insert(self, arg):
		"""Méthode permettant de redéfinir le contenu du TextEntry"""

		return self.paht.SetValue(str(arg))

	def state(self, arg):
		"""Méthode permettant de définir l'état de l'Entry
		Normal -> saisie autorisée
		Disabled -> saisie bloquée"""

		try:
			assert arg == 'normal' or arg == 'disabled'
		except TypeError:
			pass

		if arg == 'normal':
			self.paht.SetEditable(True)
		elif arg == 'disabled':
			self.paht.SetEditable(False)
