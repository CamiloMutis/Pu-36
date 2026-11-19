#!/usr/bin/env python3
"""Mide la señal de una red WiFi de 2,4 GHz con un adaptador USB y guarda los datos.

Uso:  python3 medir.py <configuracion> <red> [repeticiones]
  configuracion  nombre de la prueba: pelado, original, pu36, pu36_90grados...
  red            SSID de la red de prueba
  repeticiones   número de escaneos (por defecto 5)

Requiere Linux con NetworkManager (nmcli). Escanea con el adaptador USB, no con la
tarjeta interna. Guarda en ./mediciones.csv solo la red de prueba (anotada como
red_prueba) y cuántas redes se vieron; no guarda los nombres de las redes vecinas.
La conversión a dBm usa la fórmula de NetworkManager: dBm = % x 0,6 - 100.
"""
import csv, datetime, os, statistics, subprocess, sys, time

CSV = os.path.join(os.getcwd(), "mediciones.csv")


def adaptador_usb():
    for n in sorted(os.listdir("/sys/class/net")):
        base = f"/sys/class/net/{n}"
        if os.path.isdir(f"{base}/wireless") and "usb" in os.path.realpath(f"{base}/device"):
            return n
    return None


def escanear(iface):
    out = subprocess.run(
        ["nmcli", "-t", "-f", "SSID,BSSID,CHAN,SIGNAL", "dev", "wifi", "list", "ifname", iface, "--rescan", "yes"],
        capture_output=True, text=True, timeout=60).stdout
    redes = []
    for linea in out.splitlines():
        partes = linea.replace("\\:", "\x00").split(":")
        if len(partes) < 4:
            continue
        ssid, bssid, chan, sig = [p.replace("\x00", ":") for p in partes[:4]]
        if chan.isdigit() and int(chan) <= 14 and sig.isdigit():
            redes.append((ssid, bssid, int(chan), int(sig)))
    return redes


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    config, red = sys.argv[1], sys.argv[2]
    reps = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    iface = adaptador_usb()
    if not iface:
        print("No encuentro ningún adaptador WiFi USB conectado. Conéctalo y vuelve a intentar.")
        sys.exit(1)
    print(f"Adaptador: {iface} · configuración: {config} · {reps} escaneos")
    nuevo = not os.path.exists(CSV)
    senales = []
    with open(CSV, "a", newline="") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(["fecha", "hora", "configuracion", "equipo", "escaneo", "red", "canal", "senal_pct", "dbm_aprox", "redes_vistas"])
        for i in range(1, reps + 1):
            redes = escanear(iface)
            ahora = datetime.datetime.now()
            vistas = len({(s, b) for (s, b, _, _) in redes})
            obj = [(c, s) for (ss, _, c, s) in redes if ss == red]
            if obj:
                canal, sig = max(obj, key=lambda x: x[1])
                senales.append(sig)
                w.writerow([ahora.date(), ahora.strftime("%H:%M:%S"), config, iface, i, "red_prueba", canal, sig, round(sig * 0.6 - 100), vistas])
                print(f"  escaneo {i}: {sig} % (≈ {sig*0.6-100:.0f} dBm) · redes vistas: {vistas}")
            else:
                w.writerow([ahora.date(), ahora.strftime("%H:%M:%S"), config, iface, i, "red_prueba", "", "", "", vistas])
                print(f"  escaneo {i}: red no visible · redes vistas: {vistas}")
            time.sleep(2)
    if senales:
        p = statistics.mean(senales)
        print(f"\nPromedio: {p:.1f} % (≈ {p*0.6-100:.0f} dBm)")
    print(f"Datos guardados en {CSV}")


if __name__ == "__main__":
    main()
