from flask_restful import fields as dto
from marshmallow import Schema, fields
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped

from helpers.database import db


galinaceos_fields = {
    'id': dto.Integer,
    'SIST_CRIA': dto.Integer,
    'NIV_TERR': dto.Integer,
    'COD_TERR': dto.Integer,
    'NOM_TERR': dto.Integer,
    'CL_GAL': dto.Integer,
    'E_CRIA_GAL': dto.String,
    'E_TEM_GAL': dto.String,
    'E_GAL_VEND': dto.String,
    'E_OVOS_PROD': dto.String,
    'E_OVOS_VEND': dto.String,
    'E_SUBS': dto.String,
    'E_COMERC': dto.String,
    'E_RECEBE_ORI': dto.String,
    'E_ORI_GOV': dto.String,
    'E_ORI_PROPRIA': dto.String,
    'E_ORI_COOP': dto.String,
    'E_ORI_EMP_INT': dto.String,
    'E_ORI_EMP_PRIV': dto.String,
    'E_ORI_ONG': dto.String,
    'E_ORI_SIST_S': dto.String,
    'E_ORI_OUTRA': dto.String,
    'E_GAL_ENG': dto.String,
    'E_GAL_GALOS': dto.String,
    'E_GAL_POED': dto.String,
    'E_GAL_MATR': dto.String,
    'E_ASSOC_COOP': dto.String,
    'E_FINANC': dto.String,
    'E_FINANC_COOP': dto.String,
    'E_FINANC_INTEG': dto.String,
    'E_DAP': dto.String,
    'E_AGRIFAM': dto.String,
    'E_N_AGRIFAM': dto.String,
    'E_PRODUTOR': dto.String,
    'E_COOPERATIVA': dto.String,
    'E_SA_LDTA': dto.String,
    'E_CNPJ': dto.String,
    'GAL_TOTAL': dto.String,
    'GAL_ENG': dto.String,
    'GAL_GALOS': dto.String,
    'GAL_POED': dto.String,
    'GAL_MATR': dto.String,
    'GAL_VEND': dto.String,
    'V_GAL_VEND': dto.String,
    'Q_DZ_PROD': dto.String,
    'Q_DZ_VEND': dto.String,
    'V_Q_DZ_PROD': dto.String,
    'V_Q_DZ_VEND': dto.String,
    'A_TOTAL': dto.String,
    'A_PAST_PLANT': dto.String,
    'A_LAV_PERM': dto.String,
    'A_LAV_TEMP': dto.String,
    'A_APPRL': dto.String,
    'VTP_AGRO': dto.String,
    'RECT_AGRO': dto.String,
    'N_TRAB_TOTAL': dto.String,
    'N_TRAB_LACOS': dto.String,
}

galinaceos_id_fields = {
    'id': dto.Integer,
}


class Galinaceos(db.Model):
    __tablename__ = 'tb_avicultura_2017'

    id: Mapped[int] = mapped_column('id', primary_key=True)
    SIST_CRIA: Mapped[int] = mapped_column('sist_cria', Integer())
    NIV_TERR: Mapped[int] = mapped_column('niv_terr', Integer())
    COD_TERR: Mapped[int] = mapped_column('cod_terr', Integer())
    NOM_TERR: Mapped[int] = mapped_column('nom_terr', Integer())
    CL_GAL: Mapped[int] = mapped_column('cl_gal', Integer())
    E_CRIA_GAL: Mapped[str] = mapped_column('e_cria_gal', String())
    E_TEM_GAL: Mapped[str] = mapped_column('e_tem_gal', String())
    E_GAL_VEND: Mapped[str] = mapped_column('e_gal_vend', String())
    E_OVOS_PROD: Mapped[str] = mapped_column('e_ovos_prod', String())
    E_OVOS_VEND: Mapped[str] = mapped_column('e_ovos_vend', String())
    E_SUBS: Mapped[str] = mapped_column('e_subs', String())
    E_COMERC: Mapped[str] = mapped_column('e_comerc', String())
    E_RECEBE_ORI: Mapped[str] = mapped_column('e_recebe_ori', String())
    E_ORI_GOV: Mapped[str] = mapped_column('e_ori_gov', String())
    E_ORI_PROPRIA: Mapped[str] = mapped_column('e_ori_propria', String())
    E_ORI_COOP: Mapped[str] = mapped_column('e_ori_coop', String())
    E_ORI_EMP_INT: Mapped[str] = mapped_column('e_ori_emp_int', String())
    E_ORI_EMP_PRIV: Mapped[str] = mapped_column('e_ori_emp_priv', String())
    E_ORI_ONG: Mapped[str] = mapped_column('e_ori_ong', String())
    E_ORI_SIST_S: Mapped[str] = mapped_column('e_ori_sist_s', String())
    E_ORI_OUTRA: Mapped[str] = mapped_column('e_ori_outra', String())
    E_GAL_ENG: Mapped[str] = mapped_column('e_gal_eng', String())
    E_GAL_GALOS: Mapped[str] = mapped_column('e_gal_galos', String())
    E_GAL_POED: Mapped[str] = mapped_column('e_gal_poed', String())
    E_GAL_MATR: Mapped[str] = mapped_column('e_gal_matr', String())
    E_ASSOC_COOP: Mapped[str] = mapped_column('e_assoc_coop', String())
    E_FINANC: Mapped[str] = mapped_column('e_financ', String())
    E_FINANC_COOP: Mapped[str] = mapped_column('e_financ_coop', String())
    E_FINANC_INTEG: Mapped[str] = mapped_column('e_financ_integ', String())
    E_DAP: Mapped[str] = mapped_column('e_dap', String())
    E_AGRIFAM: Mapped[str] = mapped_column('e_agrifam', String())
    E_N_AGRIFAM: Mapped[str] = mapped_column('e_n_agrifam', String())
    E_PRODUTOR: Mapped[str] = mapped_column('e_produtor', String())
    E_COOPERATIVA: Mapped[str] = mapped_column('e_cooperativa', String())
    E_SA_LDTA: Mapped[str] = mapped_column('e_sa_ldta', String())
    E_CNPJ: Mapped[str] = mapped_column('e_cnpj', String())
    GAL_TOTAL: Mapped[str] = mapped_column('gal_total', String())
    GAL_ENG: Mapped[str] = mapped_column('gal_eng', String())
    GAL_GALOS: Mapped[str] = mapped_column('gal_galos', String())
    GAL_POED: Mapped[str] = mapped_column('gal_poed', String())
    GAL_MATR: Mapped[str] = mapped_column('gal_matr', String())
    GAL_VEND: Mapped[str] = mapped_column('gal_vend', String())
    V_GAL_VEND: Mapped[str] = mapped_column('v_gal_vend', String())
    Q_DZ_PROD: Mapped[str] = mapped_column('q_dz_prod', String())
    Q_DZ_VEND: Mapped[str] = mapped_column('q_dz_vend', String())
    V_Q_DZ_PROD: Mapped[str] = mapped_column('v_q_dz_prod', String())
    V_Q_DZ_VEND: Mapped[str] = mapped_column('v_q_dz_vend', String())
    A_TOTAL: Mapped[str] = mapped_column('a_total', String())
    A_PAST_PLANT: Mapped[str] = mapped_column('a_past_plant', String())
    A_LAV_PERM: Mapped[str] = mapped_column('a_lav_perm', String())
    A_LAV_TEMP: Mapped[str] = mapped_column('a_lav_temp', String())
    A_APPRL: Mapped[str] = mapped_column('a_apprl', String())
    VTP_AGRO: Mapped[str] = mapped_column('vtp_agro', String())
    RECT_AGRO: Mapped[str] = mapped_column('rect_agro', String())
    N_TRAB_TOTAL: Mapped[str] = mapped_column('n_trab_total', String())
    N_TRAB_LACOS: Mapped[str] = mapped_column('n_trab_lacos', String())

    def __init__(self, id, SIST_CRIA, NIV_TERR, COD_TERR, NOM_TERR, CL_GAL,
                 E_CRIA_GAL, E_TEM_GAL, E_GAL_VEND, E_OVOS_PROD, E_OVOS_VEND,
                 E_SUBS, E_COMERC, E_RECEBE_ORI, E_ORI_GOV, E_ORI_PROPRIA,
                 E_ORI_COOP, E_ORI_EMP_INT, E_ORI_EMP_PRIV, E_ORI_ONG,
                 E_ORI_SIST_S, E_ORI_OUTRA, E_GAL_ENG, E_GAL_GALOS, E_GAL_POED,
                 E_GAL_MATR, E_ASSOC_COOP, E_FINANC, E_FINANC_COOP, E_FINANC_INTEG,
                 E_DAP, E_AGRIFAM, E_N_AGRIFAM, E_PRODUTOR, E_COOPERATIVA,
                 E_SA_LDTA, E_CNPJ, GAL_TOTAL, GAL_ENG, GAL_GALOS, GAL_POED,
                 GAL_MATR, GAL_VEND, V_GAL_VEND, Q_DZ_PROD, Q_DZ_VEND,
                 V_Q_DZ_PROD, V_Q_DZ_VEND, A_TOTAL, A_PAST_PLANT, A_LAV_PERM,
                 A_LAV_TEMP, A_APPRL, VTP_AGRO, RECT_AGRO, N_TRAB_TOTAL,
                 N_TRAB_LACOS):
        self.id = id
        self.SIST_CRIA = SIST_CRIA
        self.NIV_TERR = NIV_TERR
        self.COD_TERR = COD_TERR
        self.NOM_TERR = NOM_TERR
        self.CL_GAL = CL_GAL
        self.E_CRIA_GAL = E_CRIA_GAL
        self.E_TEM_GAL = E_TEM_GAL
        self.E_GAL_VEND = E_GAL_VEND
        self.E_OVOS_PROD = E_OVOS_PROD
        self.E_OVOS_VEND = E_OVOS_VEND
        self.E_SUBS = E_SUBS
        self.E_COMERC = E_COMERC
        self.E_RECEBE_ORI = E_RECEBE_ORI
        self.E_ORI_GOV = E_ORI_GOV
        self.E_ORI_PROPRIA = E_ORI_PROPRIA
        self.E_ORI_COOP = E_ORI_COOP
        self.E_ORI_EMP_INT = E_ORI_EMP_INT
        self.E_ORI_EMP_PRIV = E_ORI_EMP_PRIV
        self.E_ORI_ONG = E_ORI_ONG
        self.E_ORI_SIST_S = E_ORI_SIST_S
        self.E_ORI_OUTRA = E_ORI_OUTRA
        self.E_GAL_ENG = E_GAL_ENG
        self.E_GAL_GALOS = E_GAL_GALOS
        self.E_GAL_POED = E_GAL_POED
        self.E_GAL_MATR = E_GAL_MATR
        self.E_ASSOC_COOP = E_ASSOC_COOP
        self.E_FINANC = E_FINANC
        self.E_FINANC_COOP = E_FINANC_COOP
        self.E_FINANC_INTEG = E_FINANC_INTEG
        self.E_DAP = E_DAP
        self.E_AGRIFAM = E_AGRIFAM
        self.E_N_AGRIFAM = E_N_AGRIFAM
        self.E_PRODUTOR = E_PRODUTOR
        self.E_COOPERATIVA = E_COOPERATIVA
        self.E_SA_LDTA = E_SA_LDTA
        self.E_CNPJ = E_CNPJ
        self.GAL_TOTAL = GAL_TOTAL
        self.GAL_ENG = GAL_ENG
        self.GAL_GALOS = GAL_GALOS
        self.GAL_POED = GAL_POED
        self.GAL_MATR = GAL_MATR
        self.GAL_VEND = GAL_VEND
        self.V_GAL_VEND = V_GAL_VEND
        self.Q_DZ_PROD = Q_DZ_PROD
        self.Q_DZ_VEND = Q_DZ_VEND
        self.V_Q_DZ_PROD = V_Q_DZ_PROD
        self.V_Q_DZ_VEND = V_Q_DZ_VEND
        self.A_TOTAL = A_TOTAL
        self.A_PAST_PLANT = A_PAST_PLANT
        self.A_LAV_PERM = A_LAV_PERM
        self.A_LAV_TEMP = A_LAV_TEMP
        self.A_APPRL = A_APPRL
        self.VTP_AGRO = VTP_AGRO
        self.RECT_AGRO = RECT_AGRO
        self.N_TRAB_TOTAL = N_TRAB_TOTAL
        self.N_TRAB_LACOS = N_TRAB_LACOS

    def toDict(self):
        return {
            "id": self.id,
            "SIST_CRIA": self.SIST_CRIA,
            "NIV_TERR": self.NIV_TERR,
            "COD_TERR": self.COD_TERR,
            "NOM_TERR": self.NOM_TERR,
            "CL_GAL": self.CL_GAL,
            "E_CRIA_GAL": self.E_CRIA_GAL,
            "E_TEM_GAL": self.E_TEM_GAL,
            "E_GAL_VEND": self.E_GAL_VEND,
            "E_OVOS_PROD": self.E_OVOS_PROD,
            "E_OVOS_VEND": self.E_OVOS_VEND,
            "E_SUBS": self.E_SUBS,
            "E_COMERC": self.E_COMERC,
            "E_RECEBE_ORI": self.E_RECEBE_ORI,
            "E_ORI_GOV": self.E_ORI_GOV,
            "E_ORI_PROPRIA": self.E_ORI_PROPRIA,
            "E_ORI_COOP": self.E_ORI_COOP,
            "E_ORI_EMP_INT": self.E_ORI_EMP_INT,
            "E_ORI_EMP_PRIV": self.E_ORI_EMP_PRIV,
            "E_ORI_ONG": self.E_ORI_ONG,
            "E_ORI_SIST_S": self.E_ORI_SIST_S,
            "E_ORI_OUTRA": self.E_ORI_OUTRA,
            "E_GAL_ENG": self.E_GAL_ENG,
            "E_GAL_GALOS": self.E_GAL_GALOS,
            "E_GAL_POED": self.E_GAL_POED,
            "E_GAL_MATR": self.E_GAL_MATR,
            "E_ASSOC_COOP": self.E_ASSOC_COOP,
            "E_FINANC": self.E_FINANC,
            "E_FINANC_COOP": self.E_FINANC_COOP,
            "E_FINANC_INTEG": self.E_FINANC_INTEG,
            "E_DAP": self.E_DAP,
            "E_AGRIFAM": self.E_AGRIFAM,
            "E_N_AGRIFAM": self.E_N_AGRIFAM,
            "E_PRODUTOR": self.E_PRODUTOR,
            "E_COOPERATIVA": self.E_COOPERATIVA,
            "E_SA_LDTA": self.E_SA_LDTA,
            "E_CNPJ": self.E_CNPJ,
            "GAL_TOTAL": self.GAL_TOTAL,
            "GAL_ENG": self.GAL_ENG,
            "GAL_GALOS": self.GAL_GALOS,
            "GAL_POED": self.GAL_POED,
            "GAL_MATR": self.GAL_MATR,
            "GAL_VEND": self.GAL_VEND,
            "V_GAL_VEND": self.V_GAL_VEND,
            "Q_DZ_PROD": self.Q_DZ_PROD,
            "Q_DZ_VEND": self.Q_DZ_VEND,
            "V_Q_DZ_PROD": self.V_Q_DZ_PROD,
            "V_Q_DZ_VEND": self.V_Q_DZ_VEND,
            "A_TOTAL": self.A_TOTAL,
            "A_PAST_PLANT": self.A_PAST_PLANT,
            "A_LAV_PERM": self.A_LAV_PERM,
            "A_LAV_TEMP": self.A_LAV_TEMP,
            "A_APPRL": self.A_APPRL,
            "VTP_AGRO": self.VTP_AGRO,
            "RECT_AGRO": self.RECT_AGRO,
            "N_TRAB_TOTAL": self.N_TRAB_TOTAL,
            "N_TRAB_LACOS": self.N_TRAB_LACOS
        }

class GalinaceosSchema(Schema):
    SIST_CRIA = fields.Int(allow_none=True, required=True)
    NIV_TERR = fields.Int(allow_none=True, required=True)
    COD_TERR = fields.Int(allow_none=True, required=True)
    NOM_TERR = fields.Int(allow_none=True, required=True)
    CL_GAL = fields.Int(allow_none=True, required=True)
    E_CRIA_GAL = fields.Str(allow_none=True, required=True)
    E_TEM_GAL = fields.Str(allow_none=True, required=True)
    E_GAL_VEND = fields.Str(allow_none=True, required=True)
    E_OVOS_PROD = fields.Str(allow_none=True, required=True)
    E_OVOS_VEND = fields.Str(allow_none=True, required=True)
    E_SUBS = fields.Str(allow_none=True, required=True)
    E_COMERC = fields.Str(allow_none=True, required=True)
    E_RECEBE_ORI = fields.Str(allow_none=True, required=True)
    E_ORI_GOV = fields.Str(allow_none=True, required=True)
    E_ORI_PROPRIA = fields.Str(allow_none=True, required=True)
    E_ORI_COOP = fields.Str(allow_none=True, required=True)
    E_ORI_EMP_INT = fields.Str(allow_none=True, required=True)
    E_ORI_EMP_PRIV = fields.Str(allow_none=True, required=True)
    E_ORI_ONG = fields.Str(allow_none=True, required=True)
    E_ORI_SIST_S = fields.Str(allow_none=True, required=True)
    E_ORI_OUTRA = fields.Str(allow_none=True, required=True)
    E_GAL_ENG = fields.Str(allow_none=True, required=True)
    E_GAL_GALOS = fields.Str(allow_none=True, required=True)
    E_GAL_POED = fields.Str(allow_none=True, required=True)
    E_GAL_MATR = fields.Str(allow_none=True, required=True)
    E_ASSOC_COOP = fields.Str(allow_none=True, required=True)
    E_FINANC = fields.Str(allow_none=True, required=True)
    E_FINANC_COOP = fields.Str(allow_none=True, required=True)
    E_FINANC_INTEG = fields.Str(allow_none=True, required=True)
    E_DAP = fields.Str(allow_none=True, required=True)
    E_AGRIFAM = fields.Str(allow_none=True, required=True)
    E_N_AGRIFAM = fields.Str(allow_none=True, required=True)
    E_PRODUTOR = fields.Str(allow_none=True, required=True)
    E_COOPERATIVA = fields.Str(allow_none=True, required=True)
    E_SA_LDTA = fields.Str(allow_none=True, required=True)
    E_CNPJ = fields.Str(allow_none=True, required=True)
    GAL_TOTAL = fields.Str(allow_none=True, required=True)
    GAL_ENG = fields.Str(allow_none=True, required=True)
    GAL_GALOS = fields.Str(allow_none=True, required=True)
    GAL_POED = fields.Str(allow_none=True, required=True)
    GAL_MATR = fields.Str(allow_none=True, required=True)
    GAL_VEND = fields.Str(allow_none=True, required=True)
    V_GAL_VEND = fields.Str(allow_none=True, required=True)
    Q_DZ_PROD = fields.Str(allow_none=True, required=True)
    Q_DZ_VEND = fields.Str(allow_none=True, required=True)
    V_Q_DZ_PROD = fields.Str(allow_none=True, required=True)
    V_Q_DZ_VEND = fields.Str(allow_none=True, required=True)
    A_TOTAL = fields.Str(allow_none=True, required=True)
    A_PAST_PLANT = fields.Str(allow_none=True, required=True)
    A_LAV_PERM = fields.Str(allow_none=True, required=True)
    A_LAV_TEMP = fields.Str(allow_none=True, required=True)
    A_APPRL = fields.Str(allow_none=True, required=True)
    VTP_AGRO = fields.Str(allow_none=True, required=True)
    RECT_AGRO = fields.Str(allow_none=True, required=True)
    N_TRAB_TOTAL = fields.Str(allow_none=True, required=True)
    N_TRAB_LACOS = fields.Str(allow_none=True, required=True)
