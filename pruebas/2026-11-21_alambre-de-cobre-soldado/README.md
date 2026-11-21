# 2026-11-21 · Alambre de cobre soldado al vivo

## Objetivo

Comprobar que el empalme entre el vivo del coaxial y el alambre de cobre conduce bien, y ver cuánto capta el cable alargado antes de montar los discos.

## Montaje

- Mismo equipo que la [prueba del 19/11](../2026-11-19_cable-pelado-vs-antena-original/): portátil con Linux y adaptador TP-Link TL-WN722N, misma red de prueba (canal 1).
- Cable de la antena original con unos 2 cm de alambre de cobre sólido soldado al vivo (el alambre no se pega al imán: es cobre).
- Dos mediciones con `herramientas/medir.py`:
  1. `alambre_soldado`: 5 escaneos.
  2. `alambre_soldado_quieto`: 8 escaneos sin tocar el adaptador ni el cable.

## Resultados

| Configuración | Señal promedio | dBm aprox. | Redes vistas (1.er escaneo) |
|---|---|---|---|
| Cable pelado (19/11) | 37,8 % | ≈ −77 | 4 |
| Alambre soldado | 67,4 % | ≈ −60 | 35 |
| **Alambre soldado, sin tocar** | **83,8 %** | **≈ −50** | **37** |
| Antena original (19/11) | 100 % | ≥ −40 | 46 |

Datos por escaneo en [mediciones.csv](mediciones.csv).

## Conclusiones

- **El empalme conduce.** La señal pasa del alambre al vivo y llega al adaptador.
- **La primera medición tuvo una caída a 9 %** en el escaneo 4. En la segunda, sin tocar nada, los 8 escaneos quedaron entre 75 y 89 %. La caída se atribuye a mover el adaptador o el cable durante el escaneo, no a la soldadura.
- **El alambre suelto ya funciona como una antena muy básica.** Con unos 2,5 cm entre vivo y alambre se acerca al cuarto de onda de 2,4 GHz (3,1 cm), por eso capta mucho más que el cable pelado. Aun así queda por debajo de la antena original.
- Las mediciones de los días 19 y 21 se hicieron en el mismo sitio, pero no se controló la posición exacta del portátil. Comparar entre días con cuidado.

## Para la próxima

- Montar los discos, soldar el alambre al parche y medir **en este mismo sitio**. El valor a superar es ≈ −50 dBm.
- Para que la diferencia con la antena original se vea, medir también **más lejos del router**, donde la original no marque 100 %.
