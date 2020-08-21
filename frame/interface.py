#!/usr/bin/env python3
# coding: utf-8
import wx
import frame.fonctionscalculs as fc
import frame.mttmgeclass as seven
import frame.mtttvaclass as three
import frame.pahtclass as one
import frame.pattcclass as four
import frame.pvttcclass as five
import frame.txmgeclass as six
import frame.txtvaclass as two


class Interface(wx.Frame):
    """Notre fenêtre principale qui hérite de Frame

    Les éléments principaux sont stockés comme attributs de cette fenêtre

    Les widgets sont créés par une méthode de classe lors de l'initialisation"""

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Calculatrice de marge', size=(365, 370),
                          style=wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        icone = wx.Icon("./calcul.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icone)
        self.CentreOnScreen()
        self.panel = wx.Panel(self)
        self.parent = parent
        self._create_widgets()

    def _create_widgets(self):
        # Instanciation des widgets à partir des différentes classes
        self.list_inst_wid = [one.Classpaht(self.panel), two.Classtxtva(self.panel),
                              three.Classmtttva(self.panel), four.Classpattc(self.panel),
                              five.Classpvttc(self.panel), six.Classtxmge(self.panel),
                              seven.Classmttmge(self.panel)]
        self.listwidgets = []

        for wid in self.list_inst_wid:
            self.listwidgets.append(wid)

        button_quit = wx.Button(self.panel, label="Quitter", pos=(20, 270), size=(140, 40))
        self.Bind(wx.EVT_BUTTON, self._closebutton, button_quit)

        button_raz = wx.Button(self.panel, label="Remise à zéro", pos=(190, 270), size=(140, 40))
        self.Bind(wx.EVT_BUTTON, self._raz, button_raz)

        button_calcul = wx.Button(self.panel, label="Calcul", pos=(100, 220), size=(140, 40))
        self.Bind(wx.EVT_BUTTON, self._cliquer, button_calcul)

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
