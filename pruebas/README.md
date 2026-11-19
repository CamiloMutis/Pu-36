# Pruebas

Una carpeta por sesión de medición, con el nombre `AAAA-MM-DD_descripcion`, por ejemplo `2026-11-25_distancia-5-a-20m`.

Cada carpeta lleva:

- `README.md`: qué se midió, dónde, con qué equipo y qué se concluyó.
- `mediciones.csv`: los datos, con las columnas de [plantilla_mediciones.csv](plantilla_mediciones.csv).
- Fotos opcionales del montaje y del lugar.

## Columnas de la plantilla

| Columna | Qué va |
|---|---|
| `fecha` | AAAA-MM-DD |
| `configuracion` | `pelado`, `original` o `pu36` |
| `equipo` | Con qué se midió: `tl-wn722n`, `router`, `celular`… |
| `distancia_m` | Distancia al router en metros |
| `angulo_grados` | 0 = apuntando al router |
| `repeticion` | 1, 2 o 3 |
| `rssi_dbm` | Señal en dBm |
| `senal_pct` | Señal en porcentaje, si la herramienta la da así |
| `descarga_mbps`, `subida_mbps`, `latencia_ms` | De Speedtest |
| `notas` | Cualquier cosa rara: gente pasando, puerta abierta… |

No se guardan los nombres de las redes vecinas: solo la red de prueba, y se puede anotar como `red_prueba`.

## Sesiones

| Fecha | Sesión | Resultado |
|---|---|---|
| 2026-11-19 | [Cable pelado contra antena original](2026-11-19_cable-pelado-vs-antena-original/) | La antena original capta muchísimo más; el vivo solo capta muy poco |

## Script de medición

`herramientas/medir.py` (Linux con NetworkManager) escanea con el adaptador USB y guarda la señal de la red de prueba:

```
python3 herramientas/medir.py <configuracion> <red> [repeticiones]
python3 herramientas/medir.py pu36 MiRed 5
```
