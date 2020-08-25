#!/usr/bin/env python3
# coding: utf-8
import wx
import frame.fonctionscalculs as fc
import frame.mttmgeclass as mttmge
import frame.mtttvaclass as mtttva
import frame.pahtclass as paht
import frame.pattcclass as pattc
import frame.pvttcclass as pvttc
import frame.txmgeclass as txmge
import frame.txtvaclass as txtva


class Interface(wx.Frame):
    """Notre fenêtre principale qui hérite de Frame

    Les éléments principaux sont stockés comme attributs de cette fenêtre

    Les widgets sont créés par une méthode de classe lors de l'initialisation"""

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Calculatrice de marge', size=(365, 375),
                          style=wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        icone = wx.Icon("./calcul.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icone)
        self.CentreOnScreen()
        self._initui()

    def _initui(self):

        self.panel = wx.Panel(self)

        # Instanciation des widgets à partir des différentes classes
        self.list_inst_wid = [paht.Classpaht(self.panel), txtva.Classtxtva(self.panel),
                              mtttva.Classmtttva(self.panel), pattc.Classpattc(self.panel),
                              pvttc.Classpvttc(self.panel), txmge.Classtxmge(self.panel),
                              mttmge.Classmttmge(self.panel)]
        self.listwidgets = []

        for wid in self.list_inst_wid:
            self.listwidgets.append(wid)

        # Création des boutons de l'interface
        button_quit = wx.Button(self.panel, label="Quitter", size=(140, 40))
        self.Bind(wx.EVT_BUTTON, self._closebutton, button_quit)

        button_raz = wx.Button(self.panel, label="Remise à zéro", size=(140, 40))
        self.Bind(wx.EVT_BUTTON, self._raz, button_raz)

        button_calcul = wx.Button(self.panel, label="Calcul", size=(140, 40))
        self.Bind(wx.EVT_BUTTON, self._cliquer, button_calcul)

        # Création du sizer principal qui contiendra tous les autres
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Mise en place des différents sizer et de leur contenu

        sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer1.AddSpacer(30)
        sizer1.Add(self.listwidgets[0], flag=wx.TOP, border=15)
        sizer1.AddSpacer(60)
        sizer1.Add(self.listwidgets[1], flag=wx.TOP, border=15)

        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer2.AddSpacer(30)
        sizer2.Add(self.listwidgets[2])
        sizer2.AddSpacer(60)
        sizer2.Add(self.listwidgets[3])

        sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer3.AddSpacer(30)
        sizer3.Add(self.listwidgets[4])
        sizer3.AddSpacer(60)
        sizer3.Add(self.listwidgets[5])

        sizer4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer4.AddSpacer(110)
        sizer4.Add(self.listwidgets[6])

        sizer5 = wx.BoxSizer(wx.VERTICAL)
        sizer5.AddSpacer(10)

        sizer6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer6.AddSpacer(100)
        sizer6.Add(button_calcul)

        sizer7 = wx.BoxSizer(wx.VERTICAL)
        sizer7.AddSpacer(10)

        sizer8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer8.Add(button_quit, flag=wx.LEFT, border=25)
        sizer8.Add(button_raz, flag=wx.LEFT, border=20)

        list_sizer = [sizer1, sizer2, sizer3, sizer4, sizer5, sizer6, sizer7, sizer8]

        for elt in list_sizer:
            sizer.Add(elt)

        self.panel.SetSizer(sizer)

        # Gestion des évènements saisie clavier
        self.Bind(wx.EVT_CHAR_HOOK, self._onchar)

        # Création de listes des libellés et entry instanciés
        self.list_labels = [self.listwidgets[0].lab_get(), self.listwidgets[1].lab_get(),
                            self.listwidgets[2].lab_get(), self.listwidgets[3].lab_get(),
                            self.listwidgets[4].lab_get(), self.listwidgets[5].lab_get(),
                            self.listwidgets[6].lab_get()]

        self.list_entry = [self.listwidgets[0], self.listwidgets[2], self.listwidgets[3],
                           self.listwidgets[4], self.listwidgets[5], self.listwidgets[6]]

    def _cliquer(self, event):
        """Méthode détaillant les étapes principales du calcul.
        
        On lance les contrôles et calculs pour trouver les résultats souhaités."""

        # Controle du nombre de données renseignées
        if self._ctrl_nb_data():
            res = wx.MessageDialog(self, "Vous devez renseigner au minimum 3 données \n"
                                         "pour avoir un maximum de résultats", "ERREUR",
                                   style=wx.OK | wx.ICON_WARNING | wx.CENTRE, pos=wx.DefaultPosition)
            res.ShowModal()

        self.list_var = self._recup_val()

        # On crée une liste des calculs à réaliser
        self.list_calculs = [fc.calc_paht(*self.list_var), fc.calc_txtva(*self.list_var),
                             fc.calc_mtttva(*self.list_var), fc.calc_pattc(*self.list_var),
                             fc.calc_pvttc(*self.list_var), fc.calc_txmge(*self.list_var),
                             fc.calc_mttmge(*self.list_var)]

        # On crée une liste vide pour insérer les résultats
        self.list_resultats = []

        # On effectue les calculs et on les places dans la liste de résultats
        for calc in self.list_calculs:
            self.list_resultats.append(calc)

        # Contrôles de cohérence
        if self.list_resultats[1] == 'Inconnu' or self.list_resultats[1] == float(0):
            control = round(self.list_resultats[4] - self.list_resultats[0], 2)
        else:
            control = round(self.list_resultats[4] / (1 + (self.list_resultats[1] / 100)) - self.list_resultats[0], 2)

        if control != self.list_resultats[6]:
            res = wx.MessageDialog(self, "Les données saisies contiennent une anomalie et/ou "
                                         "ne suffisent pas à calculer un résultat juste.", "ERREUR",
                                   style=wx.OK | wx.ICON_ERROR | wx.CENTRE, pos=wx.DefaultPosition)
            res.ShowModal()

        # mise à jour des Entry
        idx = 0
        for elt in self.list_entry:
            elt.delete()
            if idx == 1:  # On saute le résultat txtva car il fonctionne différement des autres (OptionMenu pas Entry)
                idx = 2
            elt.insert(self.list_resultats[idx])
            idx += 1

        self.listwidgets[1].insert(self.list_resultats[1])

        # Mise en state='disabled' les widgets pour figer les résultats
        for elt in self.list_entry:
            elt.state('disabled')

    def _recup_val(self):
        """Affectation des valeurs saisies dans les entry à une liste."""

        list_val = []
        for elt in self.listwidgets:
            list_val.append(elt.val_get())

        return list_val

    def _ctrl_nb_data(self):
        """Méthode vérifiant qu'au moins 3 données ont été renseignées pour les calculs"""

        idx = 0
        list_control = list(self._recup_val())
        del list_control[1]
        for elt in list_control:
            if str(elt) != '0.0' and str(elt) != '':
                idx += 1

        if self.listwidgets[1].val_get() != 'Inconnu':
            idx += 1

        if idx < 3:
            return True
        else:
            return False

    def _raz(self, event):
        """Méthode remettant tous les Widgets de saisie en mode initial"""

        for elt in self.list_entry:
            elt.state('normal')
            elt.delete()
            elt.insert(0.0)

        self.listwidgets[1].raz()

    def _onchar(self, event):
        """Méthode permettant de récupérer le code des touches clavier qui sont utilisées.

        Si la touche Escape est utilisée on ferme l'application
        Si la touche Entrée est utilisée on lance les calculs."""

        keycode = event.GetKeyCode()

        if keycode == wx.WXK_ESCAPE:
            self.Close(True)
        elif keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            self._cliquer(event)
        else:
            event.Skip()

    def _closebutton(self, event):
        self.Close(True)


if __name__ == "__main__":
    app = wx.App()
    frame = Interface(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
