import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

qr.add_data("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.idntimes.com%2Fhype%2Fhumor%2Fmuhammad-bimo-aprilianto%2Fmeme-lucu-buat-caper-ke-gebetan&psig=AOvVaw1SzRs1obI-v-BBjcDqFXkY&ust=1701501821685000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCJCJ67Ha7YIDFQAAAAAdAAAAABAE")
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color="white")

img.save("qr.png")