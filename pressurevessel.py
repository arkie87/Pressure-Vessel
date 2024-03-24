from math import log10


R = 8314/18
L = 2.1e6
Cp_l = 4200
Cp_v = 2300


def T_sat(P):
    A = 8.07131
    B = 1730.63
    C = 233.426
    return B/(A-log10(P*760/101325))-C + 273.15
    
def pressure(rho_v, T):
    return rho_v * R * T
    

def saturated(rho_v, T0=300, P0=10000):

    
    res = 1
    T, P = T0, P0
    
    while res > 1e-10:
        Tp = T
        P = pressure(rho_v, T)
        T = T_sat(P)
        res = abs(T-Tp)
        
        #print("    ", T, P, res)
        
        
    return T , P


def residual(P):
    T = T_sat(P)
    
    dm0 = (Q - (m_l_p * Cp_l + m_v_p * Cp_v) * (T - Tp))/(L + (Cp_v - Cp_l) * (T - Tp))
    dm = max(-m_v_p, min(dm0, m_l_p))

    m_l = m_l_p - dm
    m_v = m_v_p + dm
    
    Q_L = dm * L
    Q_S = (m_l * Cp_l + m_v * Cp_v) * (T - Tp)
        
    V_l = m_l/rho_l
    V_v = V - V_l
    rho_v = m_v / V_v
    
    res = rho_v * R * T - P
    
    

    return res, T, dm, m_l, m_v, Q_L, Q_S, V_l, V_v, rho_v
    
    
    



V = 1
m_l = 10
rho_l = 1000


P = 500
T = T_sat(P)
rho_v = P/(R*T)
V_v = V - m_l / rho_l
m_v = rho_v * V_v




print(f"{T=:4.1f},{P=:5.1f}")

Q = 1000000
Tp = T
Pp = P
m_l_p = m_l
m_v_p = m_v

dm = 0
alpha = 0.7
for i in range(10):
    Pp = P
  
    res, T, dm, m_l, m_v, Q_L, Q_S, V_l, V_v, rho_v = residual(P)
    r1, *_ = residual(P + 1)
    drdx = r1-res
    
    P = Pp - res/drdx
    
    print(f"{dm/m_v=:6f}, {rho_v=:.4f}, {T=:5.1f}, {P=:6.0f}, {Q_S=:0.4e}, {Q_S+Q_L=:.4e}, {res/P=:.4e}")
    

    
   





