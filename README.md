# DHBW - Verteilte Systeme 2023 - Frey, Falk

## Ergebnis als Video
https://youtu.be/g1KuwLGTjBk

## Hub (Raspberry Pi)

## Switch (Sonoff Basic R2)
Der Sonoff Smart Switch verbindet sich mit einem WLAN. Die Standard-Firmware erlaubt allerdings nur die Bedieunung über eine designierte mobile App.
Um den Switch öffentlich verwendbar zu machen, muss eine neue Firmware geflasht werden.

äää Switch flashen
1. USB-to-TTL Adapter über RX, TX, GND, 3V an den Switch anschließen (ggf. löten)
2. ggf. Triber für TTL-Adapter installieren
3. Tasmotizer Software herunterladen
4. Tasmota (oder andere, geeignete Firmware) als bin-File herunterladen und über Tasmota flashen
5. Switch wird nun einen eigenen WLAN-Endpunkt eröffnen. Suche nach Tasmota-XXX. Wenn eingeloggt, über die Einstellungen SSID und PW des eigenen WLANs eingeben.
6. Switch sollte neu starten und sich verbinden. Seine IP kann bestimmt werden mit IP-Scan oder über den Router. Ein Aufruf der IP über einen Browser sollte die Web-UI des Browsers öffnen
