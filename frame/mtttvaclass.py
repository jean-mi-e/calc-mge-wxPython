#!/usr/bin/env python3
# coding: utf-8
import wx


class Classmtttva(wx.Frame):
    """Classe du wx.TextCtrl Prix d'achat HT"""

    def __init__(self, fenetre):
        super(Classmtttva, self).__init__()

        self.lab_mtttva = wx.StaticText(fenetre, -1, "Montant T.V.A.", (25, 55))
        self.mtttva = wx.TextCtrl(fenetre, -1, value="0.00", pos=(25, 75))

        sizer = wx.GridBagSizer()
        sizer.Add(self.mtttva, (25, 75), (1, 1), wx.EXPAND)

    def val_get(self):
        """Méthode permettant de vérifier si l'entrée est numérique et de retourner
        un float"""

        try:
            float(self.mtttva.GetValue())
        except ValueError:
            res = wx.MessageDialog(self, "Le montant de T.V.A. n'est pas un nombre", "ERREUR",
                                   style=wx.OK | wx.ICON_ERROR | wx.CENTRE, pos=wx.DefaultPosition)
            res = res.ShowModal()

        if self.mtttva.GetValue() == '':
            self.mtttva.SetValue(float(0))

        return float(self.mtttva.GetValue())

    def lab_get(self):
        """Méthode retournant le contenu du Label de la classe"""

        return wx.Control.GetLabel(self.lab_mtttva)

    def delete(self):
        """Méthode effaçant le contenu de l'Entry de la classe"""

        return self.mtttva.SetValue('0')

    def insert(self, arg):
        """Méthode permettant de redéfinir le contenu du TextEntry"""

        return self.mtttva.SetValue(str(arg))

    def state(self, arg):
        """Méthode permettant de définir l'état de l'Entry
        Normal -> saisie autorisée
        Disabled -> saisie bloquée"""

        try:
            assert arg == 'normal' or arg == 'disabled'
        except TypeError:
            pass

        if arg == 'normal':
            self.mtttva.SetEditable(True)
        elif arg == 'disabled':
            self.mtttva.SetEditable(False)
