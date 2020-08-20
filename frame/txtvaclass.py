#!/usr/bin/env python3
# coding: utf-8
import wx


class Classtxtva(wx.Frame):
	"""Classe du tk.Entry Taux de la TVA"""

	def __init__(self, fenetre):
		super(Classtxtva, self).__init__()

		self.lab_txtva = wx.StaticText(fenetre, -1, "Taux de T.V.A.", (210, 5))
		self.listTaux = ["20 %", "10 %", "5,50 %", "2,10 %", "0 %", "Inconnu"]

		self.combo = wx.ComboBox(fenetre, -1, value=self.listTaux[0], choices=self.listTaux, pos=(210, 25),
								 style=wx.CB_READONLY | wx.CB_DROPDOWN)

		sizer = wx.GridBagSizer()
		sizer.Add(self.combo, (210, 25), (1, 1), wx.EXPAND)

	def val_get(self):
		"""Méthode permettant de vérifier si l'entrée est numérique et de retourner un float"""

		if self.combo.GetStringSelection() == self.listTaux[5]:
			txselec = self.listTaux[5]
		else:
			txselec = self.combo.GetStringSelection()
			txselec = txselec[:-2]
			if txselec == '5,50':
				txselec = 5.5
			elif txselec == '2,10':
				txselec = 2.1
			txselec = float(txselec)

		return txselec

	def lab_get(self):
		"""Méthode retournant le contenu du Label de la classe"""

		return wx.Control.GetLabel(self.lab_txtva)

	def delete(self):
		"""Méthode effaçant le contenu de l'Entry de la classe"""

		return self.combo.SetSelection(self.listTaux[0])

	def insert(self, arg):
		"""Méthode permettant de définir le taux de TVA dans l'OptionMenu"""

		val_arg = {float(20): '0', float(10): '1', 5.5: '2', 2.1: '3', float(0): '4', "Inconnu": 5}
		if arg in val_arg.keys():
			arg = val_arg[arg]
			return self.combo.SetValue(self.listTaux[int(arg)])
		else:
			res = wx.MessageDialog(self, "Vous avez du faire une erreur de saisie \n"
										 f"Le Taux de TVA {arg:.2f}% n'existe pas.", "ERREUR",
								   style=wx.OK | wx.ICON_ERROR | wx.CENTRE, pos=wx.DefaultPosition)
			res = res.ShowModal()
			return self.combo.SetValue(arg)

	def raz(self):

		self.combo.SetValue(self.listTaux[0])