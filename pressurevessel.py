from math import log10



def T_sat(P):
    A = 8.07131
    B = 1730.63
    C = 233.426
    return B/(A-log10(P*760/101325))-C + 273.15




L = 2.1e6
Cp_l = 4200
Cp_v = 2300

V = 1
m_l = 10
m_v = 1

rho_l = 1000

R = 8314/18

P = 10000
T = T_sat(P)



Q = 400000
Tp = T
Pp = P
m_l_p = m_l
m_v_p = m_v


alpha = 0.7

for _ in range(10):
    dTp = T - Tp
    
    dm = min((Q - (m_l_p * Cp_l + m_v_p * Cp_v) * (T - Tp))/(L + (Cp_v - Cp_l) * (T - Tp)), m_l_p)
    
    m_l = m_l_p - dm
    m_v = m_v_p + dm
    
    Q_L = dm * L
    Q_S = (m_l * Cp_l + m_v * Cp_v) * (T - Tp)
    
    V_l = m_l/rho_l
    V_v = V - V_l

    P = Pp * m_v/m_v_p
    T = (1-alpha) *T + alpha * T_sat(P)
    
    
    Res = dTp/(T-Tp) - 1
    

    print(f"{dm/m_v=:6f}, {T=:6.1f}, {P=:10f}, {Q_S+Q_L=:.6e}, {Res=:.6e}")





