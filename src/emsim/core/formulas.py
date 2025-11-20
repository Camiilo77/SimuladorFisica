# Centraliza las deducciones/fórmulas LaTeX y textos explicativos para la UI

formula_parallel_plates = r"""
\[
C = \varepsilon_0\,\varepsilon_r\,\frac{A}{d}
\]
Donde:
- \(C\) = Capacitancia [F]
- \(\varepsilon_0\) = permitividad del vacío (\(8.854 \times 10^{-12} \,\text{F/m}\))
- \(\varepsilon_r\) = permitividad relativa del dieléctrico
- \(A\) = área de las placas [m²]
- \(d\) = distancia entre placas [m]
"""

formula_sphere = r"""
\[
C = 4\pi\varepsilon_0\,r
\]
Donde:
- \(C\) = Capacitancia [F]
- \(\varepsilon_0\) = permitividad del vacío (\(8.854 \times 10^{-12} \,\text{F/m}\))
- \(r\) = radio de la esfera [m]
"""

formula_cylinder = r"""
\[
C = \frac{2\pi\varepsilon_0\varepsilon_r\,L}{\ln(b/a)}
\]
Donde:  
- \(C\): Capacitancia [F]  
- \(\varepsilon_0\): permitividad del vacío  
- \(\varepsilon_r\): permitividad relativa  
- \(L\): longitud del cilindro [m]  
- \(a\): radio interior [m]  
- \(b\): radio exterior [m]
"""
