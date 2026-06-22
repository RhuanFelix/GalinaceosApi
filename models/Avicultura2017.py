from marshmallow import Schema, fields

class Avicultura2017:
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

class Avicultura2017Schema(Schema):
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