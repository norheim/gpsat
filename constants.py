from gpkit import Variable
import astropy.constants as const

sigma = Variable("\\sigma", const.sigma_sb.value, "W / m^2 / K^4", "Stefan-Boltzman constant")
k = Variable("k", const.k_B.value, "J/K", "Boltzman constant R/Na")
mu_earth = Variable("\\mu_e", const.GM_earth.value, "m^3 / s^2", "GM Earth")
c = Variable("c", const.c.value, "m/s", "Speed of light in vacuum")
Q_s = Variable("Q_s", 1367, "W/m^2", "solar flux constant")
R_earth = Variable("R_e", const.R_earth.value, "m", "earth radius")