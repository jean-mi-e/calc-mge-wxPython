#!/usr/bin/env python3
# coding: utf-8
import wx


class Classtxmge(wx.Frame):
    """Classe du wx.TextCtrl Prix d'achat HT"""

    def __init__(self, fenetre):
        super(Classtxmge, self).__init__()

        self.lab_txmge = wx.StaticText(fenetre, -1, "Taux de marge", (210, 105))
        self.txmge = wx.TextCtrl(fenetre, -1, value="0.00", pos=(210, 125))

        sizer = wx.GridBagSizer()
        sizer.Add(self.txmge, (210, 125), (1, 1), wx.EXPAND)

    def val_get(self):
        """Méthode permettant de vérifier si l'entrée est numérique et de retourner
        un float"""

        try:
            float(self.txmge.GetValue())
        except ValueError:
            res = wx.MessageDialog(self, "Le taux de marge n'est pas un nombre", "ERREUR",
                                   style=wx.OK | wx.ICON_ERROR | wx.CENTRE, pos=wx.DefaultPosition)
            res = res.ShowModal()

        if self.txmge.GetValue() == '':
            self.txmge.SetValue(float(0))

        return float(self.txmge.GetValue())

    def lab_get(self):
        """Méthode retournant le contenu du Label de la classe"""

        return wx.Control.GetLabel(self.lab_txmge)

    def delete(self):
        """Méthode effaçant le contenu de l'Entry de la classe"""

        return self.txmge.SetValue('0')

    def insert(self, arg):
        """Méthode permettant de redéfinir le contenu du TextEntry"""

        return self.txmge.SetValue(str(arg))

    def state(self, arg):
        """Méthode permettant de définir l'état de l'Entry
        Normal -> saisie autorisée
        Disabled -> saisie bloquée"""

        try:
            assert arg == 'normal' or arg == 'disabled'
        except TypeError:
            pass

        if arg == 'normal':
            self.txmge.SetEditable(True)
        elif arg == 'disabled':
            self.txmge.SetEditable(False)
