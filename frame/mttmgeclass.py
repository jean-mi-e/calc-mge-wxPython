#!/usr/bin/env python3
# coding: utf-8
import wx


class Classmttmge(wx.Panel):
    """Classe du wx.TextCtrl Prix d'achat HT"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.lab_mttmge = wx.StaticText(self, label="Montant de la marge")
        self.mttmge = wx.TextCtrl(self, value="0.00")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lab_mttmge, flag=wx.EXPAND)
        sizer.Add(self.mttmge, proportion=1)
        sizer.Add(-1, 10)
        self.SetSizer(sizer)

        #sizer = wx.GridBagSizer()
        #sizer.Add(self.mttmge, (120, 185), (1, 1), wx.EXPAND)

    def val_get(self):
        """Méthode permettant de vérifier si l'entrée est numérique et de retourner
        un float"""

        try:
            float(self.mttmge.GetValue())
        except ValueError:
            res = wx.MessageDialog(self, "Le montant de marge n'est pas un nombre!!!", "ERREUR",
                                   style=wx.OK | wx.ICON_ERROR | wx.CENTRE, pos=wx.DefaultPosition)
            res = res.ShowModal()

        if self.mttmge.GetValue() == '':
            self.mttmge.SetValue(float(0))

        return float(self.mttmge.GetValue())

    def lab_get(self):
        """Méthode retournant le contenu du Label de la classe"""

        return wx.Control.GetLabel(self.lab_mttmge)

    def delete(self):
        """Méthode effaçant le contenu de l'Entry de la classe"""

        return self.mttmge.SetValue('0')

    def insert(self, arg):
        """Méthode permettant de redéfinir le contenu du TextEntry"""

        return self.mttmge.SetValue(str(arg))

    def state(self, arg):
        """Méthode permettant de définir l'état de l'Entry
        Normal -> saisie autorisée
        Disabled -> saisie bloquée"""

        try:
            assert arg == 'normal' or arg == 'disabled'
        except TypeError:
            pass

        if arg == 'normal':
            self.mttmge.SetEditable(True)
        elif arg == 'disabled':
            self.mttmge.SetEditable(False)
