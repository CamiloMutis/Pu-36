# 2026-11-19 · Cable pelado contra antena original

## Objetivo

Comprobar si el vivo del coaxial, sin antena, ya capta señal por sí solo, y cuánto mejora una antena de verdad. Es el punto de partida para medir después a Pu-36.

## Montaje

- Equipo: portátil con Linux, adaptador USB TP-Link TL-WN722N v2/v3 (chip RTL8188EUS), siempre en el mismo puerto USB.
- Red de prueba: el router de la casa, canal 1 de 2,4 GHz, a pocos metros.
- **Cable pelado:** adaptador con la base de su antena desarmada; solo queda a la vista unos milímetros de vivo.
- **Antena original:** un segundo adaptador igual, con su antena completa.
- 5 escaneos seguidos por configuración, con `herramientas/medir.py`.

## Resultados

| Configuración | Señal promedio | dBm aprox. | Redes vistas (1.er escaneo) |
|---|---|---|---|
| Cable pelado | 37,8 % | ≈ −77 dBm | 4 |
| Antena original | 100 % | ≥ −40 dBm | 46 |

Datos por escaneo en [mediciones.csv](mediciones.csv).

## Conclusiones

- **El vivo solo capta muy poco**: 4 redes y una señal débil. Lo que hace el trabajo es la antena, no el cable.
- **El 100 % está topado**: el adaptador no distingue señales más fuertes que −40 dBm. Estaba muy cerca del router.
- El conteo de redes de la antena original subió de 46 a 68 en los escaneos seguidos porque el sistema acumula redes. Se usa el primer escaneo.

## Para la próxima

Medir a Pu-36 **más lejos del router**, donde la antena original dé entre 50 y 70 %, para que la diferencia se vea.
