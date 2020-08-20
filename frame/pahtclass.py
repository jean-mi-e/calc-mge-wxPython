#!/usr/bin/env python3
# coding: utf-8
import wx


class Classpaht(wx.Frame):

	"""Classe du wx.TextCtrl Prix d'achat HT"""

	def __init__(self, fenetre):
		super(Classpaht, self).__init__()

		self.lab_paht = wx.StaticText(parent=fenetre, id=-1, label="Prix d'achat H.T.", pos=(25, 5))
		self.paht = wx.TextCtrl(fenetre, -1, value="0.00", pos=(25, 25))

		sizer = wx.GridBagSizer()
		sizer.Add(self.paht, (25, 25), (1, 1), wx.EXPAND)

	def val_get(self):
		"""Méthode permettant de vérifier si l'entrée est numérique et de retourner
		un float"""

		try:
			float(self.paht.GetValue())
		except ValueError:
			res = wx.MessageDialog(self, "Le PA H.T. n'est pas un nombre", "ERREUR",
								   style=wx.OK | wx.ICON_ERROR | wx.CENTRE, pos=wx.DefaultPosition)
			res = res.ShowModal()

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
