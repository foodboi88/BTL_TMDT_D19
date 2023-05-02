from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

# Định nghĩa các lựa chọn cho phương thức thanh toán
PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)

# Biểu mẫu để nhập thông tin địa chỉ và phương thức thanh toán
class CheckoutForm(forms.Form):
    # Thông tin địa chỉ giao hàng
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    # Thông tin địa chỉ thanh toán
    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)

    # Các trường checkbox để lưu thông tin thanh toán và giao hàng mặc định
    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    # Tùy chọn phương thức thanh toán
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

# Biểu mẫu để nhập mã giảm giá
class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))

# Biểu mẫu để yêu cầu hoàn tiền
class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()

# Biểu mẫu để thanh toán
class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)
