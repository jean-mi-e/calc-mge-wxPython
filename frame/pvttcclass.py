#!/usr/bin/env python3
# coding: utf-8
import wx


class Classpvttc(wx.Frame):
    """Classe du wx.TextCtrl Prix d'achat HT"""

    def __init__(self, fenetre):
        super(Classpvttc, self).__init__()

        self.lab_pvttc = wx.StaticText(fenetre, -1, "Prix de vente T.T.C.", (25, 105))
        self.pvttc = wx.TextCtrl(fenetre, -1, value="0.00", pos=(25, 125))

        sizer = wx.GridBagSizer()
        sizer.Add(self.pvttc, (25, 125), (1, 1), wx.EXPAND)

    def val_get(self):
        """Méthode permettant de vérifier si l'entrée est numérique et de retourner
        un float"""

        try:
            float(self.pvttc.GetValue())
        except ValueError:
            res = wx.MessageDialog(self, "Le PV T.T.C. n'est pas un nombre", "ERREUR",
                                   style=wx.OK | wx.ICON_ERROR | wx.CENTRE, pos=wx.DefaultPosition)
            res = res.ShowModal()

        if self.pvttc.GetValue() == '':
            self.pvttc.SetValue(float(0))

        return float(self.pvttc.GetValue())

    def lab_get(self):
        """Méthode retournant le contenu du Label de la classe"""

        return wx.Control.GetLabel(self.lab_pvttc)

    def delete(self):
        """Méthode effaçant le contenu de l'Entry de la classe"""

        return self.pvttc.SetValue('0')

    def insert(self, arg):
        """Méthode permettant de redéfinir le contenu du TextEntry"""

        return self.pvttc.SetValue(str(arg))

    def state(self, arg):
        """Méthode permettant de définir l'état de l'Entry
        Normal -> saisie autorisée
        Disabled -> saisie bloquée"""

        try:
            assert arg == 'normal' or arg == 'disabled'
        except TypeError:
            pass

        if arg == 'normal':
            self.pvttc.SetEditable(True)
        elif arg == 'disabled':
            self.pvttc.SetEditable(False)
