# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:38:00 2024

@author: jperezr
"""

import streamlit as st

# Título de la página principal
st.title("Calculadora de Retiro y Simulador de Inversiones en Energías Renovables")



# Sección de la calculadora de retiro
st.write("""
---
### Calculadora de Retiro
Esta herramienta te permite planificar tu retiro considerando los rendimientos potenciales de las inversiones en **energías renovables**. La calculadora toma en cuenta tus contribuciones actuales, el tiempo restante hasta tu retiro, y proyecta los posibles retornos con base en tus elecciones de inversión.

#### ¿Cómo Funciona?
1. **Aportaciones Iniciales y Regulares:** Introduce cuánto dinero tienes actualmente ahorrado para el retiro y cuánto planeas aportar regularmente.
2. **Horizonte de Inversión:** Selecciona cuántos años faltan para tu retiro.
3. **Crecimiento Potencial:** Basado en tus inversiones en **energía solar, eólica y geotérmica**, proyectamos un retorno estimado a lo largo del tiempo.
4. **Monto Final Estimado:** Calculamos el monto total que podrías tener al momento de tu retiro, basándonos en las tasas de crecimiento históricas de estas industrias.
""")


# Descripción general de la propuesta
st.write("""
### Inversión en Energías Renovables
Esta propuesta presenta un análisis detallado sobre la viabilidad y los beneficios de invertir en empresas del sector de **energía solar, eólica y geotérmica**. El análisis incluye datos históricos, análisis de riesgo y retorno, y el impacto ambiental de estas inversiones.

PENSIONISSSTE tiene la oportunidad de alinear su portafolio con criterios **ESG** (ambientales, sociales y de gobernanza), mientras aprovecha el crecimiento de estos sectores en un mundo cada vez más comprometido con la descarbonización.
""")

# Sidebar con enlaces a las otras apps
# st.sidebar.title("Navegación")

# Enlaces a otras páginas
# st.sidebar.markdown("[Simulación de Inversión - App 1](pages/app1.py)")
# st.sidebar.markdown("[Análisis de Riesgo - App 4](pages/app4.py)")

# Información adicional o resumen
st.write("""
---
#### Beneficios de Invertir en Energías Renovables:
1. **Crecimiento Sostenible:** Las energías renovables están experimentando un crecimiento continuo y acelerado.
2. **Diversificación:** Invertir en varias fuentes de energía como solar, eólica y geotérmica reduce el riesgo y mejora la estabilidad del portafolio.
3. **Impacto Ambiental Positivo:** Estas inversiones apoyan la reducción de emisiones de CO₂, alineándose con los objetivos de sostenibilidad globales.
4. **Atractivos Retornos a Largo Plazo:** Con la transición energética global, las empresas de energías renovables tienen un potencial significativo de crecimiento.
""")