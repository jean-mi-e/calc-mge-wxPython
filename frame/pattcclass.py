#!/usr/bin/env python3
# coding: utf-8
import wx


class Classpattc(wx.Frame):
    """Classe du wx.TextCtrl Prix d'achat HT"""

    def __init__(self, fenetre):
        super(Classpattc, self).__init__()

        self.lab_pattc = wx.StaticText(fenetre, -1, "Prix d'achat T.T.C.", (210, 55))
        self.pattc = wx.TextCtrl(fenetre, -1, value="0.00", pos=(210, 75))

        sizer = wx.GridBagSizer()
        sizer.Add(self.pattc, (210, 75), (1, 1), wx.EXPAND)

    def val_get(self):
        """Méthode permettant de vérifier si l'entrée est numérique et de retourner
        un float"""

        try:
            float(self.pattc.GetValue())
        except ValueError:
            res = wx.MessageDialog(self, "Le PA T.T.C. n'est pas un nombre", "ERREUR",
                                   style=wx.OK | wx.ICON_ERROR | wx.CENTRE, pos=wx.DefaultPosition)
            res = res.ShowModal()

        if self.pattc.GetValue() == '':
            self.pattc.SetValue(float(0))

        return float(self.pattc.GetValue())

    def lab_get(self):
        """Méthode retournant le contenu du Label de la classe"""

        return wx.Control.GetLabel(self.lab_pattc)

    def delete(self):
        """Méthode effaçant le contenu de l'Entry de la classe"""

        return self.pattc.SetValue('0')

    def insert(self, arg):
        """Méthode permettant de redéfinir le contenu du TextEntry"""

        return self.pattc.SetValue(str(arg))

    def state(self, arg):
        """Méthode permettant de définir l'état de l'Entry
        Normal -> saisie autorisée
        Disabled -> saisie bloquée"""

        try:
            assert arg == 'normal' or arg == 'disabled'
        except TypeError:
            pass

        if arg == 'normal':
            self.pattc.SetEditable(True)
        elif arg == 'disabled':
            self.pattc.SetEditable(False)
