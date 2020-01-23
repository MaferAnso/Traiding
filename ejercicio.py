
# -- ------------------------------------------------------------------------------------ -- #
# -- Proyecto: Describir brevemente el proyecto en general                                -- #
# -- Codigo: RepasoPython.py - describir brevemente el codigo                             -- #
# -- Repositorio: https://github.com/                                                     -- #
# -- Autor: Nombre de autor                                                               -- #
# -- ------------------------------------------------------------------------------------ -- #

# -- ------------------------------------------------------------- Importar con funciones -- #
import funciones as fn
import visualizaciones as vs

import pandas as pd

# -- --------------------------------------------------------- Descargar precios de OANDA -- #

# token de OANDA
OA_Ak = '7' + '74e6b7edf1977f9515e6a97c39ddfce4-0511a0509365ab62ca68696bff88f044' + '6'
OA_In = "EUR_USD"                  # Instrumento
OA_Gn = "D"                       # Granularidad de velas
fini = pd.to_datetime("2019-01-06 00:00:00").tz_localize('GMT')  # Fecha inicial
ffin = pd.to_datetime("2019-12-06 00:00:00").tz_localize('GMT')  # Fecha final

df_pe = fn.f_precios_masivos(p0_fini=fini, p1_ffin=ffin, p2_gran=OA_Gn,
                             p3_inst=OA_In, p4_oatk=OA_Ak, p5_ginc=4900)

# -- --------------------------------------------------------------- Graficar OHLC plotly -- #

vs_grafica1 = vs.g_velas(p0_de=df_pe.iloc[0:120, :])
vs_grafica1.show()

# -- ------------------------------------------------------------------- Conteno de velas -- #
