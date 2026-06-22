from models.Avicultura2017 import Avicultura2017
from repositories.Avicultura2017Repository import Avicultura2017Repository

def rowToAvicultura2017(row):
    # A ordem dos campos deve corresponder à SELECT * (id + todos os outros)
    # As colunas do banco estão em minúsculas
    (id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal,
     e_cria_gal, e_tem_gal, e_gal_vend, e_ovos_prod, e_ovos_vend,
     e_subs, e_comerc, e_recebe_ori, e_ori_gov, e_ori_propria,
     e_ori_coop, e_ori_emp_int, e_ori_emp_priv, e_ori_ong,
     e_ori_sist_s, e_ori_outra, e_gal_eng, e_gal_galos, e_gal_poed,
     e_gal_matr, e_assoc_coop, e_financ, e_financ_coop, e_financ_integ,
     e_dap, e_agrifam, e_n_agrifam, e_produtor, e_cooperativa,
     e_sa_ldta, e_cnpj, gal_total, gal_eng, gal_galos, gal_poed,
     gal_matr, gal_vend, v_gal_vend, q_dz_prod, q_dz_vend,
     v_q_dz_prod, v_q_dz_vend, a_total, a_past_plant, a_lav_perm,
     a_lav_temp, a_apprl, vtp_agro, rect_agro, n_trab_total,
     n_trab_lacos) = row
    return Avicultura2017(
        id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal,
        e_cria_gal, e_tem_gal, e_gal_vend, e_ovos_prod, e_ovos_vend,
        e_subs, e_comerc, e_recebe_ori, e_ori_gov, e_ori_propria,
        e_ori_coop, e_ori_emp_int, e_ori_emp_priv, e_ori_ong,
        e_ori_sist_s, e_ori_outra, e_gal_eng, e_gal_galos, e_gal_poed,
        e_gal_matr, e_assoc_coop, e_financ, e_financ_coop, e_financ_integ,
        e_dap, e_agrifam, e_n_agrifam, e_produtor, e_cooperativa,
        e_sa_ldta, e_cnpj, gal_total, gal_eng, gal_galos, gal_poed,
        gal_matr, gal_vend, v_gal_vend, q_dz_prod, q_dz_vend,
        v_q_dz_prod, v_q_dz_vend, a_total, a_past_plant, a_lav_perm,
        a_lav_temp, a_apprl, vtp_agro, rect_agro, n_trab_total,
        n_trab_lacos
    )

class Avicultura2017Service:
    def __init__(self):
        self.repository = Avicultura2017Repository()
    
    def get_by_filters(self, filters):
        """
        Obtém registros de avicultura 2017 aplicando filtros.
        Retorna lista de objetos Avicultura2017.
        """
        rows = self.repository.get_by_filters(filters)
        
        # Converter cada linha para objeto Avicultura2017
        aviculturas = [rowToAvicultura2017(row) for row in rows]
        return aviculturas

    