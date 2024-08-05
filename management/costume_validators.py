from django.core.exceptions import ValidationError

def digits_validation(num):
    if not num.isdigit():
        raise ValidationError(f'Phone number should be in digits!')

   