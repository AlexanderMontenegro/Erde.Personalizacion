import qrcode
from PIL import Image

# URL del sitio
url = "https://erde-personalizacion.onrender.com"

# Crear QR básico
qr = qrcode.QRCode(
    version=1,
    box_size=12,
    border=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

qr.add_data(url)
qr.make(fit=True)

# Colores inspirados en el logo de ERDE
qr_img = qr.make_image(fill_color="#020000", back_color="#ffffff").convert("RGB")

# Opcional: superponer logo circular

#try:
#   logo = Image.open("LOGO2.PNG").convert("RGBA")
#   logo_size = 90

    # Redimensionar el logo
   # logo = logo.resize((logo_size, logo_size))

    # Coordenadas para centrar el logo
    #pos = (
      #  (qr_img.size[0] - logo_size) // 2,
     #   (qr_img.size[1] - logo_size) // 2
    #)

    #qr_img.paste(logo, pos, mask=logo)
#except FileNotFoundError:
 #   print("⚠️ No se encontró 'logo.png'. El QR se generará sin logo.")

# Guardar imagen final
qr_img.save("qr_erde.png")
print("✅ Código QR generado como 'qr_erde.png'")
