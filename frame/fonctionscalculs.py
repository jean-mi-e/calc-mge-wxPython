#!/usr/bin/env python3
# coding: utf-8

def calc_paht(paht, txtva, mtttva, pattc, pvttc, txmge, mttmge):
    """Fonction calculant le prix d'achat HT s'il n'est pas renseigné"""

    if txtva == 'Inconnu':
        txtva = float(0)

    if paht != 0:
        pass
    elif txtva != 0 and mtttva != 0:
        paht = round((mtttva * 100) / txtva, 2)
    elif txtva != 0 and pattc != 0:
        paht = round(pattc / (1 + (txtva / 100)), 2)
    elif txtva != 0 and pvttc != 0 and txmge != 0:
        paht = round((pvttc / (1 + (txmge / 100))) / (1 + (txtva / 100)), 2)
    elif mtttva != 0 and pattc != 0:
        paht = round(pattc - mtttva, 2)
    elif mtttva != 0 and pvttc != 0 and txmge != 0:
        paht = round((pvttc / (1 + (txmge / 100))) - mtttva, 2)
    elif mtttva == 0 and txtva == 0 and pattc != 0:
        paht = round(pattc, 2)
    elif mtttva == 0 and txtva == 0 and pvttc != 0 and txmge != 0:
        paht = round(pvttc / (1 + (txmge / 100)), 2)
    elif mtttva == 0 and txtva == 0 and pvttc != 0 and mttmge != 0:
        paht = round(pvttc - mttmge, 2)
    return paht


def calc_txtva(paht, txtva, mtttva, pattc, pvttc, txmge, mttmge):
    """Fonction calculant le taux de TVA s'il n'est pas renseigné"""

    if txtva == 'Inconnu':
        txtva = float(0)
    if mtttva != 0:
        mtttva = calc_mtttva(paht, txtva, mtttva, pattc, pvttc, txmge, mttmge)

    if txtva != 0:
        pass
    elif paht != 0 and mtttva != 0:
        txtva = round((mtttva / paht) * 100, 2)
    elif paht != 0 and pattc != 0:
        txtva = round(((pattc - paht) / paht) * 100, 2)
    elif paht != 0 and pvttc != 0 and txmge != 0:
        txtva = round((((pvttc / (1 + (txmge / 100))) - paht) / paht) * 100, 2)
    elif mtttva != 0 and pattc != 0:
        txtva = round((mtttva / (pattc - mtttva)) * 100, 2)
    elif mtttva != 0 and pvttc != 0 and txmge != 0:
        txtva = round((mtttva / ((pvttc / (1 + (txmge / 100))) - mtttva)) * 100, 2)

    return txtva


def calc_mtttva(paht, txtva, mtttva, pattc, pvttc, txmge, mttmge):
    """Fonction calculant le montant de la TVA s'il n'est pas renseigné"""

    if txtva == 'Inconnu':
        txtva = 0

    if paht != 0:
        mtttva = round((paht * txtva) / 100, 2)
    elif paht != 0 and pattc != 0:
        mtttva = round(pattc - paht, 2)
    elif paht != 0 and pvttc != 0 and txmge != 0:
        mtttva = round((((pvttc / (1 + (txmge / 100))) - paht) / paht), 2)
    elif txtva != 0 and pattc != 0:
        mtttva = round((pattc / (1 + (txtva / 100))) * (txtva / 100), 2)
    elif txtva != 0 and pvttc != 0 and txmge != 0:
        mtttva = round(((pvttc / (1 + (txmge / 100))) / (1 + (txtva / 100))) * txtva, 2)

    return mtttva


def calc_pattc(paht, txtva, mtttva, pattc, pvttc, txmge, mttmge):
    """Fonction calculant le prix d'achat TTC s'il n'est pas renseigné"""

    if txtva == 'Inconnu':
        txtva = float(0)
    if mtttva != 0:
        mtttva = calc_mtttva(paht, txtva, mtttva, pattc, pvttc, txmge, mttmge)

    if pattc != 0:
        pass
    elif paht != 0 and txtva == 0:
        pattc = round(paht, 2)
    elif paht != 0 and txtva != 0:
        pattc = round(paht * (1 + (txtva / 100)), 2)
    elif paht != 0 and mtttva == 0:
        pattc = round(paht, 2)
    elif paht != 0 and mtttva != 0:
        pattc = round(paht + mtttva, 2)
    elif txtva != 0 and mtttva != 0:
        pattc = round(((mtttva * 100) / txtva) * (1 + (txtva / 100)), 2)
    elif pvttc != 0 and txmge != 0:
        pattc = round(pvttc / (1 + (txmge / 100)), 2)
    elif txtva == 0 and mtttva == 0 and pvttc != 0 and mttmge != 0:
        pattc = round(pvttc - mttmge, 2)

    return pattc


def calc_pvttc(paht, txtva, mtttva, pattc, pvttc, txmge, mttmge):
    """Fonction calculant le prix de vente TTC s'il n'est pas renseigné"""

    if txtva == 'Inconnu':
        txtva = float(0)
    if mtttva != 0:
        mtttva = calc_mtttva(paht, txtva, mtttva, pattc, pvttc, txmge, mttmge)

    if pvttc != 0:
        pass
    elif paht != 0 and txtva != 0 and txmge != 0:
        pvttc = round(paht * (1 + (txtva / 100)) * (1 + (txmge / 100)), 2)
    elif paht != 0 and txtva != 0 and mttmge != 0:
        pvttc = round((paht + mttmge) * (1 + (txtva / 100)), 2)
    elif paht != 0 and txtva == 0 and mttmge != 0:
        pvttc = round(paht + mttmge, 2)
    elif paht != 0 and mtttva != 0 and txmge != 0:
        pvttc = round((paht + mtttva) * (1 + (txmge / 100)), 2)
    elif pattc != 0 and txmge != 0:
        pvttc = round(pattc * (1 + (txmge / 100)), 2)
    elif txtva != 0 and mtttva != 0 and txmge != 0:
        pvttc = round(((mtttva * 100) / txtva) * (1 + (txmge / 100)) * (1 + (txtva / 100)), 2)
    elif paht != 0 and txtva == 0 and txmge != 0:
        pvttc = round(paht * (1 + (txmge / 100)), 2)
    elif paht != 0 and txtva == 0 and mttmge != 0:
        pvttc = round(paht + mttmge, 2)
    elif txtva != 0 and pattc != 0 and mttmge != 0:
        pvttc = round(((pattc / (1 + (txtva / 100))) + mttmge) * (1 + (txtva / 100)), 2)
    elif txtva == 0 and pattc != 0 and mttmge != 0:
        pvttc = round(pattc + mttmge, 2)
    elif txtva != 0 and mtttva != 0 and mttmge != 0:
        pvttc = round((((mtttva * 100) / txtva) + mttmge) * (1 + (txtva / 100)), 2)
        # paht = (mtttva * 100) / txtva
        # pvht = paht + mttmge = ((mtttva * 100) / txtva) + mttmge
        # pvttc = pvht * (1 + (txtva / 100)) = (((mtttva * 100) / txtva) + mttmge) * (1 + (txtva / 100))

    return pvttc


def calc_txmge(paht, txtva, mtttva, pattc, pvttc, txmge, mttmge):
    """Fonction calculant le taux de marge s'il n'est pas renseigné"""

    if txtva == 'Inconnu':
        txtva = float(0)
    if mtttva != 0:
        mtttva = calc_mtttva(paht, txtva, mtttva, pattc, pvttc, txmge, mttmge)

    if txmge != 0:
        pass
    elif pvttc != 0 and pattc != 0:
        txmge = round(((pvttc - pattc) / pattc) * 100, 2)
    elif pvttc != 0 and mtttva != 0 and txtva != 0:
        txmge = round((((pvttc / (1 + (txtva / 100))) - ((mtttva * 100) / txtva)) / ((mtttva * 100) / txtva)) * 100, 2)
    elif pvttc != 0 and mtttva != 0 and paht != 0:
        txmge = round(((pvttc - (paht + mtttva)) / (paht + mtttva)) * 100, 2)
    elif paht != 0 and txtva != 0 and pvttc != 0:
        txmge = round((((pvttc / (1 + (txtva / 100))) - paht) / paht) * 100, 2)
    elif txtva != 0 and mtttva != 0 and mttmge != 0:
        txmge = round((mttmge / ((mtttva * 100) / txtva)) * 100, 2)
    elif paht != 0 and mttmge != 0:
        txmge = round((mttmge / paht) * 100, 2)
    elif txtva == 0 and mtttva == 0 and pvttc != 0 and mttmge != 0:
        txmge = round((mttmge / (pvttc - mttmge)) * 100, 2)
    elif txtva != 0 and pattc != 0 and mttmge != 0:
        txmge = round((mttmge / (pattc / (1 + (txtva / 100)))) * 100, 2)
    elif paht != 0 and txtva == 0 and pvttc != 0:
        txmge = round(((pvttc - paht) / paht) * 100, 2)
    elif txtva == 0 and pattc != 0 and mttmge != 0:
        txmge = round((mttmge / pattc) * 100, 2)

    return txmge


def calc_mttmge(paht, txtva, mtttva, pattc, pvttc, txmge, mttmge):
    """Fonction calculant le montant de la marge s'il n'est pas renseigné"""

    if txtva == 'Inconnu':
        txtva = float(0)
    if mtttva != 0:
        mtttva = calc_mtttva(paht, txtva, mtttva, pattc, pvttc, txmge, mttmge)

    if mttmge != 0:
        pass
    elif paht != 0 and txtva != 0 and pvttc != 0:
        mttmge = round((pvttc / (1 + (txtva / 100))) - paht, 2)
    elif pattc != 0 and txtva != 0 and txmge != 0:
        mttmge = round(((pattc / (1 + (txtva / 100))) * (1 + (txmge / 100))) - (pattc / (1 + (txtva / 100))), 2)
    elif pattc != 0 and mtttva != 0 and txmge != 0:
        mttmge = round(((pattc - mtttva) * (1 + (txmge / 100))) - (pattc - mtttva), 2)
    elif txtva != 0 and mtttva != 0 and pvttc != 0:
        mttmge = round((pvttc / (1 + (txtva / 100))) - ((mtttva * 100) / txtva), 2)
    elif txtva != 0 and mtttva != 0 and txmge != 0:
        mttmge = round(((mtttva * 100) / txtva) * (1 + (txmge / 100)) - ((mtttva * 100) / txtva), 2)
    elif paht != 0 and txmge != 0:
        mttmge = round((paht * (1 + (txmge / 100))) - paht, 2)
    elif paht != 0 and mtttva != 0 and pvttc != 0:
        mttmge = round((pvttc / (1 + (mtttva / paht))) - paht, 2)
    elif paht != 0 and txtva == 0 and pvttc != 0:
        mttmge = round(pvttc - paht, 2)
    elif txtva == 0 and mtttva == 0 and pvttc != 0 and txmge != 0:
        mttmge = round(pvttc - (pvttc / (1 + (txmge / 100))), 2)
    elif txtva != 0 and pattc != 0 and pvttc != 0:
        mttmge = round((pvttc / (1 + (txtva / 100))) - (pattc / (1 + (txtva / 100))), 2)
    elif txtva == 0 and pattc != 0 and txmge != 0:
        mttmge = round((pattc * txmge) / 100, 2)
    elif paht != 0 and pattc != 0 and pvttc != 0:
        mttmge = round((pvttc / (1 + ((pattc - paht) / paht)) - paht), 2)
        # mtttva = pattc - paht
        # txtva = (mtttva / paht) * 100 = ((pattc - paht) / paht) * 100
        # pvht = pvttc / (1 + (txtva / 100)) = pvttc / (1 + ((pattc - paht) / paht)
        # mttmge = pvht - paht = (pvttc / (1 + ((pattc - paht) / paht)) - paht
    elif mtttva != 0 and pvttc != 0 and txmge != 0:
        mttmge = round(
            ((mtttva * 100) / ((mtttva / ((pvttc / (1 + (txmge / 100))) - mtttva)) * 100)) * (1 + (txmge / 100)) - (
                        mtttva * 100) / ((mtttva / ((pvttc / (1 + (txmge / 100))) - mtttva)) * 100), 2)
        # txtva = (mtttva / ((pvttc / (1 + (txmge / 100))) - mtttva)) * 100
        # paht = (mtttva * 100) / txtva = (mtttva * 100) / ((mtttva / ((pvttc / (1 + (txmge / 100))) - mtttva)) * 100)
        # pvht = paht * (1 + (txmge / 100)) =
        # ((mtttva * 100) / ((mtttva / ((pvttc / (1 + (txmge / 100))) - mtttva)) * 100)) * (1 +(txmge / 100))
        # mttmge = pvht - paht

    return mttmge
