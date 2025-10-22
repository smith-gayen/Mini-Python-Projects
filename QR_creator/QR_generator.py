import qrcode
from PIL import Image

# Taking UPI ID as an input
upi_id = input("Enter your UPI ID = ")

# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Defining the payment URL based on the UPI ID and the payment app
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
amazon_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'

# Create QR Codes for payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)
amazon_pay_qr = qrcode.make(amazon_pay_url)

# Save the QR code to image file (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')
amazon_pay_qr.save('amazon_pay_qr.png')

# Display the QR Codes (you may need to install PIL/Pillow Library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
amazon_pay_qr.show()